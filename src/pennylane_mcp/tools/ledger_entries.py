"""Auto-generated from docs/pennylane-openapi.json. Do not edit by hand.

Regenerate with: python scripts/generate_tools.py
"""
from typing import Any, Optional

from .._registry import tool
from ..client import PennylaneClient


@tool(
    name="pennylane_get_ledger_entries",
    description="[Accounting · Ledger Entries / Écritures comptables] List Ledger Entries Returns a list of ledger entries. **DEPRECATED BEHAVIOR:** Draft entries are filtered out. By default, entries from fiscal periods that are closed or frozen are excluded. However, if a 'date' filter is provided, it will return all entries within the specified date range, even if they fall within a closed or frozen fiscal period. **NEW BEHAVIOR :** By default, all entries (including draft ones) ... Mots-clés FR: écriture comptable, écriture, journal.",
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
                                                     'starting at 1. This parameter is deprecate'},
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
                                                      '\n'
                                                      'Number of items to return per request.\n'
                                                      'Defaults to 20 if not specified.\n'
                                                      'Must be between 1 and 100.\n'},
                          'filter': {   'type': 'string',
                                        'description': 'You can choose to filter items on specific '
                                                       'fields.\n'
                                                       'Available fields and values:\n'
                                                       '- 🆕 `id`: `lt, lteq, gt, gteq, eq, not_eq`, '
                                                       '`in`, `not_in` (only available on the new '
                                                       'version of the API : For more details, see our '
                                                       'API documentation '
                                                       'https://pennylane.readme.io/docs/2026-api-changes-guide '
                                                       'for migration'},
                          'sort': {   'type': 'string',
                                      'description': 'You can choose to sort items on specific '
                                                     'attributes\n'
                                                     'Sort field may be prefixed with `-` for '
                                                     'descending order.\n'
                                                     'Example : `date` will sort by ascending order, '
                                                     '`-date` will sort by descending order.\n'
                                                     'Available fields :\n'
                                                     '- 🆕 `id` (only available on the new version of '
                                                     'the API : For more details, see our AP'}}},
    resource="ledger_entries",
    readonly=True,
)
async def get_ledger_entries(
    client: PennylaneClient,
    use_2026_api_changes: Optional[Any] = None,
    page: Optional[Any] = None,
    per_page: Optional[Any] = None,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
    filter: Optional[Any] = None,
    sort: Optional[Any] = None,
) -> Any:
    url = "/ledger_entries"
    params = {'use_2026_api_changes': use_2026_api_changes, 'page': page, 'per_page': per_page, 'cursor': cursor, 'limit': limit, 'filter': filter, 'sort': sort}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_post_ledger_entries",
    description="[Accounting · Ledger Entries / Écritures comptables] Create a ledger entry Create a ledger entry **DEPRECATED BEHAVIOR:** The old `ledger` scope will only work on the old behavior system. As soon as you opt in to the new version, or when the sunset phase starts and you haven't explicitly opted out of the old behavior, the ledger scope will no longer work. For more details, see our API documentation https://pennylane.readme.io/docs/2026-api-changes-guide for migration ... Mots-clés FR: écriture comptable, écriture, journal.",
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
                          'body': {   'type': 'object',
                                      'description': 'Request body payload. See the Pennylane API '
                                                     'reference for the exact schema of this endpoint.',
                                      'additionalProperties': True}},
        'required': ['body']},
    resource="ledger_entries",
    readonly=False,
)
async def post_ledger_entries(
    client: PennylaneClient,
    use_2026_api_changes: Optional[Any] = None,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = "/ledger_entries"
    params = {'use_2026_api_changes': use_2026_api_changes}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.post(url, data=body)


@tool(
    name="pennylane_get_ledger_entry",
    description="[Accounting · Ledger Entries / Écritures comptables] Retrieve a Ledger entry Retrieve a ledger entry **NEW BEHAVIOR :** The old `ledger` scope will only work on the old behavior system. As soon as you opt in to the new version, or when the sunset phase starts and you haven't explicitly opted out of the old behavior, the ledger scope will no longer work. For more details, see our API documentation https://pennylane.readme.io/docs/2026-api-changes-guide for migration inst... Mots-clés FR: écriture comptable, écriture, journal.",
    input_schema={   'type': 'object',
        'properties': {   'id': {   'type': 'integer',
                                    'description': 'The unique identifier of the ledger entry'},
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
    resource="ledger_entries",
    readonly=True,
)
async def get_ledger_entry(
    client: PennylaneClient,
    id: str,
    use_2026_api_changes: Optional[Any] = None,
) -> Any:
    url = f"/ledger_entries/{id}".format(id=id)
    params = {'use_2026_api_changes': use_2026_api_changes}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_put_ledger_entries",
    description="[Accounting · Ledger Entries / Écritures comptables] Update a ledger entry Update a ledger entry **NEW BEHAVIOR :** The old `ledger` scope will only work on the old behavior system. As soon as you opt in to the new version, or when the sunset phase starts and you haven't explicitly opted out of the old behavior, the ledger scope will no longer work. For more details, see our API documentation https://pennylane.readme.io/docs/2026-api-changes-guide for migration instru... Mots-clés FR: écriture comptable, écriture, journal.",
    input_schema={   'type': 'object',
        'properties': {   'id': {   'type': 'string',
                                    'description': 'The unique identifier of the ledger entry'},
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
    resource="ledger_entries",
    readonly=False,
)
async def put_ledger_entries(
    client: PennylaneClient,
    id: str,
    use_2026_api_changes: Optional[Any] = None,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = f"/ledger_entries/{id}".format(id=id)
    params = {'use_2026_api_changes': use_2026_api_changes}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.put(url, data=body)


@tool(
    name="pennylane_get_ledger_entries_ledger_entry_lines",
    description="[Accounting · Ledger Entries / Écritures comptables] List ledger entry lines of a Ledger Entry List ledger entry lines of a Ledger Entry **DEPRECATED BEHAVIOR:** By default, returns ledger entry lines ordered by ascending IDs **NEW BEHAVIOR:** By default, returns ledger entry lines ordered by descending IDs The old `ledger` scope will only work on the old behavior system. As soon as you opt in to the new version, or when the sunset phase starts and you haven't explicitly opted out of the... Mots-clés FR: écriture comptable, écriture, journal.",
    input_schema={   'type': 'object',
        'properties': {   'ledger_entry_id': {   'type': 'number',
                                                 'description': 'Existing Ledger Entry (id)'},
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
                          'filter': {   'type': 'string',
                                        'description': 'You can choose to filter items on specific '
                                                       'fields.\n'
                                                       'Available fields : `ledger_account_id`\n'
                                                       'Available operators : `lt`, `lteq`, `gt`, '
                                                       '`gteq`, `eq`, `not_eq`, `in`, `not_in`\n'},
                          'sort': {   'type': 'string',
                                      'description': 'You can choose to sort items on specific '
                                                     'attributes\n'
                                                     'Sort field may be prefixed with `-` for '
                                                     'descending order.\n'
                                                     'Example : `id` will sort by ascending order, '
                                                     '`-id` will sort by descending order.\n'
                                                     'Available fields :\n'
                                                     '- `id`\n'}},
        'required': ['ledger_entry_id']},
    resource="ledger_entries",
    readonly=True,
)
async def get_ledger_entries_ledger_entry_lines(
    client: PennylaneClient,
    ledger_entry_id: str,
    use_2026_api_changes: Optional[Any] = None,
    page: Optional[Any] = None,
    per_page: Optional[Any] = None,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
    filter: Optional[Any] = None,
    sort: Optional[Any] = None,
) -> Any:
    url = f"/ledger_entries/{ledger_entry_id}/ledger_entry_lines".format(ledger_entry_id=ledger_entry_id)
    params = {'use_2026_api_changes': use_2026_api_changes, 'page': page, 'per_page': per_page, 'cursor': cursor, 'limit': limit, 'filter': filter, 'sort': sort}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


