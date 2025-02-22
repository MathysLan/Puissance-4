from random import randint

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

def getPionJoueur(joueur : dict) -> dict:
    """
    Renvoie un pion en fonction de la couleur du joueur passé en paramètre

    :param joueur: Paramètre qui représente le joueur
    :return: Le pion créé
    :raise TypeError: Si le paramètre n’est pas un dictionnaire
    """
    if not (type_joueur(joueur)):
        raise TypeError("getPionJoueur : le paramètre ne correspond pas à un joueur")

    return construirePion(joueur[const.COULEUR])

def setPlateauJoueur(joueur: dict, plateau : list) -> None:
    """
    Affecte un plateau passé en paramètre à un joueur en paramètre

    :param joueur: Paramètre qui représente le joueur
    :param plateau: Paramètre qui répresente le plateau
    :return: rien
    :raise TypeError: Si le paramètre n’est pas un joueur
    :raise TypeError: Si le paramètre n’est pas un plateau
    """
    if not (type_joueur(joueur)):
        raise TypeError("getPionJoueur : le paramètre ne correspond pas à un joueur")
    if not(type_plateau(plateau)):
        raise TypeError("setPlateauJoueur : Le second paramètre ne correspond pas à un plateau")
    joueur[const.PLATEAU] = plateau
    return None

def setPlacerPionJoueur(joueur: dict, fn: callable) -> None:
    """
    Affecte une foncton passé en paramètre à un joueur en paramètre

    :param joueur: Paramètre qui représente le joueur
    :param fn: Paramètre qui répresente la fonction à affecté
    :return: rien
    :raise TypeError: Si le paramètre n’est pas un joueur
    :raise TypeError: Si le paramètre n’est pas un plateau
    """
    if not (type_joueur(joueur)):
        raise TypeError(" setPlacerPionJoueur : le paramètre ne correspond pas à un joueur")
    if not( callable(fn)):
        raise TypeError("setPlacerPionJoueur : le second paramètre n’est pas une fonction")
    joueur[const.PLACER_PION] = fn
    return None

def _placerPionJoueur(joueur : dict) -> int:
    """
    Fonction qui choisit un nombre aléatoire entre 0 et NB_COLUMNS -1 en vérifiant que la colonne n'est pas pleine

    :param joueur: Paramètre qui représente le joueur
    :return: entier représentant la colonne où l'IA va jouer son piont
    :raise TypeError: Si le paramètre n’est pas un joueur
    """
    if not (type_joueur(joueur)):
        raise TypeError(" setPlacerPionJoueur : le paramètre ne correspond pas à un joueur")
    if not (getModeEtenduJoueur(joueur)):
        colonneAlea = randint(0, const.NB_COLUMNS -1)
        drapeau = False
        while drapeau == False :
            if joueur[const.PLATEAU][0][colonneAlea] == None:
                drapeau = True
            else:
                colonneAlea = randint(0, const.NB_COLUMNS -1)
    else:
        colonneAlea = randint(-const.NB_LINES, const.NB_COLUMNS + const.NB_LINES -1)
        while (0 <= colonneAlea and colonneAlea < const.NB_COLUMNS) and (joueur[const.PLATEAU][0][colonneAlea] != None):
            colonneAlea = randint(-const.NB_LINES, const.NB_COLUMNS + const.NB_LINES - 1)
    return colonneAlea

def initialiserIAJoueur(joueur: dict, booleen : bool) ->None:
    """
    Fonction qui affecte la fonction _placerPionJoueur au joueur passé en paramètre

    :param joueur:Paramètre qui représente le joueur
    :param booleen: Paramètre permettant de savoir si le joueur joue en premier (True) ou en second (False)
    :return: Rien
    :raise TypeError: Si le paramètre n’est pas un joueur
    :raise TypeError: Si le paramètre n’est pas un booléen
    """
    if not (type_joueur(joueur)):
        raise TypeError("initialiserIAJoueur : Le premier paramètre n’est pas un joueur")
    if type(booleen) != bool:
        raise TypeError("initialiserIAJoueur : Le second paramètre n’est pas un booléen")
    setPlacerPionJoueur(joueur, _placerPionJoueur)
    return None

def getModeEtenduJoueur(joueur: dict) -> bool:
    """
       Renvoie True si le joueur est en mode étendue, False sinon.
       :param joueur: Le joueur à analyser.
       :return: True si le joueur est en mode étendu, False sinon.
       :raise TypeError: Si le paramètre n'est pas un joueur.
       """
    if not (type_joueur(joueur)):
        raise TypeError("getModeEtenduJoueur : le paramètre ne correspond pas à un joueur")
    if const.MODE_ETENDU in joueur.keys():
        booleen = True
    else:
        booleen = False
    return booleen

def setModeEtenduJoueur(joueur: dict, booleen=True) -> None:
    """
        Modifie le mode étendu du joueur en fonction du booleen passé en paramètre
        :param joueur: Le joueur à modifier.
        :param booleen: La valeur booléenne à assigner au mode étendu du joueur (par défaut, True).
        :return: Aucun retour, modifie le joueur en place.
        :raise TypeError: Si le premier paramètre n'est pas un joueur.
        :raise TypeError: Si le second paramètre n'est pas un booléen.
        """
    if not (type_joueur(joueur)):
        raise TypeError("setModeEtenduJoueur : le premier paramètre ne correspond pas à un joueur")
    if type(booleen) != bool:
        raise TypeError("setModeEtenduJoueur : le second paramètre ne correspond pas à un booléen")
    if booleen:
        joueur[const.MODE_ETENDU] = True
    elif const.MODE_ETENDU in joueur:
        del joueur[const.MODE_ETENDU]
    return None
