from Model.Constantes import *
from Model.Pion import *


#
# Le plateau représente la grille où sont placés les pions.
# Il constitue le coeur du jeu car c'est dans ce fichier
# où vont être programmées toutes les règles du jeu.
#
# Un plateau sera simplement une liste de liste.
# Ce sera en fait une liste de lignes.
# Les cases du plateau ne pourront contenir que None ou un pion
#
# Pour améliorer la "rapidité" du programme, il n'y aura aucun test sur les paramètres.
# (mais c'est peut-être déjà trop tard car les tests sont fait en amont, ce qui ralentit le programme...)
#

def type_plateau(plateau: list) -> bool:
    """
    Permet de vérifier que le paramètre correspond à un plateau.
    Renvoie True si c'est le cas, False sinon.

    :param plateau: Objet qu'on veut tester
    :return: True s'il correspond à un plateau, False sinon
    """
    if type(plateau) != list:
        return False
    if len(plateau) != const.NB_LINES:
        return False
    wrong = "Erreur !"
    if next((wrong for line in plateau if type(line) != list or len(line) != const.NB_COLUMNS), True) == wrong:
        return False
    if next((wrong for line in plateau for c in line if not(c is None) and not type_pion(c)), True) == wrong:
        return False
    return True

def construirePlateau() -> list:
    """
    Fonction permettant de créer un tableau 2D avec un nombre de ligne et un nombre de colonnes constant

    :return:  Plateau qui correspond à un tableau 2D
    """
    plateau = []
    for i in range(const.NB_LINES):
        plateau.append([])
        for j in range(const.NB_COLUMNS):
            plateau[i].append(None)
    return plateau

def placerPionPlateau(plateau: list,pion: dict, nbCol : int) -> int:
    """
    Place le pion passé en paramètre dans le tableau dans une colonne passé en paramètre

    :param plateau: Paramètre correspondant à un tableau 2D
    :param pion: Paramètre correspondant au pion que l'on veut placer dans le tableau
    :param nbCol: Paramètre correspondant à la colonne ou l'on veut placer le pion dans le tableau
    :return: La ligne ou se trouve le pion après qu'il a été placé
    :raise TypeError: Si le paramètre n’est pas une liste
    :raise TypeError: Si le paramètre n’est pas un dictionnaire
    :raise TypeError: Si le paramètre n’est pas un entier
    :raise ValueError: Si le paramètre n’est compris entre 0 et la constante représentant le nombre de colonnes
    """
    if not type_plateau(plateau) :
        raise TypeError("placerPionPlateau: Le premier paramètre ne correspond pas à un plateau.")
    elif not(type_pion(pion)):
        raise TypeError("setIdPion : Le premier paramètre n’est pas un pion")
    elif type(nbCol) != int:
        raise TypeError("placerPionPlateau : Le troisième paramètre n’est pas un entier")
    elif nbCol < 0 or nbCol >= const.NB_COLUMNS:
        raise ValueError(f" La valeur de la colonne {nbCol} n’est pas correcte")
    numeroLignePion = -1
    if plateau[const.NB_LINES-1][nbCol] == None:
        plateau[const.NB_LINES-1][nbCol] = pion
        numeroLignePion = const.NB_LINES -1
    else:
        numeroLignePion = const.NB_LINES -2
        while numeroLignePion >= 0 and plateau[numeroLignePion][nbCol] != None:
            numeroLignePion -= 1
        plateau[numeroLignePion][nbCol] = pion
    return numeroLignePion

def toStringPlateau(plateau : list) -> str:
    """
    Affiche au niveau terminal avec des couleurs le tableau passé en paramètre pour faciliter le débugague

    :param plateau: Paramètre qui doit être afficher au niveau terminal
    :return: Retourne la chaine de caractère représentant le tableau passé en paramètre
    """
    res = ''
    for i in range(const.NB_LINES):
        for j in range(const.NB_COLUMNS):
            if plateau[i][j]!= None:
                if plateau[i][j][const.COULEUR] == const.ROUGE:
                    res += '\x1B[41m \x1B[0m'
                else:
                    res += '\x1B[43m \x1B[0m'
            else:
                res += ' '
            res += '|'
        res += '\n'

    res += '-' * (const.NB_COLUMNS *2+1)
    res += '\n'
    for j in range(const.NB_COLUMNS):
        res += ' '
        res += str(j)
    return res

def detecter4horizontalPlateau(plateau: list, couleur: int) -> list:
    """

    :param plateau:
    :param couleur:
    :return:
    """
    if not(type_plateau(plateau)):
        raise TypeError("Le premier paramètre ne correspond pas à un plateau")
    if type(couleur) != int:
        raise TypeError("detecter4horizontalPlateau : le second paramètre n’est pas un entier")
    if couleur not in const.COULEURS:
        raise ValueError(f"détecter4horizontalPlateau : La valeur de la couleur {couleur}n’est pas correcte")
    for ligne in range(const.NB_LINES):
        colonne = 0
        drapeau = False
        while drapeau == False and colonne <= const.NB_COLUMNS:
            
    return