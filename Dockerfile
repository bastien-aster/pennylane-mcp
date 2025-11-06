FROM python:3.11-slim

WORKDIR /app

# Copier tous les fichiers nécessaires
COPY pyproject.toml README.md ./
COPY src/ ./src/

# Installer les dépendances
RUN pip install --no-cache-dir .

# Exposer le port (Railway assignera automatiquement un port)
EXPOSE 8000

# Commande pour démarrer le serveur MCP
CMD ["python", "-m", "pennylane_mcp.server"]
