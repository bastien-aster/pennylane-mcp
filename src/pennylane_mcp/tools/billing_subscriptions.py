"""Auto-generated from docs/pennylane-openapi.json. Do not edit by hand.

Regenerate with: python scripts/generate_tools.py
"""
from typing import Any, Optional

from .._registry import tool
from ..client import PennylaneClient


@tool(
    name="pennylane_post_billing_subscriptions",
    description="[Admin · Billing Subscriptions / Abonnements récurrents] Create a billing subscription This endpoint allows you to create a subscription. Pennylane will generate the customer invoice each month. You can also link the subscription to a GoCardless mandate. > ℹ️ > This endpoint requires the following scope: `billing_subscriptions:all` Mots-clés FR: abonnement, facturation récurrente, subscription.",
    input_schema={   'type': 'object',
        'properties': {   'body': {   'type': 'object',
                                      'description': 'Request body payload. See the Pennylane API '
                                                     'reference for the exact schema of this endpoint.',
                                      'additionalProperties': True}},
        'required': ['body']},
    resource="billing_subscriptions",
    readonly=False,
)
async def post_billing_subscriptions(
    client: PennylaneClient,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = "/billing_subscriptions"
    params = None
    return await client.post(url, data=body)


@tool(
    name="pennylane_get_billing_subscriptions",
    description="[Admin · Billing Subscriptions / Abonnements récurrents] List billing subscriptions This endpoint returns a list of subscriptions. > ℹ️ > This endpoint requires one of the following scopes: `billing_subscriptions:all`, `billing_subscriptions:readonly` Mots-clés FR: abonnement, facturation récurrente, subscription.",
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
                                                       '- `id`, `start`, `customer_id`: `lt`, `lteq`, '
                                                       '`gt`, `gteq`, `eq`, `not_eq`, `in`, `not_in`\n'
                                                       '- `status`: `eq`, `not_eq`, `in`, `not_in`\n'},
                          'sort': {   'type': 'string',
                                      'description': 'You can choose to sort items on specific '
                                                     'attributes\n'
                                                     'Sort field may be prefixed with `-` for '
                                                     'descending order.\n'
                                                     'Example : `id` will sort by ascending order, '
                                                     '`-id` will sort by descending order.\n'
                                                     'Available fields : `id`\n'}}},
    resource="billing_subscriptions",
    readonly=True,
)
async def get_billing_subscriptions(
    client: PennylaneClient,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
    filter: Optional[Any] = None,
    sort: Optional[Any] = None,
) -> Any:
    url = "/billing_subscriptions"
    params = {'cursor': cursor, 'limit': limit, 'filter': filter, 'sort': sort}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_get_billing_subscription",
    description="[Admin · Billing Subscriptions / Abonnements récurrents] Get a billing subscription This endpoint returns a specific billing subscription. > ℹ️ > This endpoint requires one of the following scopes: `billing_subscriptions:all`, `billing_subscriptions:readonly` Mots-clés FR: abonnement, facturation récurrente, subscription.",
    input_schema={   'type': 'object',
        'properties': {   'id': {   'type': 'integer',
                                    'description': 'The ID of the billing subscription to retrieve'},
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
    resource="billing_subscriptions",
    readonly=True,
)
async def get_billing_subscription(
    client: PennylaneClient,
    id: str,
    use_2026_api_changes: Optional[Any] = None,
) -> Any:
    url = f"/billing_subscriptions/{id}".format(id=id)
    params = {'use_2026_api_changes': use_2026_api_changes}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_put_billing_subscriptions",
    description="[Admin · Billing Subscriptions / Abonnements récurrents] Update a billing subscription Update a billing subscription > ℹ️ > This endpoint requires the following scope: `billing_subscriptions:all` Mots-clés FR: abonnement, facturation récurrente, subscription.",
    input_schema={   'type': 'object',
        'properties': {   'id': {   'type': 'integer',
                                    'description': 'The ID of the billing subscription to retrieve'},
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
    resource="billing_subscriptions",
    readonly=False,
)
async def put_billing_subscriptions(
    client: PennylaneClient,
    id: str,
    use_2026_api_changes: Optional[Any] = None,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = f"/billing_subscriptions/{id}".format(id=id)
    params = {'use_2026_api_changes': use_2026_api_changes}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.put(url, data=body)


@tool(
    name="pennylane_get_billing_subscription_invoice_line_sections",
    description="[Admin · Billing Subscriptions / Abonnements récurrents] List the invoice line sections of a billing subscription List the invoice line sections of a billing subscription > ℹ️ > This endpoint requires one of the following scopes: `billing_subscriptions:all`, `billing_subscriptions:readonly` Mots-clés FR: abonnement, facturation récurrente, subscription.",
    input_schema={   'type': 'object',
        'properties': {   'billing_subscription_id': {'type': 'integer'},
                          'cursor': {   'type': 'string',
                                        'description': 'Cursor for pagination. Use this to fetch the '
                                                       'next set of results.\n'
                                                       'The cursor is an opaque string returned in the '
                                                       "previous response's metadata.\n"
                                                       'Leave empty for the first request.\n'},
                          'limit': {   'type': 'integer',
                                       'description': 'Number of items to return per request.\n'
                                                      'Defaults to 20 if not specified.\n'
                                                      'Must be between 1 and 100.\n'},
                          'sort': {   'type': 'string',
                                      'description': 'You can choose to sort items on specific '
                                                     'attributes\n'
                                                     'Sort field may be prefixed with `-` for '
                                                     'descending order.\n'
                                                     'Example : `id` will sort by ascending order, '
                                                     '`-id` will sort by descending order.\n'
                                                     'Available fields : `id`\n'}},
        'required': ['billing_subscription_id']},
    resource="billing_subscriptions",
    readonly=True,
)
async def get_billing_subscription_invoice_line_sections(
    client: PennylaneClient,
    billing_subscription_id: str,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
    sort: Optional[Any] = None,
) -> Any:
    url = f"/billing_subscriptions/{billing_subscription_id}/invoice_line_sections".format(billing_subscription_id=billing_subscription_id)
    params = {'cursor': cursor, 'limit': limit, 'sort': sort}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_get_billing_subscription_invoice_lines",
    description="[Admin · Billing Subscriptions / Abonnements récurrents] List invoice lines for a billing subscription List invoice lines for a billing subscription > ℹ️ > This endpoint requires one of the following scopes: `billing_subscriptions:all`, `billing_subscriptions:readonly` Mots-clés FR: abonnement, facturation récurrente, subscription.",
    input_schema={   'type': 'object',
        'properties': {   'billing_subscription_id': {'type': 'integer'},
                          'cursor': {   'type': 'string',
                                        'description': 'Cursor for pagination. Use this to fetch the '
                                                       'next set of results.\n'
                                                       'The cursor is an opaque string returned in the '
                                                       "previous response's metadata.\n"
                                                       'Leave empty for the first request.\n'},
                          'limit': {   'type': 'integer',
                                       'description': 'Number of items to return per request.\n'
                                                      'Defaults to 20 if not specified.\n'
                                                      'Must be between 1 and 100.\n'},
                          'sort': {   'type': 'string',
                                      'description': 'You can choose to sort items on specific '
                                                     'attributes\n'
                                                     'Sort field may be prefixed with `-` for '
                                                     'descending order.\n'
                                                     'Example : `id` will sort by ascending order, '
                                                     '`-id` will sort by descending order.\n'
                                                     'Available fields : `id`\n'}},
        'required': ['billing_subscription_id']},
    resource="billing_subscriptions",
    readonly=True,
)
async def get_billing_subscription_invoice_lines(
    client: PennylaneClient,
    billing_subscription_id: str,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
    sort: Optional[Any] = None,
) -> Any:
    url = f"/billing_subscriptions/{billing_subscription_id}/invoice_lines".format(billing_subscription_id=billing_subscription_id)
    params = {'cursor': cursor, 'limit': limit, 'sort': sort}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


