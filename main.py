import fonctions
from animal import *

def jouer_classification(repertoire):
    liste_jeu = [fonctions.getElemInListeAleatoire(repertoire)]
    
    jouer = 'O'
    while jouer.upper() == 'O':
        print("\n--------- Cardline ---------")
        fonctions.afficherListe(liste_jeu)
        print("----------------------------")
        
        nouvel_ani = fonctions.getElemInListeAleatoire(repertoire)
        print(f"Nouvel animal à placer : {nouvel_ani.nom}")
        
        try:
            msg = "Place ? (index de l'animal suivant ou fin de liste) : "
            pos = int(input(msg))
            
            if fonctions.testerInsertionAnimal(liste_jeu, pos, nouvel_ani):
                print("Bravo !")
                liste_jeu.insert(pos, nouvel_ani)
            else:
                print("Perdu :(")
        except ValueError:
            print("Veuillez saisir un nombre valide.")

        print("\n--------------- Cardline ---------------")
        fonctions.afficherListe(liste_jeu)
        print("------------------------------------------")
        
        jouer = input("Jouer une nouvelle carte : O/N ? ")


def main():
    running = True

    repertoire = fonctions.charger_donnees()
    
    while running:
        print("\n--- MENU ---")
        print("1 - Afficher la liste des animaux")
        print("2 - Jouer à la classification selon la taille")
        print("3. Ajouter un nouvel animal")
        print("9 - Quitter")
        
        choix = input("Votre Choix ? : ")
        
        if choix == "1":
            fonctions.afficherListe(repertoire)

        elif choix == "2":
            jouer_classification(repertoire)

        elif choix == "3":
            print("\n--- Ajouter un nouvel animal ---")
            nom = input("Nom de l'animal : ")
            nom_sci = input("Nom scientifique : ")
            taille = float(input("Taille moyenne (en m) : "))
            
            nouvel_ani = Animal(nom, nom_sci, taille)
            
            fonctions.ajouterAnimal(repertoire, nouvel_ani)
            
            print(f"{nom} a été ajouté !")

        elif choix == "9":
            print("Merci d'avoir joué !")
            running = False

if __name__ == "__main__":
    main()