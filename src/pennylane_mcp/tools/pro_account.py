"""Auto-generated from docs/pennylane-openapi.json. Do not edit by hand.

Regenerate with: python scripts/generate_tools.py
"""
from typing import Any, Optional

from .._registry import tool
from ..client import PennylaneClient


@tool(
    name="pennylane_post_pro_account_mandate_mail_requests",
    description="Send a Pro Account SEPA mandate request. This endpoint allows you to send a mandate request for a Pro Account SEPA Direct Debit mandate to a customer. Requirements: - Company must have a Pro Account (returns 404 if not) - Company must have an enabled merchant profile (returns 403 if not) > ℹ️ > This endpoint requires the following scope: `customer_mandates:all`",
    input_schema={   'type': 'object',
        'properties': {   'body': {   'type': 'object',
                                      'description': 'Request body payload. See the Pennylane API '
                                                     'reference for the exact schema of this endpoint.',
                                      'additionalProperties': True}},
        'required': ['body']},
)
async def post_pro_account_mandate_mail_requests(
    client: PennylaneClient,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = "/pro_account/mandate_requests"
    params = None
    return await client.post(url, data=body)


@tool(
    name="pennylane_get_pro_account_mandate_migrations",
    description="List mandate migration candidates. This endpoint allows you to retrieve all mandate migration candidates for your company. These are mandates that can be migrated to a Pro Account. Requirements: - Company must have a Pro Account (returns 404 if not) - Company must have an enabled merchant profile (returns 403 if not) > ℹ️ > This endpoint requires one of the following scopes: `customer_mandates:readonly`, `customer_mandates:all`",
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
                                                       '- `customer_id`: `lt`, `lteq`, `gt`, `gteq`, '
                                                       '`eq`, `not_eq`, `in`, `not_in`\n'
                                                       '- `status`: `lt`, `lteq`, `gt`, `gteq`, `eq`, '
                                                       '`not_eq`, `in`, `not_in`\n'},
                          'sort': {   'type': 'string',
                                      'description': 'You can choose to sort items on specific '
                                                     'attributes.\n'
                                                     'Sort field may be prefixed with `-` for '
                                                     'descending order.\n'
                                                     'Example: `id` will sort by ascending order, '
                                                     '`-id` will sort by descending order.\n'
                                                     'Available fields: `id`\n'}}},
)
async def get_pro_account_mandate_migrations(
    client: PennylaneClient,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
    filter: Optional[Any] = None,
    sort: Optional[Any] = None,
) -> Any:
    url = "/pro_account/mandate_migrations"
    params = {'cursor': cursor, 'limit': limit, 'filter': filter, 'sort': sort}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_post_pro_account_mandate_migrations",
    description="Migrate a mandate to Pro Account. This endpoint allows you to migrate a mandate to a Pro Account. Only mandates with status 'available' are eligible for migration. **Requirements:** - Company must have a Pro Account (returns 404 if not) - Company must have an enabled merchant profile (returns 403 if not) > ℹ️ > This endpoint requires the following scope: `customer_mandates:all`",
    input_schema={   'type': 'object',
        'properties': {   'body': {   'type': 'object',
                                      'description': 'Request body payload. See the Pennylane API '
                                                     'reference for the exact schema of this endpoint.',
                                      'additionalProperties': True}},
        'required': ['body']},
)
async def post_pro_account_mandate_migrations(
    client: PennylaneClient,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = "/pro_account/mandate_migrations"
    params = None
    return await client.post(url, data=body)


@tool(
    name="pennylane_get_pro_account_mandates",
    description="List Pro Account payment mandates. This endpoint allows you to retrieve all payment mandates associated with your company's pro account. Requirements: - Company must have a Pro Account (returns 404 if not) - Company must have an enabled merchant profile (returns 403 if not) > ℹ️ > This endpoint requires one of the following scopes: `customer_mandates:readonly`, `customer_mandates:all`",
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
                                                       'Available fields and operators:\n'
                                                       '- `status`: `eq`, `not_eq`, `in`, `not_in`\n'
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
)
async def get_pro_account_mandates(
    client: PennylaneClient,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
    filter: Optional[Any] = None,
    sort: Optional[Any] = None,
) -> Any:
    url = "/pro_account/mandates"
    params = {'cursor': cursor, 'limit': limit, 'filter': filter, 'sort': sort}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


