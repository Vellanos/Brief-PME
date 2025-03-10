import sqlite3

def executer_requete(query, description, insert_query=None):
    cursor.execute(query)
    result = cursor.fetchall()
    print(f"\n📊 {description} :")
    for row in result:
        print(row)
    
    if insert_query:
        for row in result:
            cursor.execute(insert_query, row)
        conn.commit()

# Connexion à SQLite
conn = sqlite3.connect('/data/database.db')
cursor = conn.cursor()

# a) Chiffre d'affaires total
executer_requete('''
SELECT SUM(ventes.quantite * produits.prix) AS chiffre_affaires
FROM ventes
JOIN produits ON ventes.id_reference = produits.id_reference
''', "Chiffre d'affaires total", '''
INSERT INTO analyse_chiffre_affaires (chiffre_affaires) VALUES (?)
''')

# b) Ventes par produit
executer_requete('''
SELECT produits.nom, SUM(ventes.quantite) AS total_vendu
FROM ventes
JOIN produits ON ventes.id_reference = produits.id_reference
GROUP BY produits.nom
ORDER BY total_vendu DESC
''', "Ventes par produit", '''
INSERT INTO analyse_ventes_produits (produit, total_vendu) VALUES (?, ?)
''')

# c) Ventes par ville
executer_requete('''
SELECT magasins.ville, SUM(ventes.quantite) AS total_vendu
FROM ventes
JOIN magasins ON ventes.id_magasin = magasins.id_magasin
GROUP BY magasins.ville
ORDER BY total_vendu DESC
''', "Ventes par ville", '''
INSERT INTO analyse_ventes_villes (ville, total_vendu) VALUES (?, ?)
''')

# Fermeture
conn.commit()
conn.close()
print("✅ Analyse des ventes terminée et stockée dans la base de données.")