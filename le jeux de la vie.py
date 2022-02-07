# vocabulaire utilisé : cellule noire = cellule vivante et cellule blanche = cellule morte ou qui n'a jamais vécu
import time

N = int(input("Saisie la taille de tableau que tu veux:\n"))
nb_cycles = int(input("Saisie le nombre de cycles que tu veux:\n"))

tableau = [[0 for j in range(N)] for i in range(N)]  # création du tableau
liste_future_vivantes = []
liste_future_mortes = []
x = None
y = None

print("\nSaisie des coordonnées des cellules vivantes:")

while x != '' and y != '':  # boucle qui demande les coordonnées des cellules noires tant que la réponse n'est pas une
    # chaine vide
    x = input("Quelle ligne\n")
    y = input("Quelle colonne\n")

    try:  # essaye d'ajouté la cellule dans le tableau
        tableau[int(x)][int(y)] = 1
        print("Cellule enregistrée\nCoordonnées de la cellule suivante, (renvoyez une chaine vide si vous ne voulez "
              "plus en rajouter)")

    except IndexError:  # si l'emplacement donné à la cellule noire n'est pas dans le tableau
        print("impossible d'ajouté une cellule vivante à cet endroit")
        pass

    except ValueError:  # si la raiponce n'est pas intable
        pass


def nombre_vivantes_autour(i,
                           j):  # compte le nombre de cellules noires autour de chaque cellule (que les 9 autour d'elle)

    vrai = 0  # créer et mettre à zéro un compteur de cases noires
    try:
        if tableau[i][j - 1]:  # si la cellule juste avant est noire
            vrai += 1  # ajouté 1 au compteur du nombre de cellules noires autour
    except IndexError:  # si cette case n'existe pas dans le tableau (ex: les cellules dans les angles)
        pass
    try:
        if tableau[i][j + 1]:
            vrai += 1
    except IndexError:
        pass
    try:
        if tableau[i + 1][j]:
            vrai += 1
    except IndexError:
        pass
    try:
        if tableau[i - 1][j]:
            vrai += 1
    except IndexError:
        pass
    try:
        if tableau[i + 1][j + 1]:
            vrai += 1
    except IndexError:
        pass
    try:
        if tableau[i - 1][j - 1]:
            vrai += 1
    except IndexError:
        pass
    try:
        if tableau[i + 1][j - 1]:
            vrai += 1
    except IndexError:
        pass
    try:
        if tableau[i - 1][j + 1]:
            vrai += 1
    except IndexError:
        pass

    return vrai


for ligne in tableau:  # dessine le premier tableau, avant le premier cycle
    print(ligne)

print('\n' * N)  # sauter un espace de la taille d'un tableau

for a in range(nb_cycles):  # répéter le nombre de cycles demandés par l'utilisateur

    for i in range(N):
        for j in range(N):  # pour chaque cellule
            if tableau[i][j] == 0 and nombre_vivantes_autour(i,
                                                             j) == 3:  # si elle est blanche et qu'elle a trois
                # voisines noires
                liste_future_vivantes.append([i, j])  # ajouté cette cellule à liste_future_vivantes
            elif tableau[i][j] == 1 and nombre_vivantes_autour(i, j) != 2 and nombre_vivantes_autour(i,
                                                                                                     j) != 3:  # si
                # elle est noire et qu'elle n'a pas deux ou trois voisines noires
                liste_future_mortes.append([i, j])  # ajouté cette cellule à liste_future_mortes

    for value in liste_future_vivantes:  # transformer les cellules de liste_future_vivantes en cellules noires
        tableau[value[0]][value[1]] = 1
    for value in liste_future_mortes:  # transformer les cellules de liste_future_mortes en cellules blanches
        tableau[value[0]][value[1]] = 0
    for ligne in tableau:  # afficher le tableau
        print(ligne)
    if len(liste_future_vivantes) == 0 and len(
            liste_future_mortes) == 0:  # s'il n'y a eu aucun changement arrêté le programme
        exit()
    liste_future_vivantes = []  # remettre liste_future_vivantes et liste_future_mortes à zéro
    liste_future_mortes = []
    time.sleep(1)  # attendre une seconde pour laisser le temps de voir les évolutions
    print('\n' * N)  # sauter un espace de la taille d'un tableau
