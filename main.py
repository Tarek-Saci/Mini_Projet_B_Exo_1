import matplotlib.pyplot as plt
import numpy as np

# -------fixer les parametres----------------------------------------------------
p1 = 5
p2 = 5
p3 = 7
p4 = 1
n = 100
a = -10
b = 15


# -------une fonction qui determine la solution analytique ----------------------
def integrale_analytique(p1, p2, p3, p4, a, b):
    x = a
    primitive_1 = (p1 * x) + (0.5 * p2 * x ** 2) + ((1 / 3) * p3 * x ** 3) + (0.25 * p4 * x ** 4)
    x = b
    primitive_2 = (p1 * x) + (0.5 * p2 * x ** 2) + ((1 / 3) * p3 * x ** 3) + (0.25 * p4 * x ** 4)
    resultat = primitive_2 - primitive_1
    return resultat


# -------fonction methode des rectangles-----------------------------------------
def integrale_rectangles(p1, p2, p3, p4, a, b, n):
    largeur_rectangle = (b - a) / n
    liste_aires_rectangle = []  # on initalise une liste qui va contenir toutes les aires des rectangles qu'on poura ensuite aditionner
    x = a + largeur_rectangle / 2  # on éssaye de placer x au milieu du rectangle
    while x <= b - (largeur_rectangle / 2):  # on fait varier x avec un pas égale a la largeur du rectangle
        hauteur_rectagle = (p1) + (p2 * x) + (p3 * x ** 2) + (p4 * x ** 3)
        aire = hauteur_rectagle * largeur_rectangle
        liste_aires_rectangle.append(aire)
        x += largeur_rectangle
    resultat = sum(liste_aires_rectangle)
    return resultat


# -------fonction calcule d'erreur -----------------------------------------------
def erreur(resultat_analytique, resultat_rectangle):
    # [(valeur réelle - valeur théorique)/valeur réelle] x 100
    erreur = ((resultat_analytique - resultat_rectangle) / resultat_analytique) * 100
    return erreur


# -------fonction calcul d'erreur en fonction de n -------------------------------
def erreur_fonction_n(n):
    resultat_rectangle = integrale_rectangles(p1, p2, p3, p4, a, b, n)
    resultat_analytique = integrale_analytique(p1, p2, p3, p4, a, b)
    erreur = ((resultat_analytique - resultat_rectangle) / resultat_analytique) * 100
    return erreur


# -------fonction de verification de convergence----------------------------------
def convergence(n):
    list_erreur = []  # initialiser une liste qui nous permetera de recuperer la valeur de l'integrale en fonction de n
    liste_n = []  # initialiser une liste qui nous permetera de recuperer la valeur de n a chaque iteration
    for i in range(n):
        list_erreur.append(erreur_fonction_n(i))
        list_n
    plt.plot()
    return


# --------------------------------------------------------------------------------

resultat_analytique = integrale_analytique(p1, p2, p3, p4, a, b)
resultat_rectangle = integrale_rectangles(p1, p2, p3, p4, a, b, n)
erreur = erreur_fonction_n(n)
print(f'resultat analytique : {resultat_analytique}')
print(f'resultat rectangles : {resultat_rectangle}')
print(f'erreur : {erreur} %')
