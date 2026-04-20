"""Auto-generated from docs/pennylane-openapi.json. Do not edit by hand.

Regenerate with: python scripts/generate_tools.py
"""
from typing import Any, Optional

from .._registry import tool
from ..client import PennylaneClient


@tool(
    name="pennylane_get_me",
    description="User Profile. This endpoint returns information about the company and the user associated to the token.",
    input_schema={'type': 'object', 'properties': {}},
)
async def get_me(
    client: PennylaneClient,
) -> Any:
    url = "/me"
    params = None
    return await client.get(url, params=params)


