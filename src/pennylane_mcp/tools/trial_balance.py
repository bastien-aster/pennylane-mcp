"""Auto-generated from docs/pennylane-openapi.json. Do not edit by hand.

Regenerate with: python scripts/generate_tools.py
"""
from typing import Any, Optional

from .._registry import tool
from ..client import PennylaneClient


@tool(
    name="pennylane_get_trial_balance",
    description="[Accounting · Trial Balance / Balance comptable] Get the trial balance This endpoint returns the trial balance of the current company for the given period. **DEPRECATED BEHAVIOR:** `page` and `per_page` params are **deprecated**. Please use `cursor` and `limit` for pagination instead. For more details, see our API documentation https://pennylane.readme.io/docs/2026-api-changes-guide for migration instructions. > ℹ️ > This endpoint requires the following scope: `tr... Mots-clés FR: balance, balance comptable, balance générale.",
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
                          'period_start': {   'type': 'string',
                                              'description': 'The start of the period you want the '
                                                             'trial balance for.'},
                          'period_end': {   'type': 'string',
                                            'description': 'The end of the period you want the trial '
                                                           'balance for.'},
                          'is_auxiliary': {   'type': 'boolean',
                                              'description': 'Whether to include auxiliary accounts or '
                                                             'not.'},
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
                                                      'Must be between 1 and 1000.\n'}},
        'required': ['period_start', 'period_end']},
    resource="trial_balance",
    readonly=True,
)
async def get_trial_balance(
    client: PennylaneClient,
    use_2026_api_changes: Optional[Any] = None,
    period_start: Optional[Any] = None,
    period_end: Optional[Any] = None,
    is_auxiliary: Optional[Any] = None,
    page: Optional[Any] = None,
    per_page: Optional[Any] = None,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
) -> Any:
    url = "/trial_balance"
    params = {'use_2026_api_changes': use_2026_api_changes, 'period_start': period_start, 'period_end': period_end, 'is_auxiliary': is_auxiliary, 'page': page, 'per_page': per_page, 'cursor': cursor, 'limit': limit}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


