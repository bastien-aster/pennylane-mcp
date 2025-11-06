"""Serveur MCP pour Pennylane."""
import os
import logging
from typing import Any
from dotenv import load_dotenv

from mcp.server import Server
from mcp.types import Tool, TextContent
from mcp.server.stdio import stdio_server

from .client import PennylaneClient
from .tools import invoices, customers, suppliers, transactions, accounting, quotes

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Chargement des variables d'environnement
load_dotenv()

# Initialisation du serveur MCP
app = Server("pennylane-mcp")

# Client API (sera initialisé au démarrage)
pennylane_client: PennylaneClient | None = None


# Définition des outils MCP
TOOLS = [
    # ==================== FACTURES CLIENTS ====================
    Tool(
        name="pennylane_list_customer_invoices",
        description="Liste les factures clients avec pagination et filtres",
        inputSchema={
            "type": "object",
            "properties": {
                "limit": {
                    "type": "integer",
                    "description": "Nombre de résultats (1-100)",
                    "default": 20
                },
                "cursor": {
                    "type": "string",
                    "description": "Curseur de pagination"
                },
                "filter": {
                    "type": "string",
                    "description": "Filtres (ex: 'draft:eq:true' ou 'paid:eq:false')"
                },
                "sort": {
                    "type": "string",
                    "description": "Tri (ex: '-id' pour desc, 'date' pour asc)",
                    "default": "-id"
                },
            },
        },
    ),
    Tool(
        name="pennylane_get_customer_invoice",
        description="Récupère les détails d'une facture client par son ID",
        inputSchema={
            "type": "object",
            "properties": {
                "invoice_id": {
                    "type": "integer",
                    "description": "ID de la facture"
                },
            },
            "required": ["invoice_id"],
        },
    ),
    Tool(
        name="pennylane_create_customer_invoice",
        description="Crée une nouvelle facture client (brouillon ou finalisée)",
        inputSchema={
            "type": "object",
            "properties": {
                "customer_id": {
                    "type": "integer",
                    "description": "ID du client"
                },
                "date": {
                    "type": "string",
                    "description": "Date de la facture (YYYY-MM-DD) - OBLIGATOIRE"
                },
                "deadline": {
                    "type": "string",
                    "description": "Date limite de paiement (YYYY-MM-DD) - OBLIGATOIRE"
                },
                "invoice_lines": {
                    "type": "array",
                    "description": "Lignes de facture avec label, raw_currency_unit_price, quantity, unit, vat_rate",
                    "items": {"type": "object"},
                },
                "draft": {
                    "type": "boolean",
                    "description": "OBLIGATOIRE - True = brouillon modifiable, False = facture finalisée",
                    "default": True
                },
                "currency": {
                    "type": "string",
                    "description": "Devise (EUR, USD, etc.)",
                    "default": "EUR"
                },
                "language": {
                    "type": "string",
                    "description": "Langue (fr_FR, en_GB, de_DE)",
                    "default": "fr_FR"
                },
            },
            "required": ["customer_id", "date", "deadline", "invoice_lines"],
        },
    ),
    Tool(
        name="pennylane_finalize_customer_invoice",
        description="Finalise une facture client (la rend non modifiable et génère le PDF)",
        inputSchema={
            "type": "object",
            "properties": {
                "invoice_id": {
                    "type": "integer",
                    "description": "ID de la facture"
                },
            },
            "required": ["invoice_id"],
        },
    ),
    Tool(
        name="pennylane_send_customer_invoice_email",
        description="Envoie une facture client par email",
        inputSchema={
            "type": "object",
            "properties": {
                "invoice_id": {
                    "type": "integer",
                    "description": "ID de la facture"
                },
                "recipients": {
                    "type": "array",
                    "description": "Liste d'emails destinataires (vide = utilise les emails du client)",
                    "items": {"type": "string"},
                    "default": []
                },
            },
            "required": ["invoice_id"],
        },
    ),
    Tool(
        name="pennylane_categorize_customer_invoice",
        description="Catégorise une facture client avec des catégories comptables",
        inputSchema={
            "type": "object",
            "properties": {
                "invoice_id": {
                    "type": "integer",
                    "description": "ID de la facture"
                },
                "categories": {
                    "type": "array",
                    "description": "Liste des catégories avec category_id et weight",
                    "items": {"type": "object"},
                },
            },
            "required": ["invoice_id", "categories"],
        },
    ),
    
    # ==================== FACTURES FOURNISSEURS ====================
    Tool(
        name="pennylane_list_supplier_invoices",
        description="Liste les factures fournisseurs avec pagination et filtres",
        inputSchema={
            "type": "object",
            "properties": {
                "limit": {
                    "type": "integer",
                    "description": "Nombre de résultats (1-100)",
                    "default": 20
                },
                "cursor": {
                    "type": "string",
                    "description": "Curseur de pagination"
                },
                "filter": {
                    "type": "string",
                    "description": "Filtres"
                },
                "sort": {
                    "type": "string",
                    "description": "Tri",
                    "default": "-id"
                },
            },
        },
    ),
    Tool(
        name="pennylane_get_supplier_invoice",
        description="Récupère les détails d'une facture fournisseur",
        inputSchema={
            "type": "object",
            "properties": {
                "invoice_id": {
                    "type": "integer",
                    "description": "ID de la facture fournisseur"
                },
            },
            "required": ["invoice_id"],
        },
    ),
    Tool(
        name="pennylane_categorize_supplier_invoice",
        description="Catégorise une facture fournisseur",
        inputSchema={
            "type": "object",
            "properties": {
                "invoice_id": {
                    "type": "integer",
                    "description": "ID de la facture"
                },
                "categories": {
                    "type": "array",
                    "description": "Liste des catégories avec category_id et weight",
                    "items": {"type": "object"},
                },
            },
            "required": ["invoice_id", "categories"],
        },
    ),
    
    # ==================== CLIENTS ====================
    Tool(
        name="pennylane_list_customers",
        description="Liste tous les clients (entreprises et particuliers)",
        inputSchema={
            "type": "object",
            "properties": {
                "limit": {
                    "type": "integer",
                    "description": "Nombre de résultats",
                    "default": 20
                },
                "cursor": {
                    "type": "string",
                    "description": "Curseur de pagination"
                },
                "filter": {
                    "type": "string",
                    "description": "Filtres"
                },
                "sort": {
                    "type": "string",
                    "description": "Tri",
                    "default": "-id"
                },
            },
        },
    ),
    Tool(
        name="pennylane_get_customer",
        description="Récupère les détails d'un client (générique)",
        inputSchema={
            "type": "object",
            "properties": {
                "customer_id": {
                    "type": "integer",
                    "description": "ID du client"
                },
            },
            "required": ["customer_id"],
        },
    ),
    Tool(
        name="pennylane_get_company_customer",
        description="Récupère les détails d'un client entreprise",
        inputSchema={
            "type": "object",
            "properties": {
                "customer_id": {
                    "type": "integer",
                    "description": "ID du client entreprise"
                },
            },
            "required": ["customer_id"],
        },
    ),
    Tool(
        name="pennylane_get_individual_customer",
        description="Récupère les détails d'un client particulier",
        inputSchema={
            "type": "object",
            "properties": {
                "customer_id": {
                    "type": "integer",
                    "description": "ID du client particulier"
                },
            },
            "required": ["customer_id"],
        },
    ),
    Tool(
        name="pennylane_create_company_customer",
        description="Crée un nouveau client entreprise",
        inputSchema={
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "Nom de l'entreprise"
                },
                "billing_address": {
                    "type": "object",
                    "description": "Adresse de facturation",
                    "properties": {
                        "address": {"type": "string"},
                        "postal_code": {"type": "string"},
                        "city": {"type": "string"},
                        "country_alpha2": {"type": "string"}
                    },
                    "required": ["address", "postal_code", "city", "country_alpha2"]
                },
                "delivery_address": {
                    "type": "object",
                    "description": "Adresse de livraison",
                    "properties": {
                        "address": {"type": "string"},
                        "postal_code": {"type": "string"},
                        "city": {"type": "string"},
                        "country_alpha2": {"type": "string"}
                    }
                },
                "ledger_account": {
                    "type": "object",
                    "description": "Compte comptable",
                    "properties": {
                        "number": {"type": "string"}
                    }
                },
                "emails": {
                    "type": "array",
                    "description": "Liste d'emails",
                    "items": {"type": "string"}
                },
                "phone": {
                    "type": "string",
                    "description": "Téléphone"
                },
                "vat_number": {
                    "type": "string",
                    "description": "Numéro de TVA"
                },
                "reg_no": {
                    "type": "string",
                    "description": "Numéro SIREN/SIRET"
                },
                "billing_iban": {
                    "type": "string",
                    "description": "IBAN de facturation"
                },
                "recipient": {
                    "type": "string",
                    "description": "Destinataire"
                },
                "reference": {
                    "type": "string",
                    "description": "Référence client"
                },
                "notes": {
                    "type": "string",
                    "description": "Notes"
                },
                "external_reference": {
                    "type": "string",
                    "description": "Référence externe"
                },
                "payment_conditions": {
                    "type": "string",
                    "description": "Conditions de paiement",
                    "enum": ["upon_receipt", "custom", "15_days", "30_days", "45_days", "60_days"],
                    "default": "30_days"
                },
                "billing_language": {
                    "type": "string",
                    "description": "Langue de facturation",
                    "enum": ["fr_FR", "en_GB", "de_DE"],
                    "default": "fr_FR"
                },
            },
            "required": ["name", "billing_address"],
        },
    ),
    Tool(
        name="pennylane_create_individual_customer",
        description="Crée un nouveau client particulier",
        inputSchema={
            "type": "object",
            "properties": {
                "first_name": {
                    "type": "string",
                    "description": "Prénom"
                },
                "last_name": {
                    "type": "string",
                    "description": "Nom de famille"
                },
                "billing_address": {
                    "type": "object",
                    "description": "Adresse de facturation",
                    "properties": {
                        "address": {"type": "string"},
                        "postal_code": {"type": "string"},
                        "city": {"type": "string"},
                        "country_alpha2": {"type": "string"}
                    },
                    "required": ["address", "postal_code", "city", "country_alpha2"]
                },
                "delivery_address": {
                    "type": "object",
                    "description": "Adresse de livraison",
                    "properties": {
                        "address": {"type": "string"},
                        "postal_code": {"type": "string"},
                        "city": {"type": "string"},
                        "country_alpha2": {"type": "string"}
                    }
                },
                "ledger_account": {
                    "type": "object",
                    "description": "Compte comptable",
                    "properties": {
                        "number": {"type": "string"}
                    }
                },
                "emails": {
                    "type": "array",
                    "description": "Liste d'emails",
                    "items": {"type": "string"}
                },
                "phone": {
                    "type": "string",
                    "description": "Téléphone"
                },
                "billing_iban": {
                    "type": "string",
                    "description": "IBAN de facturation"
                },
                "recipient": {
                    "type": "string",
                    "description": "Destinataire"
                },
                "reference": {
                    "type": "string",
                    "description": "Référence client"
                },
                "notes": {
                    "type": "string",
                    "description": "Notes"
                },
                "external_reference": {
                    "type": "string",
                    "description": "Référence externe"
                },
                "payment_conditions": {
                    "type": "string",
                    "description": "Conditions de paiement",
                    "enum": ["upon_receipt", "custom", "15_days", "30_days", "45_days", "60_days"],
                    "default": "30_days"
                },
                "billing_language": {
                    "type": "string",
                    "description": "Langue de facturation",
                    "enum": ["fr_FR", "en_GB", "de_DE"],
                    "default": "fr_FR"
                },
            },
            "required": ["first_name", "last_name", "billing_address"],
        },
    ),
    
    # ==================== DEVIS ====================
    Tool(
        name="pennylane_list_quotes",
        description="Liste tous les devis",
        inputSchema={
            "type": "object",
            "properties": {
                "limit": {
                    "type": "integer",
                    "description": "Nombre de résultats",
                    "default": 30
                },
                "cursor": {
                    "type": "string",
                    "description": "Curseur de pagination"
                },
                "filter": {
                    "type": "string",
                    "description": "Filtres (ex: 'status:eq:pending', 'customer_id:eq:123')"
                },
                "sort": {
                    "type": "string",
                    "description": "Tri",
                    "default": "-id"
                },
            },
        },
    ),
    Tool(
        name="pennylane_get_quote",
        description="Récupère les détails d'un devis",
        inputSchema={
            "type": "object",
            "properties": {
                "quote_id": {
                    "type": "integer",
                    "description": "ID du devis"
                },
            },
            "required": ["quote_id"],
        },
    ),
    Tool(
        name="pennylane_list_quote_invoice_line_sections",
        description="Liste les sections de lignes d'un devis",
        inputSchema={
            "type": "object",
            "properties": {
                "quote_id": {
                    "type": "integer",
                    "description": "ID du devis"
                },
                "limit": {
                    "type": "integer",
                    "description": "Nombre de résultats",
                    "default": 100
                },
                "cursor": {
                    "type": "string",
                    "description": "Curseur de pagination"
                },
                "sort": {
                    "type": "string",
                    "description": "Tri",
                    "default": "-id"
                },
            },
            "required": ["quote_id"],
        },
    ),
    Tool(
        name="pennylane_list_quote_appendices",
        description="Liste les annexes (fichiers joints) d'un devis",
        inputSchema={
            "type": "object",
            "properties": {
                "quote_id": {
                    "type": "integer",
                    "description": "ID du devis"
                },
                "limit": {
                    "type": "integer",
                    "description": "Nombre de résultats",
                    "default": 20
                },
                "cursor": {
                    "type": "string",
                    "description": "Curseur de pagination"
                },
            },
            "required": ["quote_id"],
        },
    ),
    Tool(
        name="pennylane_create_quote",
        description="Crée un nouveau devis",
        inputSchema={
            "type": "object",
            "properties": {
                "customer_id": {
                    "type": "integer",
                    "description": "ID du client"
                },
                "invoice_lines": {
                    "type": "array",
                    "description": "Lignes du devis",
                    "items": {
                        "type": "object",
                        "properties": {
                            "label": {"type": "string", "description": "Libellé de la ligne"},
                            "quantity": {"type": "number", "description": "Quantité"},
                            "raw_currency_unit_price": {"type": "string", "description": "Prix unitaire HT (jusqu'à 6 décimales)"},
                            "vat_rate": {
                                "type": "string",
                                "description": "Taux de TVA au format Pennylane (ex: FR_200 pour 20% en France, FR_100 pour 10%, FR_55 pour 5.5%, FR_21 pour 2.1%)"
                            },
                            "unit": {"type": "string", "description": "Unité (ex: 'unité', 'jour', 'heure')"},
                            "description": {"type": "string", "description": "Description de la ligne"},
                            "section_rank": {"type": "integer", "description": "Rang de la section"},
                            "ledger_account_id": {"type": "integer", "description": "ID du compte comptable"},
                            "product_id": {"type": "integer", "description": "ID du produit"},
                            "discount": {"type": "object", "description": "Remise sur la ligne"}
                        },
                        "required": ["label", "quantity", "raw_currency_unit_price", "vat_rate", "unit"]
                    }
                },
                "date": {
                    "type": "string", 
                    "description": "Date du devis (YYYY-MM-DD)"
                },
                "deadline": {
                    "type": "string",
                    "description": "Date limite (YYYY-MM-DD)"
                },
                "currency": {
                    "type": "string",
                    "description": "Devise",
                    "default": "EUR"
                },
                "language": {
                    "type": "string",
                    "description": "Langue",
                    "enum": ["fr_FR", "en_GB", "de_DE"],
                    "default": "fr_FR"
                },
                "discount": {
                    "type": "object",
                    "description": "Remise globale",
                    "properties": {
                        "type": {"type": "string", "enum": ["absolute", "percentage"]},
                        "value": {"type": "string"}
                    }
                },
                "invoice_line_sections": {
                    "type": "array",
                    "description": "Sections de lignes",
                    "items": {
                        "type": "object",
                        "properties": {
                            "rank": {"type": "integer"},
                            "title": {"type": "string"},
                            "description": {"type": "string"}
                        }
                    }
                },
                "quote_template_id": {
                    "type": "integer",
                    "description": "ID du modèle de devis"
                },
                "pdf_invoice_free_text": {
                    "type": "string",
                    "description": "Texte libre sur le PDF"
                },
                "pdf_invoice_subject": {
                    "type": "string",
                    "description": "Sujet du PDF"
                },
                "pdf_description": {
                    "type": "string",
                    "description": "Description du PDF"
                },
                "special_mention": {
                    "type": "string",
                    "description": "Mention spéciale"
                },
                "external_reference": {
                    "type": "string",
                    "description": "Référence externe"
                }
            },
            "required": ["customer_id", "invoice_lines", "date", "deadline"]
        }
    ),
    Tool(
        name="pennylane_update_quote",
        description="Met à jour un devis existant",
        inputSchema={
            "type": "object",
            "properties": {
                "quote_id": {
                    "type": "integer",
                    "description": "ID du devis"
                },
                "customer_id": {
                    "type": "integer",
                    "description": "ID du client"
                },
                "invoice_lines": {
                    "type": "object",
                    "description": "Lignes du devis (avec create pour ajouter)",
                    "properties": {
                        "create": {
                            "type": "array",
                            "items": {"type": "object"}
                        }
                    }
                },
                "date": {
                    "type": "string",
                    "description": "Date du devis (YYYY-MM-DD)"
                },
                "deadline": {
                    "type": "string",
                    "description": "Date limite (YYYY-MM-DD)"
                },
                "language": {
                    "type": "string",
                    "description": "Langue",
                    "enum": ["fr_FR", "en_GB", "de_DE"]
                },
                "discount": {
                    "type": "object",
                    "description": "Remise globale"
                },
                "quote_template_id": {
                    "type": "integer",
                    "description": "ID du modèle de devis"
                },
                "pdf_invoice_free_text": {
                    "type": "string",
                    "description": "Texte libre sur le PDF"
                },
                "pdf_invoice_subject": {
                    "type": "string",
                    "description": "Sujet du PDF"
                },
                "pdf_description": {
                    "type": "string",
                    "description": "Description du PDF"
                },
                "special_mention": {
                    "type": "string",
                    "description": "Mention spéciale"
                },
                "external_reference": {
                    "type": "string",
                    "description": "Référence externe"
                }
            },
            "required": ["quote_id"]
        }
    ),
    Tool(
        name="pennylane_update_quote_status",
        description="Met à jour le statut d'un devis",
        inputSchema={
            "type": "object",
            "properties": {
                "quote_id": {
                    "type": "integer",
                    "description": "ID du devis"
                },
                "status": {
                    "type": "string",
                    "description": "Nouveau statut du devis",
                    "enum": ["pending", "accepted", "denied", "invoiced", "expired"]
                }
            },
            "required": ["quote_id", "status"]
        }
    ),
    
    # ==================== FOURNISSEURS ====================
    Tool(
        name="pennylane_list_suppliers",
        description="Liste tous les fournisseurs",
        inputSchema={
            "type": "object",
            "properties": {
                "limit": {
                    "type": "integer",
                    "description": "Nombre de résultats (1-100)",
                    "default": 20
                },
                "cursor": {
                    "type": "string",
                    "description": "Curseur de pagination"
                },
                "filter": {
                    "type": "string",
                    "description": "Filtres (ex: 'name:start_with:Acme')"
                },
                "sort": {
                    "type": "string",
                    "description": "Tri",
                    "default": "-id"
                },
            },
        },
    ),
    Tool(
        name="pennylane_get_supplier",
        description="Récupère les détails d'un fournisseur par son ID",
        inputSchema={
            "type": "object",
            "properties": {
                "supplier_id": {
                    "type": "integer",
                    "description": "ID du fournisseur"
                },
            },
            "required": ["supplier_id"],
        },
    ),
    Tool(
        name="pennylane_create_supplier",
        description="Crée un nouveau fournisseur",
        inputSchema={
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "Nom du fournisseur"
                },
                "postal_address": {
                    "type": "object",
                    "description": "Adresse postale (address, postal_code, city, country_alpha2)"
                },
                "emails": {
                    "type": "array",
                    "description": "Liste d'emails",
                    "items": {"type": "string"}
                },
                "iban": {
                    "type": "string",
                    "description": "IBAN du fournisseur"
                },
                "vat_number": {
                    "type": "string",
                    "description": "Numéro de TVA"
                },
            },
            "required": ["name"],
        },
    ),
    
    # ==================== TRANSACTIONS ====================
    Tool(
        name="pennylane_list_transactions",
        description="Liste les transactions bancaires",
        inputSchema={
            "type": "object",
            "properties": {
                "limit": {
                    "type": "integer",
                    "description": "Nombre de résultats",
                    "default": 20
                },
                "cursor": {
                    "type": "string",
                    "description": "Curseur de pagination"
                },
                "filter": {
                    "type": "string",
                    "description": "Filtres (ex: 'bank_account_id:eq:123')"
                },
                "sort": {
                    "type": "string",
                    "description": "Tri",
                    "default": "-date"
                },
            },
        },
    ),
    Tool(
        name="pennylane_get_transaction",
        description="Récupère les détails d'une transaction",
        inputSchema={
            "type": "object",
            "properties": {
                "transaction_id": {
                    "type": "integer",
                    "description": "ID de la transaction"
                },
            },
            "required": ["transaction_id"],
        },
    ),
    Tool(
        name="pennylane_create_transaction",
        description="Crée une nouvelle transaction bancaire",
        inputSchema={
            "type": "object",
            "properties": {
                "date": {
                    "type": "string",
                    "description": "Date de la transaction (YYYY-MM-DD)"
                },
                "amount": {
                    "type": "string",
                    "description": "Montant (positif pour crédit, négatif pour débit)"
                },
                "label": {
                    "type": "string",
                    "description": "Libellé de la transaction"
                },
                "bank_account_id": {
                    "type": "integer",
                    "description": "ID du compte bancaire"
                },
                "fee": {
                    "type": "string",
                    "description": "Frais de transaction",
                    "default": "0.00"
                },
            },
            "required": ["date", "amount", "label", "bank_account_id"],
        },
    ),
    Tool(
        name="pennylane_update_transaction",
        description="Met à jour une transaction existante",
        inputSchema={
            "type": "object",
            "properties": {
                "transaction_id": {
                    "type": "integer",
                    "description": "ID de la transaction"
                },
                "date": {
                    "type": "string",
                    "description": "Nouvelle date (YYYY-MM-DD)"
                },
                "amount": {
                    "type": "string",
                    "description": "Nouveau montant"
                },
                "label": {
                    "type": "string",
                    "description": "Nouveau libellé"
                },
            },
            "required": ["transaction_id"],
        },
    ),
    Tool(
        name="pennylane_categorize_transaction",
        description="Catégorise une transaction bancaire",
        inputSchema={
            "type": "object",
            "properties": {
                "transaction_id": {
                    "type": "integer",
                    "description": "ID de la transaction"
                },
                "categories": {
                    "type": "array",
                    "description": "Catégories avec category_id et weight",
                    "items": {"type": "object"},
                },
            },
            "required": ["transaction_id", "categories"],
        },
    ),
    Tool(
        name="pennylane_match_transaction_to_customer_invoice",
        description="Associe une transaction à une facture client",
        inputSchema={
            "type": "object",
            "properties": {
                "invoice_id": {
                    "type": "integer",
                    "description": "ID de la facture client"
                },
                "transaction_id": {
                    "type": "integer",
                    "description": "ID de la transaction"
                },
                "amount": {
                    "type": "string",
                    "description": "Montant à associer (optionnel)"
                },
            },
            "required": ["invoice_id", "transaction_id"],
        },
    ),
    Tool(
        name="pennylane_unmatch_transaction_from_customer_invoice",
        description="Dissocie une transaction d'une facture client",
        inputSchema={
            "type": "object",
            "properties": {
                "invoice_id": {
                    "type": "integer",
                    "description": "ID de la facture client"
                },
                "transaction_id": {
                    "type": "integer",
                    "description": "ID de la transaction"
                },
            },
            "required": ["invoice_id", "transaction_id"],
        },
    ),
    Tool(
        name="pennylane_match_transaction_to_supplier_invoice",
        description="Associe une transaction à une facture fournisseur",
        inputSchema={
            "type": "object",
            "properties": {
                "invoice_id": {
                    "type": "integer",
                    "description": "ID de la facture fournisseur"
                },
                "transaction_id": {
                    "type": "integer",
                    "description": "ID de la transaction"
                },
                "amount": {
                    "type": "string",
                    "description": "Montant à associer (optionnel)"
                },
            },
            "required": ["invoice_id", "transaction_id"],
        },
    ),
    Tool(
        name="pennylane_unmatch_transaction_from_supplier_invoice",
        description="Dissocie une transaction d'une facture fournisseur",
        inputSchema={
            "type": "object",
            "properties": {
                "invoice_id": {
                    "type": "integer",
                    "description": "ID de la facture fournisseur"
                },
                "transaction_id": {
                    "type": "integer",
                    "description": "ID de la transaction"
                },
            },
            "required": ["invoice_id", "transaction_id"],
        },
    ),
    
    # ==================== COMPTABILITÉ ====================
    Tool(
        name="pennylane_get_trial_balance",
        description="Récupère la balance générale pour une période donnée",
        inputSchema={
            "type": "object",
            "properties": {
                "period_start": {
                    "type": "string",
                    "description": "Date de début (YYYY-MM-DD)"
                },
                "period_end": {
                    "type": "string",
                    "description": "Date de fin (YYYY-MM-DD)"
                },
                "is_auxiliary": {
                    "type": "boolean",
                    "description": "Inclure les comptes auxiliaires",
                    "default": False
                },
                "page": {
                    "type": "integer",
                    "description": "Numéro de page",
                    "default": 1
                },
                "per_page": {
                    "type": "integer",
                    "description": "Items par page (1-1000)",
                    "default": 100
                },
            },
            "required": ["period_start", "period_end"],
        },
    ),
    Tool(
        name="pennylane_list_ledger_accounts",
        description="Liste les comptes du plan comptable",
        inputSchema={
            "type": "object",
            "properties": {
                "page": {
                    "type": "integer",
                    "description": "Numéro de page",
                    "default": 1
                },
                "per_page": {
                    "type": "integer",
                    "description": "Items par page (1-1000)",
                    "default": 100
                },
                "filter": {
                    "type": "string",
                    "description": "Filtres (ex: 'enabled:eq:true')"
                },
            },
        },
    ),
    Tool(
        name="pennylane_list_categories",
        description="Liste les catégories comptables disponibles",
        inputSchema={
            "type": "object",
            "properties": {
                "limit": {
                    "type": "integer",
                    "description": "Nombre de résultats (1-100)",
                    "default": 100
                },
                "cursor": {
                    "type": "string",
                    "description": "Curseur de pagination"
                },
                "filter": {
                    "type": "string",
                    "description": "Filtres"
                },
            },
        },
    ),
    Tool(
        name="pennylane_list_bank_accounts",
        description="Liste les comptes bancaires de l'entreprise",
        inputSchema={
            "type": "object",
            "properties": {
                "limit": {
                    "type": "integer",
                    "description": "Nombre de résultats (1-100)",
                    "default": 100
                },
                "cursor": {
                    "type": "string",
                    "description": "Curseur de pagination"
                },
            },
        },
    ),
]


