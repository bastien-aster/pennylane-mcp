"""Auto-generated from docs/pennylane-openapi.json. Do not edit by hand.

Regenerate with: python scripts/generate_tools.py
"""
from typing import Any, Optional

from .._registry import tool
from ..client import PennylaneClient


@tool(
    name="pennylane_get_transactions",
    description="[Banking · Bank Transactions / Transactions bancaires] List transactions List transactions > ℹ️ > This endpoint requires one of the following scopes: `transactions:readonly`, `transactions:all` Mots-clés FR: transaction bancaire, opération bancaire, mouvement.",
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
                                                       '- `id`: `eq`, `not_eq`, `in`, `not_in`\n'
                                                       '- `bank_account_id`: `eq`, `not_eq`, `in`, '
                                                       '`not_in`\n'
                                                       '- `journal_id`: `eq`, `not_eq`, `in`, '
                                                       '`not_in`\n'
                                                       '- `date`: `eq`, `not_eq`, `gt`, `lt`, `lteq`, '
                                                       '`gteq`\n'},
                          'sort': {   'type': 'string',
                                      'description': 'You can choose to sort items on specific '
                                                     'attributes\n'
                                                     'Sort field may be prefixed with `-` for '
                                                     'descending order.\n'
                                                     'Example : `id` will sort by ascending order, '
                                                     '`-id` will sort by descending order.\n'
                                                     'Available fields : `id`\n'}}},
    resource="transactions",
)
async def get_transactions(
    client: PennylaneClient,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
    filter: Optional[Any] = None,
    sort: Optional[Any] = None,
) -> Any:
    url = "/transactions"
    params = {'cursor': cursor, 'limit': limit, 'filter': filter, 'sort': sort}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_create_transaction",
    description="[Banking · Bank Transactions / Transactions bancaires] Create a transaction Create a banking transaction > ℹ️ > This endpoint requires the following scope: `transactions:all` Mots-clés FR: transaction bancaire, opération bancaire, mouvement.",
    input_schema={   'type': 'object',
        'properties': {   'body': {   'type': 'object',
                                      'description': 'Request body payload. See the Pennylane API '
                                                     'reference for the exact schema of this endpoint.',
                                      'additionalProperties': True}},
        'required': ['body']},
    resource="transactions",
)
async def create_transaction(
    client: PennylaneClient,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = "/transactions"
    params = None
    return await client.post(url, data=body)


@tool(
    name="pennylane_get_transaction",
    description="[Banking · Bank Transactions / Transactions bancaires] Retrieve a transaction Retrieve a transaction > ℹ️ > This endpoint requires one of the following scopes: `transactions:readonly`, `transactions:all` Mots-clés FR: transaction bancaire, opération bancaire, mouvement.",
    input_schema={'type': 'object', 'properties': {'id': {'type': 'integer'}}, 'required': ['id']},
    resource="transactions",
)
async def get_transaction(
    client: PennylaneClient,
    id: str,
) -> Any:
    url = f"/transactions/{id}".format(id=id)
    params = None
    return await client.get(url, params=params)


@tool(
    name="pennylane_update_transaction",
    description="[Banking · Bank Transactions / Transactions bancaires] Update a transaction This endpoint returns the updated transaction. > ℹ️ > This endpoint requires the following scope: `transactions:all` Mots-clés FR: transaction bancaire, opération bancaire, mouvement.",
    input_schema={   'type': 'object',
        'properties': {   'id': {'type': 'integer'},
                          'body': {   'type': 'object',
                                      'description': 'Request body payload. See the Pennylane API '
                                                     'reference for the exact schema of this endpoint.',
                                      'additionalProperties': True}},
        'required': ['id', 'body']},
    resource="transactions",
)
async def update_transaction(
    client: PennylaneClient,
    id: str,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = f"/transactions/{id}".format(id=id)
    params = None
    return await client.put(url, data=body)


@tool(
    name="pennylane_get_transaction_categories",
    description="[Banking · Bank Transactions / Transactions bancaires] List categories of a bank transaction List categories of a bank transaction > ℹ️ > This endpoint requires one of the following scopes: `transactions:readonly`, `transactions:all` Mots-clés FR: transaction bancaire, opération bancaire, mouvement.",
    input_schema={   'type': 'object',
        'properties': {   'transaction_id': {'type': 'integer'},
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
        'required': ['transaction_id']},
    resource="transactions",
)
async def get_transaction_categories(
    client: PennylaneClient,
    transaction_id: str,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
) -> Any:
    url = f"/transactions/{transaction_id}/categories".format(transaction_id=transaction_id)
    params = {'cursor': cursor, 'limit': limit}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_put_transaction_categories",
    description="[Banking · Bank Transactions / Transactions bancaires] Categorize a bank transaction Update the categories of a transaction. You can pass categories that don't belong to the same category group. The sum of categories of a same group must equal `1`. In the following example, the two first categories belong to the same category group A, the sum of the weights is `1`. The third category belongs to a category group B, its weight is `1`. ``` [ { 'id': 59, 'weight': '0.5' }, // categ... Mots-clés FR: transaction bancaire, opération bancaire, mouvement.",
    input_schema={   'type': 'object',
        'properties': {   'transaction_id': {'type': 'integer'},
                          'body': {   'type': 'object',
                                      'description': 'Request body payload. See the Pennylane API '
                                                     'reference for the exact schema of this endpoint.',
                                      'additionalProperties': True}},
        'required': ['transaction_id', 'body']},
    resource="transactions",
)
async def put_transaction_categories(
    client: PennylaneClient,
    transaction_id: str,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = f"/transactions/{transaction_id}/categories".format(transaction_id=transaction_id)
    params = None
    return await client.put(url, data=body)


@tool(
    name="pennylane_get_transaction_matched_invoices",
    description="[Banking · Bank Transactions / Transactions bancaires] List invoices matched to a bank transaction List invoices matched to a bank transaction > ℹ️ > This endpoint requires one of the following scopes: `transactions:readonly`, `transactions:all` Mots-clés FR: transaction bancaire, opération bancaire, mouvement.",
    input_schema={   'type': 'object',
        'properties': {   'transaction_id': {'type': 'integer'},
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
        'required': ['transaction_id']},
    resource="transactions",
)
async def get_transaction_matched_invoices(
    client: PennylaneClient,
    transaction_id: str,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
) -> Any:
    url = f"/transactions/{transaction_id}/matched_invoices".format(transaction_id=transaction_id)
    params = {'cursor': cursor, 'limit': limit}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


