"""Auto-generated from docs/pennylane-openapi.json. Do not edit by hand.

Regenerate with: python scripts/generate_tools.py
"""
from typing import Any, Optional

from .._registry import tool
from ..client import PennylaneClient


@tool(
    name="pennylane_get_customers",
    description="[Sales · Customers (unified) / Clients (unifié)] List customers (company and individual) This endpoint returns a list of both company and individual customers > ℹ️ > This endpoint requires one of the following scopes: `customers:all`, `customers:readonly` Mots-clés FR: client, contact, acheteur.",
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
                                                       '- `customer_type`: `eq`, `not_eq`\n'
                                                       '- `ledger_account_id`: `eq`, `not_eq`\n'
                                                       '- `name`: `start_with`, `eq`\n'
                                                       '- `external_reference`: `start_with`, `eq`, '
                                                       '`not_eq`'},
                          'sort': {   'type': 'string',
                                      'description': 'You can choose to sort items on specific '
                                                     'attributes\n'
                                                     'Sort field may be prefixed with `-` for '
                                                     'descending order.\n'
                                                     'Example : `id` will sort by ascending order, '
                                                     '`-id` will sort by descending order.\n'
                                                     'Available fields : `id`\n'}}},
    resource="customers",
)
async def get_customers(
    client: PennylaneClient,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
    filter: Optional[Any] = None,
    sort: Optional[Any] = None,
) -> Any:
    url = "/customers"
    params = {'cursor': cursor, 'limit': limit, 'filter': filter, 'sort': sort}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_get_customer",
    description="[Sales · Customers (unified) / Clients (unifié)] Retrieve a customer This endpoint returns a customer. > ℹ️ > This endpoint requires one of the following scopes: `customers:all`, `customers:readonly` Mots-clés FR: client, contact, acheteur.",
    input_schema={   'type': 'object',
        'properties': {   'id': {'type': 'integer', 'description': 'Customer identifier'},
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
    resource="customers",
)
async def get_customer(
    client: PennylaneClient,
    id: str,
    use_2026_api_changes: Optional[Any] = None,
) -> Any:
    url = f"/customers/{id}".format(id=id)
    params = {'use_2026_api_changes': use_2026_api_changes}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_get_customer_categories",
    description="[Sales · Customers (unified) / Clients (unifié)] List categories of a customer List categories of a customer > ℹ️ > This endpoint requires one of the following scopes: `customers:readonly`, `customers:all` Mots-clés FR: client, contact, acheteur.",
    input_schema={   'type': 'object',
        'properties': {   'customer_id': {'type': 'integer'},
                          'cursor': {   'type': 'string',
                                        'description': 'Cursor for pagination. Use this to fetch the '
                                                       'next set of results.\n'
                                                       'The cursor is an opaque string returned in the '
                                                       "previous response's metadata.\n"
                                                       'Leave empty for the first request.\n'},
                          'limit': {   'type': 'integer',
                                       'description': 'Number of items to return per request.\n'
                                                      'Defaults to 20 if not specified.\n'
                                                      'Must be between 1 and 100.\n'}},
        'required': ['customer_id']},
    resource="customers",
)
async def get_customer_categories(
    client: PennylaneClient,
    customer_id: str,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
) -> Any:
    url = f"/customers/{customer_id}/categories".format(customer_id=customer_id)
    params = {'cursor': cursor, 'limit': limit}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_put_customer_categories",
    description="[Sales · Customers (unified) / Clients (unifié)] Categorize a customer Update the categories of a customer. You can pass categories that don't belong to the same category group. The sum of categories of a same group must equal `1`. In the following example, the two first categories belong to the same category group A, the sum of the weights is `1`. The third category belongs to a category group B, its weight is `1`. ``` [ { 'id': 59, 'weight': '0.5' }, // category... Mots-clés FR: client, contact, acheteur.",
    input_schema={   'type': 'object',
        'properties': {   'customer_id': {'type': 'integer'},
                          'body': {   'type': 'object',
                                      'description': 'Request body payload. See the Pennylane API '
                                                     'reference for the exact schema of this endpoint.',
                                      'additionalProperties': True}},
        'required': ['customer_id', 'body']},
    resource="customers",
)
async def put_customer_categories(
    client: PennylaneClient,
    customer_id: str,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = f"/customers/{customer_id}/categories".format(customer_id=customer_id)
    params = None
    return await client.put(url, data=body)


@tool(
    name="pennylane_get_customer_contacts",
    description="[Sales · Customers (unified) / Clients (unifié)] List contacts of a customer List contacts of a customer > ℹ️ > This endpoint requires one of the following scopes: `customers:all`, `customers:readonly` Mots-clés FR: client, contact, acheteur.",
    input_schema={   'type': 'object',
        'properties': {   'customer_id': {'type': 'integer'},
                          'cursor': {   'type': 'string',
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
                                                     'Available fields : `id`\n'}},
        'required': ['customer_id']},
    resource="customers",
)
async def get_customer_contacts(
    client: PennylaneClient,
    customer_id: str,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
    sort: Optional[Any] = None,
) -> Any:
    url = f"/customers/{customer_id}/contacts".format(customer_id=customer_id)
    params = {'cursor': cursor, 'limit': limit, 'sort': sort}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


