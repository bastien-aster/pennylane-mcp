"""Auto-generated from docs/pennylane-openapi.json. Do not edit by hand.

Regenerate with: python scripts/generate_tools.py
"""
from typing import Any, Optional

from .._registry import tool
from ..client import PennylaneClient


@tool(
    name="pennylane_get_pa_registrations",
    description="[Admin · Portail Anaf Registrations / Inscriptions Portail Anaf] List PA Registrations Returns all PA (Plateforme Agrée) registrations for the company, including activation status and exchange direction. Use this to determine whether the company has completed PA onboarding. Records with an empty `siret` represent the SIREN-level (head office), other records represent establishments. > ℹ️ > This endpoint requires the following scope: `pa_registrations:readonly` Mots-clés FR: Portail Anaf, Pro Account registration.",
    input_schema={'type': 'object', 'properties': {}},
    resource="pa_registrations",
)
async def get_pa_registrations(
    client: PennylaneClient,
) -> Any:
    url = "/pa_registrations"
    params = None
    return await client.get(url, params=params)


