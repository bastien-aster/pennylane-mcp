"""Auto-generated from docs/pennylane-openapi.json. Do not edit by hand.

Regenerate with: python scripts/generate_tools.py
"""
from typing import Any, Optional

from .._registry import tool
from ..client import PennylaneClient


@tool(
    name="pennylane_get_bank_accounts",
    description="List bank accounts. List bank_accounts > ℹ️ > This endpoint requires one of the following scopes: `bank_accounts:all`, `bank_accounts:readonly`",
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
                          'sort': {   'type': 'string',
                                      'description': 'You can choose to sort items on specific '
                                                     'attributes\n'
                                                     'Sort field may be prefixed with `-` for '
                                                     'descending order.\n'
                                                     'Example : `id` will sort by ascending order, '
                                                     '`-id` will sort by descending order.\n'
                                                     'Available fields : `id`\n'}}},
)
async def get_bank_accounts(
    client: PennylaneClient,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
    sort: Optional[Any] = None,
) -> Any:
    url = "/bank_accounts"
    params = {'cursor': cursor, 'limit': limit, 'sort': sort}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_post_bank_account",
    description="Create a bank account. Create a bank account > ℹ️ > This endpoint requires the following scope: `bank_accounts:all`",
    input_schema={   'type': 'object',
        'properties': {   'body': {   'type': 'object',
                                      'description': 'Request body payload. See the Pennylane API '
                                                     'reference for the exact schema of this endpoint.',
                                      'additionalProperties': True}},
        'required': ['body']},
)
async def post_bank_account(
    client: PennylaneClient,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = "/bank_accounts"
    params = None
    return await client.post(url, data=body)


@tool(
    name="pennylane_get_bank_account",
    description="Retrieve a bank account. Retrieve a bank account > ℹ️ > This endpoint requires one of the following scopes: `bank_accounts:all`, `bank_accounts:readonly`",
    input_schema={'type': 'object', 'properties': {'id': {'type': 'integer'}}, 'required': ['id']},
)
async def get_bank_account(
    client: PennylaneClient,
    id: str,
) -> Any:
    url = f"/bank_accounts/{id}".format(id=id)
    params = None
    return await client.get(url, params=params)


