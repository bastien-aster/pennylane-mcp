"""Auto-generated from docs/pennylane-openapi.json. Do not edit by hand.

Regenerate with: python scripts/generate_tools.py
"""
from typing import Any, Optional

from .._registry import tool
from ..client import PennylaneClient


@tool(
    name="pennylane_create_purchase_request_import",
    description="[Purchasing · Purchase Requests / Demandes d'achat] Import a purchase order. Import a purchase order. This will create a purchase request with an existing purchase order attached. The purchase request will be **automatically validated**. > ℹ️ > This endpoint requires the following scope: `purchase_requests:all` Mots-clés FR: demande d'achat, bon de commande interne, approvisionnement.",
    input_schema={   'type': 'object',
        'properties': {   'body': {   'type': 'object',
                                      'description': 'Request body payload. See the Pennylane API '
                                                     'reference for the exact schema of this endpoint.',
                                      'additionalProperties': True}},
        'required': ['body']},
    resource="purchase_requests",
    readonly=False,
)
async def create_purchase_request_import(
    client: PennylaneClient,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = "/purchase_requests/imports"
    params = None
    return await client.post(url, data=body)


@tool(
    name="pennylane_get_purchase_request",
    description="[Purchasing · Purchase Requests / Demandes d'achat] Retrieve a purchase request Retrieve a purchase request > ℹ️ > This endpoint requires one of the following scopes: `purchase_requests:all`, `purchase_requests:readonly` Mots-clés FR: demande d'achat, bon de commande interne, approvisionnement.",
    input_schema={'type': 'object', 'properties': {'id': {'type': 'integer'}}, 'required': ['id']},
    resource="purchase_requests",
    readonly=True,
)
async def get_purchase_request(
    client: PennylaneClient,
    id: str,
) -> Any:
    url = f"/purchase_requests/{id}".format(id=id)
    params = None
    return await client.get(url, params=params)


@tool(
    name="pennylane_get_purchase_requests",
    description="[Purchasing · Purchase Requests / Demandes d'achat] List purchase requests List purchase requests > ℹ️ > This endpoint requires one of the following scopes: `purchase_requests:all`, `purchase_requests:readonly` Mots-clés FR: demande d'achat, bon de commande interne, approvisionnement.",
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
                                                       '- `reviewed_by_id`: `eq`, `not_eq`, `in`, '
                                                       '`not_in`\n'
                                                       '- `user_id`: `eq`, `not_eq`, `in`, `not_in`\n'
                                                       '- `supplier_id`: `eq`, `not_eq`, `in`, '
                                                       '`not_in`\n'},
                          'sort': {   'type': 'string',
                                      'description': 'You can choose to sort items on specific '
                                                     'attributes\n'
                                                     'Sort field may be prefixed with `-` for '
                                                     'descending order.\n'
                                                     'Example : `id` will sort by ascending order, '
                                                     '`-id` will sort by descending order.\n'
                                                     'Available fields : `id`\n'}}},
    resource="purchase_requests",
    readonly=True,
)
async def get_purchase_requests(
    client: PennylaneClient,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
    filter: Optional[Any] = None,
    sort: Optional[Any] = None,
) -> Any:
    url = "/purchase_requests"
    params = {'cursor': cursor, 'limit': limit, 'filter': filter, 'sort': sort}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


