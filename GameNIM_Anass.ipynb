{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "c09fdb0b-5e95-4404-aa7b-924a2681b806",
   "metadata": {},
   "source": [
    "Partie 1 — Version Simple (Sans POO avancée)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "2b7c381f-0faa-46a1-9eae-8c18556f13a0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Votre nom :  Anass\n",
      "Premier ? (Rien=Oui, Autre=Non) :  Non\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "||||||||||||||| (15)\n",
      "Robot prend 1 bâtons\n",
      "|||||||||||||| (14)\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Anass, prenez 1 à 3 bâtons :  3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "||||||||||| (11)\n",
      "Robot prend 2 bâtons\n",
      "||||||||| (9)\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Anass, prenez 1 à 3 bâtons :  2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "||||||| (7)\n",
      "Robot prend 1 bâtons\n",
      "|||||| (6)\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Anass, prenez 1 à 3 bâtons :  4\n",
      "Anass, prenez 1 à 3 bâtons :  7\n",
      "Anass, prenez 1 à 3 bâtons :  3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "||| (3)\n",
      "Robot prend 1 bâtons\n",
      "|| (2)\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Anass, prenez 1 à 1 bâtons :  2\n",
      "Anass, prenez 1 à 1 bâtons :  3\n",
      "Anass, prenez 1 à 1 bâtons :  1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "| (1)\n",
      "Robot prend 2 bâtons\n",
      "\n",
      "Anass a gagné !\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "class Humain:\n",
    "    def __init__(self, nom):\n",
    "        self.nom = nom\n",
    "\n",
    "    def jouer(self, restant):\n",
    "        if restant in [2, 3]:\n",
    "            maxi = restant - 1 \n",
    "        else:\n",
    "            maxi = 3\n",
    "        while True:\n",
    "            try:\n",
    "                choix = int(input(f\"{self.nom}, prenez 1 à {maxi} bâtons : \"))\n",
    "                if 1 <= choix <= maxi:\n",
    "                    return choix\n",
    "            except ValueError:\n",
    "                pass\n",
    "class Ordinateur:\n",
    "\n",
    "    def __init__(self, nom):\n",
    "        self.nom = nom\n",
    "\n",
    "    def jouer(self, restant):\n",
    "        if restant in [2, 3]:\n",
    "            maxi = restant - 1\n",
    "        else:\n",
    "            maxi = 3\n",
    "        choix = random.randint(1, maxi)\n",
    "        print(f\"{self.nom} prend {choix} bâtons\")\n",
    "        return choix \n",
    "if __name__ == \"__main__\":\n",
    "    batons = 15                     \n",
    "    nom = input(\"Votre nom : \")\n",
    "    h = Humain(nom)\n",
    "    o = Ordinateur(\"Robot\")\n",
    "    joueurs = [h, o]           \n",
    "    premier = input(\"Premier ? (Rien=Oui, Autre=Non) : \")\n",
    "    if premier == \"\":\n",
    "        tour = 0  \n",
    "    else:\n",
    "        tour = 1  \n",
    "    while batons >= 1:\n",
    "\n",
    "        print(\"|\" * batons + f\" ({batons})\")\n",
    "        choix = joueurs[tour].jouer(batons)\n",
    "        batons -= choix\n",
    "        tour = (tour + 1) % 2\n",
    "    gagnant = joueurs[tour].nom\n",
    "    print(f\"\\n{gagnant} a gagné !\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "260f0c8c-fd18-4abb-aa8c-c4fdc6f56904",
   "metadata": {},
   "source": [
    "Partie 2 — Version Avancée (POO avec héritage)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "c31bb05e-0639-4c3b-a5be-10bdd55928d0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Votre nom :  Anass\n",
      "Premier ? (Rien=Oui, Autre=Non) :  Oui\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "||||||||||||||| Il reste: 15 bâtons\n",
      "Robot prend 1 bâtons\n",
      "|||||||||||||| Il reste: 14 bâtons\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Anass, prenez 1 à 3 bâtons :  2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "|||||||||||| Il reste: 12 bâtons\n",
      "Robot prend 2 bâtons\n",
      "|||||||||| Il reste: 10 bâtons\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Anass, prenez 1 à 3 bâtons :  3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "||||||| Il reste: 7 bâtons\n",
      "Robot prend 2 bâtons\n",
      "||||| Il reste: 5 bâtons\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Anass, prenez 1 à 3 bâtons :  5\n",
      "Anass, prenez 1 à 3 bâtons :  0\n",
      "Anass, prenez 1 à 3 bâtons :  3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "|| Il reste: 2 bâtons\n",
      "Robot prend 1 bâtons\n",
      "| Il reste: 1 bâtons\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Anass, prenez 1 à 3 bâtons :  2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Robot a gagné !\n",
      "Fin\n"
     ]
    }
   ],
   "source": [
    "from abc import ABC, abstractmethod\n",
    "import random\n",
    "class Joueur(ABC):\n",
    "    def __init__(self, nom):\n",
    "        self.nom = nom\n",
    "    @abstractmethod\n",
    "    def _jouer(self, restant):\n",
    "        pass\n",
    "\n",
    "class Humain(Joueur):\n",
    "    def _jouer(self, restant):\n",
    "        maxi = restant - 1 if restant in [2, 3] else 3\n",
    "        while True:\n",
    "            try:\n",
    "                choix = int(input(f\"{self.nom}, prenez 1 à {maxi} bâtons : \"))\n",
    "                if 1 <= choix <= maxi:\n",
    "                    return choix\n",
    "            except ValueError:\n",
    "                pass\n",
    "\n",
    "class Ordinateur(Joueur):\n",
    "    def _jouer(self, restant):\n",
    "        maxi = restant - 1 if restant in [2, 3] else 3\n",
    "        choix = random.randint(1, maxi)\n",
    "        print(f\"{self.nom} prend {choix} bâtons\")\n",
    "        return choix\n",
    "\n",
    "class JeuNim:\n",
    "    def __init__(self, batons):\n",
    "        self.batons = batons                    \n",
    "        nomHumain = input(\"Votre nom : \")\n",
    "        rep = input(\"Premier ? (Rien=Oui, Autre=Non) : \")\n",
    "        self.tour = 0 if rep == \"\" else 1\n",
    "        self.joueurs = (Humain(nomHumain), Ordinateur(\"Robot\"))\n",
    "    def __str__(self):\n",
    "        return \"|\" * self.batons + f\" Il reste: {self.batons} bâtons\"\n",
    "\n",
    "    def lancer(self):\n",
    "        while self.batons >= 1:\n",
    "            print(self)\n",
    "            choix = self.joueurs[self.tour]._jouer(self.batons)\n",
    "            self.batons -= choix\n",
    "            self.tour = (self.tour + 1) % 2\n",
    "        print(f\"\\n{self.joueurs[self.tour].nom} a gagné !\")\n",
    "        print(\"Fin\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    partie = JeuNim(15)\n",
    "    partie.lancer()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
