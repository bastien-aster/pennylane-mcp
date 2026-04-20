"""Auto-generated from docs/pennylane-openapi.json. Do not edit by hand.

Regenerate with: python scripts/generate_tools.py
"""
from typing import Any, Optional

from .._registry import tool
from ..client import PennylaneClient


@tool(
    name="pennylane_post_file_attachments",
    description="[Purchasing · File Attachments / Pièces jointes] Upload a file Upload a file to attach to any resource that provides a `file_attachment_id`. The maximum allowed file size is 100MB. Note that this will not upload a file into the DMS (GED). > ℹ️ > This endpoint requires the following scope: `file_attachments:all` Mots-clés FR: pièce jointe, PJ, justificatif, document.",
    input_schema={   'type': 'object',
        'properties': {   'body': {   'type': 'object',
                                      'description': 'Request body payload. See the Pennylane API '
                                                     'reference for the exact schema of this endpoint.',
                                      'additionalProperties': True}},
        'required': ['body']},
    resource="file_attachments",
    readonly=False,
)
async def post_file_attachments(
    client: PennylaneClient,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = "/file_attachments"
    params = None
    return await client.post(url, data=body)


@tool(
    name="pennylane_get_file_attachments",
    description="[Purchasing · File Attachments / Pièces jointes] List attachments List attachments > ‼️ > This endpoint is **DEPRECATED** > ℹ️ > This endpoint requires one of the following scopes: `file_attachments:all`, `file_attachments:readonly` Mots-clés FR: pièce jointe, PJ, justificatif, document.",
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
                          'sort': {   'type': 'string',
                                      'description': 'You can choose to sort items on specific '
                                                     'attributes\n'
                                                     'Sort field may be prefixed with `-` for '
                                                     'descending order.\n'
                                                     'Example : `id` will sort by ascending order, '
                                                     '`-id` will sort by descending order.\n'
                                                     'Available fields : `id`\n'}}},
    resource="file_attachments",
    readonly=True,
)
async def get_file_attachments(
    client: PennylaneClient,
    cursor: Optional[Any] = None,
    limit: Optional[Any] = None,
    sort: Optional[Any] = None,
) -> Any:
    url = "/file_attachments"
    params = {'cursor': cursor, 'limit': limit, 'sort': sort}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


