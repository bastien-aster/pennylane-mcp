"""Auto-generated from docs/pennylane-openapi.json. Do not edit by hand.

Regenerate with: python scripts/generate_tools.py
"""
from typing import Any, Optional

from .._registry import tool
from ..client import PennylaneClient


@tool(
    name="pennylane_post_products",
    description="[Sales · Products / Produits] Create a product Create a product > ℹ️ > This endpoint requires the following scope: `products:all` Mots-clés FR: produit, catalogue, article, référence.",
    input_schema={   'type': 'object',
        'properties': {   'body': {   'type': 'object',
                                      'description': 'Request body payload. See the Pennylane API '
                                                     'reference for the exact schema of this endpoint.',
                                      'additionalProperties': True}},
        'required': ['body']},
    resource="products",
    readonly=False,
)
async def post_products(
    client: PennylaneClient,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = "/products"
    params = None
    return await client.post(url, data=body)


@tool(
    name="pennylane_get_products",
    description="[Sales · Products / Produits] List products List products > ℹ️ > This endpoint requires one of the following scopes: `products:all`, `products:readonly` Mots-clés FR: produit, catalogue, article, référence.",
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
                                                       '- `id` : `lt`, `lteq`, `gt`, `gteq`, `eq`, '
                                                       '`not_eq`, `in`, `not_in`\n'
                                                       '- `label` : `eq`, `in`\n'
                                                       '- `reference` : `eq`, `in`\n'
                                                       '- `external_reference` : `eq`, `not_eq`, `in`, '
                                                       '`not_in`\n'},
                          'sort': {   'type': 'string',
                                      'description': 'You can choose to sort items on specific '
                                                     'attributes\n'
                                                     'Sort field may be prefixed with `-` for '
                                                     'descending order.\n'
                                                     'Example : `id` will sort by ascending order, '
                                                     '`-id` will sort by descending order.\n'
                                                     'Available fields : `id`\n'}}},
    resource="products",
    readonly=True,
)
async def get_products(
    client: PennylaneClient,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
    filter: Optional[Any] = None,
    sort: Optional[Any] = None,
) -> Any:
    url = "/products"
    params = {'cursor': cursor, 'limit': limit, 'filter': filter, 'sort': sort}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_put_product",
    description="[Sales · Products / Produits] Update a product Update a product > ℹ️ > This endpoint requires the following scope: `products:all` Mots-clés FR: produit, catalogue, article, référence.",
    input_schema={   'type': 'object',
        'properties': {   'id': {'type': 'integer'},
                          'body': {   'type': 'object',
                                      'description': 'Request body payload. See the Pennylane API '
                                                     'reference for the exact schema of this endpoint.',
                                      'additionalProperties': True}},
        'required': ['id', 'body']},
    resource="products",
    readonly=False,
)
async def put_product(
    client: PennylaneClient,
    id: str,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = f"/products/{id}".format(id=id)
    params = None
    return await client.put(url, data=body)


@tool(
    name="pennylane_get_product",
    description="[Sales · Products / Produits] Retrieve a product Retrieve a product > ℹ️ > This endpoint requires one of the following scopes: `products:all`, `products:readonly` Mots-clés FR: produit, catalogue, article, référence.",
    input_schema={'type': 'object', 'properties': {'id': {'type': 'integer'}}, 'required': ['id']},
    resource="products",
    readonly=True,
)
async def get_product(
    client: PennylaneClient,
    id: str,
) -> Any:
    url = f"/products/{id}".format(id=id)
    params = None
    return await client.get(url, params=params)


