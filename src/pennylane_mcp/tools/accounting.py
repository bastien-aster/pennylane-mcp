"""Outils pour la comptabilité."""
from typing import Any
from ..client import PennylaneClient


async def get_trial_balance(
    client: PennylaneClient,
    period_start: str,
    period_end: str,
    is_auxiliary: bool = False,
    page: int = 1,
    per_page: int = 100
) -> dict[str, Any]:
    """
    Récupère la balance générale.
    
    Args:
        period_start: Date de début (YYYY-MM-DD)
        period_end: Date de fin (YYYY-MM-DD)
        is_auxiliary: Inclure les comptes auxiliaires
        page: Numéro de page (commence à 1)
        per_page: Nombre d'items par page (1-1000)
    """
    params = {
        "period_start": period_start,
        "period_end": period_end,
        "is_auxiliary": is_auxiliary,
        "page": page,
        "per_page": per_page
    }
    return await client.get("trial_balance", params)


async def list_ledger_accounts(
    client: PennylaneClient,
    page: int = 1,
    per_page: int = 100,
    filter_query: str | None = None
) -> dict[str, Any]:
    """
    Liste les comptes du plan comptable.
    
    Args:
        page: Numéro de page (commence à 1)
        per_page: Nombre d'items par page (1-1000)
        filter_query: Filtres (ex: "enabled:eq:true")
    """
    params = {"page": page, "per_page": per_page}
    if filter_query:
        params["filter"] = filter_query
    return await client.get("ledger_accounts", params)


async def list_categories(
    client: PennylaneClient,
    limit: int = 100,
    cursor: str | None = None,
    filter_query: str | None = None,
    sort: str = "-id"
) -> dict[str, Any]:
    """
    Liste les catégories comptables.
    
    Args:
        limit: Nombre de résultats (1-100)
        cursor: Curseur de pagination
        filter_query: Filtres (ex: "label:start_with:HR")
        sort: Tri (ex: "-id" pour desc)
    """
    params = {"limit": limit, "sort": sort}
    if cursor:
        params["cursor"] = cursor
    if filter_query:
        params["filter"] = filter_query
    return await client.get("categories", params)


async def list_bank_accounts(
    client: PennylaneClient,
    limit: int = 100,
    cursor: str | None = None,
    sort: str = "-id"
) -> dict[str, Any]:
    """
    Liste les comptes bancaires.
    
    Args:
        limit: Nombre de résultats (1-100)
        cursor: Curseur de pagination
        sort: Tri (ex: "-id" pour desc)
    """
    params = {"limit": limit, "sort": sort}
    if cursor:
        params["cursor"] = cursor
    return await client.get("bank_accounts", params)


async def export_fec(client: PennylaneClient, fiscal_year_id: int) -> dict[str, Any]:
    """
    Lance un export FEC.
    
    Args:
        fiscal_year_id: ID de l'année fiscale
    """
    return await client.post("exports/fec", {"fiscal_year_id": fiscal_year_id})