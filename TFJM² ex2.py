#  aide pour l'exercice 2 du TFJM 12ème édition
def mov(formation):  # retourne une liste avec les partions qui découle d'une formation
    # exemple, input = (1, 2, 1) output [[[1, 2, 3], [1, 0, 1], [1, 2, 1]]]
    new_formation = []

    for element in formation:
        new_formation.append(list(formation))

    for bird in range(len(new_formation)):
        new_formation[bird][bird] = 0 - new_formation[bird][bird]

        if bird - 1 > -1:
            new_formation[bird][bird] += new_formation[bird][bird - 1]
        else:
            new_formation[bird][bird] += 0

        try:
            new_formation[bird][bird] += new_formation[bird][bird + 1]
        except IndexError:
            new_formation[bird][bird] += 0
    return [list(i) for i in new_formation]


def boucle(possible_formation):
    # va execute mov() jusqu'à que tous les résultats soient obtenus
    # applique la règle de la limite de fils par rapport à k
    # envoie les partition obtenues à formation
    a = []
    try:
        for sheet_music in possible_formation:
            a.append(mov(sheet_music))
            for b in range(len(a)):
                for c in range(len(a[b])):
                    if k:
                        a[b][c] = [i for i in a[b][c] if abs(i) <= k]
                    possible_formation.add(tuple(a[b][c]))
    except RuntimeError:
        boucle(possible_formation)


def bloc_note(final_set): # enregister les résultats obtenu dans un bloc note
    doc = open('final_set.txt', 'w', encoding='UTF-8')
    doc.write(str(final_set))
    doc.close()


if __name__ == '__main__':
    k = False  # mettre la valeur de k, mettre False si le nombre de fils est infini
    start = []  # mettre la partition de d'épart, avec l'exemple de l'exercice, se serait : start = [-2, # 1, 2, 0]
    text = False  # Mettre True si vous voulez que le résultat soit écrit dans un bloc note

    if k:
        start = [i for i in start if abs(i) <= k]
    formation = {tuple(start)}

    boucle(formation)
    print(formation)
    print('There are', len(formation), 'possibility')
    if text:
        bloc_note(formation)
