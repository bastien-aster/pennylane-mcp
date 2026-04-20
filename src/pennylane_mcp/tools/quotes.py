"""Auto-generated from docs/pennylane-openapi.json. Do not edit by hand.

Regenerate with: python scripts/generate_tools.py
"""
from typing import Any, Optional

from .._registry import tool
from ..client import PennylaneClient


@tool(
    name="pennylane_list_quotes",
    description="[Sales · Quotes / Devis] List quotes Lists quotes > ℹ️ > This endpoint requires one of the following scopes: `quotes:all`, `quotes:readonly` Mots-clés FR: devis, proposition commerciale, offre.",
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
                                                       '- `status`: `eq`, `not_eq`, `in`, `not_in`\n'
                                                       '\n'
                                                       'Available statuses:\n'
                                                       '- accepted: a quote that has been accepted\n'
                                                       '- denied: a quote that has b'},
                          'sort': {   'type': 'string',
                                      'description': 'You can choose to sort items on specific '
                                                     'attributes\n'
                                                     'Sort field may be prefixed with `-` for '
                                                     'descending order.\n'
                                                     'Example : `id` will sort by ascending order, '
                                                     '`-id` will sort by descending order.\n'
                                                     'Available fields : `id`\n'}}},
    resource="quotes",
    readonly=True,
)
async def list_quotes(
    client: PennylaneClient,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
    filter: Optional[Any] = None,
    sort: Optional[Any] = None,
) -> Any:
    url = "/quotes"
    params = {'cursor': cursor, 'limit': limit, 'filter': filter, 'sort': sort}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_post_quotes",
    description="[Sales · Quotes / Devis] Create a quote This endpoint allows you to create a quote > ℹ️ > This endpoint requires the following scope: `quotes:all` Mots-clés FR: devis, proposition commerciale, offre.",
    input_schema={   'type': 'object',
        'properties': {   'body': {   'type': 'object',
                                      'description': 'Request body payload. See the Pennylane API '
                                                     'reference for the exact schema of this endpoint.',
                                      'additionalProperties': True}},
        'required': ['body']},
    resource="quotes",
    readonly=False,
)
async def post_quotes(
    client: PennylaneClient,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = "/quotes"
    params = None
    return await client.post(url, data=body)


@tool(
    name="pennylane_get_quote",
    description="[Sales · Quotes / Devis] Retrieve a quote This endpoint retrieves a quote. > ℹ️ > This endpoint requires one of the following scopes: `quotes:all`, `quotes:readonly` Mots-clés FR: devis, proposition commerciale, offre.",
    input_schema={'type': 'object', 'properties': {'id': {'type': 'integer'}}, 'required': ['id']},
    resource="quotes",
    readonly=True,
)
async def get_quote(
    client: PennylaneClient,
    id: str,
) -> Any:
    url = f"/quotes/{id}".format(id=id)
    params = None
    return await client.get(url, params=params)


@tool(
    name="pennylane_update_quote",
    description="[Sales · Quotes / Devis] Update a quote This endpoint allows you to update a quote > ℹ️ > This endpoint requires the following scope: `quotes:all` Mots-clés FR: devis, proposition commerciale, offre.",
    input_schema={   'type': 'object',
        'properties': {   'id': {'type': 'integer'},
                          'body': {   'type': 'object',
                                      'description': 'Request body payload. See the Pennylane API '
                                                     'reference for the exact schema of this endpoint.',
                                      'additionalProperties': True}},
        'required': ['id', 'body']},
    resource="quotes",
    readonly=False,
)
async def update_quote(
    client: PennylaneClient,
    id: str,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = f"/quotes/{id}".format(id=id)
    params = None
    return await client.put(url, data=body)


@tool(
    name="pennylane_get_quote_appendices",
    description="[Sales · Quotes / Devis] List appendices of a quote List appendices of a quote > ℹ️ > This endpoint requires one of the following scopes: `quotes:all`, `quotes:readonly` Mots-clés FR: devis, proposition commerciale, offre.",
    input_schema={   'type': 'object',
        'properties': {   'quote_id': {'type': 'integer'},
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
        'required': ['quote_id']},
    resource="quotes",
    readonly=True,
)
async def get_quote_appendices(
    client: PennylaneClient,
    quote_id: str,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
) -> Any:
    url = f"/quotes/{quote_id}/appendices".format(quote_id=quote_id)
    params = {'cursor': cursor, 'limit': limit}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_post_quote_appendices",
    description="[Sales · Quotes / Devis] Upload an appendix for a quote Upload a file that will be an appendix attached to a quote. Note that this will not upload a file into the DMS (GED). > ℹ️ > This endpoint requires the following scope: `quotes:all` Mots-clés FR: devis, proposition commerciale, offre.",
    input_schema={   'type': 'object',
        'properties': {   'quote_id': {'type': 'integer'},
                          'body': {   'type': 'object',
                                      'description': 'Request body payload. See the Pennylane API '
                                                     'reference for the exact schema of this endpoint.',
                                      'additionalProperties': True}},
        'required': ['quote_id', 'body']},
    resource="quotes",
    readonly=False,
)
async def post_quote_appendices(
    client: PennylaneClient,
    quote_id: str,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = f"/quotes/{quote_id}/appendices".format(quote_id=quote_id)
    params = None
    return await client.post(url, data=body)


@tool(
    name="pennylane_get_quote_invoice_lines",
    description="[Sales · Quotes / Devis] List invoice lines for a quote List invoice lines for a quote > ℹ️ > This endpoint requires one of the following scopes: `quotes:all`, `quotes:readonly` Mots-clés FR: devis, proposition commerciale, offre.",
    input_schema={   'type': 'object',
        'properties': {   'quote_id': {'type': 'integer'},
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
        'required': ['quote_id']},
    resource="quotes",
    readonly=True,
)
async def get_quote_invoice_lines(
    client: PennylaneClient,
    quote_id: str,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
    sort: Optional[Any] = None,
) -> Any:
    url = f"/quotes/{quote_id}/invoice_lines".format(quote_id=quote_id)
    params = {'cursor': cursor, 'limit': limit, 'sort': sort}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_get_quote_invoice_line_sections",
    description="[Sales · Quotes / Devis] List invoice line sections for a quote List invoice line sections for a quote > ℹ️ > This endpoint requires one of the following scopes: `quotes:all`, `quotes:readonly` Mots-clés FR: devis, proposition commerciale, offre.",
    input_schema={   'type': 'object',
        'properties': {   'quote_id': {'type': 'integer'},
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
        'required': ['quote_id']},
    resource="quotes",
    readonly=True,
)
async def get_quote_invoice_line_sections(
    client: PennylaneClient,
    quote_id: str,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
    sort: Optional[Any] = None,
) -> Any:
    url = f"/quotes/{quote_id}/invoice_line_sections".format(quote_id=quote_id)
    params = {'cursor': cursor, 'limit': limit, 'sort': sort}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_send_by_email_quote",
    description="[Sales · Quotes / Devis] Send a quote by email This endpoint allows you to send a quote by email to your customer. This requires that the PDF file for that document has been generated (this process can take a few minutes), so if you just created the quote in our system, we may return a 409 error. You should retry the request in a few minutes - if you receive a 204 response, that means that the email is on its way. For more information about... Mots-clés FR: devis, proposition commerciale, offre.",
    input_schema={   'type': 'object',
        'properties': {   'id': {'type': 'integer'},
                          'body': {   'type': 'object',
                                      'description': 'Request body payload. See the Pennylane API '
                                                     'reference for the exact schema of this endpoint.',
                                      'additionalProperties': True}},
        'required': ['id']},
    resource="quotes",
    readonly=False,
)
async def send_by_email_quote(
    client: PennylaneClient,
    id: str,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = f"/quotes/{id}/send_by_email".format(id=id)
    params = None
    return await client.post(url, data=body)


@tool(
    name="pennylane_update_status_quote",
    description="[Sales · Quotes / Devis] Update status of a quote This endpoint allows you to update the status of a quote > ℹ️ > This endpoint requires the following scope: `quotes:all` Mots-clés FR: devis, proposition commerciale, offre.",
    input_schema={   'type': 'object',
        'properties': {   'id': {'type': 'integer'},
                          'body': {   'type': 'object',
                                      'description': 'Request body payload. See the Pennylane API '
                                                     'reference for the exact schema of this endpoint.',
                                      'additionalProperties': True}},
        'required': ['id', 'body']},
    resource="quotes",
    readonly=False,
)
async def update_status_quote(
    client: PennylaneClient,
    id: str,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = f"/quotes/{id}/update_status".format(id=id)
    params = None
    return await client.put(url, data=body)


