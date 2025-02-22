# Model/Pion.py

from Model.Constantes import *


#
# Ce fichier implémente les données/fonctions concernant le pion
# dans le jeu du Puissance 4
#
# Un pion est caractérisé par :
# - sa couleur (const.ROUGE ou const.JAUNE)
# - un identifiant de type int (pour l'interface graphique)
#
# L'identifiant sera initialisé par défaut à None
#

def type_pion(pion: dict) -> bool:
    """
    Détermine si le paramètre peut être ou non un Pion

    :param pion: Paramètre dont on veut savoir si c'est un Pion ou non
    :return: True si le paramètre correspond à un Pion, False sinon.
    """
    return type(pion) == dict and len(pion) == 2 and const.COULEUR in pion.keys() \
        and const.ID in pion.keys() \
        and pion[const.COULEUR] in const.COULEURS \
        and (pion[const.ID] is None or type(pion[const.ID]) == int)



def construirePion(couleur: int) -> dict:
    """
    Construit le pion en prenant la couleur passé en paramètre

    :param couleur: Paramètre qui représente la couleur du pion
    :return: Le pion sous forme de dictionnaire
    :raise TypeError: Si le paramètre n’est pas un entier
    :raise ValueError: Si l’entier ne représente pas une couleur
    """
    if type(couleur) != int:
        raise TypeError("construirePion : Le paramètre n’est pas de type entier")
    elif couleur not in const.COULEURS:
        raise ValueError(f"construirePion : la couleur {couleur} n’est pas correcte ")

    return {const.COULEUR : couleur, const.ID : None }

def getCouleurPion(pion: dict)-> int:
    """
    Renvoie la couleur du pion passé en paramètre

    :param pion: Paramètre ou l'on veut la couleur
    :return: La couleur du pion
    :raise TypeError: Si le paramètre n’est pas un dictionnaire
    """
    if not (type_pion(pion)):
        raise TypeError("getCouleurPion : Le paramètre n’est pas un pion ")
    return pion[const.COULEUR]

def setCouleurPion(pion: dict, couleur : int) -> None:
    """
    Change la couleur du pion passé en paramètre avec la couleur passé en paramètre

    :param pion: Paramètre on l'on veut changer la couleur
    :param couleur: Paramètre correspondant à la couleur que l'on veut mettre
    :return: Rien
    :raise TypeError: Si le paramètre n’est pas un dictionnaire
    :raise TypeError: Si le paramètre n’est pas un entier
    :raise ValueError: Si l’entier ne représente pas une couleur
    """

    if not (type_pion(pion)):
        raise TypeError("setCouleurPion : Le premier paramètre n’est pas un pion")
    elif type(couleur) != int:
        raise TypeError("« setCouleurPion : Le second paramètre n’est pas un entier.")
    elif couleur not in const.COULEURS:
        raise ValueError(f"setCouleurPion : Le second paramètre {couleur} n’est pas une couleur")
    pion[const.COULEUR] = couleur
    return None

def getIdPion(pion : dict) -> int:
    """
    Renvoie l'id du pion passé en paramètre

    :param pion: Paramètre où on ve savoir l'identifiant
    :return: Retourne l'ID
    :raise TypeError: Si le paramètre n’est pas un dictionnaire
    """
    if not (type_pion(pion)):
        raise TypeError("getIdPion : Le paramètre n’est pas un pion")
    return pion[const.ID]

def setIdPion(pion: dict, id : int) -> None:
    """
    Change l'id du pion passé en paramètre par l'id passé en paramètre

    :param pion: Paramètre d'on l'on veut changer l'id
    :param id: Paramètre correspondant au nouveau id
    :return: Rien
    :raise TypeError: Si le paramètre n’est pas un dictionnaire
    :raise TypeError: Si le paramètre n’est pas un entier
    """
    if not(type_pion(pion)):
        raise TypeError("setIdPion : Le premier paramètre n’est pas un pion")
    elif type(id) != int:
        raise TypeError("setIdPion : Le second paramètre n’est pas un entier")
    pion[const.ID] = id
    return None

