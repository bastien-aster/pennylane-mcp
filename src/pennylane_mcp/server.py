"""Pennylane MCP server entry point."""
from __future__ import annotations

import asyncio
import json
import logging
import os
from typing import Optional

from dotenv import load_dotenv
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import TextContent, Tool

from . import tools  # noqa: F401 — triggers @tool registration for every module
from ._metadata import resolve_allowed_resources
from ._registry import TOOLS, ToolSpec
from .client import PennylaneClient

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

app: Server = Server("pennylane-mcp")
pennylane_client: Optional[PennylaneClient] = None
_active_tools: list[ToolSpec] = []


@app.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(name=t.name, description=t.description, inputSchema=t.input_schema)
        for t in _active_tools
    ]


@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    global pennylane_client
    if pennylane_client is None:
        raise RuntimeError("Pennylane client not initialized")

    spec = next((t for t in _active_tools if t.name == name), None)
    if spec is None:
        return [TextContent(type="text", text=f"Error: unknown or disabled tool '{name}'")]

    try:
        result = await spec.handler(pennylane_client, **(arguments or {}))
        return [TextContent(type="text", text=json.dumps(result, indent=2, ensure_ascii=False))]
    except Exception as exc:
        logger.exception("Tool %s failed", name)
        return [TextContent(type="text", text=f"Error executing {name}: {exc}")]


def _select_tools() -> list[ToolSpec]:
    allowed = resolve_allowed_resources(os.getenv("PENNYLANE_TOOLS"))
    if allowed is None:
        return list(TOOLS)
    return [t for t in TOOLS if t.resource in allowed]


async def main() -> None:
    global pennylane_client, _active_tools

    api_key = os.getenv("PENNYLANE_API_KEY")
    if not api_key:
        raise ValueError("PENNYLANE_API_KEY environment variable is required")

    base_url = os.getenv("PENNYLANE_BASE_URL", "https://app.pennylane.com/api/external/v2")

    _active_tools = _select_tools()
    pennylane_client = PennylaneClient(api_key, base_url)
    logger.info(
        "Pennylane MCP server starting — %d/%d tools active (PENNYLANE_TOOLS=%s)",
        len(_active_tools), len(TOOLS), os.getenv("PENNYLANE_TOOLS", "all"),
    )
    logger.info("Base URL: %s", base_url)

    try:
        async with stdio_server() as (read_stream, write_stream):
            await app.run(read_stream, write_stream, app.create_initialization_options())
    finally:
        if pennylane_client is not None:
            await pennylane_client.close()
            logger.info("Pennylane client closed")


def _run() -> None:
    asyncio.run(main())


if __name__ == "__main__":
    _run()
