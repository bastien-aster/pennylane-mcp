"""Auto-generated from docs/pennylane-openapi.json. Do not edit by hand.

Regenerate with: python scripts/generate_tools.py
"""
from typing import Any, Optional

from .._registry import tool
from ..client import PennylaneClient


@tool(
    name="pennylane_post_individual_customer",
    description="[Sales · Individual Customers / Clients particuliers] Create an individual customer This endpoint returns the created individual customer. > ℹ️ > This endpoint requires the following scope: `customers:all` Mots-clés FR: client particulier, client B2C, personne physique.",
    input_schema={   'type': 'object',
        'properties': {   'body': {   'type': 'object',
                                      'description': 'Request body payload. See the Pennylane API '
                                                     'reference for the exact schema of this endpoint.',
                                      'additionalProperties': True}},
        'required': ['body']},
    resource="individual_customers",
    readonly=False,
)
async def post_individual_customer(
    client: PennylaneClient,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = "/individual_customers"
    params = None
    return await client.post(url, data=body)


@tool(
    name="pennylane_get_individual_customer",
    description="[Sales · Individual Customers / Clients particuliers] Retrieve an individual customer This endpoint returns an individual customer. > ℹ️ > This endpoint requires one of the following scopes: `customers:all`, `customers:readonly` Mots-clés FR: client particulier, client B2C, personne physique.",
    input_schema={   'type': 'object',
        'properties': {   'id': {'type': 'string', 'description': 'Individual customer identifier'},
                          'use_2026_api_changes': {   'type': 'boolean',
                                                      'description': 'If you are already using the '
                                                                     '`X-Use-2026-API-Changes` header, '
                                                                     'you can ignore this parameter.\n'
                                                                     '\n'
                                                                     'The Pennylane API is introducing '
                                                                     'important changes, which will be '
                                                                     'rolled out in three phases: '
                                                                     'preview, sunset and cleanup.\n'
                                                                     '\n'
                                                                     '**For new user**, please use '
                                                                     'this parameter with `true` value '
                                                                     'to opt in directly t'}},
        'required': ['id']},
    resource="individual_customers",
    readonly=True,
)
async def get_individual_customer(
    client: PennylaneClient,
    id: str,
    use_2026_api_changes: Optional[Any] = None,
) -> Any:
    url = f"/individual_customers/{id}".format(id=id)
    params = {'use_2026_api_changes': use_2026_api_changes}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_put_individual_customer",
    description="[Sales · Individual Customers / Clients particuliers] Update an individual customer This endpoint returns the updated individual customer. > ℹ️ > This endpoint requires the following scope: `customers:all` Mots-clés FR: client particulier, client B2C, personne physique.",
    input_schema={   'type': 'object',
        'properties': {   'id': {'type': 'string', 'description': 'Individual customer identifier'},
                          'use_2026_api_changes': {   'type': 'boolean',
                                                      'description': 'If you are already using the '
                                                                     '`X-Use-2026-API-Changes` header, '
                                                                     'you can ignore this parameter.\n'
                                                                     '\n'
                                                                     'The Pennylane API is introducing '
                                                                     'important changes, which will be '
                                                                     'rolled out in three phases: '
                                                                     'preview, sunset and cleanup.\n'
                                                                     '\n'
                                                                     '**For new user**, please use '
                                                                     'this parameter with `true` value '
                                                                     'to opt in directly t'},
                          'body': {   'type': 'object',
                                      'description': 'Request body payload. See the Pennylane API '
                                                     'reference for the exact schema of this endpoint.',
                                      'additionalProperties': True}},
        'required': ['id', 'body']},
    resource="individual_customers",
    readonly=False,
)
async def put_individual_customer(
    client: PennylaneClient,
    id: str,
    use_2026_api_changes: Optional[Any] = None,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = f"/individual_customers/{id}".format(id=id)
    params = {'use_2026_api_changes': use_2026_api_changes}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.put(url, data=body)


