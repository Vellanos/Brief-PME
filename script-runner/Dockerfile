FROM python:3.12

WORKDIR /app

# Copier les fichiers du dossier local dans /app dans le conteneur
COPY . /app

# Installer les dépendances Python nécessaires
RUN pip install pandas requests

# Exécuter tous les scripts en séquence
CMD ["bash", "-c", "python db_setup.py && python import_csv.py && python analyse_ventes.py && tail -f /dev/null"]
