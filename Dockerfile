FROM python:3.11-slim

WORKDIR /app

# Copier les fichiers de dépendances
COPY pyproject.toml ./

# Installer les dépendances
RUN pip install --no-cache-dir -e .

# Copier le code source
COPY src/ ./src/

# Exposer le port (Railway assignera automatiquement un port)
EXPOSE 8000

# Commande pour démarrer le serveur MCP
CMD ["python", "-m", "pennylane_mcp.server"]
