from Model.Constantes import *
from Model.Plateau import *
from Model.Pion import *

p = construirePlateau()
print(p)
pion = construirePion(const.JAUNE)
line = placerPionPlateau(p, pion, 2)
print("Placement d’un pion en colonne 2. Numéro de ligne :", line)
print(p)
# Essais sur les couleurs
print("\x1B[43m \x1B[0m : carré jaune ")
print("\x1B[41m \x1B[0m : carré rouge ")
print("\x1B[41mA\x1B[0m : A sur fond rouge")


from Model.Constantes import *
from Model.Plateau import *
from Model.Pion import *
from random import randint, choice
p = construirePlateau()
for _ in range(20):
 placerPionPlateau(p, construirePion(1),
 randint(0, const.NB_COLUMNS - 1))
print(toStringPlateau(p))
resultat = getPionsGagnantsPlateau(p)
for couleur in resultat:
 print("Ligne horizontale : ",couleur[0])
 print("Ligne vertical : ", couleur[1])
 print("Ligne diagonal direct : ", couleur[2])
 print("Ligne diagonal indirect: ", couleur[3])
 print()

print(isRempliPlateau(p))