import mysql.connector
import substitut

db = mysql.connector.connect(host="localhost",user="root",password="root", database="stockage_donnees")
cursor = db.cursor()
print("")
decision = input ("Voulez vous enregistrer ce résultat dans notre base de donnée ? (oui ou non) ")
if decision == "oui":
    cursor.execute("""set session sql_mode = 'NO_ENGINE_SUBSTITUTION';""")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sauvegarde(
        id int(5) NOT NULL AUTO_INCREMENT,
        id_category int(5) DEFAULT NULL,
        nom_produit varchar(50) DEFAULT NULL,
        nutriscore varchar(50) DEFAULT NULL,
        lien LONGTEXT DEFAULT NULL,
        PRIMARY KEY(id)
    );
    """)
    print (substitut.valeur_sub)
    sql = """INSERT INTO sauvegarde(id_category, nom_produit, nutriscore, lien)
             VALUES (%s, %s, %s, %s)"""

    cursor.execute(sql, (substitut.valeur_sub["categorie"], substitut.valeur_sub["nom_produit"], substitut.valeur_sub["nutriscore"], substitut.valeur_sub["lien"], ))
    db.commit()

save = input ("Voulez vous visionner vos substituts sauvegardés ? (oui ou non) : ")

affichage_save = """SELECT * FROM sauvegarde"""
cursor.execute(affichage_save)
rows = cursor.fetchall()

if save == "oui":

    for row in rows:
        print("")
        print ("ID", row[0])
        print ("Catégorie :", row[1])
        print ("Nom du produit :", row[2])
        print ("Nutriscore :", row[3])
        print ("Lien :", row[4])
        print("")
    
    

db.close()
