# On a créé un tableau 2D rdm_mat contenant des valeurs aléatoires.
import numpy as np
rd = np.random
rdm_mat = rd.randn(4,2)
print(rdm_mat)

# Donner le type de la variable rdm_mat
rdm_mat.dtype

# Donner la somme des éléments de ce tableau 2D
rdm_mat.cumsum()[-1]


# Faire en sorte de récupérer la valeur maximale sur chaque ligne (sans boucles) 
# avec la fonction np.max
np.amax(rdm_mat, axis=1)


# Faire de même pour récupérer la valeur maximum pour chaque colonne (sans boucles)
np.amax(rdm_mat, axis=0)

# Faire la même chose (max des lignes) en définissant un tableau avec une boucle
#  for et la fonction max de numpy


# On crée un vecteur aléatoire de taille 100 rdm_vect
rdm_vect = np.random.randn(100)
rdm_vect.shape
rdm_vect


# Récupérer la position de la valeur maximale du vecteur avec la méthode np.argmax
np.argmax(rdm_vect)


# Afficher cette valeur
rdm_vect[92]


# Convertir le vecteur en un tableau 10, 10
r = rdm_vect.reshape(10, 10); r

# Calculer la moyenne de chaque ligne de ce tableau (sans boucles)
r.mean(axis=0)

# Faire un tableau qui contient la moyenne de chaque colonne du tableau

# Calculer la somme de chaque colonne (sans boucles)
r.mean(axis=1)

# Calculer la somme pour chaque ligne (sans boucles)
r.sum(axis=0)