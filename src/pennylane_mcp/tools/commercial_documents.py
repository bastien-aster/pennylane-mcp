"""Auto-generated from docs/pennylane-openapi.json. Do not edit by hand.

Regenerate with: python scripts/generate_tools.py
"""
from typing import Any, Optional

from .._registry import tool
from ..client import PennylaneClient


@tool(
    name="pennylane_list_commercial_documents",
    description="List commercial documents. This endpoint lists commercial documents. > ℹ️ > This endpoint requires one of the following scopes: `commercial_documents:all`, `commercial_documents:readonly`",
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
                                                       '- `id`, `customer_id`: `lt`, `lteq`, `gt`, '
                                                       '`gteq`, `eq`, `not_eq`, `in`, `not_in`\n'
                                                       '- `document_type`: `eq`, `not_eq`, `in`, '
                                                       '`not_in`\n'
                                                       '\n'
                                                       'Available document_types:\n'
                                                       '- proforma\n'
                                                       '- shipping_order\n'
                                                       '- purchasing_order\n'},
                          'sort': {   'type': 'string',
                                      'description': 'You can choose to sort items on specific '
                                                     'attributes\n'
                                                     'Sort field may be prefixed with `-` for '
                                                     'descending order.\n'
                                                     'Example : `id` will sort by ascending order, '
                                                     '`-id` will sort by descending order.\n'
                                                     'Available fields : `id`\n'}}},
)
async def list_commercial_documents(
    client: PennylaneClient,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
    filter: Optional[Any] = None,
    sort: Optional[Any] = None,
) -> Any:
    url = "/commercial_documents"
    params = {'cursor': cursor, 'limit': limit, 'filter': filter, 'sort': sort}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_get_commercial_document",
    description="Retrieve a commercial document. This endpoint retrieves a commercial document. > ℹ️ > This endpoint requires one of the following scopes: `commercial_documents:all`, `commercial_documents:readonly`",
    input_schema={'type': 'object', 'properties': {'id': {'type': 'integer'}}, 'required': ['id']},
)
async def get_commercial_document(
    client: PennylaneClient,
    id: str,
) -> Any:
    url = f"/commercial_documents/{id}".format(id=id)
    params = None
    return await client.get(url, params=params)


@tool(
    name="pennylane_get_commercial_document_appendices",
    description="List appendices of a commercial document. List appendices of a commercial document > ℹ️ > This endpoint requires one of the following scopes: `commercial_documents:all`, `commercial_documents:readonly`",
    input_schema={   'type': 'object',
        'properties': {   'commercial_document_id': {'type': 'integer'},
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
        'required': ['commercial_document_id']},
)
async def get_commercial_document_appendices(
    client: PennylaneClient,
    commercial_document_id: str,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
) -> Any:
    url = f"/commercial_documents/{commercial_document_id}/appendices".format(commercial_document_id=commercial_document_id)
    params = {'cursor': cursor, 'limit': limit}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_post_commercial_document_appendices",
    description="Upload an appendix for a commercial document. Upload a file that will be an appendix attached to a commercial document. Note that this will not upload a file into the DMS (GED). > ℹ️ > This endpoint requires the following scope: `commercial_documents:all`",
    input_schema={   'type': 'object',
        'properties': {   'commercial_document_id': {'type': 'integer'},
                          'body': {   'type': 'object',
                                      'description': 'Request body payload. See the Pennylane API '
                                                     'reference for the exact schema of this endpoint.',
                                      'additionalProperties': True}},
        'required': ['commercial_document_id', 'body']},
)
async def post_commercial_document_appendices(
    client: PennylaneClient,
    commercial_document_id: str,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = f"/commercial_documents/{commercial_document_id}/appendices".format(commercial_document_id=commercial_document_id)
    params = None
    return await client.post(url, data=body)


@tool(
    name="pennylane_get_commercial_document_invoice_lines",
    description="List invoice lines for a commercial document. List invoice lines for a commercial document > ℹ️ > This endpoint requires one of the following scopes: `commercial_documents:all`, `commercial_documents:readonly`",
    input_schema={   'type': 'object',
        'properties': {   'commercial_document_id': {'type': 'integer'},
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
        'required': ['commercial_document_id']},
)
async def get_commercial_document_invoice_lines(
    client: PennylaneClient,
    commercial_document_id: str,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
    sort: Optional[Any] = None,
) -> Any:
    url = f"/commercial_documents/{commercial_document_id}/invoice_lines".format(commercial_document_id=commercial_document_id)
    params = {'cursor': cursor, 'limit': limit, 'sort': sort}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_get_commercial_document_invoice_line_sections",
    description="List invoice line sections for a commercial document. List invoice line sections for a commercial document > ℹ️ > This endpoint requires one of the following scopes: `commercial_documents:all`, `commercial_documents:readonly`",
    input_schema={   'type': 'object',
        'properties': {   'commercial_document_id': {'type': 'integer'},
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
        'required': ['commercial_document_id']},
)
async def get_commercial_document_invoice_line_sections(
    client: PennylaneClient,
    commercial_document_id: str,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
    sort: Optional[Any] = None,
) -> Any:
    url = f"/commercial_documents/{commercial_document_id}/invoice_line_sections".format(commercial_document_id=commercial_document_id)
    params = {'cursor': cursor, 'limit': limit, 'sort': sort}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


