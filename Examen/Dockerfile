# Utiliser une image Python
FROM python:3.9

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier de dépendances
COPY app/requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste de l'application
COPY app .

# Exposer le port
EXPOSE 8000

# Commande pour exécuter l'application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
