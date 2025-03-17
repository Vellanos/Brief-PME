import sqlite3
import pandas as pd
import requests
from io import StringIO

# URLs des fichiers CSV
URLS = {
    "magasins": "https://docs.google.com/spreadsheets/d/e/2PACX-1vSawI56WBC64foMT9pKCiY594fBZk9Lyj8_bxfgmq-8ck_jw1Z49qDeMatCWqBxehEVoM6U1zdYx73V/pub?gid=714623615&single=true&output=csv",
    "produits": "https://docs.google.com/spreadsheets/d/e/2PACX-1vSawI56WBC64foMT9pKCiY594fBZk9Lyj8_bxfgmq-8ck_jw1Z49qDeMatCWqBxehEVoM6U1zdYx73V/pub?gid=0&single=true&output=csv",
    "ventes": "https://docs.google.com/spreadsheets/d/e/2PACX-1vSawI56WBC64foMT9pKCiY594fBZk9Lyj8_bxfgmq-8ck_jw1Z49qDeMatCWqBxehEVoM6U1zdYx73V/pub?gid=760830694&single=true&output=csv"
}

# Connexion à SQLite
conn = sqlite3.connect('/data/database.db')
cursor = conn.cursor()

def telecharger_csv(url):
    response = requests.get(url)
    if response.status_code == 200:
        return pd.read_csv(StringIO(response.text))
    else:
        print(f"Erreur lors du téléchargement : {url}")
        return None

def nettoyer_donnees(df, table):
    if table == "magasins":
        df.columns = ["id_magasin", "ville", "nombre_salaries"]
    elif table == "produits":
        df.columns = ["nom", "id_reference", "prix", "stock"]
    elif table == "ventes":
        df.columns = ["date_vente", "id_reference", "quantite", "id_magasin"]
    return df

def importer_csv(df, table, unique_column):
    if df is not None:
        df = nettoyer_donnees(df, table)
        existing_ids = set(row[0] for row in cursor.execute(f"SELECT {unique_column} FROM {table}").fetchall())
        df_filtered = df[~df[unique_column].isin(existing_ids)]
        df_filtered.to_sql(table, conn, if_exists='append', index=False)
        print(f"{len(df_filtered)} nouvelles lignes ajoutées à {table}")

# Importation des fichiers
importer_csv(telecharger_csv(URLS['magasins']), 'magasins', 'id_magasin')
importer_csv(telecharger_csv(URLS['produits']), 'produits', 'id_reference')
importer_csv(telecharger_csv(URLS['ventes']), 'ventes', 'id_magasin')

# Fermeture
conn.commit()
conn.close()
print("Importation des données terminée.")