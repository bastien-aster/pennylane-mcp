"""Outils pour la gestion des clients."""
from typing import Any
from ..client import PennylaneClient


async def list_customers(
    client: PennylaneClient,
    limit: int = 20,
    cursor: str | None = None,
    filter_query: str | None = None,
    sort: str = "-id"
) -> dict[str, Any]:
    """Liste tous les clients (entreprises et particuliers)."""
    params = {"limit": limit, "sort": sort}
    if cursor:
        params["cursor"] = cursor
    if filter_query:
        params["filter"] = filter_query
    
    return await client.get("customers", params)


async def get_customer(client: PennylaneClient, customer_id: int) -> dict[str, Any]:
    """Récupère les détails d'un client (générique)."""
    return await client.get(f"customers/{customer_id}")


async def get_company_customer(client: PennylaneClient, customer_id: int) -> dict[str, Any]:
    """Récupère les détails d'un client entreprise."""
    return await client.get(f"company_customers/{customer_id}")


async def get_individual_customer(client: PennylaneClient, customer_id: int) -> dict[str, Any]:
    """Récupère les détails d'un client particulier."""
    return await client.get(f"individual_customers/{customer_id}")


async def create_company_customer(
    client: PennylaneClient,
    name: str,
    billing_address: dict[str, str],
    emails: list[str] | None = None,
    phone: str | None = None,
    vat_number: str | None = None,
    payment_conditions: str = "30_days",
    billing_language: str = "fr_FR",
    **kwargs
) -> dict[str, Any]:
    """
    Crée un client entreprise.
    
    Args:
        name: Nom de l'entreprise
        billing_address: Adresse de facturation avec:
            - address (str): Rue
            - postal_code (str): Code postal
            - city (str): Ville
            - country_alpha2 (str): Code pays (ex: "FR")
        emails: Liste d'emails
        phone: Téléphone
        vat_number: Numéro de TVA
        payment_conditions: Conditions de paiement (upon_receipt, 15_days, 30_days, 45_days, 60_days)
        billing_language: Langue (fr_FR, en_GB, de_DE)
        **kwargs: Autres paramètres (delivery_address, recipient, etc.)
    """
    data = {
        "name": name,
        "billing_address": billing_address,
        "payment_conditions": payment_conditions,
        "billing_language": billing_language,
    }
    
    if emails:
        data["emails"] = emails
    if phone:
        data["phone"] = phone
    if vat_number:
        data["vat_number"] = vat_number
    
    data.update(kwargs)
    
    return await client.post("company_customers", data)


async def create_individual_customer(
    client: PennylaneClient,
    first_name: str,
    last_name: str,
    billing_address: dict[str, str],
    emails: list[str] | None = None,
    phone: str | None = None,
    payment_conditions: str = "30_days",
    billing_language: str = "fr_FR",
    **kwargs
) -> dict[str, Any]:
    """Crée un client particulier."""
    data = {
        "first_name": first_name,
        "last_name": last_name,
        "billing_address": billing_address,
        "payment_conditions": payment_conditions,
        "billing_language": billing_language,
    }
    
    if emails:
        data["emails"] = emails
    if phone:
        data["phone"] = phone
    
    data.update(kwargs)
    
    return await client.post("individual_customers", data)