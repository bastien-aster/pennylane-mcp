"""Auto-generated from docs/pennylane-openapi.json. Do not edit by hand.

Regenerate with: python scripts/generate_tools.py
"""
from typing import Any, Optional

from .._registry import tool
from ..client import PennylaneClient


@tool(
    name="pennylane_export_analytical_general_ledger",
    description="Create an Analytical General Ledger export. This endpoint allows you to create an Analytical General Ledger export. The generated export file is an xlsx file, using the in-line analytical mode by default. > ℹ️ > This endpoint requires the following scope: `exports:agl`",
    input_schema={   'type': 'object',
        'properties': {   'body': {   'type': 'object',
                                      'description': 'Request body payload. See the Pennylane API '
                                                     'reference for the exact schema of this endpoint.',
                                      'additionalProperties': True}},
        'required': ['body']},
)
async def export_analytical_general_ledger(
    client: PennylaneClient,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = "/exports/analytical_general_ledgers"
    params = None
    return await client.post(url, data=body)


@tool(
    name="pennylane_get_analytical_general_ledger_export",
    description="Retrieve an Analytical General Ledger export. The endpoint returns a specific Analytical General Ledger export. The export file is an xlsx file, using the in-line analytical mode. > ℹ️ > This endpoint requires the following scope: `exports:agl`",
    input_schema={   'type': 'object',
        'properties': {'id': {'type': 'integer', 'description': 'Existing export identifier (id)'}},
        'required': ['id']},
)
async def get_analytical_general_ledger_export(
    client: PennylaneClient,
    id: str,
) -> Any:
    url = f"/exports/analytical_general_ledgers/{id}".format(id=id)
    params = None
    return await client.get(url, params=params)


@tool(
    name="pennylane_export_fec",
    description="Create a FEC export. This endpoint allows you to create a FEC export > ℹ️ > This endpoint requires the following scope: `exports:fec`",
    input_schema={   'type': 'object',
        'properties': {   'body': {   'type': 'object',
                                      'description': 'Request body payload. See the Pennylane API '
                                                     'reference for the exact schema of this endpoint.',
                                      'additionalProperties': True}},
        'required': ['body']},
)
async def export_fec(
    client: PennylaneClient,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = "/exports/fecs"
    params = None
    return await client.post(url, data=body)


@tool(
    name="pennylane_get_fec_export",
    description="Retrieve a FEC export. The endpoint returns a specific FEC export > ℹ️ > This endpoint requires the following scope: `exports:fec`",
    input_schema={   'type': 'object',
        'properties': {'id': {'type': 'integer', 'description': 'Existing export identifier (id)'}},
        'required': ['id']},
)
async def get_fec_export(
    client: PennylaneClient,
    id: str,
) -> Any:
    url = f"/exports/fecs/{id}".format(id=id)
    params = None
    return await client.get(url, params=params)


@tool(
    name="pennylane_export_general_ledger",
    description="Create a General Ledger export. This endpoint allows you to create a General Ledger export. The generated export file is an xlsx file. > ℹ️ > This endpoint requires the following scope: `exports:gl`",
    input_schema={   'type': 'object',
        'properties': {   'body': {   'type': 'object',
                                      'description': 'Request body payload. See the Pennylane API '
                                                     'reference for the exact schema of this endpoint.',
                                      'additionalProperties': True}},
        'required': ['body']},
)
async def export_general_ledger(
    client: PennylaneClient,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = "/exports/general_ledgers"
    params = None
    return await client.post(url, data=body)


@tool(
    name="pennylane_get_general_ledger_export",
    description="Retrieve a General Ledger export. The endpoint returns a specific General Ledger export. The export file is an xlsx file. > ℹ️ > This endpoint requires the following scope: `exports:gl`",
    input_schema={   'type': 'object',
        'properties': {'id': {'type': 'integer', 'description': 'Existing export identifier (id)'}},
        'required': ['id']},
)
async def get_general_ledger_export(
    client: PennylaneClient,
    id: str,
) -> Any:
    url = f"/exports/general_ledgers/{id}".format(id=id)
    params = None
    return await client.get(url, params=params)


