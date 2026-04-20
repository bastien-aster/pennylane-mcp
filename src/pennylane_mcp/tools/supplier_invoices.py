"""Auto-generated from docs/pennylane-openapi.json. Do not edit by hand.

Regenerate with: python scripts/generate_tools.py
"""
from typing import Any, Optional

from .._registry import tool
from ..client import PennylaneClient


@tool(
    name="pennylane_get_supplier_invoice_lines",
    description="List invoice lines for a supplier invoice. List invoice lines for a supplier invoice > ℹ️ > This endpoint requires one of the following scopes: `supplier_invoices:all`, `supplier_invoices:readonly`",
    input_schema={   'type': 'object',
        'properties': {   'supplier_invoice_id': {'type': 'integer'},
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
        'required': ['supplier_invoice_id']},
)
async def get_supplier_invoice_lines(
    client: PennylaneClient,
    supplier_invoice_id: str,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
    sort: Optional[Any] = None,
) -> Any:
    url = f"/supplier_invoices/{supplier_invoice_id}/invoice_lines".format(supplier_invoice_id=supplier_invoice_id)
    params = {'cursor': cursor, 'limit': limit, 'sort': sort}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_get_supplier_invoices",
    description="List supplier invoices. This endpoint returns a list of supplier invoices. > ℹ️ > This endpoint requires one of the following scopes: `supplier_invoices:all`, `supplier_invoices:readonly`",
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
                                                       '- `id`: `lt`, `lteq`, `gt`, `gteq`, `eq`, '
                                                       '`not_eq`, `in`, `not_in`\n'
                                                       '- `supplier_id`: `lt`, `lteq`, `gt`, `gteq`, '
                                                       '`eq`, `not_eq`, `in`, `not_in`\n'
                                                       '- `invoice_number`: `eq`, `not_eq`, `in`, '
                                                       '`not_in`\n'
                                                       '- `date`: `lt`, `lteq`, `g'},
                          'sort': {   'type': 'string',
                                      'description': 'You can choose to sort items on specific '
                                                     'attributes\n'
                                                     'Sort field may be prefixed with `-` for '
                                                     'descending order.\n'
                                                     'Example : `id` will sort by ascending order, '
                                                     '`-id` will sort by descending order.\n'
                                                     'Available fields : `id`, `date`\n'}}},
)
async def get_supplier_invoices(
    client: PennylaneClient,
    use_2026_api_changes: Optional[Any] = None,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
    filter: Optional[Any] = None,
    sort: Optional[Any] = None,
) -> Any:
    url = "/supplier_invoices"
    params = {'use_2026_api_changes': use_2026_api_changes, 'cursor': cursor, 'limit': limit, 'filter': filter, 'sort': sort}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_get_supplier_invoice",
    description="Retrieve a supplier invoice. This endpoint returns a supplier invoice. > ℹ️ > This endpoint requires one of the following scopes: `supplier_invoices:all`, `supplier_invoices:readonly`",
    input_schema={   'type': 'object',
        'properties': {   'id': {'type': 'integer', 'description': 'Supplier invoice identifier'},
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
async def get_supplier_invoice(
    client: PennylaneClient,
    id: str,
    use_2026_api_changes: Optional[Any] = None,
) -> Any:
    url = f"/supplier_invoices/{id}".format(id=id)
    params = {'use_2026_api_changes': use_2026_api_changes}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_put_supplier_invoice",
    description="Update a supplier invoice. This endpoint allows you to update a supplier invoice. > ℹ️ > This endpoint requires the following scope: `supplier_invoices:all`",
    input_schema={   'type': 'object',
        'properties': {   'id': {'type': 'integer', 'description': 'Supplier invoice identifier'},
                          'body': {   'type': 'object',
                                      'description': 'Request body payload. See the Pennylane API '
                                                     'reference for the exact schema of this endpoint.',
                                      'additionalProperties': True}},
        'required': ['id', 'body']},
)
async def put_supplier_invoice(
    client: PennylaneClient,
    id: str,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = f"/supplier_invoices/{id}".format(id=id)
    params = None
    return await client.put(url, data=body)


@tool(
    name="pennylane_get_supplier_invoice_categories",
    description="List categories of a supplier invoice. List categories of a supplier invoice > ℹ️ > This endpoint requires one of the following scopes: `supplier_invoices:all`, `supplier_invoices:readonly`",
    input_schema={   'type': 'object',
        'properties': {   'supplier_invoice_id': {'type': 'integer'},
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
        'required': ['supplier_invoice_id']},
)
async def get_supplier_invoice_categories(
    client: PennylaneClient,
    supplier_invoice_id: str,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
) -> Any:
    url = f"/supplier_invoices/{supplier_invoice_id}/categories".format(supplier_invoice_id=supplier_invoice_id)
    params = {'cursor': cursor, 'limit': limit}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_put_supplier_invoice_categories",
    description="Categorize a supplier invoice. Update the categories of a supplier invoice. You can pass categories that don't belong to the same category group. The sum of categories of a same group must equal `1`. In the following example, the two first categories belong to the same category group A, the sum of the weights is `1`. The third category belongs to a category group B, its weight is `1`. ``` [ { 'id': 59, 'weight': '0.5' }, // category group A { 'id': 33, 'weight': '0.5' }, // category group A { 'id': 65, 'weight': '1' } // c...",
    input_schema={   'type': 'object',
        'properties': {   'supplier_invoice_id': {'type': 'integer'},
                          'body': {   'type': 'object',
                                      'description': 'Request body payload. See the Pennylane API '
                                                     'reference for the exact schema of this endpoint.',
                                      'additionalProperties': True}},
        'required': ['supplier_invoice_id', 'body']},
)
async def put_supplier_invoice_categories(
    client: PennylaneClient,
    supplier_invoice_id: str,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = f"/supplier_invoices/{supplier_invoice_id}/categories".format(supplier_invoice_id=supplier_invoice_id)
    params = None
    return await client.put(url, data=body)


@tool(
    name="pennylane_get_supplier_invoice_payments",
    description="List payments for a supplier invoice. List payments for a supplier invoice > ℹ️ > This endpoint requires one of the following scopes: `supplier_invoices:all`, `supplier_invoices:readonly`",
    input_schema={   'type': 'object',
        'properties': {   'supplier_invoice_id': {'type': 'integer'},
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
        'required': ['supplier_invoice_id']},
)
async def get_supplier_invoice_payments(
    client: PennylaneClient,
    supplier_invoice_id: str,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
    sort: Optional[Any] = None,
) -> Any:
    url = f"/supplier_invoices/{supplier_invoice_id}/payments".format(supplier_invoice_id=supplier_invoice_id)
    params = {'cursor': cursor, 'limit': limit, 'sort': sort}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_update_supplier_invoice_payment_status",
    description="Update a supplier invoice payment status. This endpoint allows you to update the payment status of a supplier invoice. > ℹ️ > This endpoint requires the following scope: `supplier_invoices:all`",
    input_schema={   'type': 'object',
        'properties': {   'supplier_invoice_id': {   'type': 'integer',
                                                     'description': 'Supplier invoice identifier'},
                          'body': {   'type': 'object',
                                      'description': 'Request body payload. See the Pennylane API '
                                                     'reference for the exact schema of this endpoint.',
                                      'additionalProperties': True}},
        'required': ['supplier_invoice_id', 'body']},
)
async def update_supplier_invoice_payment_status(
    client: PennylaneClient,
    supplier_invoice_id: str,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = f"/supplier_invoices/{supplier_invoice_id}/payment_status".format(supplier_invoice_id=supplier_invoice_id)
    params = None
    return await client.put(url, data=body)


@tool(
    name="pennylane_get_supplier_invoice_matched_transactions",
    description="List matched transactions for a supplier invoice. List matched transactions for a supplier invoice > ℹ️ > This endpoint requires one of the following scopes: `supplier_invoices:all`, `supplier_invoices:readonly`",
    input_schema={   'type': 'object',
        'properties': {   'supplier_invoice_id': {'type': 'integer'},
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
        'required': ['supplier_invoice_id']},
)
async def get_supplier_invoice_matched_transactions(
    client: PennylaneClient,
    supplier_invoice_id: str,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
    sort: Optional[Any] = None,
) -> Any:
    url = f"/supplier_invoices/{supplier_invoice_id}/matched_transactions".format(supplier_invoice_id=supplier_invoice_id)
    params = {'cursor': cursor, 'limit': limit, 'sort': sort}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_post_supplier_invoice_matched_transactions",
    description="Match a transaction to a supplier invoice. This endpoint allows you to match a transaction to a supplier invoice. You can match one transaction with one supplier invoice at a time. To match multiple transactions to a supplier invoice, you need to call this endpoint multiple times. It's possible to match a transaction to multiple supplier invoices too. > ℹ️ > This endpoint requires the following scope: `supplier_invoices:all`",
    input_schema={   'type': 'object',
        'properties': {   'supplier_invoice_id': {'type': 'integer'},
                          'body': {   'type': 'object',
                                      'description': 'Request body payload. See the Pennylane API '
                                                     'reference for the exact schema of this endpoint.',
                                      'additionalProperties': True}},
        'required': ['supplier_invoice_id', 'body']},
)
async def post_supplier_invoice_matched_transactions(
    client: PennylaneClient,
    supplier_invoice_id: str,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = f"/supplier_invoices/{supplier_invoice_id}/matched_transactions".format(supplier_invoice_id=supplier_invoice_id)
    params = None
    return await client.post(url, data=body)


@tool(
    name="pennylane_delete_supplier_invoice_matched_transactions",
    description="Unmatch a transaction to a supplier invoice. This endpoint allows you to unmatch a transaction to a supplier invoice. > ℹ️ > This endpoint requires the following scope: `supplier_invoices:all`",
    input_schema={   'type': 'object',
        'properties': {'supplier_invoice_id': {'type': 'integer'}, 'id': {'type': 'integer'}},
        'required': ['supplier_invoice_id', 'id']},
)
async def delete_supplier_invoice_matched_transactions(
    client: PennylaneClient,
    supplier_invoice_id: str,
    id: str,
) -> Any:
    url = f"/supplier_invoices/{supplier_invoice_id}/matched_transactions/{id}".format(supplier_invoice_id=supplier_invoice_id, id=id)
    params = None
    return await client.delete(url)


@tool(
    name="pennylane_post_supplier_invoice_linked_purchase_requests",
    description="Link a purchase request to a supplier invoice. This endpoint allows you to link a purchase request to a supplier invoice. You can link one purchase request with one supplier invoice at a time. To link multiple purchase request to a supplier invoice, you need to call this endpoint multiple times. It's possible to link a purchase request to multiple supplier invoices too. > ℹ️ > This endpoint requires the following scope: `supplier_invoices:all`",
    input_schema={   'type': 'object',
        'properties': {   'supplier_invoice_id': {'type': 'integer'},
                          'body': {   'type': 'object',
                                      'description': 'Request body payload. See the Pennylane API '
                                                     'reference for the exact schema of this endpoint.',
                                      'additionalProperties': True}},
        'required': ['supplier_invoice_id', 'body']},
)
async def post_supplier_invoice_linked_purchase_requests(
    client: PennylaneClient,
    supplier_invoice_id: str,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = f"/supplier_invoices/{supplier_invoice_id}/linked_purchase_requests".format(supplier_invoice_id=supplier_invoice_id)
    params = None
    return await client.post(url, data=body)


@tool(
    name="pennylane_import_supplier_invoice",
    description="Import a supplier invoice with a file attached. This endpoint allows you to import a supplier invoice with a file attached. > ℹ️ > This endpoint requires the following scope: `supplier_invoices:all`",
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
async def import_supplier_invoice(
    client: PennylaneClient,
    use_2026_api_changes: Optional[Any] = None,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = "/supplier_invoices/import"
    params = {'use_2026_api_changes': use_2026_api_changes}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.post(url, data=body)


@tool(
    name="pennylane_create_supplier_invoice_e_invoice_import",
    description="Import a supplier e-invoice. Import a supplier invoice from an e-invoice file (Factur-X format). The file must be a valid Factur-X PDF. Optionally provide `invoice_options` to pre-fill supplier and line-level data. Invoice line `e_invoice_line_id` must match Factur-X BT-126 (LineID). > ℹ️ > This endpoint requires the following scope: `supplier_invoices:all`",
    input_schema={   'type': 'object',
        'properties': {   'body': {   'type': 'object',
                                      'description': 'Request body payload. See the Pennylane API '
                                                     'reference for the exact schema of this endpoint.',
                                      'additionalProperties': True}},
        'required': ['body']},
)
async def create_supplier_invoice_e_invoice_import(
    client: PennylaneClient,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = "/supplier_invoices/e_invoices/imports"
    params = None
    return await client.post(url, data=body)


@tool(
    name="pennylane_validate_accounting_supplier_invoice",
    description="Validate the accounting of a supplier invoice. Turn the supplier invoice into a Complete state. > ℹ️ > This endpoint requires the following scope: `supplier_invoices:all`",
    input_schema={   'type': 'object',
        'properties': {   'id': {'type': 'integer'},
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
async def validate_accounting_supplier_invoice(
    client: PennylaneClient,
    id: str,
    use_2026_api_changes: Optional[Any] = None,
) -> Any:
    url = f"/supplier_invoices/{id}/validate_accounting".format(id=id)
    params = {'use_2026_api_changes': use_2026_api_changes}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.put(url, data=body)


@tool(
    name="pennylane_put_supplier_invoice_e_invoice_status",
    description="Update e-invoice status for a supplier invoice. Applies an electronic invoicing lifecycle transition: dispute, refuse, or undispute (approved). Dispute and refuse require a reason. > ℹ️ > This endpoint requires the following scope: `supplier_invoices:all`",
    input_schema={   'type': 'object',
        'properties': {   'supplier_invoice_id': {'type': 'integer'},
                          'body': {   'type': 'object',
                                      'description': 'Request body payload. See the Pennylane API '
                                                     'reference for the exact schema of this endpoint.',
                                      'additionalProperties': True}},
        'required': ['supplier_invoice_id', 'body']},
)
async def put_supplier_invoice_e_invoice_status(
    client: PennylaneClient,
    supplier_invoice_id: str,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = f"/supplier_invoices/{supplier_invoice_id}/e_invoice_status".format(supplier_invoice_id=supplier_invoice_id)
    params = None
    return await client.put(url, data=body)


