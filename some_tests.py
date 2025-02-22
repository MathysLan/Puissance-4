from Model.Constantes import *
from Model.Plateau import *
from Model.Pion import *
from Model.IAJoueur import *

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
 placerPionPlateau(p, construirePion(choice(const.COULEURS)),
 randint(0, const.NB_COLUMNS - 1))
print(toStringPlateau(p))
print(getPionsGagnantsPlateau(p))
print(isRempliPlateau(p))
historigramme = {2:'______________J_J___RRJJ_J_RJJJ_J_RRJJJRRJ',4:'______________R__R_J_R__J_JRRR_JRJJRRJJJJJ'}
print(encoderPlateau(p))
print(isPatPlateau(p,historigramme))
print(historigramme)
print(herisitqueMatrice(p))
