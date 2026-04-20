"""Auto-generated from docs/pennylane-openapi.json. Do not edit by hand.

Regenerate with: python scripts/generate_tools.py
"""
from typing import Any, Optional

from .._registry import tool
from ..client import PennylaneClient


@tool(
    name="pennylane_get_category_groups",
    description="[Accounting · Category Groups / Groupes de catégories] List category groups This endpoint returns a list of category groups > ℹ️ > This endpoint requires one of the following scopes: `categories:all`, `categories:readonly` Mots-clés FR: groupe de catégories, axe analytique.",
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
                                                      'Must be between 1 and 100.\n'}}},
    resource="category_groups",
    readonly=True,
)
async def get_category_groups(
    client: PennylaneClient,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
) -> Any:
    url = "/category_groups"
    params = {'cursor': cursor, 'limit': limit}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_get_category_group",
    description="[Accounting · Category Groups / Groupes de catégories] Retrieve a category group This endpoint returns a specific category group. > ℹ️ > This endpoint requires one of the following scopes: `categories:all`, `categories:readonly` Mots-clés FR: groupe de catégories, axe analytique.",
    input_schema={   'type': 'object',
        'properties': {   'id': {   'type': 'string',
                                    'description': 'The unique identifier of the category group'}},
        'required': ['id']},
    resource="category_groups",
    readonly=True,
)
async def get_category_group(
    client: PennylaneClient,
    id: str,
) -> Any:
    url = f"/category_groups/{id}".format(id=id)
    params = None
    return await client.get(url, params=params)


@tool(
    name="pennylane_get_category_group_categories",
    description="[Accounting · Category Groups / Groupes de catégories] List categories of a category group List categories of a category group > ℹ️ > This endpoint requires one of the following scopes: `categories:all`, `categories:readonly` Mots-clés FR: groupe de catégories, axe analytique.",
    input_schema={   'type': 'object',
        'properties': {   'category_group_id': {   'type': 'integer',
                                                   'description': 'The unique identifier of the '
                                                                  'category group'},
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
        'required': ['category_group_id']},
    resource="category_groups",
    readonly=True,
)
async def get_category_group_categories(
    client: PennylaneClient,
    category_group_id: str,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
) -> Any:
    url = f"/category_groups/{category_group_id}/categories".format(category_group_id=category_group_id)
    params = {'cursor': cursor, 'limit': limit}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


