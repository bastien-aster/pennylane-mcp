"""Auto-generated from docs/pennylane-openapi.json. Do not edit by hand.

Regenerate with: python scripts/generate_tools.py
"""
from typing import Any, Optional

from .._registry import tool
from ..client import PennylaneClient


@tool(
    name="pennylane_company_fiscal_years",
    description="[Accounting · Fiscal Years / Exercices fiscaux] List Company's Fiscal Years This endpoint returns a list of fiscal years of the company. **DEPRECATED BEHAVIOR:** By default, returns fiscal years ordered by ascending `start` date. **NEW BEHAVIOR:** By default, returns fiscal years ordered by descending IDs A new `sort` query parameter is now available allowing to sort by `id` or `start` attributes. For more details, see our API documentation https://pennylane.readme.io/... Mots-clés FR: exercice fiscal, année fiscale, clôture.",
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
                          'page': {   'type': 'integer',
                                      'description': 'This pagination system is **DEPRECATED**. For '
                                                     'more details, see our API documentation '
                                                     'https://pennylane.readme.io/docs/2026-api-changes-guide '
                                                     'for migration instructions.\n'
                                                     'Items are paginated, this is the current page '
                                                     'which will be returned. The page index is '
                                                     'starting at 1.'},
                          'per_page': {   'type': 'integer',
                                          'description': 'This pagination system is **DEPRECATED**. '
                                                         'For more details, see our API documentation '
                                                         'https://pennylane.readme.io/docs/2026-api-changes-guide '
                                                         'for migration instructions.\n'
                                                         'Items are paginated. By default, you get 20 '
                                                         'items per page. You can specify another '
                                                         'number of items per page.'},
                          'cursor': {   'type': 'string',
                                        'description': 'This pagination system is only available in '
                                                       'the new version of the API. For more details, '
                                                       'see our API documentation '
                                                       'https://pennylane.readme.io/docs/2026-api-changes-guide '
                                                       'for migration instructions.\n'
                                                       'Use this to fetch the next set of results. The '
                                                       'cursor is an opaque string returned in the '
                                                       'previous r'},
                          'limit': {   'type': 'integer',
                                       'description': 'This pagination system is only available in the '
                                                      'new version of the API.\n'
                                                      'For more details, see our API documentation '
                                                      'https://pennylane.readme.io/docs/2026-api-changes-guide '
                                                      'for migration instructions.\n'
                                                      'Number of items to return per request.\n'
                                                      'Defaults to 20 if not specified.\n'
                                                      'Must be between 1 and 100.\n'},
                          'sort': {   'type': 'string',
                                      'description': 'You can choose to sort items on specific '
                                                     'attributes\n'
                                                     'Sort field may be prefixed with `-` for '
                                                     'descending order.\n'
                                                     'Example : `id` will sort by ascending order, '
                                                     '`-id` will sort by descending order.\n'
                                                     'Available fields :\n'
                                                     '- `id`, `start`\n'}}},
    resource="fiscal_years",
    readonly=True,
)
async def company_fiscal_years(
    client: PennylaneClient,
    use_2026_api_changes: Optional[Any] = None,
    page: Optional[Any] = None,
    per_page: Optional[Any] = None,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
    sort: Optional[Any] = None,
) -> Any:
    url = "/fiscal_years"
    params = {'use_2026_api_changes': use_2026_api_changes, 'page': page, 'per_page': per_page, 'cursor': cursor, 'limit': limit, 'sort': sort}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


