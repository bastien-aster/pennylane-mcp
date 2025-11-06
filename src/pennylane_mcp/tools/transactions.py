"""Outils pour la gestion des transactions bancaires."""
from typing import Any
from ..client import PennylaneClient


async def list_transactions(
    client: PennylaneClient,
    limit: int = 20,
    cursor: str | None = None,
    filter_query: str | None = None,
    sort: str = "-date"
) -> dict[str, Any]:
    """Liste les transactions bancaires."""
    params = {"limit": limit, "sort": sort}
    if cursor:
        params["cursor"] = cursor
    if filter_query:
        params["filter"] = filter_query
    
    return await client.get("transactions", params)


async def get_transaction(client: PennylaneClient, transaction_id: int) -> dict[str, Any]:
    """Récupère les détails d'une transaction."""
    return await client.get(f"transactions/{transaction_id}")


async def create_transaction(
    client: PennylaneClient,
    date: str,
    amount: str,
    label: str,
    bank_account_id: int,
    fee: str = "0.00",
    **kwargs
) -> dict[str, Any]:
    """
    Crée une transaction bancaire.
    
    Args:
        date: Date de la transaction (YYYY-MM-DD)
        amount: Montant (positif pour crédit, négatif pour débit)
        label: Libellé de la transaction
        bank_account_id: ID du compte bancaire
        fee: Frais de transaction
        **kwargs: Autres paramètres optionnels
    """
    data = {
        "bank_account_id": bank_account_id,
        "label": label,
        "date": date,
        "amount": amount,
        "fee": fee,
        **kwargs
    }
    return await client.post("transactions", data)


async def update_transaction(
    client: PennylaneClient,
    transaction_id: int,
    **kwargs
) -> dict[str, Any]:
    """
    Met à jour une transaction.
    
    Args:
        transaction_id: ID de la transaction
        **kwargs: Champs à mettre à jour (date, amount, label, etc.)
    """
    return await client.put(f"transactions/{transaction_id}", kwargs)


async def categorize_transaction(
    client: PennylaneClient,
    transaction_id: int,
    categories: list[dict[str, Any]]
) -> dict[str, Any]:
    """
    Catégorise une transaction.
    
    Args:
        transaction_id: ID de la transaction
        categories: Liste des catégories avec category_id et weight
    """
    return await client.put(
        f"transactions/{transaction_id}/categories",
        {"categories": categories}
    )


async def match_transaction_to_customer_invoice(
    client: PennylaneClient,
    invoice_id: int,
    transaction_id: int,
    amount: str | None = None
) -> dict[str, Any]:
    """
    Associe une transaction à une facture client.
    
    Args:
        invoice_id: ID de la facture client
        transaction_id: ID de la transaction
        amount: Montant à associer (optionnel, par défaut le montant total)
    """
    data = {"transaction_id": transaction_id}
    if amount:
        data["amount"] = amount
    return await client.post(f"customer_invoices/{invoice_id}/matched_transactions", data)


async def unmatch_transaction_from_customer_invoice(
    client: PennylaneClient,
    invoice_id: int,
    transaction_id: int
) -> dict[str, Any]:
    """
    Dissocie une transaction d'une facture client.
    
    Args:
        invoice_id: ID de la facture client
        transaction_id: ID de la transaction
    """
    return await client.delete(f"customer_invoices/{invoice_id}/matched_transactions/{transaction_id}")


async def match_transaction_to_supplier_invoice(
    client: PennylaneClient,
    invoice_id: int,
    transaction_id: int,
    amount: str | None = None
) -> dict[str, Any]:
    """
    Associe une transaction à une facture fournisseur.
    
    Args:
        invoice_id: ID de la facture fournisseur
        transaction_id: ID de la transaction
        amount: Montant à associer (optionnel, par défaut le montant total)
    """
    data = {"transaction_id": transaction_id}
    if amount:
        data["amount"] = amount
    return await client.post(f"supplier_invoices/{invoice_id}/matched_transactions", data)


async def unmatch_transaction_from_supplier_invoice(
    client: PennylaneClient,
    invoice_id: int,
    transaction_id: int
) -> dict[str, Any]:
    """
    Dissocie une transaction d'une facture fournisseur.
    
    Args:
        invoice_id: ID de la facture fournisseur
        transaction_id: ID de la transaction
    """
    return await client.delete(f"supplier_invoices/{invoice_id}/matched_transactions/{transaction_id}")