"""Auto-generated from docs/pennylane-openapi.json. Do not edit by hand.

Regenerate with: python scripts/generate_tools.py
"""
from typing import Any, Optional

from .._registry import tool
from ..client import PennylaneClient


@tool(
    name="pennylane_create_e_invoice_import",
    description="[Admin · E-Invoicing / Facturation électronique] [BETA] Import e-invoices This endpoint allows you to import an e-invoice. > ‼️ > This endpoint is **DEPRECATED** > As an alternative, please use either: > - [Import a customer e-invoice](https://pennylane.readme.io/reference/createcustomerinvoiceeinvoiceimport) endpoint > - [Import a supplier e-invoice](https://pennylane.readme.io/reference/createsupplierinvoiceeinvoiceimport) endpoint > ℹ️ > This endpoint requires the... Mots-clés FR: facture électronique, e-invoicing, factur-X, PPF.",
    input_schema={   'type': 'object',
        'properties': {   'body': {   'type': 'object',
                                      'description': 'Request body payload. See the Pennylane API '
                                                     'reference for the exact schema of this endpoint.',
                                      'additionalProperties': True}},
        'required': ['body']},
    resource="e_invoices",
)
async def create_e_invoice_import(
    client: PennylaneClient,
    body: Optional[dict[str, Any]] = None,
) -> Any:
    url = "/e-invoices/imports"
    params = None
    return await client.post(url, data=body)


