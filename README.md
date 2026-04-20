# Pennylane MCP

Branche ta compta Pennylane directement sur Claude. **161 outils** pour lire et modifier ta compta depuis une simple conversation.

[🇫🇷 Français](#-français) · [🇬🇧 English](#-english)

---

<a id="-français"></a>

## 🇫🇷 Français

### 🚀 Installation ultra-rapide (5 minutes chrono)

**Tu auras besoin :**
- Un Mac (ou Linux)
- Un compte [Pennylane](https://pennylane.com)
- [Claude Desktop](https://claude.ai/download) installé

**Tu n'as jamais ouvert le Terminal ?** Pas de panique. Fais `Cmd + Espace`, tape `Terminal`, appuie sur Entrée. C'est cette fenêtre noire qui s'ouvre — on va copier-coller dedans, c'est tout.

---

### Étape 1 · Installer les prérequis (une seule fois)

Copie-colle ces **2 commandes** dans le Terminal, l'une après l'autre :

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

```bash
brew install python@3.12 git && curl -LsSf https://astral.sh/uv/install.sh | sh
```

> Si Homebrew est déjà installé, la 1re commande ne fera rien de cassant. Tu peux la passer.

---

### Étape 2 · Télécharger le serveur

Copie-colle :

```bash
cd ~ && git clone https://github.com/bastien-aster/pennylane-mcp.git && cd pennylane-mcp && uv venv && uv pip install -e .
```

---

### Étape 3 · Récupérer ta clé API Pennylane

1. Va sur [app.pennylane.com](https://app.pennylane.com) et connecte-toi
2. Clique **Paramètres → API → Clés API**
3. Clique **Créer une nouvelle clé**
4. **Coche tous les scopes disponibles** (pour avoir accès à tout)
5. **Copie la clé tout de suite** — elle ne s'affichera qu'une seule fois !

📘 [Doc officielle Pennylane API](https://pennylane.readme.io/docs/api-overview)

---

### Étape 4 · Sauvegarder ta clé dans le projet

Dans le Terminal :

```bash
cd ~/pennylane-mcp && cp .env.example .env && open -e .env
```

Un fichier s'ouvre. Remplace `your_api_key_here` par **ta** clé (celle que tu viens de copier). Sauvegarde avec `Cmd + S` et ferme.

---

### Étape 5 · Trouver ton nom d'utilisateur Mac

Tape dans le Terminal :

```bash
whoami
```

**Note le résultat** (ex: `jamesbond`). Tu vas en avoir besoin à l'étape suivante.

---

### Étape 6 · Brancher sur Claude Desktop

1. Ouvre **Claude Desktop**
2. En haut à gauche : **Claude → Paramètres** (ou `Cmd + ,`)
3. Onglet **Développeur** → **Modifier la config**
4. Un fichier JSON s'ouvre. **Colle ce bloc dedans** (s'il y a déjà du contenu, ajoute-le en faisant attention aux virgules) :

```json
{
  "mcpServers": {
    "pennylane": {
      "command": "uv",
      "args": [
        "--directory",
        "/Users/TON_NOM_ICI/pennylane-mcp",
        "run",
        "pennylane-mcp"
      ],
      "env": {
        "PENNYLANE_API_KEY": "TA_CLÉ_ICI",
        "PENNYLANE_BASE_URL": "https://app.pennylane.com/api/external/v2"
      }
    }
  }
}
```

5. **Remplace** :
   - `TON_NOM_ICI` → ce que `whoami` a affiché à l'étape 5
   - `TA_CLÉ_ICI` → ta clé API Pennylane
6. Sauvegarde (`Cmd + S`) et ferme
7. **Quitte complètement Claude Desktop** : `Cmd + Q` (pas juste fermer la fenêtre !)
8. Rouvre Claude Desktop

---

### Étape 7 · Tester que ça marche

Dans une nouvelle conversation Claude, demande :

> Liste mes 5 dernières factures clients Pennylane.

Si Claude te répond avec de vraies factures de ton compte, **tu as gagné** 🎉

---

<details>
<summary><b>🎛️ Optionnel · N'activer qu'un sous-ensemble des 161 outils</b></summary>

Si tu trouves que Claude se perd parmi 161 outils, tu peux n'en activer qu'une partie. Ajoute la variable d'environnement `PENNYLANE_TOOLS` dans ta config Claude Desktop (bloc `"env"`, à côté de `PENNYLANE_API_KEY`) :

```json
"env": {
  "PENNYLANE_API_KEY": "TA_CLÉ_ICI",
  "PENNYLANE_BASE_URL": "https://app.pennylane.com/api/external/v2",
  "PENNYLANE_TOOLS": "sales,accounting"
}
```

**Profils disponibles :**

| Profil | Combien d'outils | Ce qu'il contient |
|---|---:|---|
| `sales` | 56 | Factures clients, devis, clients (entreprise/particulier), produits, documents commerciaux |
| `purchasing` | 27 | Factures fournisseurs, fournisseurs, demandes d'achat, pièces jointes |
| `accounting` | 30 | Écritures, lignes, comptes grand livre, journaux, catégories, balance, exercices fiscaux |
| `banking` | 11 | Transactions bancaires, comptes bancaires, établissements |
| `mandates` | 14 | Mandats SEPA, mandats GoCardless, Pro Account |
| `admin` | 23 | Profil, exports FEC/AGL, changelogs, abonnements, e-invoicing |
| `all` | 161 | Tout (défaut si la variable n'est pas définie) |

Tu peux combiner : `PENNYLANE_TOOLS=sales,banking,mandates`. Relance Claude Desktop après modification.

</details>

---

### 🆘 Ça marche pas ?

| Symptôme | Solution |
|---|---|
| "Claude dit qu'il n'a pas accès à Pennylane" | Vérifie que tu as bien quitté Claude Desktop avec `Cmd + Q` puis rouvert. Pas juste fermer la fenêtre. |
| "Erreur 401 Unauthorized" | Ta clé est fausse ou expirée. Régénère une nouvelle clé sur Pennylane et remplace dans `.env` **et** dans la config Claude Desktop. |
| "Erreur 403 Forbidden" | Il te manque un scope. Supprime ta clé Pennylane, recrée-la en cochant **tous** les scopes. |
| "command not found: uv" ou "git" | Refais l'Étape 1. Ouvre un **nouveau** Terminal après (important). |
| "Erreur dans Claude Desktop → Développeur → Logs" | Ouvre les logs, cherche ligne en rouge. Souvent : chemin `/Users/TON_NOM_ICI/...` mal remplacé. |

Si rien ne marche : ouvre une issue sur [GitHub](https://github.com/bastien-aster/pennylane-mcp/issues) avec une capture de l'erreur.

---

### 🧑‍💻 Bonus · Utilisation dans Claude Code

Si tu utilises aussi [Claude Code](https://claude.com/claude-code) (la CLI), une seule commande :

```bash
claude mcp add pennylane --scope user -- uv --directory /Users/TON_NOM_ICI/pennylane-mcp run pennylane-mcp
```

Puis ajoute tes variables d'env dans `~/.zshrc` :

```bash
echo 'export PENNYLANE_API_KEY="ta_clé"' >> ~/.zshrc
echo 'export PENNYLANE_BASE_URL="https://app.pennylane.com/api/external/v2"' >> ~/.zshrc
source ~/.zshrc
```

Vérifie avec `claude mcp list`.

---

### C'est quoi ce truc ?

Ce serveur expose **161 outils** couvrant quasiment toute la [Pennylane Company API v2](https://pennylane.readme.io/docs/api-overview) :

- 🧾 Factures clients & fournisseurs (liste, création, modification, envoi, paiement…)
- 💼 Clients & fournisseurs (CRUD complet)
- 📝 Devis (cycle complet)
- 💰 Transactions & rapprochements
- 📊 Compta profonde : écritures, lignes, lettrage, journaux, balance
- 📤 Exports FEC, AGL, Grand Livre
- 📦 Produits, abonnements, documents commerciaux
- 🏦 Mandats SEPA & GoCardless
- ⚙️ Rate limiting auto (5 req/s) + retry sur erreurs

### ⚠️ Company API vs Firm API — lis ça avant d'installer

Pennylane a **deux API différentes**. Tu dois savoir laquelle tu as.

| | **Company API** ← ce MCP | Firm API |
|---|---|---|
| Pour qui | Entreprises qui utilisent Pennylane pour leur propre compta | Cabinets comptables qui gèrent les livres de plusieurs clients |
| Tu te connectes et tu vois... | Ta compta d'entreprise | Une liste d'entreprises clientes |
| Doc | [pennylane.readme.io](https://pennylane.readme.io/) | [firm-api.pennylane.com](https://firm-api.pennylane.com/docs) |

**Ce MCP ne supporte que la Company API.** Si tu es une entreprise classique qui utilise Pennylane pour sa compta, c'est bon pour toi. Si tu es comptable et que tu factures à tes clients, il te faut la Firm API (produit séparé, non supporté ici).

### 🔒 Sécurité

Ce fork a été audité :
- Pas de `subprocess`, pas de télémétrie, pas de connexion externe autre que l'API Pennylane
- La clé API n'est envoyée qu'en en-tête `Authorization: Bearer`, jamais loggée
- `.env` est dans le `.gitignore` et l'historique git a été purgé

**À toi de :**
- Utiliser une clé avec le minimum de scopes nécessaires
- Faire tourner tes clés régulièrement
- Ne **jamais** commit `.env`
- Signaler les failles en **Security Advisory privée** (onglet Security → Report a vulnerability)

### 🗺️ Mises à jour

La spec OpenAPI complète est dans [`docs/pennylane-openapi.json`](docs/pennylane-openapi.json). Les outils sont régénérés à partir d'elle :

```bash
python scripts/generate_tools.py
```

Quand Pennylane sort de nouveaux endpoints : remplace le fichier de spec et relance le script.

**Non exposé volontairement :** `webhook_subscription` (utilise Make ou équivalent à la place) et Firm API (produit séparé).

### Contribuer

Les PR sont bienvenues — notamment pour :
- Tests contre un compte sandbox Pennylane
- Nouveaux profils ou ajustement du découpage existant (voir [`src/pennylane_mcp/_metadata.py`](src/pennylane_mcp/_metadata.py))
- Mots-clés français supplémentaires dans les descriptions

### Crédits & Licence

Forké depuis [Akilinoxx/pennylane-mcp](https://github.com/Akilinoxx/pennylane-mcp). Licence MIT.

Pennylane et les marques associées appartiennent à Pennylane. Ce projet n'est pas affilié à Pennylane.

---

<a id="-english"></a>

## 🇬🇧 English

### 🚀 Quick install (5 minutes)

**You'll need:**
- A Mac (or Linux)
- A [Pennylane](https://pennylane.com) account
- [Claude Desktop](https://claude.ai/download) installed

**Never opened a Terminal?** No stress. Hit `Cmd + Space`, type `Terminal`, press Enter. That's the black window — we'll just copy-paste into it.

---

### Step 1 · Install prerequisites (one time only)

Copy-paste these **2 commands** into the Terminal, one after the other:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

```bash
brew install python@3.12 git && curl -LsSf https://astral.sh/uv/install.sh | sh
```

> If Homebrew is already installed, the first command is a safe no-op. Skip it.

---

### Step 2 · Download the server

Copy-paste:

```bash
cd ~ && git clone https://github.com/bastien-aster/pennylane-mcp.git && cd pennylane-mcp && uv venv && uv pip install -e .
```

---

### Step 3 · Get your Pennylane API key

1. Log into [app.pennylane.com](https://app.pennylane.com)
2. **Settings → API → API Keys**
3. Click **Create a new key**
4. **Tick every available scope**
5. **Copy the key immediately** — it's shown only once!

📘 [Official Pennylane API docs](https://pennylane.readme.io/docs/api-overview)

---

### Step 4 · Save your key in the project

In the Terminal:

```bash
cd ~/pennylane-mcp && cp .env.example .env && open -e .env
```

A file opens. Replace `your_api_key_here` with **your** key. Save with `Cmd + S` and close.

---

### Step 5 · Find your Mac username

Type in the Terminal:

```bash
whoami
```

**Note the output** (e.g. `jamesbond`). You'll need it in the next step.

---

### Step 6 · Wire it into Claude Desktop

1. Open **Claude Desktop**
2. Top-left: **Claude → Settings** (or `Cmd + ,`)
3. **Developer** tab → **Edit Config**
4. A JSON file opens. **Paste this block** (if there's already content, merge carefully with commas):

```json
{
  "mcpServers": {
    "pennylane": {
      "command": "uv",
      "args": [
        "--directory",
        "/Users/YOUR_USERNAME_HERE/pennylane-mcp",
        "run",
        "pennylane-mcp"
      ],
      "env": {
        "PENNYLANE_API_KEY": "YOUR_KEY_HERE",
        "PENNYLANE_BASE_URL": "https://app.pennylane.com/api/external/v2"
      }
    }
  }
}
```

5. **Replace**:
   - `YOUR_USERNAME_HERE` → what `whoami` showed in Step 5
   - `YOUR_KEY_HERE` → your Pennylane API key
6. Save (`Cmd + S`) and close
7. **Fully quit Claude Desktop**: `Cmd + Q` (not just close the window!)
8. Reopen Claude Desktop

---

### Step 7 · Test it

In a new Claude conversation, ask:

> List my 5 most recent Pennylane customer invoices.

If Claude responds with real invoices from your account, **you're done** 🎉

---

<details>
<summary><b>🎛️ Optional · Enable only a subset of the 161 tools</b></summary>

If Claude gets lost among 161 tools, you can enable only a subset. Add the `PENNYLANE_TOOLS` environment variable to your Claude Desktop config (inside the `"env"` block, next to `PENNYLANE_API_KEY`):

```json
"env": {
  "PENNYLANE_API_KEY": "YOUR_KEY_HERE",
  "PENNYLANE_BASE_URL": "https://app.pennylane.com/api/external/v2",
  "PENNYLANE_TOOLS": "sales,accounting"
}
```

**Available profiles:**

| Profile | Tools | What's in it |
|---|---:|---|
| `sales` | 56 | Customer invoices, quotes, customers (company/individual), products, commercial documents |
| `purchasing` | 27 | Supplier invoices, suppliers, purchase requests, file attachments |
| `accounting` | 30 | Ledger entries/lines/accounts, journals, categories, trial balance, fiscal years |
| `banking` | 11 | Bank transactions, bank accounts, bank establishments |
| `mandates` | 14 | SEPA mandates, GoCardless mandates, Pro Account |
| `admin` | 23 | Profile, FEC/AGL exports, changelogs, billing subscriptions, e-invoicing |
| `all` | 161 | Everything (default when the variable isn't set) |

You can combine: `PENNYLANE_TOOLS=sales,banking,mandates`. Restart Claude Desktop after editing.

</details>

---

### 🆘 Not working?

| Symptom | Fix |
|---|---|
| "Claude says it has no Pennylane access" | Make sure you fully quit with `Cmd + Q` then reopened. Not just closing the window. |
| "401 Unauthorized" | Wrong or expired key. Regenerate in Pennylane and update **both** `.env` **and** Claude Desktop config. |
| "403 Forbidden" | Missing scope. Delete your Pennylane key, create a new one with **all** scopes ticked. |
| "command not found: uv" or "git" | Redo Step 1. Open a **fresh** Terminal afterwards (important). |
| "Errors in Claude Desktop → Developer → Logs" | Open logs, find the red line. Usually: `/Users/YOUR_USERNAME_HERE/...` path not replaced. |

If none of that helps: open an issue on [GitHub](https://github.com/bastien-aster/pennylane-mcp/issues) with a screenshot.

---

### 🧑‍💻 Bonus · Use with Claude Code

If you use [Claude Code](https://claude.com/claude-code) (the CLI) too, a single command:

```bash
claude mcp add pennylane --scope user -- uv --directory /Users/YOUR_USERNAME_HERE/pennylane-mcp run pennylane-mcp
```

Then add your env vars to `~/.zshrc`:

```bash
echo 'export PENNYLANE_API_KEY="your_key"' >> ~/.zshrc
echo 'export PENNYLANE_BASE_URL="https://app.pennylane.com/api/external/v2"' >> ~/.zshrc
source ~/.zshrc
```

Verify with `claude mcp list`.

---

### What is this?

This server exposes **161 tools** covering nearly the entire [Pennylane Company API v2](https://pennylane.readme.io/docs/api-overview):

- 🧾 Customer & supplier invoices (list, create, update, send, mark paid…)
- 💼 Customers & suppliers (full CRUD)
- 📝 Quotes (full lifecycle)
- 💰 Transactions & matching
- 📊 Deep accounting: entries, lines, lettering, journals, trial balance
- 📤 FEC, AGL, General Ledger exports
- 📦 Products, billing subscriptions, commercial documents
- 🏦 SEPA & GoCardless mandates
- ⚙️ Automatic rate limiting (5 req/s) + retry on errors

### ⚠️ Company API vs Firm API — read this before installing

Pennylane has **two different APIs**. You need to know which one you have.

| | **Company API** ← this MCP | Firm API |
|---|---|---|
| Who for | Companies using Pennylane for their own accounting | Accounting firms managing multiple client books |
| When you log in you see... | Your own company's accounting | A list of client companies |
| Docs | [pennylane.readme.io](https://pennylane.readme.io/) | [firm-api.pennylane.com](https://firm-api.pennylane.com/docs) |

**This MCP only supports the Company API.** If you're a regular business using Pennylane for internal accounting, you're good. If you're an accountant billing clients through Pennylane, you need the Firm API (separate product, not supported here).

### 🔒 Security

This fork has been audited:
- No `subprocess`, no telemetry, no outbound connection other than the Pennylane API
- API key only sent in `Authorization: Bearer` header, never logged
- `.env` is gitignored and git history was purged

**Your responsibilities:**
- Use a key with minimum required scopes
- Rotate keys regularly
- **Never** commit `.env`
- Report vulnerabilities as **private Security Advisory** (Security tab → Report a vulnerability)

### 🗺️ Updates

The full OpenAPI spec is in [`docs/pennylane-openapi.json`](docs/pennylane-openapi.json). Tools are regenerated from it:

```bash
python scripts/generate_tools.py
```

When Pennylane ships new endpoints: replace the spec file and rerun the script.

**Deliberately not exposed:** `webhook_subscription` (use Make or similar instead) and the Firm API (separate product).

### Contributing

PRs welcome — especially for:
- Tests against a sandbox Pennylane account
- New profiles or adjustments to the existing grouping (see [`src/pennylane_mcp/_metadata.py`](src/pennylane_mcp/_metadata.py))
- Additional French keywords in tool descriptions

### Credits & License

Forked from [Akilinoxx/pennylane-mcp](https://github.com/Akilinoxx/pennylane-mcp). MIT License.

Pennylane and related marks are Pennylane trademarks. This project is not affiliated with Pennylane.
