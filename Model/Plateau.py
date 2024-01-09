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

def detecter4diagonaleDirectePlateau(plateau:list, couleur:int)-> list:
    """
    Lister les pions de la couleur choisie qui sont alignés par 4 sur la diagonale directe
    :param plateau: Le plateau à analyser
    :param couleur: La couleur pour laquelle on souhaite chercher des pions alignés sur le diagonale directe
    :return: La liste des pions de la couleur choisie qui sont alignés par 4, une liste vide s'il n'y en a pas
    :raise TypeError: Si le paramètre n'est pas un plateau
    :raise TypeError: Si le paramètre n'est pas un entier
    :raise ValueError: Si l'entier ne représente pas une couleur
    """
    if type_plateau(plateau) == False:
        raise TypeError("detecter4diagonaleDirectePlateau : Le premier paramètre ne correspond pas à un plateau.")
    if type(couleur) != int:
        raise TypeError("detecter4diagonaleDirectePlateau : Le second paramètre n'est pas un entier.")
    if couleur not in const.COULEURS:
        raise ValueError("detecter4diagonaleDirectePlateau : La valeur de la couleur {couleur} n'est pas correcte.")
    listePion = []
    for colonne in range(const.NB_COLUMNS - 4, -1, -1):
        i = 0
        # Nouvelle diagonale : réinitialisation du compteur de pions alignés
        nbPionsAlignes = 0
        while i < (const.NB_LINES) and (colonne + i) < const.NB_COLUMNS:
            # Si on n'est pas sur un pion, ou que ce n'est pas un pion de la bonne couleur
            if plateau[i][colonne + i] == None or plateau[i][colonne + i][const.COULEUR] != couleur:
                # Remise du compteur de pions alignés à 0
                nbPionsAlignes = 0
            # Sinon, c'est un pion de la bonne couleur
            elif plateau[i][colonne + i][const.COULEUR] == couleur:
                # On incrémente le compteur de pions alignés de 1
                nbPionsAlignes += 1
            # Si on a 4 pions alignés
            if nbPionsAlignes == 4:
                # On ajoute ces 4 pions à la liste résultat, et on réinitialise le compteur
                listePion += [plateau[i-3][colonne + (i-3)], plateau[i-2][colonne + (i-2)], plateau[i-1][colonne + (i-1)], plateau[i][colonne + i]]
                nbPionsAlignes = 0
            i += 1
    for ligne in range(1, const.NB_LINES - 3):
        i = 0
        # Nouvelle diagonale : réinitialisation du compteur de pions alignés
        nbPionsAlignes = 0
        while i < (const.NB_COLUMNS) and (ligne + i) < const.NB_LINES:
            # Si on n'est pas sur un pion, ou que ce n'est pas un pion de la bonne couleur
            if plateau[ligne + i][i] == None or plateau[ligne + i][i][const.COULEUR] != couleur:
                # Remise du compteur de pions alignés à 0
                nbPionsAlignes = 0
            # Sinon, c'est un pion de la bonne couleur
            elif plateau[ligne + i][i][const.COULEUR] == couleur:
                # On incrémente le compteur de pions alignés de 1
                nbPionsAlignes += 1
            # Si on a 4 pions alignés
            if nbPionsAlignes == 4:
                # On ajoute ces 4 pions à la liste résultat, et on réinitialise le compteur
                listePion += [plateau[ligne + (i-3)][i-3], plateau[ligne + (i-2)][i-2], plateau[ligne + (i-1)][i-1], plateau[ligne + i][i]]
                nbPionsAlignes = 0
            i += 1
    return listePion
