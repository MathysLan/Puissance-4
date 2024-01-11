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

def plateauMatrice(plateau: list) -> list:
    matrice = []
    for i in range(const.NB_LINES):
        matrice.append([])
        for j in range(const.NB_COLUMNS):
            if plateau[i][j]== None:
                matrice[i] += '_'
            else:
                if plateau[i][j][const.COULEUR] == const.ROUGE:
                    matrice[i] += 'R'
                else:
                    matrice[i] += 'J'
    return matrice

