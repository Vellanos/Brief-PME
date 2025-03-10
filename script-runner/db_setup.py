import sqlite3

# Connexion à SQLite
conn = sqlite3.connect('/data/database.db')
cursor = conn.cursor()

# Création des tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS magasins (
    id_magasin INTEGER PRIMARY KEY,
    ville TEXT NOT NULL,
    nombre_salaries INTEGER NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS produits (
    id_reference TEXT PRIMARY KEY,
    nom TEXT NOT NULL,
    prix REAL NOT NULL,
    stock INTEGER NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS ventes (
    id_vente INTEGER PRIMARY KEY AUTOINCREMENT,
    date_vente DATE NOT NULL,
    id_reference TEXT NOT NULL,
    quantite INTEGER NOT NULL,
    id_magasin INTEGER NOT NULL,
    FOREIGN KEY(id_reference) REFERENCES produits(id_reference),
    FOREIGN KEY(id_magasin) REFERENCES magasins(id_magasin)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS analyse_chiffre_affaires (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    chiffre_affaires REAL NOT NULL,
    date_analyse TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS analyse_ventes_produits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produit TEXT NOT NULL,
    total_vendu INTEGER NOT NULL,
    date_analyse TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS analyse_ventes_villes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ville TEXT NOT NULL,
    total_vendu INTEGER NOT NULL,
    date_analyse TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

# Sauvegarde et fermeture
conn.commit()
conn.close()
print("✅ Base de données et tables créées avec succès.")