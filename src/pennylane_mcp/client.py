"""Client HTTP pour l'API Pennylane."""
import asyncio
import logging
import random
import time
from typing import Any, Optional

import httpx

logger = logging.getLogger(__name__)

PENNYLANE_RATE_LIMIT_PER_SECOND = 5
MAX_RETRIES = 4
RETRY_BASE_DELAY_SECONDS = 0.5


class PennylaneClient:
    """Client pour interagir avec l'API Pennylane.

    Enforces Pennylane's 5 req/s rate limit client-side and retries with
    exponential backoff on 429 / 5xx responses.
    """

    def __init__(self, api_key: str, base_url: str = "https://app.pennylane.com/api/external/v2"):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.client = httpx.AsyncClient(
            headers={
                "Authorization": f"Bearer {api_key}",
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
            timeout=30.0,
        )
        self._rate_lock = asyncio.Lock()
        self._request_timestamps: list[float] = []

    async def _respect_rate_limit(self) -> None:
        async with self._rate_lock:
            now = time.monotonic()
            self._request_timestamps = [t for t in self._request_timestamps if now - t < 1.0]
            if len(self._request_timestamps) >= PENNYLANE_RATE_LIMIT_PER_SECOND:
                sleep_for = 1.0 - (now - self._request_timestamps[0])
                if sleep_for > 0:
                    await asyncio.sleep(sleep_for)
                now = time.monotonic()
                self._request_timestamps = [t for t in self._request_timestamps if now - t < 1.0]
            self._request_timestamps.append(time.monotonic())

    async def _request(self, method: str, endpoint: str, **kwargs: Any) -> dict[str, Any]:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        last_exc: Optional[Exception] = None

        for attempt in range(MAX_RETRIES + 1):
            await self._respect_rate_limit()
            try:
                response = await self.client.request(method, url, **kwargs)

                if response.status_code == 429 or 500 <= response.status_code < 600:
                    if attempt == MAX_RETRIES:
                        response.raise_for_status()
                    retry_after = response.headers.get("Retry-After")
                    if retry_after and retry_after.isdigit():
                        delay = float(retry_after)
                    else:
                        delay = RETRY_BASE_DELAY_SECONDS * (2 ** attempt) + random.uniform(0, 0.25)
                    logger.warning(
                        "Pennylane returned %s on %s %s — retry %d/%d in %.2fs",
                        response.status_code, method, endpoint, attempt + 1, MAX_RETRIES, delay,
                    )
                    await asyncio.sleep(delay)
                    continue

                response.raise_for_status()
                return response.json()

            except httpx.HTTPStatusError as e:
                logger.error(f"HTTP error {e.response.status_code}: {e.response.text}")
                raise Exception(f"API error: {e.response.status_code} - {e.response.text}")
            except httpx.TransportError as e:
                last_exc = e
                if attempt == MAX_RETRIES:
                    logger.error(f"Transport error after {MAX_RETRIES} retries: {e}")
                    raise
                delay = RETRY_BASE_DELAY_SECONDS * (2 ** attempt) + random.uniform(0, 0.25)
                logger.warning("Transport error on %s %s — retry %d/%d in %.2fs: %s",
                               method, endpoint, attempt + 1, MAX_RETRIES, delay, e)
                await asyncio.sleep(delay)

        if last_exc:
            raise last_exc
        raise RuntimeError("Exhausted retries without response")

    async def get(self, endpoint: str, params: Optional[dict[str, Any]] = None) -> dict[str, Any]:
        return await self._request("GET", endpoint, params=params)

    async def post(self, endpoint: str, data: Optional[dict[str, Any]] = None) -> dict[str, Any]:
        return await self._request("POST", endpoint, json=data)

    async def put(self, endpoint: str, data: Optional[dict[str, Any]] = None) -> dict[str, Any]:
        return await self._request("PUT", endpoint, json=data)

    async def delete(self, endpoint: str) -> dict[str, Any]:
        return await self._request("DELETE", endpoint)

    async def close(self):
        await self.client.aclose()
