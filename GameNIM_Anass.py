Partie 1 — Version Simple (Sans POO avancée):

import random
class Humain:
    def __init__(self, nom):
        self.nom = nom

    def jouer(self, restant):
        if restant in [2, 3]:
            maxi = restant - 1 
        else:
            maxi = 3
        while True:
            try:
                choix = int(input(f"{self.nom}, prenez 1 à {maxi} bâtons : "))
                if 1 <= choix <= maxi:
                    return choix
            except ValueError:
                print("Vous avez taper une valeur invalide,veuiller vous entrer une autre valeur valide ! ")
class Ordinateur:

    def __init__(self, nom):
        self.nom = nom

    def jouer(self, restant):
        if restant in [2, 3]:
            maxi = restant - 1
        else:
            maxi = 3
        choix = random.randint(1, maxi)
        print(f"{self.nom} prend {choix} bâtons")
        return choix 
if __name__ == "__main__":
    batons = 15                     
    nom = input("Votre nom : ")
    h = Humain(nom)
    o = Ordinateur("Robot")
    joueurs = [h, o]           
    premier = input("Premier ? (Rien=Oui, Autre=Non) : ")
    if premier == "":
        tour = 0  
    else:
        tour = 1  
    while batons >= 1:

        print("|" * batons + f" ({batons})")
        choix = joueurs[tour].jouer(batons)
        batons -= choix
        tour = (tour + 1) % 2
    gagnant = joueurs[tour].nom
    print(f"\n{gagnant} a gagné !")

Résultat:

Votre nom :  Anass
Premier ? (Rien=Oui, Autre=Non) :  Non
||||||||||||||| (15)
Robot prend 1 bâtons
|||||||||||||| (14)
Anass, prenez 1 à 3 bâtons :  3
||||||||||| (11)
Robot prend 2 bâtons
||||||||| (9)
Anass, prenez 1 à 3 bâtons :  2
||||||| (7)
Robot prend 1 bâtons
|||||| (6)
Anass, prenez 1 à 3 bâtons :  4
Anass, prenez 1 à 3 bâtons :  7
Anass, prenez 1 à 3 bâtons :  3
||| (3)
Robot prend 1 bâtons
|| (2)
Anass, prenez 1 à 1 bâtons :  2
Anass, prenez 1 à 1 bâtons :  3
Anass, prenez 1 à 1 bâtons :  1
| (1)
Robot prend 2 bâtons
Anass a gagné !

Partie 2 — Version Avancée (POO avec héritage):

from abc import ABC, abstractmethod
import random
class Joueur(ABC):
    def __init__(self, nom):
        self.nom = nom
    @abstractmethod
    def _jouer(self, restant):
        pass

class Humain(Joueur):
    def _jouer(self, restant):
        maxi = restant - 1 if restant in [2, 3] else 3
        while True:
            try:
                choix = int(input(f"{self.nom}, prenez 1 à {maxi} bâtons : "))
                if 1 <= choix <= maxi:
                    return choix
            except ValueError:
                pass

class Ordinateur(Joueur):
    def _jouer(self, restant):
        maxi = restant - 1 if restant in [2, 3] else 3
        choix = random.randint(1, maxi)
        print(f"{self.nom} prend {choix} bâtons")
        return choix

class JeuNim:
    def __init__(self, batons):
        self.batons = batons                    
        nomHumain = input("Votre nom : ")
        rep = input("Premier ? (Rien=Oui, Autre=Non) : ")
        self.tour = 0 if rep == "" else 1
        self.joueurs = (Humain(nomHumain), Ordinateur("Robot"))
    def __str__(self):
        return "|" * self.batons + f" Il reste: {self.batons} bâtons"

    def lancer(self):
        while self.batons >= 1:
            print(self)
            choix = self.joueurs[self.tour]._jouer(self.batons)
            self.batons -= choix
            self.tour = (self.tour + 1) % 2
        print(f"\n{self.joueurs[self.tour].nom} a gagné !")
        print("Fin")

if __name__ == "__main__":
    partie = JeuNim(15)
    partie.lancer()

Résultat:

Votre nom :  Anass
Premier ? (Rien=Oui, Autre=Non) :  Oui
||||||||||||||| Il reste: 15 bâtons
Robot prend 1 bâtons
|||||||||||||| Il reste: 14 bâtons
Anass, prenez 1 à 3 bâtons :  2
|||||||||||| Il reste: 12 bâtons
Robot prend 2 bâtons
|||||||||| Il reste: 10 bâtons
Anass, prenez 1 à 3 bâtons :  3
||||||| Il reste: 7 bâtons
Robot prend 2 bâtons
||||| Il reste: 5 bâtons
Anass, prenez 1 à 3 bâtons :  5
Anass, prenez 1 à 3 bâtons :  0
Anass, prenez 1 à 3 bâtons :  3
|| Il reste: 2 bâtons
Robot prend 1 bâtons
| Il reste: 1 bâtons
Anass, prenez 1 à 3 bâtons :  2

Robot a gagné !
Fin

