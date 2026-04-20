"""Auto-generated from docs/pennylane-openapi.json. Do not edit by hand.

Regenerate with: python scripts/generate_tools.py
"""
from typing import Any, Optional

from .._registry import tool
from ..client import PennylaneClient


@tool(
    name="pennylane_get_me",
    description="[Admin · User Profile / Profil utilisateur] User Profile This endpoint returns information about the company and the user associated to the token. Mots-clés FR: profil, utilisateur courant, mon compte.",
    input_schema={'type': 'object', 'properties': {}},
    resource="me",
)
async def get_me(
    client: PennylaneClient,
) -> Any:
    url = "/me"
    params = None
    return await client.get(url, params=params)


