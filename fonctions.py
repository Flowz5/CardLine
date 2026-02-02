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


def testerInsertionAnimal(listeAni: List[Animal], pos: int, unAni: Animal) -> bool:
    prec = getElemPrecedent(listeAni, pos)
    suiv = getElemSuivant(listeAni, pos)

    valide_prec = True
    if prec is not None:
        valide_prec = prec.comparer(unAni)

    valide_suiv = True
    if suiv is not None:
        valide_suiv = unAni.comparer(suiv)

    return valide_prec and valide_suiv

def charger_donnees() -> List[Animal]:
    return [
        Animal("Le coq", "Gallus gallus", 0.45),
        Animal("Le bison", "Bison bison", 1.90),
        Animal("L'éléphant d'Asie", "Elephas maximus", 2.70),
        Animal("La hyène tachetée", "Crocuta crocuta", 1.30)
    ]

def ajouterAnimal(liste: List[object], ani: object) -> None:
    liste.append(ani)