@app.list_tools()
async def list_tools() -> list[Tool]:
    """Liste tous les outils disponibles."""
    return TOOLS


@app.call_tool()
async def call_tool(name: str, arguments: Any) -> list[TextContent]:
    """Exécute un outil."""
    if not pennylane_client:
        raise RuntimeError("Pennylane client not initialized")
    
    try:
        result = None
        
        # ==================== FACTURES CLIENTS ====================
        if name == "pennylane_list_customer_invoices":
            result = await invoices.list_customer_invoices(
                pennylane_client,
                limit=arguments.get("limit", 20),
                cursor=arguments.get("cursor"),
                filter_query=arguments.get("filter"),
                sort=arguments.get("sort", "-id"),
            )
        
        elif name == "pennylane_get_customer_invoice":
            result = await invoices.get_customer_invoice(
                pennylane_client,
                arguments["invoice_id"]
            )
        
        elif name == "pennylane_create_customer_invoice":
            result = await invoices.create_customer_invoice(
                pennylane_client,
                customer_id=arguments["customer_id"],
                date=arguments["date"],
                deadline=arguments["deadline"],
                invoice_lines=arguments["invoice_lines"],
                draft=arguments.get("draft", True),
                currency=arguments.get("currency", "EUR"),
                language=arguments.get("language", "fr_FR"),
                **{k: v for k, v in arguments.items() 
                   if k not in ["customer_id", "date", "deadline", "invoice_lines", "draft", "currency", "language"]}
            )
        
        elif name == "pennylane_finalize_customer_invoice":
            result = await invoices.finalize_customer_invoice(
                pennylane_client,
                arguments["invoice_id"]
            )
        
        elif name == "pennylane_send_customer_invoice_email":
            result = await invoices.send_customer_invoice_by_email(
                pennylane_client,
                invoice_id=arguments["invoice_id"],
                recipients=arguments.get("recipients", [])
            )
        
        elif name == "pennylane_categorize_customer_invoice":
            result = await invoices.categorize_invoice(
                pennylane_client,
                invoice_id=arguments["invoice_id"],
                invoice_type="customer",
                categories=arguments["categories"]
            )
        
        # ==================== FACTURES FOURNISSEURS ====================
        elif name == "pennylane_list_supplier_invoices":
            result = await invoices.list_supplier_invoices(
                pennylane_client,
                limit=arguments.get("limit", 20),
                cursor=arguments.get("cursor"),
                filter_query=arguments.get("filter"),
                sort=arguments.get("sort", "-id")
            )
        
        elif name == "pennylane_get_supplier_invoice":
            result = await invoices.get_supplier_invoice(
                pennylane_client,
                arguments["invoice_id"]
            )
        
        elif name == "pennylane_categorize_supplier_invoice":
            result = await invoices.categorize_invoice(
                pennylane_client,
                invoice_id=arguments["invoice_id"],
                invoice_type="supplier",
                categories=arguments["categories"]
            )
        
        # ==================== DEVIS ====================
        elif name == "pennylane_list_quotes":
            result = await quotes.list_quotes(
                pennylane_client,
                limit=arguments.get("limit", 30),
                cursor=arguments.get("cursor"),
                filter_query=arguments.get("filter"),
                sort=arguments.get("sort", "-id")
            )
        
        elif name == "pennylane_get_quote":
            result = await quotes.get_quote(
                pennylane_client,
                arguments["quote_id"]
            )
        
        elif name == "pennylane_list_quote_invoice_line_sections":
            result = await quotes.list_quote_invoice_line_sections(
                pennylane_client,
                quote_id=arguments["quote_id"],
                limit=arguments.get("limit", 100),
                cursor=arguments.get("cursor"),
                sort=arguments.get("sort", "-id")
            )
        
        elif name == "pennylane_list_quote_appendices":
            result = await quotes.list_quote_appendices(
                pennylane_client,
                quote_id=arguments["quote_id"],
                limit=arguments.get("limit", 20),
                cursor=arguments.get("cursor")
            )
        
        elif name == "pennylane_create_quote":
            # Extraire les paramètres principaux
            main_params = {
                "customer_id": arguments["customer_id"],
                "invoice_lines": arguments["invoice_lines"],
                "date": arguments["date"],
                "deadline": arguments["deadline"],
                "currency": arguments.get("currency", "EUR"),
                "language": arguments.get("language", "fr_FR"),
            }
            
            # Ajouter les paramètres optionnels s'ils sont présents
            optional_params = ["discount", "invoice_line_sections", "quote_template_id",
                             "pdf_invoice_free_text", "pdf_invoice_subject", "pdf_description",
                             "special_mention", "external_reference"]
            
            for param in optional_params:
                if param in arguments:
                    main_params[param] = arguments[param]
            
            result = await quotes.create_quote(
                pennylane_client,
                **main_params
            )
        
        elif name == "pennylane_update_quote":
            result = await quotes.update_quote(
                pennylane_client,
                quote_id=arguments["quote_id"],
                **{k: v for k, v in arguments.items() if k != "quote_id"}
            )
        
        elif name == "pennylane_update_quote_status":
            result = await quotes.update_quote_status(
                pennylane_client,
                quote_id=arguments["quote_id"],
                status=arguments["status"]
            )
        
        # ==================== CLIENTS ====================
        elif name == "pennylane_list_customers":
            result = await customers.list_customers(
                pennylane_client,
                limit=arguments.get("limit", 20),
                cursor=arguments.get("cursor"),
                filter_query=arguments.get("filter"),
                sort=arguments.get("sort", "-id")
            )
        
        elif name == "pennylane_get_customer":
            result = await customers.get_customer(
                pennylane_client,
                arguments["customer_id"]
            )
        
        elif name == "pennylane_get_company_customer":
            result = await customers.get_company_customer(
                pennylane_client,
                arguments["customer_id"]
            )
        
        elif name == "pennylane_get_individual_customer":
            result = await customers.get_individual_customer(
                pennylane_client,
                arguments["customer_id"]
            )
        
        elif name == "pennylane_create_company_customer":
            # Extraire les paramètres principaux
            main_params = {
                "name": arguments["name"],
                "billing_address": arguments["billing_address"],
                "payment_conditions": arguments.get("payment_conditions", "30_days"),
                "billing_language": arguments.get("billing_language", "fr_FR"),
            }
            
            # Ajouter les paramètres optionnels s'ils sont présents
            optional_params = ["emails", "phone", "vat_number", "reg_no", "billing_iban", 
                             "recipient", "reference", "notes", "external_reference", 
                             "delivery_address", "ledger_account"]
            
            for param in optional_params:
                if param in arguments:
                    main_params[param] = arguments[param]
            
            result = await customers.create_company_customer(
                pennylane_client,
                **main_params
            )
        
        elif name == "pennylane_create_individual_customer":
            # Extraire les paramètres principaux
            main_params = {
                "first_name": arguments["first_name"],
                "last_name": arguments["last_name"],
                "billing_address": arguments["billing_address"],
                "payment_conditions": arguments.get("payment_conditions", "30_days"),
                "billing_language": arguments.get("billing_language", "fr_FR"),
            }
            
            # Ajouter les paramètres optionnels s'ils sont présents
            optional_params = ["emails", "phone", "billing_iban", "recipient", "reference", 
                             "notes", "external_reference", "delivery_address", "ledger_account"]
            
            for param in optional_params:
                if param in arguments:
                    main_params[param] = arguments[param]
            
            result = await customers.create_individual_customer(
                pennylane_client,
                **main_params
            )
        
        # ==================== FOURNISSEURS ====================
        elif name == "pennylane_list_suppliers":
            result = await suppliers.list_suppliers(
                pennylane_client,
                limit=arguments.get("limit", 20),
                cursor=arguments.get("cursor"),
                filter_query=arguments.get("filter"),
                sort=arguments.get("sort", "-id")
            )
        
        elif name == "pennylane_get_supplier":
            result = await suppliers.get_supplier(
                pennylane_client,
                arguments["supplier_id"]
            )
        
        elif name == "pennylane_create_supplier":
            result = await suppliers.create_supplier(
                pennylane_client,
                name=arguments["name"],
                postal_address=arguments.get("postal_address"),
                emails=arguments.get("emails"),
                iban=arguments.get("iban"),
                vat_number=arguments.get("vat_number"),
                **{k: v for k, v in arguments.items() 
                   if k not in ["name", "postal_address", "emails", "iban", "vat_number"]}
            )
        
        # ==================== TRANSACTIONS ====================
        elif name == "pennylane_list_transactions":
            result = await transactions.list_transactions(
                pennylane_client,
                limit=arguments.get("limit", 20),
                cursor=arguments.get("cursor"),
                filter_query=arguments.get("filter"),
                sort=arguments.get("sort", "-date")
            )
        
        elif name == "pennylane_get_transaction":
            result = await transactions.get_transaction(
                pennylane_client,
                arguments["transaction_id"]
            )
        
        elif name == "pennylane_create_transaction":
            result = await transactions.create_transaction(
                pennylane_client,
                date=arguments["date"],
                amount=arguments["amount"],
                label=arguments["label"],
                bank_account_id=arguments["bank_account_id"],
                fee=arguments.get("fee", "0.00"),
                **{k: v for k, v in arguments.items() 
                   if k not in ["date", "amount", "label", "bank_account_id", "fee"]}
            )
        
        elif name == "pennylane_update_transaction":
            result = await transactions.update_transaction(
                pennylane_client,
                transaction_id=arguments["transaction_id"],
                **{k: v for k, v in arguments.items() if k != "transaction_id"}
            )
        
        elif name == "pennylane_categorize_transaction":
            result = await transactions.categorize_transaction(
                pennylane_client,
                transaction_id=arguments["transaction_id"],
                categories=arguments["categories"]
            )
        
        elif name == "pennylane_match_transaction_to_customer_invoice":
            result = await transactions.match_transaction_to_customer_invoice(
                pennylane_client,
                invoice_id=arguments["invoice_id"],
                transaction_id=arguments["transaction_id"],
                amount=arguments.get("amount")
            )
        
        elif name == "pennylane_unmatch_transaction_from_customer_invoice":
            result = await transactions.unmatch_transaction_from_customer_invoice(
                pennylane_client,
                invoice_id=arguments["invoice_id"],
                transaction_id=arguments["transaction_id"]
            )
        
        elif name == "pennylane_match_transaction_to_supplier_invoice":
            result = await transactions.match_transaction_to_supplier_invoice(
                pennylane_client,
                invoice_id=arguments["invoice_id"],
                transaction_id=arguments["transaction_id"],
                amount=arguments.get("amount")
            )
        
        elif name == "pennylane_unmatch_transaction_from_supplier_invoice":
            result = await transactions.unmatch_transaction_from_supplier_invoice(
                pennylane_client,
                invoice_id=arguments["invoice_id"],
                transaction_id=arguments["transaction_id"]
            )
        
        # ==================== COMPTABILITÉ ====================
        elif name == "pennylane_get_trial_balance":
            result = await accounting.get_trial_balance(
                pennylane_client,
                period_start=arguments["period_start"],
                period_end=arguments["period_end"],
                is_auxiliary=arguments.get("is_auxiliary", False),
                page=arguments.get("page", 1),
                per_page=arguments.get("per_page", 100)
            )
        
        elif name == "pennylane_list_ledger_accounts":
            result = await accounting.list_ledger_accounts(
                pennylane_client,
                page=arguments.get("page", 1),
                per_page=arguments.get("per_page", 100),
                filter_query=arguments.get("filter")
            )
        
        elif name == "pennylane_list_categories":
            result = await accounting.list_categories(
                pennylane_client,
                limit=arguments.get("limit", 100),
                cursor=arguments.get("cursor"),
                filter_query=arguments.get("filter")
            )
        
        elif name == "pennylane_list_bank_accounts":
            result = await accounting.list_bank_accounts(
                pennylane_client,
                limit=arguments.get("limit", 100),
                cursor=arguments.get("cursor")
            )
        
        else:
            raise ValueError(f"Unknown tool: {name}")
        
        # Formatage de la réponse
        import json
        return [TextContent(type="text", text=json.dumps(result, indent=2, ensure_ascii=False))]
    
    except Exception as e:
        logger.error(f"Error executing tool {name}: {str(e)}", exc_info=True)
        return [TextContent(type="text", text=f"Error: {str(e)}")]


async def main():
    """Point d'entrée principal."""
    global pennylane_client
    
    # Récupération de la clé API
    api_key = os.getenv("PENNYLANE_API_KEY")
    if not api_key:
        raise ValueError("PENNYLANE_API_KEY environment variable is required")
    
    base_url = os.getenv("PENNYLANE_BASE_URL", "https://app.pennylane.com/api/external/v2")
    
    # Initialisation du client
    pennylane_client = PennylaneClient(api_key, base_url)
    logger.info("Pennylane MCP server starting...")
    logger.info(f"Base URL: {base_url}")
    logger.info(f"Available tools: {len(TOOLS)}")
    
    try:
        async with stdio_server() as (read_stream, write_stream):
            await app.run(read_stream, write_stream, app.create_initialization_options())
    finally:
        if pennylane_client:
            await pennylane_client.close()
            logger.info("Pennylane client closed")


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())