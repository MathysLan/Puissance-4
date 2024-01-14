from Model.Joueur import *

def setJeuAdversaireJoueur(joueur: dict,colonne: int) -> None:
    """
    Affecte une foncton passé en paramètre à un joueur en paramètre

    :param joueur: Paramètre qui représente le joueur
    :param fn: Paramètre qui répresente la fonction à affecté
    :return: rien
    :raise TypeError: Si le paramètre n’est pas un joueur
    :raise TypeError: Si le paramètre n’est pas un plateau
    """
    if not (type_joueur(joueur)):
        raise TypeError("setJeuAdversaireJoueur: le paramètre ne correspond pas à un joueur")
    if type(colonne) != int:
        raise TypeError("setJeuAdversaireJoueur: le paramètre n'est pas un entier")
    joueur[const.JEU_ADVERSAIRE] = colonne
    return None


def herisitqueMatrice(plateau: list) -> list:
    """

    """
    matrice = []
    for ligne in range(const.NB_LINES):
        matrice.append([])
        for colonne in range(const.NB_COLUMNS):
            matrice[ligne].append(0)
            matrice[ligne][colonne] += heristiqueMatriceHorizontal(plateau, ligne, colonne)
            matrice[ligne][colonne] += heristiqueMatriceVertical(plateau, ligne, colonne)
    return matrice

def heristiqueMatriceHorizontal(plateau: list, ligne: int, colonne: int) -> int:
    """

    """
    compteur = 0
    if colonne == 0 :
        compteur = 1
    elif colonne == const.NB_COLUMNS - 1:
        compteur = 1
    elif colonne == const.NB_COLUMNS// 2:

        compteur = 4
    elif const.NB_COLUMNS // 2 - 1  == colonne or colonne == const.NB_COLUMNS // 2 +1 :
        compteur = 3
    else:
        compteur = 2
    return compteur

def heristiqueMatriceVertical(plateau: list, ligne: int, colonne: int)-> int:
    """

    """
    if ligne == 0:
        compteur = 1
    elif ligne == const.NB_LINES - 1:
        compteur = 1
    elif ligne == const.NB_LINES // 2:

        compteur = 4
    elif const.NB_LINES // 2 - 1 == ligne or ligne == const.NB_LINES // 2 + 1:
        compteur = 3
    else:
        compteur = 2
    return compteur

def heristiqueMatriceDiagonaleDirect(plateau: list, ligne: int, colonne: int)-> int:
    """

    """
    compteur = 0
    if (ligne == 0 and colonne == 0) or (ligne == const.NB_LINES -1 and colonne == const.NB_COLUMNS -1):
        compteur 1

    return compteur