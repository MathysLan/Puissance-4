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