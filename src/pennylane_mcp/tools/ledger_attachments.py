"""Auto-generated from docs/pennylane-openapi.json. Do not edit by hand.

Regenerate with: python scripts/generate_tools.py
"""
from typing import Any, Optional

from .._registry import tool
from ..client import PennylaneClient


@tool(
    name="pennylane_get_ledger_attachments",
    description="[Accounting · Ledger Attachments / Pièces jointes comptables] List attachments List attachments > ‼️ > This endpoint is **DEPRECATED** > As soon as you opt in to the new version, or when the sunset phase starts and you haven't explicitly opted out of the old behavior, this endpoint will no longer work. For more details, see our API documentation https://pennylane.readme.io/docs/2026-api-changes-guide for migration instructions. > ℹ️ > This endpoint requires the following ... Mots-clés FR: pièce jointe comptable, justificatif d'écriture.",
    input_schema={   'type': 'object',
        'properties': {   'page': {   'type': 'integer',
                                      'description': 'Attachments are paginated, this is the current '
                                                     'page which will be returned. The page index is '
                                                     'starting at 1.'},
                          'per_page': {   'type': 'integer',
                                          'description': 'Attachments are paginated. By default, you '
                                                         'get 20 attachments per page. You can specify '
                                                         'another number of attachments per page.'}}},
    resource="ledger_attachments",
)
async def get_ledger_attachments(
    client: PennylaneClient,
    page: Optional[Any] = None,
    per_page: Optional[Any] = None,
) -> Any:
    url = "/ledger_attachments"
    params = {'page': page, 'per_page': per_page}
    params = {k: v for k, v in params.items() if v is not None}
    return await client.get(url, params=params)


@tool(
    name="pennylane_post_ledger_attachments",
    description="[Accounting · Ledger Attachments / Pièces jointes comptables] Upload a file Upload a file to attach to a ledger entry. The maximum allowed file size is 100MB. Note that this will not upload a file into the DMS (GED). > ‼️ > This endpoint is **DEPRECATED** > As an alternative, please use the [File Attachments: Upload a file](https://pennylane.readme.io/reference/postfileattachments#/) endpoint. > ℹ️ > This endpoint requires the following scope: `ledger` Mots-clés FR: pièce jointe comptable, justificatif d'écriture.",
    input_schema={   'type': 'object',
        'properties': {   'body': {   'type': 'object',
                                      'description': 'Request body payload. See the Pennylane API '
                                                     'reference for the exact schema of this endpoint.',
                                      'additionalProperties': True}},
        'required': ['body']},
    resource="ledger_attachments",
)
async def post_ledger_attachments(
    client: PennylaneClient,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = "/ledger_attachments"
    params = None
    return await client.post(url, data=body)


