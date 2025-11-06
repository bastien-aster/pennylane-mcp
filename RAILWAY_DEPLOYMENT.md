# Déploiement du serveur MCP Pennylane sur Railway

## 📦 Étapes de déploiement

### 1. Préparer le repository Git

```bash
cd /home/goupilus/Documents/pennylane_mcp
git init
git add .
git commit -m "Initial commit - Pennylane MCP Server"
```

### 2. Créer un compte Railway

1. Aller sur [railway.app](https://railway.app)
2. Se connecter avec GitHub
3. Créer un nouveau projet

### 3. Déployer sur Railway

**Option A : Via GitHub (recommandé)**
1. Pusher votre code sur GitHub
2. Dans Railway : "New Project" → "Deploy from GitHub repo"
3. Sélectionner votre repository
4. Railway détectera automatiquement le Dockerfile

**Option B : Via Railway CLI**
```bash
npm install -g @railway/cli
railway login
railway init
railway up
```

### 4. Configurer les variables d'environnement

Dans Railway Dashboard → Variables :
- `PENNYLANE_API_KEY` : Votre clé API Pennylane
- `PENNYLANE_BASE_URL` : `https://app.pennylane.com/api/external/v2`

⚠️ **Important** : Ne commitez JAMAIS votre clé API dans le code !

### 5. Obtenir l'URL du serveur

Une fois déployé, Railway vous donnera une URL publique :
- Format : `https://votre-projet.railway.app`
- Ou domaine personnalisé si configuré

## 🔌 Configuration dans Dust

### Ajouter le serveur MCP dans Dust

1. Aller dans Dust → Settings → MCP Servers
2. Ajouter un nouveau serveur :
   - **Name** : `Pennylane MCP`
   - **URL** : `https://votre-projet.railway.app`
   - **API Key** : Votre `PENNYLANE_API_KEY`

### Structure de la requête Dust

Dust communiquera avec votre serveur MCP via :
```
POST https://votre-projet.railway.app/mcp
Headers:
  Authorization: Bearer <PENNYLANE_API_KEY>
  Content-Type: application/json
```

## 🔒 Sécurité

Le serveur MCP utilise votre clé API Pennylane pour authentifier les requêtes.
Assurez-vous que :
1. La clé API est stockée uniquement dans les variables d'environnement Railway
2. La clé API Pennylane a les permissions appropriées
3. Vous surveillez les logs Railway pour détecter toute activité suspecte

## 📊 Monitoring

Dans Railway Dashboard :
- **Logs** : Voir les logs en temps réel
- **Metrics** : CPU, RAM, requêtes
- **Deployments** : Historique des déploiements

## 🔄 Mise à jour

Pour déployer une nouvelle version :
```bash
git add .
git commit -m "Update MCP server"
git push
```

Railway redéploiera automatiquement.

## 🛠️ Dépannage

### Le serveur ne démarre pas
- Vérifier les logs Railway
- Vérifier que `PENNYLANE_API_KEY` est défini
- Vérifier que le Dockerfile est correct

### Erreurs d'authentification
- Vérifier que la clé API Pennylane est valide
- Vérifier que la clé n'a pas expiré

### Timeout
- Augmenter les ressources dans Railway (plan payant)
- Optimiser les requêtes vers l'API Pennylane
