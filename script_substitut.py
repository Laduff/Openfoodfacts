import mysql.connector

db = mysql.connector.connect(host="localhost",user="root",password="root", database="stockage_donnees")
cursor = db.cursor()

affichage_categories = """SELECT * FROM categories"""
cursor.execute(affichage_categories)
rows = cursor.fetchall()
for row in rows:
    print ("ID", row[0])
    print ("Catégorie :", row[1])
    print ("Nombre de produits :", row[2])
    print("")

print("")
choix_categorie = input("Veuillez entrer le numéro de la catégorie voulue : ")
print("")
affichage_produits = """SELECT id, id_category, nom_produit, nutriscore, lien FROM produits WHERE id_category = %s"""
cursor.execute(affichage_produits, (choix_categorie, ))
donnees = cursor.fetchall()
stock = []
ID_produit = 1

for donnee in donnees:
    infos = {}
    infos["ID"] = ID_produit
    infos["categorie"] = donnee[1]
    infos["nom_produit"] = donnee[2]
    infos["nutriscore"] = donnee[3]
    infos["lien"] = donnee[4]
    stock.append(infos)
    print ("ID", ID_produit)
    print ("Catégorie :", donnee[1])
    print ("Nom du produit :", donnee[2])
    print ("Nutriscore :", donnee[3])
    print ("Lien :", donnee[4])
    print("")
    ID_produit+=1



choix_produit = int (input("sélectionnez le numéro du produit que vous voulez substituer : " ))
print (stock[choix_produit-1])

if stock[choix_produit - 1]["nutriscore"] == "a":
    print("")
    print("Ce produit est très bien vous pouvez le dévorer")

if stock[choix_produit - 1]["nutriscore"] == "b":
    boucle = 0
    while boucle < 100:
        try :
            if stock[boucle]["nutriscore"] == "a":
                print (stock[boucle])
                break
            if stock[boucle]["nutriscore"] == "b":
                if stock[boucle]==stock[choix_produit-1]:
                    print("Ce produit est l'un des meilleurs dans notre base de donnée")                    
                else:
                    print (stock[boucle])
                break
        except IndexError:
            print("Ce produit est l'un des meilleurs dans notre base de donnée")
            break
        boucle +=1
        
if stock[choix_produit - 1]["nutriscore"] == "c":
    boucle = 0
    while boucle < 100:
        try :
            if stock[boucle]["nutriscore"] == "a":
                print (stock[boucle])
                break

            if stock[boucle]["nutriscore"] == "b":
                print (stock[boucle])
                break

            if stock[boucle]["nutriscore"] == "c":
                if stock[boucle] == stock[choix_produit-1]:
                    print("Ce produit est l'un des meilleurs dans notre base de donnée")                    
                else:
                    print (stock[boucle])
                break
        except IndexError:
            print("Ce produit est l'un des meilleurs dans notre base de donnée")
            break
        boucle +=1

if stock[choix_produit - 1]["nutriscore"] == "d":               
    boucle = 0
    while boucle < 1000:
        try :
            if stock[boucle]["nutriscore"] == "a":
                print (stock[boucle])
                break

            if stock[boucle]["nutriscore"] == "b":
                print (stock[boucle])
                break

            if stock[boucle]["nutriscore"] == "c":
                print (stock[boucle])
                break

            if stock[boucle]["nutriscore"] == "d":
                if stock[boucle] == stock[choix_produit-1]:
                    print("Ce produit est l'un des meilleurs dans notre base de donnée")                    
                else:
                    print (stock[boucle])
                break
                
        except IndexError:
            print("Ce produit est l'un des meilleurs dans notre base de donnée")
            break
        boucle +=1

if stock[choix_produit - 1]["nutriscore"] == "e":
    boucle = 0
    while boucle < 100:
        try :
            if stock[boucle]["nutriscore"] == "a":
                print (stock[boucle])
                break

            if stock[boucle]["nutriscore"] == "b":
                print (stock[boucle])
                break
            
            if stock[boucle]["nutriscore"] == "c":
                print (stock[boucle])
                break
            
            if stock[boucle]["nutriscore"] == "d":
                print (stock[boucle])
                break

            if stock[boucle]["nutriscore"] == "e":
                if stock[boucle] == stock[choix_produit-1]:
                    print("Ce produit est l'un des meilleurs dans notre base de donnée")                    
                else:
                    print (stock[boucle])
                break
            
        except IndexError:
            print("Ce produit est l'un des meilleurs dans notre base de donnée")
            break
        boucle +=1

if stock[choix_produit - 1]["nutriscore"] == "f":
    boucle = 0
    while boucle < 100:
        try :
            if stock[boucle]["nutriscore"] == "a":
                print (stock[boucle])
                break

            if stock[boucle]["nutriscore"] == "b":
                print (stock[boucle])
                break
            
            if stock[boucle]["nutriscore"] == "c":
                print (stock[boucle])
                break
            
            if stock[boucle]["nutriscore"] == "d":
                print (stock[boucle])
                break
            
            if stock[boucle]["nutriscore"] == "e":
                print (stock[boucle])
                break

            if stock[boucle]["nutriscore"] == "f":
                if stock[boucle] == stock[choix_produit-1]:
                    print("Ce produit est l'un des meilleurs dans notre base de donnée")                    
                else:
                    print (stock[boucle])
                break
            
        except IndexError:
            print("Ce produit est l'un des meilleurs dans notre base de donnée")
            break
        boucle +=1

valeur_sub = stock[boucle]

