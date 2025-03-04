import sqlite3

def executer_requete(query, description):
    cursor.execute(query)
    print(f"\n📊 {description} :")
    for row in cursor.fetchall():
        print(row)

# Connexion à SQLite
conn = sqlite3.connect('/data/database.db')
cursor = conn.cursor()

# a) Chiffre d'affaires total
executer_requete('''
SELECT SUM(ventes.quantite * produits.prix) AS chiffre_affaires
FROM ventes
JOIN produits ON ventes.id_reference = produits.id_reference
''', "Chiffre d'affaires total")

# b) Ventes par produit
executer_requete('''
SELECT produits.nom, SUM(ventes.quantite) AS total_vendu
FROM ventes
JOIN produits ON ventes.id_reference = produits.id_reference
GROUP BY produits.nom
ORDER BY total_vendu DESC
''', "Ventes par produit")

# c) Ventes par ville
executer_requete('''
SELECT magasins.ville, SUM(ventes.quantite) AS total_vendu
FROM ventes
JOIN magasins ON ventes.id_magasin = magasins.id_magasin
GROUP BY magasins.ville
ORDER BY total_vendu DESC
''', "Ventes par ville")

# Fermeture
conn.close()
print("✅ Analyse des ventes terminée.")