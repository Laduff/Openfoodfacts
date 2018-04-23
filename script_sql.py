import mysql.connector

db = mysql.connector.connect(host="localhost",user="root",password="root", database="stockage_donnees")
cursor = db.cursor()

class script_sql:
    def __init__(self, category, number_product, ID_category, liste):
        self.category = category
        self.number_product = number_product
        self.ID_category = ID_category
        self.liste = liste
        
        cursor.execute("""set session sql_mode = 'NO_ENGINE_SUBSTITUTION';""")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS produits(
            id int(5) NOT NULL AUTO_INCREMENT,
            id_category varchar(50) DEFAULT NULL,
            nom_produit varchar(50) DEFAULT NULL,
            nutriscore varchar(50) DEFAULT NULL,
            lien LONGTEXT DEFAULT NULL,
            PRIMARY KEY(id)
            );
            """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS categories(
            id int(5) NOT NULL AUTO_INCREMENT,
            nom_categorie varchar(50) DEFAULT NULL,
            nombre_produits varchar(50) DEFAULT NULL,
            PRIMARY KEY(id)
            );
            """)

        sql_category = """INSERT INTO categories(nom_categorie, nombre_produits)
                        VALUES (%s, %s)"""

        cursor.execute(sql_category, (category, number_product))
        db.commit()


        nombre = 0

        while nombre < 1000:

            try :
            
                # Prepare SQL query to INSERT a record into the database.
                sql = """INSERT INTO produits(id_category, nom_produit,
                     nutriscore, lien)
                     VALUES (%s, %s, %s, %s)"""
                nombre = nombre + 1
            
                # Execute the SQL command
                cursor.execute(sql, (ID_category, liste[nombre]["nom_produit"], liste[nombre]["nutriscore"], liste[nombre]["lien"]))
                # Commit your changes in the database
                db.commit()
                   
            except IndexError:
                nombre = nombre + 1
                break

