# Pennylane MCP Server

[English](#english) · [Français](#français)

An MCP (Model Context Protocol) server that gives Claude direct access to your [Pennylane](https://pennylane.com) accounting data — invoices, customers, suppliers, transactions, ledger, and more.

---

<a id="english"></a>

## 🇬🇧 English

### What it does

This server exposes **38 tools** covering the Pennylane V2 API, letting Claude read and write invoices, manage customers and suppliers, query transactions, fetch the trial balance, and categorize entries on your behalf.

**Features**
- Customer & supplier invoices (list, get, create, finalize, email, categorize)
- Customer management (list, get, create — both companies and individuals)
- Quote lifecycle (list, get, create, update, change status)
- Suppliers (list, get, create)
- Transactions (list, get, create, update, categorize, match/unmatch with invoices)
- Accounting (trial balance, ledger accounts, categories, bank accounts)
- **Client-side rate limiting** (5 req/s, Pennylane's official limit)
- **Exponential backoff retry** on 429 / 5xx, honoring `Retry-After`

### Prerequisites

| Tool | Why | Install |
|---|---|---|
| Python ≥ 3.10 | Runtime | macOS: `brew install python@3.12` |
| `uv` | Package manager (recommended) | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| Git | Cloning | `brew install git` |
| Pennylane account | Obvious | [pennylane.com](https://pennylane.com) |

### Step 1 — Get your Pennylane API key

1. Log into Pennylane
2. Go to **Settings → API → API Keys**
3. Click **Create a new key**
4. Grant these scopes (check all that apply to what you want Claude to do):
   - `customers:all` · `products:all` · `customer_invoices:all` · `quotes:all`
   - `suppliers:all` · `supplier_invoices:all` · `ledger` · `trial_balance:readonly`
   - `categories:all` · `transactions:readonly` · `bank_accounts:readonly`
5. **Copy the key immediately** — it's shown only once. Store it somewhere safe (password manager).

> ⚠️ Never commit this key to git. The `.gitignore` in this repo blocks `.env` files, but double-check before pushing.

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
4. Reopen Claude Desktop → the hammer/tool icon should now show Pennylane tools

### Step 4B — Use with Claude Code

One command:

```bash
claude mcp add pennylane --scope user -- uv --directory /absolute/path/to/pennylane-mcp run pennylane-mcp
```

Then set your environment variables (Claude Code inherits your shell env):

```bash
export PENNYLANE_API_KEY="your_actual_key_here"
export PENNYLANE_BASE_URL="https://app.pennylane.com/api/external/v2"
```

To make it permanent, add those `export` lines to your `~/.zshrc` or `~/.bashrc`.

Verify with:

```bash
claude mcp list
```

### Step 5 — Test it

Open a new Claude conversation and ask:

> "List my 5 most recent customer invoices from Pennylane."

If Claude responds with real invoice data from your account, you're done 🎉

### Troubleshooting

| Error | Fix |
|---|---|
| `PENNYLANE_API_KEY environment variable is required` | `.env` file missing or key not set. Run `cp .env.example .env` and edit it. |
| `API error: 401 - Unauthorized` | Key is wrong or revoked. Regenerate in Pennylane settings. |
| `API error: 403 - Forbidden` | Key missing scopes. Create a new key with the required scopes (see Step 1). |
| `API error: 429 - Too Many Requests` | Client rate limit shouldn't let this happen. If it does, wait 60s and retry — built-in retry handles it. |
| `command not found: uv` | Install uv: `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| Tools don't appear in Claude Desktop | Fully quit (⌘Q) and reopen. Check Claude Desktop → Settings → Developer → Logs for errors. |

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

Current coverage: **38 tools** across the 7 most-used Pennylane V2 API domains (invoices, customers, quotes, suppliers, transactions, accounting, bank accounts).

**Not yet exposed — contributions welcome:**

| Domain | Scopes needed |
|---|---|
| FEC / AGL exports | `exports:fec`, `exports:agl` |
| Fiscal years | `fiscal_years:readonly` |
| File attachments | `file_attachments:all` |
| Billing subscriptions | `billing_subscriptions:all` |
| Commercial documents | `commercial_documents:all` |
| Customer mandates | `customer_mandates:all` |
| E-invoicing | `e_invoices:all` |
| Beneficial owners (RBE) | (see Pennylane docs) |

Each new tool follows the same pattern as those in `src/pennylane_mcp/tools/`: one function per endpoint, registered in `server.py`. Open an issue to request a specific endpoint or submit a PR.

### Contributing

PRs welcome — especially for:
- Additional Pennylane V2 endpoints (see Roadmap above)
- Tests
- Improved error messages

### Credits & License

Forked from [Akilinoxx/pennylane-mcp](https://github.com/Akilinoxx/pennylane-mcp). MIT License.

---

<a id="français"></a>

## 🇫🇷 Français

### Ce que ça fait

Ce serveur expose **38 outils** couvrant l'API Pennylane V2, permettant à Claude de lire et d'écrire des factures, gérer clients et fournisseurs, interroger des transactions, récupérer la balance, et catégoriser des écritures pour toi.

**Fonctionnalités**
- Factures clients & fournisseurs (liste, détail, création, finalisation, envoi par email, catégorisation)
- Gestion clients (liste, détail, création — entreprises et particuliers)
- Cycle de vie des devis (liste, détail, création, modification, changement de statut)
- Fournisseurs (liste, détail, création)
- Transactions (liste, détail, création, modification, catégorisation, rapprochement factures)
- Comptabilité (balance, comptes du grand livre, catégories, comptes bancaires)
- **Rate limiting côté client** (5 req/s, limite officielle Pennylane)
- **Retry avec backoff exponentiel** sur 429 / 5xx, respect du `Retry-After`

### Prérequis

| Outil | Pourquoi | Installation |
|---|---|---|
| Python ≥ 3.10 | Runtime | macOS : `brew install python@3.12` |
| `uv` | Gestionnaire de paquets (recommandé) | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| Git | Pour cloner | `brew install git` |
| Compte Pennylane | Évident | [pennylane.com](https://pennylane.com) |

### Étape 1 — Obtenir ta clé API Pennylane

1. Connecte-toi à Pennylane
2. Va dans **Paramètres → API → Clés API**
3. Clique sur **Créer une nouvelle clé**
4. Accorde ces scopes (coche ceux qui correspondent à ce que tu veux faire faire à Claude) :
   - `customers:all` · `products:all` · `customer_invoices:all` · `quotes:all`
   - `suppliers:all` · `supplier_invoices:all` · `ledger` · `trial_balance:readonly`
   - `categories:all` · `transactions:readonly` · `bank_accounts:readonly`
5. **Copie la clé immédiatement** — elle n'est affichée qu'une fois. Stocke-la dans un gestionnaire de mots de passe.

> ⚠️ Ne commit jamais cette clé sur git. Le `.gitignore` du repo bloque les fichiers `.env`, mais vérifie quand même avant tout push.

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
4. Rouvre Claude Desktop → l'icône marteau/outils doit maintenant afficher les outils Pennylane

### Étape 4B — Utilisation avec Claude Code

Une seule commande :

```bash
claude mcp add pennylane --scope user -- uv --directory /chemin/absolu/vers/pennylane-mcp run pennylane-mcp
```

Puis exporte tes variables d'environnement (Claude Code hérite de ton shell) :

```bash
export PENNYLANE_API_KEY="ta_vraie_clé_ici"
export PENNYLANE_BASE_URL="https://app.pennylane.com/api/external/v2"
```

Pour que ce soit permanent, ajoute ces lignes `export` à ton `~/.zshrc` ou `~/.bashrc`.

Vérifie avec :

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

Couverture actuelle : **38 outils** répartis sur les 7 domaines de l'API Pennylane V2 les plus utilisés (factures, clients, devis, fournisseurs, transactions, comptabilité, comptes bancaires).

**Pas encore exposé — contributions bienvenues :**

| Domaine | Scopes requis |
|---|---|
| Exports FEC / AGL | `exports:fec`, `exports:agl` |
| Exercices fiscaux | `fiscal_years:readonly` |
| Pièces jointes | `file_attachments:all` |
| Abonnements | `billing_subscriptions:all` |
| Documents commerciaux | `commercial_documents:all` |
| Mandats clients | `customer_mandates:all` |
| E-facturation | `e_invoices:all` |
| Bénéficiaires effectifs (RBE) | (voir doc Pennylane) |

Chaque nouvel outil suit le même pattern que ceux de `src/pennylane_mcp/tools/` : une fonction par endpoint, enregistrée dans `server.py`. Ouvre une issue pour demander un endpoint précis ou soumets une PR.

### Contribuer

Les PR sont bienvenues — notamment pour :
- Endpoints Pennylane V2 additionnels (voir Roadmap ci-dessus)
- Tests
- Messages d'erreur améliorés

### Crédits & Licence

Forké depuis [Akilinoxx/pennylane-mcp](https://github.com/Akilinoxx/pennylane-mcp). Licence MIT.
