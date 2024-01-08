from Model.Constantes import *
from Model.Pion import *
from Model.Plateau import *



#
# Ce fichier contient les fonctions gérant le joueur
#
# Un joueur sera un dictionnaire avec comme clé :
# - const.COULEUR : la couleur du joueur entre const.ROUGE et const.JAUNE
# - const.PLACER_PION : la fonction lui permettant de placer un pion, None par défaut,
#                       signifiant que le placement passe par l'interface graphique.
# - const.PLATEAU : référence sur le plateau de jeu, nécessaire pour l'IA, None par défaut
# - d'autres constantes nécessaires pour lui permettre de jouer à ajouter par la suite...
#

def type_joueur(joueur: dict) -> bool:
    """
    Détermine si le paramètre peut correspondre à un joueur.

    :param joueur: Paramètre à tester
    :return: True s'il peut correspondre à un joueur, False sinon.
    """
    if type(joueur) != dict:
        return False
    if const.COULEUR not in joueur or joueur[const.COULEUR] not in const.COULEURS:
        return False
    if const.PLACER_PION not in joueur or (joueur[const.PLACER_PION] is not None
            and not callable(joueur[const.PLACER_PION])):
        return False
    if const.PLATEAU not in joueur or (joueur[const.PLATEAU] is not None and
        not type_plateau(joueur[const.PLATEAU])):
        return False
    return True

def construireJoueur(couleur: int) -> dict:
    """
    Constructeur du joueur avec la couleur passé en paramètre

    :param couleur: Paramètre qui représente la couleur du joueur
    :return: Le joueur sous forme de dictionnaire
    :raise TypeError: Si le paramètre n’est pas un entier
    :raise ValueError: Si l’entier ne représente pas une couleur
    """
    if type(couleur) != int:
        raise TypeError("construirePion : Le paramètre n’est pas de type entier")
    elif couleur not in const.COULEURS:
        raise ValueError(f"construirePion : la couleur {couleur} n’est pas correcte ")

    return {const.COULEUR : couleur, const.PLATEAU : None, const.PLACER_PION : None}

def getCouleurJoueur(joueur : dict) -> int:
    """
    Renvoie la couleur du joueur passé en paramètre

    :param joueur: Paramètre ou l'on veut la couleur
    :return: La couleur du joueur
    :raise TypeError: Si le paramètre n’est pas un dictionnaire
    """

    if not (type_joueur(joueur)):
        raise TypeError("getCouleurJoueur : Le paramètre ne correspond pas à un joueur ")
    return joueur[const.COULEUR]

def getPlateauJoueur(joueur: dict) -> list:
    """
    Renvoie le plateau du joueur passé en paramètre

    :param joueur: Paramètre ou l'on veut le plateau
    :return: Le plateau du joueur
    :raise TypeError: Si le paramètre n’est pas un dictionnaire
    """
    if not (type_joueur(joueur)):
        raise TypeError("getPlateauJoueur : Le paramètre ne correspond pas à un joueur ")
    return joueur[const.PLATEAU]

def getPlacerPionJoueur(joueur : dict) -> str:
    """
    Renvoie la fonction du joueur passé en paramètre

    :param joueur: Paramètre ou l'on veut la couleur
    :return: La fonction du joueur
    :raise TypeError: Si le paramètre n’est pas un dictionnaire
    """
    if not (type_joueur(joueur)):
        raise TypeError("getPlacerPionJoueur : le paramètre ne correspond pas à un joueur")
    return joueur[const.PLACER_PION]