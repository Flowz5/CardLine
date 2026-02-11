from typing import List

from animal import Animal
# On importe tes nouvelles fonctions ici
from fonctions import (
    afficherListe, getElemPrecedent, getElemSuivant, getElemInListeAleatoire, 
    charger_donnees, ajouterAnimal, saisir_entier, get_valeur_comparaison
)

# --- CONFIGURATION ---
CRITERE_JEU = "taille"  # Peut être changé par "poids" ou "longevite"

# -------------------------------------------------------------------------------------------
# fonction d'affichage et de comparaison
# -------------------------------------------------------------------------------------------

def choisirPlace(numMax : int) -> int:
    """Permet de choisir la position pour placer la carte en respectant la taille de la liste."""
    # On délègue la gestion d'erreur à fonctions.py
    return saisir_entier(f"Place ? (entre 0 et {numMax}) : ", 0, numMax)

def comparer(ani: Animal, autreAni: Animal) -> bool:
    """Compare ani et autreAni selon le critère défini en haut du fichier."""
    val1 = get_valeur_comparaison(ani, CRITERE_JEU)
    val2 = get_valeur_comparaison(autreAni, CRITERE_JEU)
    return val1 <= val2

def jouerNouvelleCarte() -> str:
    """Permet de proposer de jouer une nouvelle carte O/N"""
    choix = input("Jouer une nouvelle carte : O/N ? ")
    while choix.upper() != 'O' and choix.upper() != 'N':
        choix = input("Jouer une nouvelle carte : O/N ? ")
    return choix.upper()

def menu():
    """Affichage du menu et sélection du choix du joueur"""
    print("\n--- MENU ---")
    print("1 - afficher la liste des animaux")
    print(f"2 - jouer à la classification selon : {CRITERE_JEU}")
    print("3 - ajouter un nouvel animal ")
    print("9 - quitter")
    
    # On utilise aussi la fonction sécurisée ici (choix entre 1 et 9)
    return saisir_entier("Votre Choix ? : ", 1, 9)

def testerInsertionAnimal(listeAni : List[Animal], pos: int, unAni: Animal)-> bool:
    """Permet de vérifier la position pour l'insertion dans une liste"""
    
    # Vérification avec le précédent
    prec = getElemPrecedent(listeAni, pos)
    if prec is not None and not comparer(prec, unAni):
        return False

    # Vérification avec le suivant
    suiv = getElemSuivant(listeAni, pos)
    if suiv is not None and not comparer(unAni, suiv):
        return False
            
    return True

# ----------------------------------------------------------------------------------------------------------------#
# PROGRAMME PRINCIPAL --------------------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------------------------------------------#

# création des cartes
listeAnimaux = []
#TODO ETAPE 1 : création des animaux
listeAnimaux = charger_donnees()

print(f"Bienvenue dans le jeu Cardline : le but consiste à ordonnner les animaux selon : {CRITERE_JEU}")
choix = menu()

while choix != 9:

    if choix == 1:
        print("\n--- Liste des animaux ---")
        afficherListe(listeAnimaux)

    elif choix == 2:
        print("\n--- Début de la partie ---")

        #ETAPE2 - partie Niveau 1 : 1 carte à placer par rapport à une carte de cardline
        cardline = []
        premier = getElemInListeAleatoire(listeAnimaux)
        cardline.append(premier)
        
        jouer = 'O'
        
        while jouer == 'O':
            print("\n--------- Cardline ---------")
            afficherListe(cardline)
            print("----------------------------")
            
            nouvel_ani = getElemInListeAleatoire(listeAnimaux)
            valeur = get_valeur_comparaison(nouvel_ani, CRITERE_JEU)
            
            print(f"Nouvel animal à placer : {nouvel_ani.nom}")
            # Mode triche pour tester (tu peux retirer cette ligne)
            # print(f"(DEBUG: sa valeur est {valeur})") 
            
            pos = choisirPlace(len(cardline))
            
            if testerInsertionAnimal(cardline, pos, nouvel_ani):
                print("Bravo ! Placement correct.")
                cardline.insert(pos, nouvel_ani)
            else:
                print(f"Perdu :( {nouvel_ani.nom} faisait {valeur}.")
            
            jouer = jouerNouvelleCarte()

    elif choix == 3 :
        print("\n--- Ajout d'un animal ---")
        nom = input("Nom : ")
        sci = input("Nom scientifique : ")
        try:
            t = float(input("Taille (m) : "))
            p = float(input("Poids (kg) : "))
            l = int(input("Longevité (ans) : "))
            
            nouvel_ani = Animal(nom, sci, taille=t, poids=p, longevite=l)
            ajouterAnimal(listeAnimaux, nouvel_ani)
            print("Animal ajouté !")
        except ValueError:
            print("Erreur : Il faut saisir des nombres pour les statistiques.")

    choix = menu()

print("Merci d'avoir joué !")