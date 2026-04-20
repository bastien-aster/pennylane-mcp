"""Auto-generated from docs/pennylane-openapi.json. Do not edit by hand.

Regenerate with: python scripts/generate_tools.py
"""
from typing import Any, Optional

from .._registry import tool
from ..client import PennylaneClient


@tool(
    name="pennylane_get_customer_invoices_changes",
    description="Get customer invoices changes events. Returns the list of changes based on the provided `start_date`. If no `start_date` is provided it returns the oldest set of recorded changes. Changes for the last 4 weeks are retained. The items will be returned using `processed_at` in ASC order (oldest first). > ℹ️ > This endpoint requires one of the following scopes: `customer_invoices:all`, `customer_invoices:readonly`",
    input_schema={   'type': 'object',
        'properties': {   'cursor': {   'type': 'string',
                                        'description': 'Cursor for pagination. Use this to fetch the '
                                                       'next set of results. The cursor is an opaque '
                                                       "string returned in the previous response's "
                                                       'metadata. Leave empty for the first request.'},
                          'limit': {   'type': 'integer',
                                       'description': 'Number of items to return per request.\n'
                                                      'Defaults to 20 if not specified.\n'
                                                      'Must be between 1 and 1000.\n'},
                          'start_date': {   'type': 'string',
                                            'description': 'Filter the changes based on the event '
                                                           'date. The date should follow RFC3339 '
                                                           'format. If no date is provided, the oldest '
                                                           'changes will be returned. Changes for the '
                                                           'last 4 weeks are retained, thus providing '
                                                           'a `start_date` older than that will result '
                                                           'in a 422 response. Providing both '
                                                           '`start_date` and `cur'}}},
)
async def get_customer_invoices_changes(
    client: PennylaneClient,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
    start_date: Optional[Any] = None,
) -> Any:
    url = "/changelogs/customer_invoices"
    params = {'cursor': cursor, 'limit': limit, 'start_date': start_date}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_get_supplier_invoices_changes",
    description="Get supplier invoices changes events. Returns the list of changes based on the provided `start_date`. If no `start_date` is provided it returns the oldest set of recorded changes. Changes for the last 4 weeks are retained. The items will be returned using `processed_at` in ASC order (oldest first). > ℹ️ > This endpoint requires one of the following scopes: `supplier_invoices:all`, `supplier_invoices:readonly`",
    input_schema={   'type': 'object',
        'properties': {   'cursor': {   'type': 'string',
                                        'description': 'Cursor for pagination. Use this to fetch the '
                                                       'next set of results. The cursor is an opaque '
                                                       "string returned in the previous response's "
                                                       'metadata. Leave empty for the first request.'},
                          'limit': {   'type': 'integer',
                                       'description': 'Number of items to return per request.\n'
                                                      'Defaults to 20 if not specified.\n'
                                                      'Must be between 1 and 1000.\n'},
                          'start_date': {   'type': 'string',
                                            'description': 'Filter the changes based on the event '
                                                           'date. The date should follow RFC3339 '
                                                           'format. If no date is provided, the oldest '
                                                           'changes will be returned. Changes for the '
                                                           'last 4 weeks are retained, thus providing '
                                                           'a `start_date` older than that will result '
                                                           'in a 422 response. Providing both '
                                                           '`start_date` and `cur'}}},
)
async def get_supplier_invoices_changes(
    client: PennylaneClient,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
    start_date: Optional[Any] = None,
) -> Any:
    url = "/changelogs/supplier_invoices"
    params = {'cursor': cursor, 'limit': limit, 'start_date': start_date}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_get_customer_changes",
    description="Get customer changes events. Returns the list of changes based on the provided `start_date`. If no `start_date` is provided it returns the oldest set of recorded changes. Changes for the last 4 weeks are retained. The items will be returned using `processed_at` in ASC order (oldest first). > ℹ️ > This endpoint requires one of the following scopes: `customers:all`, `customers:readonly`",
    input_schema={   'type': 'object',
        'properties': {   'cursor': {   'type': 'string',
                                        'description': 'Cursor for pagination. Use this to fetch the '
                                                       'next set of results. The cursor is an opaque '
                                                       "string returned in the previous response's "
                                                       'metadata. Leave empty for the first request.'},
                          'limit': {   'type': 'integer',
                                       'description': 'Number of items to return per request.\n'
                                                      'Defaults to 20 if not specified.\n'
                                                      'Must be between 1 and 1000.\n'},
                          'start_date': {   'type': 'string',
                                            'description': 'Filter the changes based on the event '
                                                           'date. The date should follow RFC3339 '
                                                           'format. If no date is provided, the oldest '
                                                           'changes will be returned. Changes for the '
                                                           'last 4 weeks are retained, thus providing '
                                                           'a `start_date` older than that will result '
                                                           'in a 422 response. Providing both '
                                                           '`start_date` and `cur'}}},
)
async def get_customer_changes(
    client: PennylaneClient,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
    start_date: Optional[Any] = None,
) -> Any:
    url = "/changelogs/customers"
    params = {'cursor': cursor, 'limit': limit, 'start_date': start_date}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_get_supplier_changes",
    description="Get supplier changes events. Returns the list of changes based on the provided `start_date`. If no `start_date` is provided it returns the oldest set of recorded changes. Changes for the last 4 weeks are retained. The items will be returned using `processed_at` in ASC order (oldest first). > ℹ️ > This endpoint requires one of the following scopes: `suppliers:all`, `suppliers:readonly`",
    input_schema={   'type': 'object',
        'properties': {   'cursor': {   'type': 'string',
                                        'description': 'Cursor for pagination. Use this to fetch the '
                                                       'next set of results. The cursor is an opaque '
                                                       "string returned in the previous response's "
                                                       'metadata. Leave empty for the first request.'},
                          'limit': {   'type': 'integer',
                                       'description': 'Number of items to return per request.\n'
                                                      'Defaults to 20 if not specified.\n'
                                                      'Must be between 1 and 1000.\n'},
                          'start_date': {   'type': 'string',
                                            'description': 'Filter the changes based on the event '
                                                           'date. The date should follow RFC3339 '
                                                           'format. If no date is provided, the oldest '
                                                           'changes will be returned. Changes for the '
                                                           'last 4 weeks are retained, thus providing '
                                                           'a `start_date` older than that will result '
                                                           'in a 422 response. Providing both '
                                                           '`start_date` and `cur'}}},
)
async def get_supplier_changes(
    client: PennylaneClient,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
    start_date: Optional[Any] = None,
) -> Any:
    url = "/changelogs/suppliers"
    params = {'cursor': cursor, 'limit': limit, 'start_date': start_date}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_get_product_changes",
    description="Get product change events. Returns the list of changes based on the provided `start_date`. If no `start_date` is provided it returns the oldest set of recorded changes. Changes for the last 4 weeks are retained. The items will be returned using `processed_at` in ASC order (oldest first). > ℹ️ > This endpoint requires one of the following scopes: `products:all`, `products:readonly`",
    input_schema={   'type': 'object',
        'properties': {   'cursor': {   'type': 'string',
                                        'description': 'Cursor for pagination. Use this to fetch the '
                                                       'next set of results. The cursor is an opaque '
                                                       "string returned in the previous response's "
                                                       'metadata. Leave empty for the first request.'},
                          'limit': {   'type': 'integer',
                                       'description': 'Number of items to return per request.\n'
                                                      'Defaults to 20 if not specified.\n'
                                                      'Must be between 1 and 1000.\n'},
                          'start_date': {   'type': 'string',
                                            'description': 'Filter the changes based on the event '
                                                           'date. The date should follow RFC3339 '
                                                           'format. If no date is provided, the oldest '
                                                           'changes will be returned. Changes for the '
                                                           'last 4 weeks are retained, thus providing '
                                                           'a `start_date` older than that will result '
                                                           'in a 422 response. Providing both '
                                                           '`start_date` and `cur'}}},
)
async def get_product_changes(
    client: PennylaneClient,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
    start_date: Optional[Any] = None,
) -> Any:
    url = "/changelogs/products"
    params = {'cursor': cursor, 'limit': limit, 'start_date': start_date}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_get_ledger_entry_line_changes",
    description="Get ledger entry line change events. Returns the list of changes based on the provided `start_date`. If no `start_date` is provided it returns the oldest set of recorded changes. Changes for the last 4 weeks are retained. The items will be returned using `processed_at` in ASC order (oldest first). **NEW BEHAVIOR :** The old `ledger` scope will only work on the old behavior system. As soon as you opt in to the new version, or when the sunset phase starts and you haven't explicitly opted out of the old behavior, the ledger scope w...",
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
                                                       'next set of results. The cursor is an opaque '
                                                       "string returned in the previous response's "
                                                       'metadata. Leave empty for the first request.'},
                          'limit': {   'type': 'integer',
                                       'description': 'Number of items to return per request.\n'
                                                      'Defaults to 20 if not specified.\n'
                                                      'Must be between 1 and 1000.\n'},
                          'start_date': {   'type': 'string',
                                            'description': 'Filter the changes based on the event '
                                                           'date. The date should follow RFC3339 '
                                                           'format. If no date is provided, the oldest '
                                                           'changes will be returned. Changes for the '
                                                           'last 4 weeks are retained, thus providing '
                                                           'a `start_date` older than that will result '
                                                           'in a 422 response. Providing both '
                                                           '`start_date` and `cur'}}},
)
async def get_ledger_entry_line_changes(
    client: PennylaneClient,
    use_2026_api_changes: Optional[Any] = None,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
    start_date: Optional[Any] = None,
) -> Any:
    url = "/changelogs/ledger_entry_lines"
    params = {'use_2026_api_changes': use_2026_api_changes, 'cursor': cursor, 'limit': limit, 'start_date': start_date}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_get_transaction_changes",
    description="Get transaction change events. Returns the list of changes based on the provided `start_date`. If no `start_date` is provided it returns the oldest set of recorded changes. Changes for the last 4 weeks are retained. The items will be returned using `processed_at` in ASC order (oldest first). > ℹ️ > This endpoint requires one of the following scopes: `transactions:all`, `transactions:readonly`",
    input_schema={   'type': 'object',
        'properties': {   'cursor': {   'type': 'string',
                                        'description': 'Cursor for pagination. Use this to fetch the '
                                                       'next set of results. The cursor is an opaque '
                                                       "string returned in the previous response's "
                                                       'metadata. Leave empty for the first request.'},
                          'limit': {   'type': 'integer',
                                       'description': 'Number of items to return per request.\n'
                                                      'Defaults to 20 if not specified.\n'
                                                      'Must be between 1 and 1000.\n'},
                          'start_date': {   'type': 'string',
                                            'description': 'Filter the changes based on the event '
                                                           'date. The date should follow RFC3339 '
                                                           'format. If no date is provided, the oldest '
                                                           'changes will be returned. Changes for the '
                                                           'last 4 weeks are retained, thus providing '
                                                           'a `start_date` older than that will result '
                                                           'in a 422 response. Providing both '
                                                           '`start_date` and `cur'}}},
)
async def get_transaction_changes(
    client: PennylaneClient,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
    start_date: Optional[Any] = None,
) -> Any:
    url = "/changelogs/transactions"
    params = {'cursor': cursor, 'limit': limit, 'start_date': start_date}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_get_quote_changes",
    description="Get quotes changes events. Returns the list of changes based on the provided `start_date`. If no `start_date` is provided it returns the oldest set of recorded changes. Changes for the last 4 weeks are retained. The items will be returned using `processed_at` in ASC order (oldest first). > ℹ️ > This endpoint requires one of the following scopes: `quotes:all`, `quotes:readonly`",
    input_schema={   'type': 'object',
        'properties': {   'cursor': {   'type': 'string',
                                        'description': 'Cursor for pagination. Use this to fetch the '
                                                       'next set of results. The cursor is an opaque '
                                                       "string returned in the previous response's "
                                                       'metadata. Leave empty for the first request.'},
                          'limit': {   'type': 'integer',
                                       'description': 'Number of items to return per request.\n'
                                                      'Defaults to 20 if not specified.\n'
                                                      'Must be between 1 and 1000.\n'},
                          'start_date': {   'type': 'string',
                                            'description': 'Filter the changes based on the event '
                                                           'date. The date should follow RFC3339 '
                                                           'format. If no date is provided, the oldest '
                                                           'changes will be returned. Changes for the '
                                                           'last 4 weeks are retained, thus providing '
                                                           'a `start_date` older than that will result '
                                                           'in a 422 response. Providing both '
                                                           '`start_date` and `cur'}}},
)
async def get_quote_changes(
    client: PennylaneClient,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
    start_date: Optional[Any] = None,
) -> Any:
    url = "/changelogs/quotes"
    params = {'cursor': cursor, 'limit': limit, 'start_date': start_date}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