def detecter4diagonaleIndirectePlateau(plateau: list, couleur: int) -> list:
    """
    Lister les pions de la couleur choisie qui sont alignés par 4 sur la diagonale indirecte
    :param plateau: Le plateau à analyser
    :param couleur: La couleur pour laquelle on souhaite chercher des pions alignés sur le diagonale indirecte
    :return: La liste des pions de la couleur choisie qui sont alignés par 4, une liste vide s'il n'y en a pas
    :raise TypeError: Si le paramètre n'est pas un plateau
    :raise TypeError: Si le paramètre n'est pas un entier
    :raise ValueError: Si l'entier ne représente pas une couleur
    """
    if type_plateau(plateau) == False:
        raise TypeError("detecter4diagonaleDirectePlateau : Le premier paramètre ne correspond pas à un plateau.")
    if type(couleur) != int:
        raise TypeError("detecter4diagonaleDirectePlateau : Le second paramètre n'est pas un entier.")
    if couleur not in const.COULEURS:
        raise ValueError("detecter4diagonaleDirectePlateau : La valeur de la couleur {couleur} n'est pas correcte.")
    listePion = []

    # Diagonale montante (de gauche à droite)
    for colonne in range(const.NB_COLUMNS - 4):
        i = 0
        nbPionsAlignes = 0

        while i < (const.NB_LINES) and (colonne + i) < const.NB_COLUMNS:
            if plateau[i][colonne + i] == None or plateau[i][colonne + i][const.COULEUR] != couleur:
                nbPionsAlignes = 0
            elif plateau[i][colonne + i][const.COULEUR] == couleur:
                nbPionsAlignes += 1
            if nbPionsAlignes == 4:
                if (i - 3) >= 0 and (colonne + (i - 3)) >= 0:
                    listePion += [plateau[i - 3][colonne + (i - 3)], plateau[i - 2][colonne + (i - 2)], plateau[i - 1][colonne + (i - 1)], plateau[i][colonne + i]]
                nbPionsAlignes = 0
            i += 1

    for ligne in range(1, const.NB_LINES - 3):
        i = 0
        # Nouvelle diagonale : réinitialisation du compteur de pions alignés
        nbPionsAlignes = 0
        while 0 <= (const.NB_COLUMNS -1-i) and (ligne + i) < const.NB_LINES:

            # Si on n'est pas sur un pion, ou que ce n'est pas un pion de la bonne couleur
            if plateau[ligne + i][const.NB_COLUMNS -1 -i] == None or plateau[ligne + i][const.NB_COLUMNS -1 -i][const.COULEUR] != couleur:
                # Remise du compteur de pions alignés à 0
                nbPionsAlignes = 0
            # Sinon, c'est un pion de la bonne couleur

            else:
                # On incrémente le compteur de pions alignés de 1
                nbPionsAlignes += 1
            # Si on a 4 pions alignés
            if nbPionsAlignes == 4:
                # On ajoute ces 4 pions à la liste résultat, et on réinitialise le compteur
                listePion += [plateau[ligne + (i-3)][const.NB_COLUMNS -1 -(i-3)], plateau[ligne + (i-2)][const.NB_COLUMNS -1 -(i-2)], plateau[ligne + (i-1)][const.NB_COLUMNS -1 -(i-1)], plateau[ligne + i][const.NB_COLUMNS -1 -i]]
                nbPionsAlignes = 0


            i += 1
    return listePion
def getPionsGagnantsPlateau(plateau: list) -> list:
    """
    Récupère les pions gagnants présents sur le plateau.
    :param plateau: Le plateau à analyser.
    :return: La liste des pions gagnants, une liste vide s'il n'y en a pas.
    :raise TypeError: Si le paramètre n'est pas un plateau.
    """
    if not(type_plateau(plateau)):
        raise TypeError("getPionsGagnantsPlateau : Le paramètre n’est pas un plateau ")
    listeSerie4PionsAlignes = []
    for couleur in range(len(const.COULEURS)):
        listeSerie4PionsAlignes += detecter4horizontalPlateau(plateau, couleur)
        listeSerie4PionsAlignes += detecter4verticalPlateau(plateau, couleur)
        listeSerie4PionsAlignes += detecter4diagonaleDirectePlateau(plateau,couleur)
        listeSerie4PionsAlignes += detecter4diagonaleIndirectePlateau(plateau, couleur)
    return listeSerie4PionsAlignes

def isRempliPlateau(plateau : list) -> bool:
    """
    Vérifie si le plateau est complètement rempli de pions.
    :param plateau: Le plateau à vérifier.
    :return: True si le plateau est complètement rempli, False sinon.
    :raise TypeError: Si le paramètre n'est pas un plateau
    """
    if not (type_plateau(plateau)):
        raise TypeError("isRempliPlateau : Le paramètre n’est pas un plateau ")
    drapeau = True
    ligne = 0
    while ligne < const.NB_LINES and drapeau ==  True:
        colonne = 0
        while colonne < const.NB_COLUMNS and drapeau ==  True:
            if plateau[ligne][colonne] is None:
                drapeau = False # S'il y a au moins une case vide, le plateau n'est pas complètement rempli
            colonne += 1
        ligne += 1
    return drapeau