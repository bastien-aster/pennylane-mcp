"""Auto-generated from docs/pennylane-openapi.json. Do not edit by hand.

Regenerate with: python scripts/generate_tools.py
"""
from typing import Any, Optional

from .._registry import tool
from ..client import PennylaneClient


@tool(
    name="pennylane_get_suppliers",
    description="[Purchasing · Suppliers / Fournisseurs] List suppliers List suppliers > ℹ️ > This endpoint requires one of the following scopes: `suppliers:all`, `suppliers:readonly` Mots-clés FR: fournisseur, prestataire.",
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
                                                       '- `ledger_account_id`: `eq`, `not_eq`\n'
                                                       '- `name`: `start_with`\n'
                                                       '- `external_reference`: `eq`, `not_eq`, `in`, '
                                                       '`not_in`\n'
                                                       '- `emails`: `in`\n'},
                          'sort': {   'type': 'string',
                                      'description': 'You can choose to sort items on specific '
                                                     'attributes\n'
                                                     'Sort field may be prefixed with `-` for '
                                                     'descending order.\n'
                                                     'Example : `id` will sort by ascending order, '
                                                     '`-id` will sort by descending order.\n'
                                                     'Available fields : `id`\n'}}},
    resource="suppliers",
)
async def get_suppliers(
    client: PennylaneClient,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
    filter: Optional[Any] = None,
    sort: Optional[Any] = None,
) -> Any:
    url = "/suppliers"
    params = {'cursor': cursor, 'limit': limit, 'filter': filter, 'sort': sort}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_post_supplier",
    description="[Purchasing · Suppliers / Fournisseurs] Create a Supplier This endpoint returns the created supplier. > ℹ️ > This endpoint requires the following scope: `suppliers:all` Mots-clés FR: fournisseur, prestataire.",
    input_schema={   'type': 'object',
        'properties': {   'body': {   'type': 'object',
                                      'description': 'Request body payload. See the Pennylane API '
                                                     'reference for the exact schema of this endpoint.',
                                      'additionalProperties': True}},
        'required': ['body']},
    resource="suppliers",
)
async def post_supplier(
    client: PennylaneClient,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = "/suppliers"
    params = None
    return await client.post(url, data=body)


@tool(
    name="pennylane_get_supplier",
    description="[Purchasing · Suppliers / Fournisseurs] Retrieve a supplier This endpoint returns a supplier. > ℹ️ > This endpoint requires one of the following scopes: `suppliers:all`, `suppliers:readonly` Mots-clés FR: fournisseur, prestataire.",
    input_schema={   'type': 'object',
        'properties': {   'id': {'type': 'integer', 'description': 'Supplier identifier'},
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
    resource="suppliers",
)
async def get_supplier(
    client: PennylaneClient,
    id: str,
    use_2026_api_changes: Optional[Any] = None,
) -> Any:
    url = f"/suppliers/{id}".format(id=id)
    params = {'use_2026_api_changes': use_2026_api_changes}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_put_supplier",
    description="[Purchasing · Suppliers / Fournisseurs] Update a supplier This endpoint returns the updated supplier. > ℹ️ > This endpoint requires the following scope: `suppliers:all` Mots-clés FR: fournisseur, prestataire.",
    input_schema={   'type': 'object',
        'properties': {   'id': {'type': 'integer'},
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
    resource="suppliers",
)
async def put_supplier(
    client: PennylaneClient,
    id: str,
    use_2026_api_changes: Optional[Any] = None,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = f"/suppliers/{id}".format(id=id)
    params = {'use_2026_api_changes': use_2026_api_changes}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.put(url, data=body)


@tool(
    name="pennylane_get_supplier_categories",
    description="[Purchasing · Suppliers / Fournisseurs] List categories of a supplier List categories of a supplier > ℹ️ > This endpoint requires one of the following scopes: `suppliers:readonly`, `suppliers:all` Mots-clés FR: fournisseur, prestataire.",
    input_schema={   'type': 'object',
        'properties': {   'supplier_id': {'type': 'integer'},
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
        'required': ['supplier_id']},
    resource="suppliers",
)
async def get_supplier_categories(
    client: PennylaneClient,
    supplier_id: str,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
) -> Any:
    url = f"/suppliers/{supplier_id}/categories".format(supplier_id=supplier_id)
    params = {'cursor': cursor, 'limit': limit}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_put_supplier_categories",
    description="[Purchasing · Suppliers / Fournisseurs] Categorize a supplier Update the categories of a supplier. You can pass categories that don't belong to the same category group. The sum of categories of a same group must equal `1`. In the following example, the two first categories belong to the same category group A, the sum of the weights is `1`. The third category belongs to a category group B, its weight is `1`. ``` [ { 'id': 59, 'weight': '0.5' }, // category... Mots-clés FR: fournisseur, prestataire.",
    input_schema={   'type': 'object',
        'properties': {   'supplier_id': {'type': 'integer'},
                          'body': {   'type': 'object',
                                      'description': 'Request body payload. See the Pennylane API '
                                                     'reference for the exact schema of this endpoint.',
                                      'additionalProperties': True}},
        'required': ['supplier_id', 'body']},
    resource="suppliers",
)
async def put_supplier_categories(
    client: PennylaneClient,
    supplier_id: str,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = f"/suppliers/{supplier_id}/categories".format(supplier_id=supplier_id)
    params = None
    return await client.put(url, data=body)


