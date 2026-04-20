"""Auto-generated from docs/pennylane-openapi.json. Do not edit by hand.

Regenerate with: python scripts/generate_tools.py
"""
from typing import Any, Optional

from .._registry import tool
from ..client import PennylaneClient


@tool(
    name="pennylane_get_sepa_mandates",
    description="[Mandates · SEPA Mandates / Mandats SEPA] List SEPA mandates This endpoint allows you to retrieve all SEPA mandates associated with your company > ℹ️ > This endpoint requires one of the following scopes: `customer_mandates:all`, `customer_mandates:readonly` Mots-clés FR: mandat SEPA, prélèvement SEPA, autorisation de prélèvement.",
    input_schema={   'type': 'object',
        'properties': {   'cursor': {   'type': 'string',
                                        'description': 'Cursor for pagination. Use this to fetch the '
                                                       'next set of results.\n'
                                                       'The cursor is an opaque string returned in the '
                                                       "previous response's metadata.\n"
                                                       'Leave empty for the first request.\n'},
                          'limit': {   'type': 'integer',
                                       'description': 'Number of items to return per request.\n'
                                                      'Defaults to 20 if not specified.\n'
                                                      'Must be between 1 and 100.\n'},
                          'filter': {   'type': 'string',
                                        'description': 'You can choose to filter items on specific '
                                                       'fields.\n'
                                                       'Available fields and values:\n'
                                                       '- `id`: `lt`, `lteq`, `gt`, `gteq`, `eq`, '
                                                       '`not_eq`, `in`, `not_in`\n'
                                                       '- `customer_id`: `lt`, `lteq`, `gt`, `gteq`, '
                                                       '`eq`, `not_eq`, `in`, `not_in`\n'},
                          'sort': {   'type': 'string',
                                      'description': 'You can choose to sort items on specific '
                                                     'attributes.\n'
                                                     'Sort field may be prefixed with `-` for '
                                                     'descending order.\n'
                                                     'Example: `id` will sort by ascending order, '
                                                     '`-id` will sort by descending order.\n'
                                                     'Available fields: `id`\n'}}},
    resource="sepa_mandates",
)
async def get_sepa_mandates(
    client: PennylaneClient,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
    filter: Optional[Any] = None,
    sort: Optional[Any] = None,
) -> Any:
    url = "/sepa_mandates"
    params = {'cursor': cursor, 'limit': limit, 'filter': filter, 'sort': sort}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_post_sepa_mandates",
    description="[Mandates · SEPA Mandates / Mandats SEPA] Create a SEPA mandate This endpoint allows you to create a SEPA mandate to enable direct debit payments > ℹ️ > This endpoint requires the following scope: `customer_mandates:all` Mots-clés FR: mandat SEPA, prélèvement SEPA, autorisation de prélèvement.",
    input_schema={   'type': 'object',
        'properties': {   'use_2026_api_changes': {   'type': 'boolean',
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
        'required': ['body']},
    resource="sepa_mandates",
)
async def post_sepa_mandates(
    client: PennylaneClient,
    use_2026_api_changes: Optional[Any] = None,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = "/sepa_mandates"
    params = {'use_2026_api_changes': use_2026_api_changes}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.post(url, data=body)


@tool(
    name="pennylane_get_sepa_mandate",
    description="[Mandates · SEPA Mandates / Mandats SEPA] Get a SEPA mandate This endpoint allows you to retrieve a specific SEPA mandate by ID > ℹ️ > This endpoint requires one of the following scopes: `customer_mandates:all`, `customer_mandates:readonly` Mots-clés FR: mandat SEPA, prélèvement SEPA, autorisation de prélèvement.",
    input_schema={   'type': 'object',
        'properties': {'id': {'type': 'integer', 'description': 'ID of the SEPA mandate to retrieve'}},
        'required': ['id']},
    resource="sepa_mandates",
)
async def get_sepa_mandate(
    client: PennylaneClient,
    id: str,
) -> Any:
    url = f"/sepa_mandates/{id}".format(id=id)
    params = None
    return await client.get(url, params=params)


@tool(
    name="pennylane_put_sepa_mandate",
    description="[Mandates · SEPA Mandates / Mandats SEPA] Update a SEPA mandate This endpoint allows you to update an existing SEPA mandate > ℹ️ > This endpoint requires the following scope: `customer_mandates:all` Mots-clés FR: mandat SEPA, prélèvement SEPA, autorisation de prélèvement.",
    input_schema={   'type': 'object',
        'properties': {   'id': {'type': 'integer', 'description': 'ID of the SEPA mandate to update'},
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
    resource="sepa_mandates",
)
async def put_sepa_mandate(
    client: PennylaneClient,
    id: str,
    use_2026_api_changes: Optional[Any] = None,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = f"/sepa_mandates/{id}".format(id=id)
    params = {'use_2026_api_changes': use_2026_api_changes}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.put(url, data=body)


@tool(
    name="pennylane_delete_sepa_mandate",
    description="[Mandates · SEPA Mandates / Mandats SEPA] Delete a SEPA mandate This endpoint allows you to delete a specific SEPA mandate > ℹ️ > This endpoint requires the following scope: `customer_mandates:all` Mots-clés FR: mandat SEPA, prélèvement SEPA, autorisation de prélèvement.",
    input_schema={   'type': 'object',
        'properties': {'id': {'type': 'integer', 'description': 'ID of the SEPA mandate to delete'}},
        'required': ['id']},
    resource="sepa_mandates",
)
async def delete_sepa_mandate(
    client: PennylaneClient,
    id: str,
) -> Any:
    url = f"/sepa_mandates/{id}".format(id=id)
    params = None
    return await client.delete(url)


