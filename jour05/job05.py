nb_marche = input('Entrer le nombre de marche : ')
hauteur_marche = input('Entrer hauteur des marches : ')

def distance(marche,hauteur):
    marche = int(marche)
    hauteur = float(hauteur)
    nb_marche_semaine = marche * 2 * 5 * 7
    distance_cm = nb_marche_semaine * hauteur
    distance_m = float(distance_cm/100)
    distance_m = str(distance_m)
    return distance_m
distance(nb_marche,hauteur_marche)

distance_total = distance(nb_marche,hauteur_marche)
print(distance_total)

print('Pour ' + nb_marche + ' marche de ' + hauteur_marche + ' cm, le gardien parcours ' + distance_total + ' m par semaine.')
