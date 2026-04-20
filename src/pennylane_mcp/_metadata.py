"""Resource metadata driving description enrichment and profile filtering.

Edit this file to change domain grouping, display names, or French keywords —
then regenerate tools with: python scripts/generate_tools.py
"""
from __future__ import annotations

PROFILES: dict[str, set[str]] = {
    "sales": {
        "customer_invoices",
        "quotes",
        "customers",
        "company_customers",
        "individual_customers",
        "products",
        "commercial_documents",
        "customer_invoice_templates",
    },
    "purchasing": {
        "supplier_invoices",
        "suppliers",
        "purchase_requests",
        "file_attachments",
    },
    "accounting": {
        "ledger_entries",
        "ledger_entry_lines",
        "ledger_accounts",
        "journals",
        "categories",
        "category_groups",
        "trial_balance",
        "fiscal_years",
        "ledger_attachments",
    },
    "banking": {
        "transactions",
        "bank_accounts",
        "bank_establishments",
    },
    "mandates": {
        "sepa_mandates",
        "gocardless_mandates",
        "pro_account",
    },
    "admin": {
        "me",
        "exports",
        "changelogs",
        "billing_subscriptions",
        "pa_registrations",
        "e_invoices",
    },
}


# Resource → display labels and French keywords woven into tool descriptions
# so Claude matches French-speaking users' intent. Keywords stay lowercase.
RESOURCE_METADATA: dict[str, dict[str, object]] = {
    "customer_invoices": {
        "label_en": "Customer Invoices",
        "label_fr": "Factures clients",
        "keywords_fr": ["facture client", "facturation", "vente", "encaissement", "avoir client"],
    },
    "supplier_invoices": {
        "label_en": "Supplier Invoices",
        "label_fr": "Factures fournisseurs",
        "keywords_fr": ["facture fournisseur", "achat", "dépense", "décaissement", "avoir fournisseur"],
    },
    "quotes": {
        "label_en": "Quotes",
        "label_fr": "Devis",
        "keywords_fr": ["devis", "proposition commerciale", "offre"],
    },
    "customers": {
        "label_en": "Customers (unified)",
        "label_fr": "Clients (unifié)",
        "keywords_fr": ["client", "contact", "acheteur"],
    },
    "company_customers": {
        "label_en": "Company Customers",
        "label_fr": "Clients entreprise",
        "keywords_fr": ["client entreprise", "client B2B", "société cliente"],
    },
    "individual_customers": {
        "label_en": "Individual Customers",
        "label_fr": "Clients particuliers",
        "keywords_fr": ["client particulier", "client B2C", "personne physique"],
    },
    "products": {
        "label_en": "Products",
        "label_fr": "Produits",
        "keywords_fr": ["produit", "catalogue", "article", "référence"],
    },
    "commercial_documents": {
        "label_en": "Commercial Documents",
        "label_fr": "Documents commerciaux",
        "keywords_fr": ["bon de commande", "bon de livraison", "document commercial"],
    },
    "customer_invoice_templates": {
        "label_en": "Customer Invoice Templates",
        "label_fr": "Modèles de factures clients",
        "keywords_fr": ["modèle de facture", "template facture"],
    },
    "suppliers": {
        "label_en": "Suppliers",
        "label_fr": "Fournisseurs",
        "keywords_fr": ["fournisseur", "prestataire"],
    },
    "purchase_requests": {
        "label_en": "Purchase Requests",
        "label_fr": "Demandes d'achat",
        "keywords_fr": ["demande d'achat", "bon de commande interne", "approvisionnement"],
    },
    "file_attachments": {
        "label_en": "File Attachments",
        "label_fr": "Pièces jointes",
        "keywords_fr": ["pièce jointe", "PJ", "justificatif", "document"],
    },
    "ledger_entries": {
        "label_en": "Ledger Entries",
        "label_fr": "Écritures comptables",
        "keywords_fr": ["écriture comptable", "écriture", "journal"],
    },
    "ledger_entry_lines": {
        "label_en": "Ledger Entry Lines",
        "label_fr": "Lignes d'écriture",
        "keywords_fr": ["ligne d'écriture", "lettrage", "rapprochement comptable"],
    },
    "ledger_accounts": {
        "label_en": "Ledger Accounts",
        "label_fr": "Comptes du grand livre",
        "keywords_fr": ["compte comptable", "grand livre", "plan comptable"],
    },
    "journals": {
        "label_en": "Journals",
        "label_fr": "Journaux",
        "keywords_fr": ["journal comptable", "journal de vente", "journal d'achat"],
    },
    "categories": {
        "label_en": "Categories (analytical)",
        "label_fr": "Catégories (analytique)",
        "keywords_fr": ["catégorie", "analytique", "comptabilité analytique"],
    },
    "category_groups": {
        "label_en": "Category Groups",
        "label_fr": "Groupes de catégories",
        "keywords_fr": ["groupe de catégories", "axe analytique"],
    },
    "trial_balance": {
        "label_en": "Trial Balance",
        "label_fr": "Balance comptable",
        "keywords_fr": ["balance", "balance comptable", "balance générale"],
    },
    "fiscal_years": {
        "label_en": "Fiscal Years",
        "label_fr": "Exercices fiscaux",
        "keywords_fr": ["exercice fiscal", "année fiscale", "clôture"],
    },
    "ledger_attachments": {
        "label_en": "Ledger Attachments",
        "label_fr": "Pièces jointes comptables",
        "keywords_fr": ["pièce jointe comptable", "justificatif d'écriture"],
    },
    "transactions": {
        "label_en": "Bank Transactions",
        "label_fr": "Transactions bancaires",
        "keywords_fr": ["transaction bancaire", "opération bancaire", "mouvement"],
    },
    "bank_accounts": {
        "label_en": "Bank Accounts",
        "label_fr": "Comptes bancaires",
        "keywords_fr": ["compte bancaire", "IBAN", "RIB"],
    },
    "bank_establishments": {
        "label_en": "Bank Establishments",
        "label_fr": "Établissements bancaires",
        "keywords_fr": ["banque", "établissement bancaire"],
    },
    "sepa_mandates": {
        "label_en": "SEPA Mandates",
        "label_fr": "Mandats SEPA",
        "keywords_fr": ["mandat SEPA", "prélèvement SEPA", "autorisation de prélèvement"],
    },
    "gocardless_mandates": {
        "label_en": "GoCardless Mandates",
        "label_fr": "Mandats GoCardless",
        "keywords_fr": ["mandat GoCardless", "prélèvement GoCardless"],
    },
    "pro_account": {
        "label_en": "Pro Account",
        "label_fr": "Compte Pro Pennylane",
        "keywords_fr": ["compte pro", "Pennylane Pro Account"],
    },
    "me": {
        "label_en": "User Profile",
        "label_fr": "Profil utilisateur",
        "keywords_fr": ["profil", "utilisateur courant", "mon compte"],
    },
    "exports": {
        "label_en": "Exports (FEC / AGL / GL)",
        "label_fr": "Exports comptables (FEC / AGL / GL)",
        "keywords_fr": ["FEC", "AGL", "grand livre", "export comptable"],
    },
    "changelogs": {
        "label_en": "Changelogs (delta sync)",
        "label_fr": "Changelogs (sync delta)",
        "keywords_fr": ["changelog", "synchronisation", "delta", "audit"],
    },
    "billing_subscriptions": {
        "label_en": "Billing Subscriptions",
        "label_fr": "Abonnements récurrents",
        "keywords_fr": ["abonnement", "facturation récurrente", "subscription"],
    },
    "pa_registrations": {
        "label_en": "Portail Anaf Registrations",
        "label_fr": "Inscriptions Portail Anaf",
        "keywords_fr": ["Portail Anaf", "Pro Account registration"],
    },
    "e_invoices": {
        "label_en": "E-Invoicing",
        "label_fr": "Facturation électronique",
        "keywords_fr": ["facture électronique", "e-invoicing", "factur-X", "PPF"],
    },
}


def resource_to_profile(resource: str) -> str:
    """Return the profile a resource belongs to, or 'other' if unclassified."""
    for profile, resources in PROFILES.items():
        if resource in resources:
            return profile
    return "other"


def resolve_allowed_resources(tools_env: str | None) -> set[str] | None:
    """Parse the PENNYLANE_TOOLS env var into the set of allowed resources.

    Returns None to mean "allow everything" (when env is missing or 'all').
    Unknown profile names are ignored with a warning semantics left to the
    caller (we return only the resources we could resolve).
    """
    if not tools_env:
        return None
    raw = tools_env.strip().lower()
    if raw in ("all", "*", ""):
        return None
    allowed: set[str] = set()
    for token in (t.strip() for t in raw.split(",") if t.strip()):
        if token in PROFILES:
            allowed.update(PROFILES[token])
        else:
            # Treat unknown tokens as direct resource names (escape hatch).
            allowed.add(token)
    return allowed
