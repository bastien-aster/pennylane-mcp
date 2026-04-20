"""Auto-generated from docs/pennylane-openapi.json. Do not edit by hand.

Regenerate with: python scripts/generate_tools.py
"""
from typing import Any, Optional

from .._registry import tool
from ..client import PennylaneClient


@tool(
    name="pennylane_post_customer_invoices",
    description="Create a customer invoice. This endpoint allows you to create a draft or finalized customer invoice or credit note > ℹ️ > This endpoint requires the following scope: `customer_invoices:all`",
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
)
async def post_customer_invoices(
    client: PennylaneClient,
    use_2026_api_changes: Optional[Any] = None,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = "/customer_invoices"
    params = {'use_2026_api_changes': use_2026_api_changes}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.post(url, data=body)


@tool(
    name="pennylane_get_customer_invoices",
    description="List customer invoices. List customer invoices and credit notes > ℹ️ > This endpoint requires one of the following scopes: `customer_invoices:all`, `customer_invoices:readonly`",
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
                          'filter': {   'type': 'string',
                                        'description': 'You can choose to filter items on specific '
                                                       'fields.\n'
                                                       'Available fields and values:\n'
                                                       '- `id`, `date`, `customer_id`, '
                                                       '`billing_subscription_id`, `quote_id`: `lt`, '
                                                       '`lteq`, `gt`, `gteq`, `eq`, `not_eq`, `in`, '
                                                       '`not_in`\n'
                                                       '- `invoice_number`: `eq`, `not_eq`, `in`, '
                                                       '`not_in`\n'
                                                       '- `draft`: `eq` (boolean)\n'
                                                       '- `credit_note'},
                          'sort': {   'type': 'string',
                                      'description': 'You can choose to sort items on specific '
                                                     'attributes\n'
                                                     'Sort field may be prefixed with `-` for '
                                                     'descending order.\n'
                                                     'Example : `id` will sort by ascending order, '
                                                     '`-id` will sort by descending order.\n'
                                                     'Available fields : `id`, `date`\n'},
                          'include': {   'type': 'string',
                                         'description': 'You can choose to include additional related '
                                                        'resources in the response.\n'
                                                        'When specified, related resources will be '
                                                        'returned in a separate `included` section.\n'
                                                        'Available includes: `invoice_lines`\n'
                                                        '\n'
                                                        '⚠️ **Warning**: This feature is currently '
                                                        'experimental and may change or be removed in '
                                                        'future releases.\n'
                                                        'We'}}},
)
async def get_customer_invoices(
    client: PennylaneClient,
    use_2026_api_changes: Optional[Any] = None,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
    filter: Optional[Any] = None,
    sort: Optional[Any] = None,
    include: Optional[Any] = None,
) -> Any:
    url = "/customer_invoices"
    params = {'use_2026_api_changes': use_2026_api_changes, 'cursor': cursor, 'limit': limit, 'filter': filter, 'sort': sort, 'include': include}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_import_customer_invoices",
    description="Import an invoice with file attached. This endpoint allows you to import an invoice. ℹ️ To ensure consistency, **we will apply validations on amounts in accordance with our rounding policy**. We allow a difference up to 1 cent per invoice_line between the total amounts and the sum of invoice lines. For further details, please refer to our [article](https://help.pennylane.com/fr/articles/61575-comprendre-l-arrondi-de-tva-d-un-produit) on rounding policy. > ℹ️ > This endpoint requires the following scope: `customer_invoices:all`",
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
)
async def import_customer_invoices(
    client: PennylaneClient,
    use_2026_api_changes: Optional[Any] = None,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = "/customer_invoices/import"
    params = {'use_2026_api_changes': use_2026_api_changes}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.post(url, data=body)


@tool(
    name="pennylane_create_customer_invoice_e_invoice_import",
    description="Import a customer e-invoice. Import a customer invoice from an e-invoice file (Factur-X format). The file must be a valid Factur-X PDF. Optionally provide `invoice_options` to pre-fill customer and line-level data. Invoice line `e_invoice_line_id` must match Factur-X BT-126 (LineID). > ℹ️ > This endpoint requires the following scope: `customer_invoices:all`",
    input_schema={   'type': 'object',
        'properties': {   'body': {   'type': 'object',
                                      'description': 'Request body payload. See the Pennylane API '
                                                     'reference for the exact schema of this endpoint.',
                                      'additionalProperties': True}},
        'required': ['body']},
)
async def create_customer_invoice_e_invoice_import(
    client: PennylaneClient,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = "/customer_invoices/e_invoices/imports"
    params = None
    return await client.post(url, data=body)


@tool(
    name="pennylane_create_customer_invoice_from_quote",
    description="Create a customer invoice from a quote. This endpoint allows you to create a customer invoice from an existing quote. The invoice will inherit the quote's data (customer, lines, etc.). > ℹ️ > This endpoint requires the following scope: `customer_invoices:all`",
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
)
async def create_customer_invoice_from_quote(
    client: PennylaneClient,
    use_2026_api_changes: Optional[Any] = None,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = "/customer_invoices/create_from_quote"
    params = {'use_2026_api_changes': use_2026_api_changes}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.post(url, data=body)


@tool(
    name="pennylane_get_customer_invoice_invoice_line_sections",
    description="List invoice line sections for a customer invoice. List invoice line sections for a customer invoice > ℹ️ > This endpoint requires one of the following scopes: `customer_invoices:all`, `customer_invoices:readonly`",
    input_schema={   'type': 'object',
        'properties': {   'customer_invoice_id': {'type': 'integer'},
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
        'required': ['customer_invoice_id']},
)
async def get_customer_invoice_invoice_line_sections(
    client: PennylaneClient,
    customer_invoice_id: str,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
    sort: Optional[Any] = None,
) -> Any:
    url = f"/customer_invoices/{customer_invoice_id}/invoice_line_sections".format(customer_invoice_id=customer_invoice_id)
    params = {'cursor': cursor, 'limit': limit, 'sort': sort}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_get_customer_invoice_invoice_lines",
    description="List invoice lines for a customer invoice. List invoice lines for a customer invoice > ℹ️ > This endpoint requires one of the following scopes: `customer_invoices:all`, `customer_invoices:readonly`",
    input_schema={   'type': 'object',
        'properties': {   'customer_invoice_id': {'type': 'integer'},
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
                                                     'Available fields : `id`, `rank`\n'}},
        'required': ['customer_invoice_id']},
)
async def get_customer_invoice_invoice_lines(
    client: PennylaneClient,
    customer_invoice_id: str,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
    sort: Optional[Any] = None,
) -> Any:
    url = f"/customer_invoices/{customer_invoice_id}/invoice_lines".format(customer_invoice_id=customer_invoice_id)
    params = {'cursor': cursor, 'limit': limit, 'sort': sort}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_get_customer_invoice_payments",
    description="List payments for a customer invoice. List payments for a customer invoice > ℹ️ > This endpoint requires one of the following scopes: `customer_invoices:all`, `customer_invoices:readonly`",
    input_schema={   'type': 'object',
        'properties': {   'customer_invoice_id': {'type': 'integer'},
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
        'required': ['customer_invoice_id']},
)
async def get_customer_invoice_payments(
    client: PennylaneClient,
    customer_invoice_id: str,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
    sort: Optional[Any] = None,
) -> Any:
    url = f"/customer_invoices/{customer_invoice_id}/payments".format(customer_invoice_id=customer_invoice_id)
    params = {'cursor': cursor, 'limit': limit, 'sort': sort}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_get_customer_invoice_matched_transactions",
    description="List matched transactions for a customer invoice. List matched transactions for a customer invoice > ℹ️ > This endpoint requires one of the following scopes: `customer_invoices:all`, `customer_invoices:readonly`",
    input_schema={   'type': 'object',
        'properties': {   'customer_invoice_id': {'type': 'integer'},
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
        'required': ['customer_invoice_id']},
)
async def get_customer_invoice_matched_transactions(
    client: PennylaneClient,
    customer_invoice_id: str,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
    sort: Optional[Any] = None,
) -> Any:
    url = f"/customer_invoices/{customer_invoice_id}/matched_transactions".format(customer_invoice_id=customer_invoice_id)
    params = {'cursor': cursor, 'limit': limit, 'sort': sort}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_post_customer_invoice_matched_transactions",
    description="Match a transaction to a customer invoice. This endpoint allows you to match a transaction to a customer invoice. It is not applicable for draft invoices. You can match one transaction with one customer invoice at a time. To match multiple transactions to a customer invoice, you need to call this endpoint multiple times. It's possible to match a transaction to multiple customer invoices too. > ℹ️ > This endpoint requires the following scope: `customer_invoices:all`",
    input_schema={   'type': 'object',
        'properties': {   'customer_invoice_id': {'type': 'integer'},
                          'body': {   'type': 'object',
                                      'description': 'Request body payload. See the Pennylane API '
                                                     'reference for the exact schema of this endpoint.',
                                      'additionalProperties': True}},
        'required': ['customer_invoice_id', 'body']},
)
async def post_customer_invoice_matched_transactions(
    client: PennylaneClient,
    customer_invoice_id: str,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = f"/customer_invoices/{customer_invoice_id}/matched_transactions".format(customer_invoice_id=customer_invoice_id)
    params = None
    return await client.post(url, data=body)


@tool(
    name="pennylane_delete_customer_invoice_matched_transactions",
    description="Unmatch a transaction to a customer invoice. This endpoint allows you to unmatch a transaction to a customer invoice. It is not applicable for draft invoices. > ℹ️ > This endpoint requires the following scope: `customer_invoices:all`",
    input_schema={   'type': 'object',
        'properties': {'customer_invoice_id': {'type': 'integer'}, 'id': {'type': 'integer'}},
        'required': ['customer_invoice_id', 'id']},
)
async def delete_customer_invoice_matched_transactions(
    client: PennylaneClient,
    customer_invoice_id: str,
    id: str,
) -> Any:
    url = f"/customer_invoices/{customer_invoice_id}/matched_transactions/{id}".format(customer_invoice_id=customer_invoice_id, id=id)
    params = None
    return await client.delete(url)


@tool(
    name="pennylane_get_customer_invoice_appendices",
    description="List appendices of a customer invoice. List appendices of a customer invoice > ℹ️ > This endpoint requires one of the following scopes: `customer_invoices:all`, `customer_invoices:readonly`",
    input_schema={   'type': 'object',
        'properties': {   'customer_invoice_id': {'type': 'integer'},
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
        'required': ['customer_invoice_id']},
)
async def get_customer_invoice_appendices(
    client: PennylaneClient,
    customer_invoice_id: str,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
) -> Any:
    url = f"/customer_invoices/{customer_invoice_id}/appendices".format(customer_invoice_id=customer_invoice_id)
    params = {'cursor': cursor, 'limit': limit}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_post_customer_invoice_appendices",
    description="Upload an appendix for a customer invoice. Upload a file that will be an appendix attached to a customer invoice. Note that this will not upload a file into the DMS (GED). > ℹ️ > This endpoint requires the following scope: `customer_invoices:all`",
    input_schema={   'type': 'object',
        'properties': {   'customer_invoice_id': {'type': 'integer'},
                          'body': {   'type': 'object',
                                      'description': 'Request body payload. See the Pennylane API '
                                                     'reference for the exact schema of this endpoint.',
                                      'additionalProperties': True}},
        'required': ['customer_invoice_id', 'body']},
)
async def post_customer_invoice_appendices(
    client: PennylaneClient,
    customer_invoice_id: str,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = f"/customer_invoices/{customer_invoice_id}/appendices".format(customer_invoice_id=customer_invoice_id)
    params = None
    return await client.post(url, data=body)


@tool(
    name="pennylane_get_customer_invoice",
    description="Retrieve a customer invoice. Retrieve a customer invoice or a credit note > ℹ️ > This endpoint requires one of the following scopes: `customer_invoices:all`, `customer_invoices:readonly`",
    input_schema={   'type': 'object',
        'properties': {   'id': {   'type': 'integer',
                                    'description': 'The unique identifier of the customer invoice'},
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
)
async def get_customer_invoice(
    client: PennylaneClient,
    id: str,
    use_2026_api_changes: Optional[Any] = None,
) -> Any:
    url = f"/customer_invoices/{id}".format(id=id)
    params = {'use_2026_api_changes': use_2026_api_changes}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_update_customer_invoice",
    description="Update a customer invoice. Update a customer invoice > ℹ️ > This endpoint requires the following scope: `customer_invoices:all`",
    input_schema={   'type': 'object',
        'properties': {   'id': {   'type': 'integer',
                                    'description': 'The unique identifier of the customer invoice'},
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
)
async def update_customer_invoice(
    client: PennylaneClient,
    id: str,
    use_2026_api_changes: Optional[Any] = None,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = f"/customer_invoices/{id}".format(id=id)
    params = {'use_2026_api_changes': use_2026_api_changes}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.put(url, data=body)


@tool(
    name="pennylane_delete_customer_invoices",
    description="Delete draft invoice. Delete a draft customer invoice or draft credit note > ℹ️ > This endpoint requires the following scope: `customer_invoices:all`",
    input_schema={   'type': 'object',
        'properties': {   'id': {   'type': 'integer',
                                    'description': 'The unique identifier of the customer invoice'}},
        'required': ['id']},
)
async def delete_customer_invoices(
    client: PennylaneClient,
    id: str,
) -> Any:
    url = f"/customer_invoices/{id}".format(id=id)
    params = None
    return await client.delete(url)


@tool(
    name="pennylane_mark_as_paid_customer_invoice",
    description="Mark a customer invoice as paid. Mark a customer invoice as paid. No automatic reconciliation will be done once the invoice is marked as paid > ℹ️ > This endpoint requires the following scope: `customer_invoices:all`",
    input_schema={   'type': 'object',
        'properties': {   'id': {   'type': 'integer',
                                    'description': 'The unique identifier of the customer invoice'}},
        'required': ['id']},
)
async def mark_as_paid_customer_invoice(
    client: PennylaneClient,
    id: str,
) -> Any:
    url = f"/customer_invoices/{id}/mark_as_paid".format(id=id)
    params = None
    return await client.put(url, data=body)


@tool(
    name="pennylane_send_by_email_customer_invoice",
    description="Send a customer invoice by email. This endpoint allows you to send a finalized, imported customer invoice or credit note by email to your customer. This requires that the PDF file for that document has been generated (this process can take a few minutes), so if you just created the invoice in our system, we may return a 409 error. You should retry the request in a few minutes - if you receive a 204 response, that means that the email is on its way. For more information about email sending, please read [this guide](https://pen...",
    input_schema={   'type': 'object',
        'properties': {   'id': {   'type': 'integer',
                                    'description': 'The unique identifier of the customer invoice'},
                          'body': {   'type': 'object',
                                      'description': 'Request body payload. See the Pennylane API '
                                                     'reference for the exact schema of this endpoint.',
                                      'additionalProperties': True}},
        'required': ['id']},
)
async def send_by_email_customer_invoice(
    client: PennylaneClient,
    id: str,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = f"/customer_invoices/{id}/send_by_email".format(id=id)
    params = None
    return await client.post(url, data=body)


@tool(
    name="pennylane_get_customer_invoice_categories",
    description="List categories of a customer invoice. List categories of a customer invoice > ℹ️ > This endpoint requires one of the following scopes: `customer_invoices:all`, `customer_invoices:readonly`",
    input_schema={   'type': 'object',
        'properties': {   'customer_invoice_id': {'type': 'integer'},
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
        'required': ['customer_invoice_id']},
)
async def get_customer_invoice_categories(
    client: PennylaneClient,
    customer_invoice_id: str,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
) -> Any:
    url = f"/customer_invoices/{customer_invoice_id}/categories".format(customer_invoice_id=customer_invoice_id)
    params = {'cursor': cursor, 'limit': limit}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_put_customer_invoice_categories",
    description="Categorize a customer invoice. This endpoint is not applicable for draft invoices. Update the categories of a customer invoice. You can pass categories that don't belong to the same category group. The sum of categories of a same group must equal `1`. In the following example, the two first categories belong to the same category group A, the sum of the weights is `1`. The third category belongs to a category group B, its weight is `1`. ``` [ { 'id': 59, 'weight': '0.5' }, // category group A { 'id': 33, 'weight': '0.5' }, ...",
    input_schema={   'type': 'object',
        'properties': {   'customer_invoice_id': {'type': 'integer'},
                          'body': {   'type': 'object',
                                      'description': 'Request body payload. See the Pennylane API '
                                                     'reference for the exact schema of this endpoint.',
                                      'additionalProperties': True}},
        'required': ['customer_invoice_id', 'body']},
)
async def put_customer_invoice_categories(
    client: PennylaneClient,
    customer_invoice_id: str,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = f"/customer_invoices/{customer_invoice_id}/categories".format(customer_invoice_id=customer_invoice_id)
    params = None
    return await client.put(url, data=body)


@tool(
    name="pennylane_update_imported_customer_invoice",
    description="Update an Imported customer invoice. Update an imported customer invoice or credit note. It is not applicable for draft invoices. > ℹ️ > This endpoint requires the following scope: `customer_invoices:all`",
    input_schema={   'type': 'object',
        'properties': {   'id': {   'type': 'integer',
                                    'description': 'The ID of the imported customer invoice'},
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
)
async def update_imported_customer_invoice(
    client: PennylaneClient,
    id: str,
    use_2026_api_changes: Optional[Any] = None,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = f"/customer_invoices/{id}/update_imported".format(id=id)
    params = {'use_2026_api_changes': use_2026_api_changes}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.put(url, data=body)


@tool(
    name="pennylane_finalize_customer_invoice",
    description="Turn the draft invoice into a finalized invoice.. Convert the draft customer invoice or credit note into a finalized one. Once finalized, the resource can no longer be edited. > ℹ️ > This endpoint requires the following scope: `customer_invoices:all`",
    input_schema={   'type': 'object',
        'properties': {   'id': {   'type': 'integer',
                                    'description': 'The unique identifier of the customer invoice'},
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
)
async def finalize_customer_invoice(
    client: PennylaneClient,
    id: str,
    use_2026_api_changes: Optional[Any] = None,
) -> Any:
    url = f"/customer_invoices/{id}/finalize".format(id=id)
    params = {'use_2026_api_changes': use_2026_api_changes}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.put(url, data=body)


@tool(
    name="pennylane_link_credit_note",
    description="Link a credit note to a customer invoice. Link a credit note to a customer invoice > ℹ️ > This endpoint requires the following scope: `customer_invoices:all`",
    input_schema={   'type': 'object',
        'properties': {   'id': {   'type': 'integer',
                                    'description': 'The unique identifier of the customer invoice'},
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
)
async def link_credit_note(
    client: PennylaneClient,
    id: str,
    use_2026_api_changes: Optional[Any] = None,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = f"/customer_invoices/{id}/link_credit_note".format(id=id)
    params = {'use_2026_api_changes': use_2026_api_changes}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.post(url, data=body)


@tool(
    name="pennylane_get_customer_invoice_custom_header_fields",
    description="List custom header fields for a customer invoice. List custom header fields for a customer invoice > ℹ️ > This endpoint requires one of the following scopes: `customer_invoices:all`, `customer_invoices:readonly`",
    input_schema={   'type': 'object',
        'properties': {   'customer_invoice_id': {'type': 'integer'},
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
        'required': ['customer_invoice_id']},
)
async def get_customer_invoice_custom_header_fields(
    client: PennylaneClient,
    customer_invoice_id: str,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
    sort: Optional[Any] = None,
) -> Any:
    url = f"/customer_invoices/{customer_invoice_id}/custom_header_fields".format(customer_invoice_id=customer_invoice_id)
    params = {'cursor': cursor, 'limit': limit, 'sort': sort}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


