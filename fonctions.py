import random
from typing import List
from animal import Animal

def afficherListe(liste: List[object]) -> None:
    for i in range(len(liste)):
        print(f"{i} - {liste[i]}")

def getElemPrecedent(liste: List[object], pos: int) -> object:
    return liste[pos - 1] if pos > 0 else None

def getElemSuivant(liste: List[object], pos: int) -> object:
    return liste[pos] if pos < len(liste) else None

def getElemInListeAleatoire(liste: List[object]) -> object:
    return random.choice(liste)

def charger_donnees() -> List[Animal]:
    return [
        Animal("Le coq", "Gallus gallus", 0.45, 2.5, 10),
        Animal("Le bison", "Bison bison", 1.90, 900, 20),
        Animal("L'éléphant d'Asie", "Elephas maximus", 2.70, 4000, 48),
        Animal("La hyène tachetée", "Crocuta crocuta", 1.30, 70, 20)
    ]

def ajouterAnimal(liste: List[object], ani: object) -> None:
    liste.append(ani)

def saisir_entier(msg: str, min_val: int, max_val: int) -> int:
    """Fonction blindée pour saisir un entier entre min et max."""
    while True:
        try:
            valeur = int(input(msg))
            if min_val <= valeur <= max_val:
                return valeur
            print(f"Erreur : Veuillez choisir un nombre entre {min_val} et {max_val}.")
        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier valide.")

def get_valeur_comparaison(ani: Animal, critere: str) -> float:
    """Récupère dynamiquement la valeur (taille, poids...) d'un animal."""
    return getattr(ani, critere, 0)