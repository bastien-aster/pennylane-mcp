# Pennylane MCP Server

[English](#english) · [Français](#français)

An MCP (Model Context Protocol) server that gives Claude direct access to your [Pennylane](https://pennylane.com) accounting data — invoices, customers, suppliers, transactions, ledger, exports, and more.

**Covers 161 endpoints of the Pennylane Company API v2**, auto-generated from the [official OpenAPI spec](docs/pennylane-openapi.json).

---

<a id="english"></a>

## 🇬🇧 English

### What it does

This server exposes **161 tools** covering nearly the entire [Pennylane Company API v2](https://pennylane.readme.io/docs/api-overview), letting Claude read and write to your Pennylane workspace — invoices, quotes, customers, suppliers, transactions, ledger entries, mandates (SEPA + GoCardless), exports (FEC / AGL / General Ledger), billing subscriptions, commercial documents, and more.

**Highlights**
- Customer & supplier invoices: list, get, create, update, finalize, email, mark paid, import, match transactions, appendices, line sections, payments
- Quotes (full lifecycle including appendices and email)
- Customers: company, individual, contacts, categories
- Suppliers & products: full CRUD + categorization
- Ledger entries / entry lines / lettering / accounts
- Exports: FEC, Analytical General Ledger, General Ledger
- Billing subscriptions & commercial documents
- SEPA mandates & GoCardless mandates
- Bank accounts & bank establishments
- Changelogs (delta sync endpoints for 8 domains)
- Purchase requests, fiscal years, categories, journals, category groups
- **Client-side rate limiting** (5 req/s, Pennylane's official limit)
- **Exponential backoff retry** on 429 / 5xx, honoring `Retry-After`

> Skipped on purpose: `webhook_subscription` — use [Make](https://make.com) or your own webhook infrastructure instead of letting Claude manage webhooks.

### ⚠️ Which Pennylane API is this? Company vs Firm

Pennylane exposes **two distinct APIs**. You must know which one you have before going further:

| | **Company API** ← this MCP | Firm API |
|---|---|---|
| Who uses it | Companies using Pennylane for their own accounting | Accounting firms managing multiple client companies |
| Authentication | Single API key scoped to one company | Firm-level key with per-client impersonation |
| Base URL | `https://app.pennylane.com/api/external/v2` | Different base URL (see Pennylane Firm API docs) |
| Token location | Pennylane dashboard → Settings → API | Firm admin panel |
| **Docs** | https://pennylane.readme.io/ (current doc site) | https://firm-api.pennylane.com/docs (separate product) |

**This MCP server only supports the Company API.** If you run a regular business and use Pennylane internally for your own accounting (like we do at Aster Développement), this is what you want. If you are an accountant managing multiple client books through Pennylane, you need the Firm API instead — which has a different schema and would require a separate MCP implementation.

When in doubt: if you log into Pennylane and see **your own company's accounting**, you have Company API access. If you log in and see a **list of client companies**, you have the Firm API.

### Prerequisites

| Tool | Why | Install |
|---|---|---|
| Python ≥ 3.10 | Runtime | macOS: `brew install python@3.12` |
| `uv` | Package manager (recommended) | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| Git | Cloning | `brew install git` |
| Pennylane Company account | Obvious | [pennylane.com](https://pennylane.com) |

### Step 1 — Get your Pennylane API key

1. Log into [Pennylane](https://app.pennylane.com)
2. Go to **Settings → API → API Keys**
3. Click **Create a new key**
4. Grant these scopes (or only the subset you need):
   - `customers:all` · `products:all` · `customer_invoices:all` · `quotes:all`
   - `suppliers:all` · `supplier_invoices:all` · `ledger` · `trial_balance:readonly`
   - `categories:all` · `transactions:readonly` · `bank_accounts:readonly`
   - `exports:fec` · `exports:agl` · `fiscal_years:readonly` · `file_attachments:all`
   - `billing_subscriptions:all` · `commercial_documents:all`
   - `customer_mandates:all` · `e_invoices:all`
5. **Copy the key immediately** — it's shown only once. Store it in a password manager.

📘 Official docs: [https://pennylane.readme.io/docs/api-overview](https://pennylane.readme.io/docs/api-overview)

> ⚠️ Never commit this key to git. The `.gitignore` blocks `.env` files, but double-check before pushing.

### Step 2 — Clone & install

```bash
git clone https://github.com/bastien-aster/pennylane-mcp.git
cd pennylane-mcp
uv venv
uv pip install -e .
```

If you don't use `uv`, plain pip works:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

### Step 3 — Configure your API key

```bash
cp .env.example .env
```

Open `.env` and paste your key:

```
PENNYLANE_API_KEY=your_actual_key_here
PENNYLANE_BASE_URL=https://app.pennylane.com/api/external/v2
```

### Step 4A — Use with Claude Desktop

1. Open Claude Desktop → **Settings → Developer → Edit Config**
2. Add this block to `claude_desktop_config.json` (replace `/absolute/path/to/pennylane-mcp` with your actual clone path):

```json
{
  "mcpServers": {
    "pennylane": {
      "command": "uv",
      "args": [
        "--directory",
        "/absolute/path/to/pennylane-mcp",
        "run",
        "pennylane-mcp"
      ],
      "env": {
        "PENNYLANE_API_KEY": "your_actual_key_here",
        "PENNYLANE_BASE_URL": "https://app.pennylane.com/api/external/v2"
      }
    }
  }
}
```

3. Save and **fully quit Claude Desktop** (⌘Q on macOS, not just close the window)
4. Reopen Claude Desktop → the tool icon now lists the 161 Pennylane tools

### Step 4B — Use with Claude Code

One command:

```bash
claude mcp add pennylane --scope user -- uv --directory /absolute/path/to/pennylane-mcp run pennylane-mcp
```

Then set your environment variables:

```bash
export PENNYLANE_API_KEY="your_actual_key_here"
export PENNYLANE_BASE_URL="https://app.pennylane.com/api/external/v2"
```

To make it permanent, add those `export` lines to your `~/.zshrc` or `~/.bashrc`.

Verify:

```bash
claude mcp list
```

### Step 5 — Test it

Open a new Claude conversation and ask:

> "List my 5 most recent customer invoices from Pennylane."

If Claude returns real invoice data from your account, you're done 🎉

### Troubleshooting

| Error | Fix |
|---|---|
| `PENNYLANE_API_KEY environment variable is required` | `.env` file missing or key not set. Run `cp .env.example .env` and edit it. |
| `API error: 401 - Unauthorized` | Key is wrong or revoked. Regenerate in Pennylane settings. |
| `API error: 403 - Forbidden` | Key missing scopes. Create a new key with the required scopes (see Step 1). |
| `API error: 429 - Too Many Requests` | Client rate limit shouldn't let this happen. If it does, wait 60s — built-in retry handles it. |
| `command not found: uv` | Install uv: `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| Tools don't appear in Claude Desktop | Fully quit (⌘Q) and reopen. Check Claude Desktop → Settings → Developer → Logs. |
| Too many tools, Claude picks the wrong one | Consider splitting the MCP into focused scopes per your use case — open an issue if you need this. |

### 🔒 Security

This fork has been audited before distribution:
- No subprocess execution, no `eval`/`exec`, no third-party telemetry
- **Single outbound destination:** the Pennylane API (configurable via `PENNYLANE_BASE_URL`)
- API token sent only as `Authorization: Bearer` header; never logged
- `.env` is gitignored and the fork's git history was purged with `git filter-repo` to remove a leaked key that was present in the upstream repository

**Your responsibilities as a user:**
- Use a dedicated Pennylane API key with the **minimum scopes** you actually need
- Rotate keys periodically, and immediately if you suspect any leak
- Never commit `.env` or hardcode the key in source files
- If you find a vulnerability, open a **private security advisory** on this repo (Security tab → Report a vulnerability), not a public issue

### 🗺️ Roadmap & Updates

The full Pennylane Company API v2 spec is pinned in [docs/pennylane-openapi.json](docs/pennylane-openapi.json) and the tool modules under `src/pennylane_mcp/tools/` are regenerated from it by running:

```bash
python scripts/generate_tools.py
```

When Pennylane ships new endpoints, update the spec file and rerun the script — no hand-editing needed.

**What's NOT covered and by choice:**
- `webhook_subscription` — use Make, n8n, or your own webhook infrastructure
- Firm API — different product, requires a separate MCP implementation

**Known limitations:**
- Request bodies are passed through as free-form JSON. Claude figures out the right shape from the Pennylane docs — but for complex endpoints (e.g., creating a compound invoice with line items), point Claude at the [Pennylane docs page](https://pennylane.readme.io/reference) for the specific endpoint when the first try fails.

### Contributing

PRs welcome — especially for:
- Richer tool descriptions (auto-generated ones are terse)
- Tests against a sandbox Pennylane account
- A subset/profile system so users can enable only the scopes they need (e.g., "sales", "accounting", "exports")

### Credits & License

Forked from [Akilinoxx/pennylane-mcp](https://github.com/Akilinoxx/pennylane-mcp). MIT License.

Pennylane, Pennylane Company API, and related marks are trademarks of Pennylane. This project is not affiliated with or endorsed by Pennylane.

---

<a id="français"></a>

## 🇫🇷 Français

### Ce que ça fait

Ce serveur expose **161 outils** couvrant quasiment toute la [Pennylane Company API v2](https://pennylane.readme.io/docs/api-overview), permettant à Claude de lire et d'écrire dans ton compte Pennylane — factures, devis, clients, fournisseurs, transactions, écritures comptables, mandats (SEPA + GoCardless), exports (FEC / AGL / Grand Livre), abonnements, documents commerciaux, et plus.

**Points clés**
- Factures clients & fournisseurs : liste, détail, création, modification, finalisation, envoi email, marquer payé, import, rapprochement transactions, pièces jointes, sections de lignes, paiements
- Devis (cycle complet avec pièces jointes et envoi par email)
- Clients : entreprises, particuliers, contacts, catégories
- Fournisseurs & produits : CRUD complet + catégorisation
- Écritures comptables / lignes / lettrage / comptes du grand livre
- Exports : FEC, Grand Livre analytique, Grand Livre
- Abonnements & documents commerciaux
- Mandats SEPA & mandats GoCardless
- Comptes bancaires & établissements bancaires
- Changelogs (endpoints de sync delta sur 8 domaines)
- Demandes d'achat, exercices fiscaux, catégories, journaux, groupes de catégories
- **Rate limiting côté client** (5 req/s, limite officielle Pennylane)
- **Retry avec backoff exponentiel** sur 429 / 5xx, respect du `Retry-After`

> Volontairement non exposé : `webhook_subscription` — utilise [Make](https://make.com) ou ta propre infra webhook plutôt que de laisser Claude gérer ça.

### ⚠️ Quelle API Pennylane ? Company vs Firm

Pennylane expose **deux API distinctes**. Il faut savoir laquelle tu as avant d'aller plus loin :

| | **Company API** ← ce MCP | Firm API |
|---|---|---|
| Utilisateur cible | Entreprises qui utilisent Pennylane pour leur propre compta | Cabinets d'expertise comptable gérant plusieurs clients |
| Authentification | Clé API unique, limitée à une entreprise | Clé au niveau cabinet avec impersonation par client |
| Base URL | `https://app.pennylane.com/api/external/v2` | Base URL différente (voir doc Firm API) |
| Emplacement du token | Dashboard Pennylane → Paramètres → API | Admin cabinet |
| **Documentation** | https://pennylane.readme.io/ (le site ci-dessus) | https://firm-api.pennylane.com/docs (produit séparé) |

**Ce serveur MCP ne supporte que la Company API.** Si tu es une entreprise classique qui utilise Pennylane pour ta propre compta (comme nous chez Aster Développement), c'est exactement ce qu'il te faut. Si tu es comptable et que tu gères les livres de plusieurs clients via Pennylane, il te faut la Firm API — qui a un schéma différent et nécessite une implémentation MCP séparée.

En cas de doute : si quand tu te connectes à Pennylane tu vois **ta propre compta d'entreprise**, tu as accès à la Company API. Si tu vois une **liste d'entreprises clientes**, tu as la Firm API.

### Prérequis

| Outil | Pourquoi | Installation |
|---|---|---|
| Python ≥ 3.10 | Runtime | macOS : `brew install python@3.12` |
| `uv` | Gestionnaire de paquets (recommandé) | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| Git | Pour cloner | `brew install git` |
| Compte Pennylane Company | Évident | [pennylane.com](https://pennylane.com) |

### Étape 1 — Obtenir ta clé API Pennylane

1. Connecte-toi à [Pennylane](https://app.pennylane.com)
2. Va dans **Paramètres → API → Clés API**
3. Clique sur **Créer une nouvelle clé**
4. Accorde ces scopes (ou seulement le sous-ensemble dont tu as besoin) :
   - `customers:all` · `products:all` · `customer_invoices:all` · `quotes:all`
   - `suppliers:all` · `supplier_invoices:all` · `ledger` · `trial_balance:readonly`
   - `categories:all` · `transactions:readonly` · `bank_accounts:readonly`
   - `exports:fec` · `exports:agl` · `fiscal_years:readonly` · `file_attachments:all`
   - `billing_subscriptions:all` · `commercial_documents:all`
   - `customer_mandates:all` · `e_invoices:all`
5. **Copie la clé immédiatement** — elle n'est affichée qu'une fois. Stocke-la dans un gestionnaire de mots de passe.

📘 Documentation officielle : [https://pennylane.readme.io/docs/api-overview](https://pennylane.readme.io/docs/api-overview)

> ⚠️ Ne commit jamais cette clé sur git. Le `.gitignore` bloque les `.env`, mais vérifie quand même avant tout push.

### Étape 2 — Cloner & installer

```bash
git clone https://github.com/bastien-aster/pennylane-mcp.git
cd pennylane-mcp
uv venv
uv pip install -e .
```

Si tu n'utilises pas `uv`, pip fait aussi le job :

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

### Étape 3 — Configurer ta clé

```bash
cp .env.example .env
```

Ouvre `.env` et colle ta clé :

```
PENNYLANE_API_KEY=ta_vraie_clé_ici
PENNYLANE_BASE_URL=https://app.pennylane.com/api/external/v2
```

### Étape 4A — Utilisation avec Claude Desktop

1. Ouvre Claude Desktop → **Paramètres → Développeur → Modifier la config**
2. Ajoute ce bloc dans `claude_desktop_config.json` (remplace `/chemin/absolu/vers/pennylane-mcp` par le vrai chemin de ton clone) :

```json
{
  "mcpServers": {
    "pennylane": {
      "command": "uv",
      "args": [
        "--directory",
        "/chemin/absolu/vers/pennylane-mcp",
        "run",
        "pennylane-mcp"
      ],
      "env": {
        "PENNYLANE_API_KEY": "ta_vraie_clé_ici",
        "PENNYLANE_BASE_URL": "https://app.pennylane.com/api/external/v2"
      }
    }
  }
}
```

3. Enregistre et **quitte complètement Claude Desktop** (⌘Q sur macOS, pas juste fermer la fenêtre)
4. Rouvre Claude Desktop → l'icône d'outils affiche maintenant les 161 outils Pennylane

### Étape 4B — Utilisation avec Claude Code

Une seule commande :

```bash
claude mcp add pennylane --scope user -- uv --directory /chemin/absolu/vers/pennylane-mcp run pennylane-mcp
```

Puis exporte tes variables d'environnement :

```bash
export PENNYLANE_API_KEY="ta_vraie_clé_ici"
export PENNYLANE_BASE_URL="https://app.pennylane.com/api/external/v2"
```

Pour que ce soit permanent, ajoute ces lignes `export` à ton `~/.zshrc` ou `~/.bashrc`.

Vérifie :

```bash
claude mcp list
```

### Étape 5 — Tester

Ouvre une nouvelle conversation Claude et demande :

> « Liste mes 5 dernières factures clients dans Pennylane. »

Si Claude te répond avec de vraies factures de ton compte, c'est bon 🎉

### Dépannage

| Erreur | Solution |
|---|---|
| `PENNYLANE_API_KEY environment variable is required` | Fichier `.env` manquant ou clé non définie. Fais `cp .env.example .env` et édite-le. |
| `API error: 401 - Unauthorized` | Clé erronée ou révoquée. Régénère une clé dans les paramètres Pennylane. |
| `API error: 403 - Forbidden` | Clé avec scopes insuffisants. Crée une nouvelle clé avec les bons scopes (voir Étape 1). |
| `API error: 429 - Too Many Requests` | Ne devrait pas arriver grâce au rate limiting client. Si ça arrive, attends 60s — le retry intégré gère. |
| `command not found: uv` | Installe uv : `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| Les outils n'apparaissent pas dans Claude Desktop | Quitte complètement (⌘Q) et rouvre. Vérifie les logs via Paramètres → Développeur. |
| Trop d'outils, Claude choisit le mauvais | Envisage de splitter le MCP en scopes ciblés selon ton usage — ouvre une issue si tu as besoin de ça. |

### 🔒 Sécurité

Ce fork a été audité avant d'être distribué :
- Aucun `subprocess`, aucun `eval`/`exec`, aucune télémétrie tierce
- **Une seule destination sortante :** l'API Pennylane (configurable via `PENNYLANE_BASE_URL`)
- Le token API n'est envoyé qu'en en-tête `Authorization: Bearer`, jamais loggé
- `.env` est dans le `.gitignore` et l'historique git du fork a été purgé avec `git filter-repo` pour retirer une clé leakée présente dans le repo upstream

**Tes responsabilités en tant qu'utilisateur :**
- Utilise une clé API Pennylane dédiée avec le **minimum de scopes** nécessaires
- Fais tourner tes clés régulièrement, et immédiatement en cas de doute
- Ne commit jamais `.env` et ne hard-code jamais la clé dans le code
- Si tu trouves une faille, ouvre une **security advisory privée** (onglet Security → Report a vulnerability), pas une issue publique

### 🗺️ Roadmap & Mises à jour

La spec OpenAPI complète de la Company API v2 est figée dans [docs/pennylane-openapi.json](docs/pennylane-openapi.json) et les modules d'outils sous `src/pennylane_mcp/tools/` sont générés à partir d'elle via :

```bash
python scripts/generate_tools.py
```

Quand Pennylane livre de nouveaux endpoints, mets à jour le fichier de spec et relance le script — rien à éditer à la main.

**Ce qui n'est PAS couvert, et pourquoi :**
- `webhook_subscription` — utilise Make, n8n, ou ta propre infra webhook
- Firm API — produit différent, nécessite une implémentation MCP séparée

**Limitations connues :**
- Les bodies de requêtes POST/PUT sont passés en JSON libre. Claude trouve la bonne forme grâce à la doc Pennylane — mais pour les endpoints complexes (ex: créer une facture composée avec lignes), pointe Claude vers la [page de doc Pennylane](https://pennylane.readme.io/reference) de l'endpoint spécifique si le premier essai échoue.

### Contribuer

Les PR sont bienvenues — notamment pour :
- Descriptions d'outils plus riches (l'auto-génération reste succincte)
- Tests contre un compte sandbox Pennylane
- Un système de profil/sous-ensemble pour n'activer que les scopes dont tu as besoin (ex: "ventes", "compta", "exports")

### Crédits & Licence

Forké depuis [Akilinoxx/pennylane-mcp](https://github.com/Akilinoxx/pennylane-mcp). Licence MIT.

Pennylane, Pennylane Company API et les marques associées sont des marques de Pennylane. Ce projet n'est ni affilié à ni soutenu par Pennylane.
