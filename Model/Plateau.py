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
    Fonction permettant de savoir s'il y a 4 pions de même couleur à la suite horizontalement

    :param plateau: Paramètre où l'on va chercher si 4 pions sont alignés
    :param couleur: Paramètre correspondant à la couleur du pion que l'on cherche
    :return: Renvoie la liste des pions qui sont 4 à la suite en fonction de la couleur passé en paramètre
    :raise TypeError: Si le paramètre n’est pas une liste
    :raise TypeError: Si le paramètre n’est pas un entier
    :raise ValueError: Si le paramètre n'est pas compris dans les couleurs constantes
    """
    if not(type_plateau(plateau)):
        raise TypeError("Le premier paramètre ne correspond pas à un plateau")
    if type(couleur) != int:
        raise TypeError("detecter4horizontalPlateau : le second paramètre n’est pas un entier")
    if couleur not in const.COULEURS:
        raise ValueError(f"détecter4horizontalPlateau : La valeur de la couleur {couleur}n’est pas correcte")
    listePionsHorizontal = []
    # Pour chaque ligne
    for ligne in range(const.NB_LINES):
        colonne = 0
        compteurPions = 0
        # Tant qu'on arrive pas à la fin des colonnes
        while colonne < const.NB_COLUMNS:
            # Si l'élement n'est pas un pion ou que le pion n'est pas de la bonne couleur compteur à 0
            if plateau[ligne][colonne] == None or plateau[ligne][colonne][const.COULEUR] != couleur:
                compteurPions =0
            # Sinon si le pion est de la bonne couleur compteur + 1
            elif plateau[ligne][colonne][const.COULEUR] == couleur:
                compteurPions += 1
            # Si le compteut est égal à 4 c'est qu'on a bien les 4 pions donc on les prend en repartant en arrière
            if compteurPions == 4:
                listePionsHorizontal += [plateau[ligne][colonne-3], plateau[ligne][colonne-2],plateau[ligne][colonne-1], plateau[ligne][colonne]]
            colonne +=1
    return listePionsHorizontal

def detecter4verticalPlateau(plateau: list, couleur: int) -> list:
    """
    Fonction permettant de savoir s'il y a 4 pions de même couleur à la suite verticalement

    :param plateau: Paramètre où l'on va chercher si 4 pions sont alignés
    :param couleur: Paramètre correspondant à la couleur du pion que l'on cherche
    :return: Renvoie la liste des pions qui sont 4 à la suite en fonction de la couleur passé en paramètre
    :raise TypeError: Si le paramètre n’est pas une liste
    :raise TypeError: Si le paramètre n’est pas un entier
    :raise ValueError: Si le paramètre n'est pas compris dans les couleurs constantes
    """
    if not(type_plateau(plateau)):
        raise TypeError("Le premier paramètre ne correspond pas à un plateau")
    if type(couleur) != int:
        raise TypeError("detecter4verticalPlateau : le second paramètre n’est pas un entier")
    if couleur not in const.COULEURS:
        raise ValueError(f"détecter4verticalPlateau : La valeur de la couleur {couleur}n’est pas correcte")
    listePionsVertical = []
    # Pour chaque colonne
    for colonne in range(const.NB_LINES):
        ligne = 0
        compteurPions = 0
        # Tant qu'on arrive pas à la fin des ligne
        while ligne < const.NB_LINES:
            # Si l'élement n'est pas un pion ou que le pion n'est pas de la bonne couleur compteur à 0
            if plateau[ligne][colonne] == None or plateau[ligne][colonne][const.COULEUR] != couleur:
                compteurPions =0
            # Sinon si le pion est de la bonne couleur compteur + 1
            elif plateau[ligne][colonne][const.COULEUR] == couleur:
                compteurPions += 1
            # Si le compteut est égal à 4 c'est qu'on a bien les 4 pions donc on les prend en repartant en arrière
            if compteurPions == 4:
                listePionsVertical += [plateau[ligne-3][colonne], plateau[ligne-2][colonne],plateau[ligne-1][colonne ], plateau[ligne][colonne]]
            ligne +=1
    return listePionsVertical

def detecter4diagonaleDirectePlateau(plateau : list, couleur : int) -> list:
    """
    Fonction permettant de savoir s'il y a 4 pions de même couleur à la suite diagonalement direct

    :param plateau: Paramètre où l'on va chercher si 4 pions sont alignés
    :param couleur: Paramètre correspondant à la couleur du pion que l'on cherche
    :return: Renvoie la liste des pions qui sont 4 à la suite en fonction de la couleur passé en paramètre
    :raise TypeError: Si le paramètre n’est pas une liste
    :raise TypeError: Si le paramètre n’est pas un entier
    :raise ValueError: Si le paramètre n'est pas compris dans les couleurs constantes
    """
    if not(type_plateau(plateau)):
        raise TypeError("Le premier paramètre ne correspond pas à un plateau")
    if type(couleur) != int:
        raise TypeError("detecter4verticalPlateau : le second paramètre n’est pas un entier")
    if couleur not in const.COULEURS:
        raise ValueError(f"détecter4verticalPlateau : La valeur de la couleur {couleur}n’est pas correcte")
    listePiontDiagonal = []
    # POur chaque ligne -3 car il ne peut pas avoir de diagonale qui part de 3 ligne en arrière
    for ligne in range(const.NB_LINES - 3):
        # de même pour les colonnes
        for colonnes in range(const.NB_COLUMNS -3):
            # Si l'element est bien de la bonne couleur alors on teste les 4 prochains piont en diagonale
            if plateau[ligne][colonnes] != None and plateau[ligne][colonnes][const.COULEUR] == couleur:
                i = 0
                drapeau = True
                # Tant que compteur (i) est inférieur à 4 et que drapeau ( qui sert a sortir de la boucle si un des pions n'est pas le bon) est égal a true
                while i < 4 and drapeau == True:
                    # Si l'élement en diagonale n'est pas bon alors on arrête la boucle
                    if plateau[ligne+i][colonnes+i] == None or plateau[ligne+i][colonnes+i][const.COULEUR]!= couleur:
                        drapeau = False
                    i +=1
                # Si le drapeau est égal à True alors c'est qu'il n'y a pas de problème donc ajoute les pions
                if drapeau == True:
                    listePiontDiagonal += [plateau[ligne][colonnes], plateau[ligne+1][colonnes+1],plateau[ligne+2][colonnes+2 ], plateau[ligne+3][colonnes+3]]
    return listePiontDiagonal

def detecter4diagonaleIndirectePlateau(plateau: list, couleur: int) -> list:
    """
    Fonction permettant de savoir s'il y a 4 pions de même couleur à la suite diagonalement indirect

    :param plateau: Paramètre où l'on va chercher si 4 pions sont alignés
    :param couleur: Paramètre correspondant à la couleur du pion que l'on cherche
    :return: Renvoie la liste des pions qui sont 4 à la suite en fonction de la couleur passé en paramètre
    :raise TypeError: Si le paramètre n’est pas une liste
    :raise TypeError: Si le paramètre n’est pas un entier
    :raise ValueError: Si le paramètre n'est pas compris dans les couleurs constantes
    """
    if not(type_plateau(plateau)):
        raise TypeError("Le premier paramètre ne correspond pas à un plateau")
    if type(couleur) != int:
        raise TypeError("detecter4verticalPlateau : le second paramètre n’est pas un entier")
    if couleur not in const.COULEURS:
        raise ValueError(f"détecter4verticalPlateau : La valeur de la couleur {couleur}n’est pas correcte")
    listePiontDiagonal = []
    # POur chaque ligne -3 car il ne peut pas avoir de diagonale qui part de 3 ligne en arrière
    for ligne in range(const.NB_LINES-3):
        # de même pour les colonnes
        for colonnes in range(const.NB_COLUMNS-1,3,-1):
            # Si l'element est bien de la bonne couleur alors on teste les 4 prochains piont en diagonale
            if plateau[ligne][colonnes] != None and plateau[ligne][colonnes][const.COULEUR] == couleur:
                i = 0
                drapeau = True
                # Tant que compteur (i) est inférieur à 4 et que drapeau ( qui sert a sortir de la boucle si un des pions n'est pas le bon) est égal a true
                while i < 4 and drapeau == True:
                    # Si l'élement en diagonale n'est pas bon alors on arrête la boucle
                    if plateau[ligne+i][colonnes-i] == None or plateau[ligne+i][colonnes-i][const.COULEUR]!= couleur:
                        drapeau = False
                    i +=1
                # Si le drapeau est égal à True alors c'est qu'il n'y a pas de problème donc ajoute les pions
                if drapeau == True and not(plateau[ligne][colonnes] in listePiontDiagonal):
                    listePiontDiagonal += [plateau[ligne][colonnes], plateau[ligne+1][colonnes-1],plateau[ligne+2][colonnes-2 ], plateau[ligne+3][colonnes-3]]
    return listePiontDiagonal

