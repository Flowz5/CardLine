from __future__ import annotations

class Animal:
    def __init__(self, nom, nom_scientifique, taille, poids=0, longevite=0):
        self.nom = nom
        self.nom_scientifique = nom_scientifique
        self.taille = float(taille)
        self.poids = float(poids)
        self.longevite = int(longevite)

    def comparer(self, other: Animal) -> bool:
        return self.taille <= other.taille

    def __str__(self):
        return f"{self.nom}"