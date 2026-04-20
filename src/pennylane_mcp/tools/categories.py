"""Auto-generated from docs/pennylane-openapi.json. Do not edit by hand.

Regenerate with: python scripts/generate_tools.py
"""
from typing import Any, Optional

from .._registry import tool
from ..client import PennylaneClient


@tool(
    name="pennylane_get_categories",
    description="[Accounting · Categories (analytical) / Catégories (analytique)] List categories List categories > ℹ️ > This endpoint requires one of the following scopes: `categories:all`, `categories:readonly` Mots-clés FR: catégorie, analytique, comptabilité analytique.",
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
                                                       '- `label` : `start_with`, `eq`, `in`\n'
                                                       '- `category_group_id` : `lt`, `lteq`, `gt`, '
                                                       '`gteq`, `eq`, `not_eq`, `in`, `not_in`\n'
                                                       '- `analytical_code` : `eq`, `not'},
                          'sort': {   'type': 'string',
                                      'description': 'You can choose to sort items on specific '
                                                     'attributes\n'
                                                     'Sort field may be prefixed with `-` for '
                                                     'descending order.\n'
                                                     'Example : `id` will sort by ascending order, '
                                                     '`-id` will sort by descending order.\n'
                                                     'Available fields : `id`\n'}}},
    resource="categories",
    readonly=True,
)
async def get_categories(
    client: PennylaneClient,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
    filter: Optional[Any] = None,
    sort: Optional[Any] = None,
) -> Any:
    url = "/categories"
    params = {'cursor': cursor, 'limit': limit, 'filter': filter, 'sort': sort}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_post_categories",
    description="[Accounting · Categories (analytical) / Catégories (analytique)] Create a category Create a category > ℹ️ > This endpoint requires the following scope: `categories:all` Mots-clés FR: catégorie, analytique, comptabilité analytique.",
    input_schema={   'type': 'object',
        'properties': {   'body': {   'type': 'object',
                                      'description': 'Request body payload. See the Pennylane API '
                                                     'reference for the exact schema of this endpoint.',
                                      'additionalProperties': True}},
        'required': ['body']},
    resource="categories",
    readonly=False,
)
async def post_categories(
    client: PennylaneClient,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = "/categories"
    params = None
    return await client.post(url, data=body)


@tool(
    name="pennylane_get_category",
    description="[Accounting · Categories (analytical) / Catégories (analytique)] Retrieve a category This endpoint returns a specific category. > ℹ️ > This endpoint requires one of the following scopes: `categories:all`, `categories:readonly` Mots-clés FR: catégorie, analytique, comptabilité analytique.",
    input_schema={   'type': 'object',
        'properties': {   'id': {   'type': 'string',
                                    'description': 'The unique identifier of the category'}},
        'required': ['id']},
    resource="categories",
    readonly=True,
)
async def get_category(
    client: PennylaneClient,
    id: str,
) -> Any:
    url = f"/categories/{id}".format(id=id)
    params = None
    return await client.get(url, params=params)


@tool(
    name="pennylane_update_category",
    description="[Accounting · Categories (analytical) / Catégories (analytique)] Update a category This endpoint updates a category. > ℹ️ > This endpoint requires the following scope: `categories:all` Mots-clés FR: catégorie, analytique, comptabilité analytique.",
    input_schema={   'type': 'object',
        'properties': {   'id': {   'type': 'string',
                                    'description': 'The unique identifier of the category'},
                          'body': {   'type': 'object',
                                      'description': 'Request body payload. See the Pennylane API '
                                                     'reference for the exact schema of this endpoint.',
                                      'additionalProperties': True}},
        'required': ['id', 'body']},
    resource="categories",
    readonly=False,
)
async def update_category(
    client: PennylaneClient,
    id: str,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = f"/categories/{id}".format(id=id)
    params = None
    return await client.put(url, data=body)


