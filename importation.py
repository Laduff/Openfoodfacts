import requests
import mysql.connector
from script_sql import *

#connexion with database
db = mysql.connector.connect(host="localhost",user="root",password="root", database="stockage_donnees")
cursor = db.cursor()

#generate ID_category
ID_category = 1

continuer = 0
while continuer == 0:
    #choice of category
    category = input("Entrez une catégorie : " )
    page = 1
    number_product = 0
    liste = []

    while page < 4:
        r =(requests.get("https://fr-en.openfoodfacts.org/category/"+ category + "/" + str(page) + ".json"))
        data = r.json()
        nombre = 0 
        page += 1
        while nombre < 100:

            try :
                #stock data in "infos" and append in "liste"
                data_tri = data["products"][nombre]
                infos = {}        
                infos["nom_produit"] = data_tri["product_name"]
                infos["nutriscore"] = data_tri["nutrition_grade_fr"]
                infos["lien"] = data_tri["url"]
                liste.append(infos)
                number_product += 1
                nombre = nombre + 1
            
               
            except KeyError:
                break
                print("rien")
                nombre = nombre + 1

            #stop the while function
            except IndexError:
                print("calcul en cours...")
                break
    

        print(liste)
        print("")
        print("Le nombre de produits trouvés : %s" % number_product)

    #import the script sql to save data in database
    script = script_sql(category, number_product, ID_category, liste)
    
        
    ID_category +=1
    print("")

db.close()
