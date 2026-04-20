"""Auto-generated from docs/pennylane-openapi.json. Do not edit by hand.

Regenerate with: python scripts/generate_tools.py
"""
from typing import Any, Optional

from .._registry import tool
from ..client import PennylaneClient


@tool(
    name="pennylane_get_gocardless_mandates",
    description="[Mandates · GoCardless Mandates / Mandats GoCardless] List gocardless mandates List gocardless mandates > ℹ️ > This endpoint requires one of the following scopes: `customer_mandates:all`, `customer_mandates:readonly` Mots-clés FR: mandat GoCardless, prélèvement GoCardless.",
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
                                                       '- `customer_id`: `lt`, `lteq`, `gt`, `gteq`, '
                                                       '`eq`, `not_eq`, `in`, `not_in`\n'
                                                       '- `external_reference`: `eq`\n'},
                          'sort': {   'type': 'string',
                                      'description': 'You can choose to sort items on specific '
                                                     'attributes.\n'
                                                     'Sort field may be prefixed with `-` for '
                                                     'descending order.\n'
                                                     'Example: `id` will sort by ascending order, '
                                                     '`-id` will sort by descending order.\n'
                                                     'Available fields: `id`\n'}}},
    resource="gocardless_mandates",
)
async def get_gocardless_mandates(
    client: PennylaneClient,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
    filter: Optional[Any] = None,
    sort: Optional[Any] = None,
) -> Any:
    url = "/gocardless_mandates"
    params = {'cursor': cursor, 'limit': limit, 'filter': filter, 'sort': sort}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_get_gocardless_mandate",
    description="[Mandates · GoCardless Mandates / Mandats GoCardless] Get a Gocardless mandate This endpoint allows you to retrieve a specific Gocardless mandate by ID. > ℹ️ > This endpoint requires one of the following scopes: `customer_mandates:all`, `customer_mandates:readonly` Mots-clés FR: mandat GoCardless, prélèvement GoCardless.",
    input_schema={   'type': 'object',
        'properties': {   'id': {   'type': 'integer',
                                    'description': 'ID of the Gocardless mandate to retrieve'}},
        'required': ['id']},
    resource="gocardless_mandates",
)
async def get_gocardless_mandate(
    client: PennylaneClient,
    id: str,
) -> Any:
    url = f"/gocardless_mandates/{id}".format(id=id)
    params = None
    return await client.get(url, params=params)


@tool(
    name="pennylane_post_gocardless_mandate_mail_requests",
    description="[Mandates · GoCardless Mandates / Mandats GoCardless] Send a GoCardless mandate email request This endpoint allows you to send an email request for a GoCardless mandate to a recipient. > ℹ️ > This endpoint requires the following scope: `customer_mandates:all` Mots-clés FR: mandat GoCardless, prélèvement GoCardless.",
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
    resource="gocardless_mandates",
)
async def post_gocardless_mandate_mail_requests(
    client: PennylaneClient,
    use_2026_api_changes: Optional[Any] = None,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = "/gocardless_mandates/mail_requests"
    params = {'use_2026_api_changes': use_2026_api_changes}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.post(url, data=body)


@tool(
    name="pennylane_post_gocardless_mandate_cancellations",
    description="[Mandates · GoCardless Mandates / Mandats GoCardless] Cancel a Gocardless mandate Cancels a specific Gocardless mandate by ID. The mandate must be in a cancellable state, having one of the following statuses: `pending_submission`, `submitted` or `active`. > ℹ️ > This endpoint requires the following scope: `customer_mandates:all` Mots-clés FR: mandat GoCardless, prélèvement GoCardless.",
    input_schema={   'type': 'object',
        'properties': {   'gocardless_mandate_id': {   'type': 'integer',
                                                       'description': 'ID of the Gocardless mandate to '
                                                                      'cancel'}},
        'required': ['gocardless_mandate_id']},
    resource="gocardless_mandates",
)
async def post_gocardless_mandate_cancellations(
    client: PennylaneClient,
    gocardless_mandate_id: str,
) -> Any:
    url = f"/gocardless_mandates/{gocardless_mandate_id}/cancellations".format(gocardless_mandate_id=gocardless_mandate_id)
    params = None
    return await client.post(url, data=body)


@tool(
    name="pennylane_post_gocardless_mandate_associations",
    description="[Mandates · GoCardless Mandates / Mandats GoCardless] Associate a GoCardless mandate to a customer This endpoint allows you to associate a GoCardless mandate to a customer. > ℹ️ > This endpoint requires the following scope: `customer_mandates:all` Mots-clés FR: mandat GoCardless, prélèvement GoCardless.",
    input_schema={   'type': 'object',
        'properties': {   'gocardless_mandate_id': {   'type': 'integer',
                                                       'description': 'GoCardless Mandate identifier'},
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
        'required': ['gocardless_mandate_id', 'body']},
    resource="gocardless_mandates",
)
async def post_gocardless_mandate_associations(
    client: PennylaneClient,
    gocardless_mandate_id: str,
    use_2026_api_changes: Optional[Any] = None,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = f"/gocardless_mandates/{gocardless_mandate_id}/associations".format(gocardless_mandate_id=gocardless_mandate_id)
    params = {'use_2026_api_changes': use_2026_api_changes}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.post(url, data=body)


