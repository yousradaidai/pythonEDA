
# Q1 : Importer le package numpy
import numpy as np


# Q2 : Afficher la version de numpy et la configuration
print(np.__version__)
print(np.show_config())


# Q3 : Créer un vecteur nul de taille 10
x = np.zeros(10)
print(x)


# Q4 : Créer un vecteur null de taille 10 et affecter la valeur 1 à la 4ème place
#  (index 4) du vecteur
arr = np.empty(10)
arr[4] = 1
print (arr)


# Q5 : Créer un vecteur Z de 40 valeurs allant de 10 à 50
z = np.linspace(10, 49, 40)
print(z)


# Q6 : Inverser Z (le premier élément devient donc le dernier)
zz = z[::-1]
print(zz)


# Q7 : Créer une matrice 3x3 avec des valeurs comprise entre 0 et 8
np.arange(9).reshape(1,3,3)


# Q8 : Créer une matrice identié 3x3
c = np.arange(9).reshape(1,3,3)
print(c)


# Q9 : Créer une matrice 3x3x3 avec des valeurs random
rd = np.random
rd.rand(3,3,3)


# Q10 : Créer une matrice 10x10 avec des valeurs random et afficher le minimum
#  et maximum de cette matrice
rd = np.random
rd.rand(10,10)


# Q11 : Créer une matrice 5x5 avec les valeurs 1,2,3,4 en dessous de la diagonale
neo = np.arange(1,5,1)
np.diag(neo,-1)


# Q12 : Créer une liste random de taille 5 et donner la somme de ses éléments
arr1 = np.random.rand(5).cumsum()
print("Total de {} = {}".format(arr1, arr1.sum()))


# Q13 : Créer une liste random de taille 5 et donner la moyenne de ses éléments
rd = np.random
rd.randint(0,5,5).mean()


# Q14 : En utilisant une fonction, donner la taille de la liste suivante :
# l = [x for x in range(11)]
l = [x for x in range(11)]
print(len(l))


# Q15 : Créer un tableau de taille 10 avec des valeurs comprises entre 0 et 1 EXCLUS
rd = np.arange(0, 1, 0.1)
print(rd)


# Q16 : Soit deux tableau A et B de dimension 1 et de taille 5, créer A et B et
#  afficher True si A et B sont égaux False sinon
A = np.array([0,1,2,3,4])
B = np.array([0,1,2,3,6])

if np.greater_equal(A, B).all():
    print("TRUE")
else :
    print("FALSE")


# Q17 : Convertir un tableau de float32 de dimension 1 et de taille 10 en un tableau de
#  meme taille et dimension mais de type int32

a2_float = np.arange(0.0, 10.0, 1.5)
print("float : {}".format(a2_float))
a2_int = a2_float.astype(int)
print("int : {}".format(a2_int))


# Q18 : Normaliser une matrice random 5x5
# La normalisation d'un nombre X consiste à lui retirer sa moyenne et a diviser le 
# tout par son écart type
m = np.random.rand(5, 5)
print(m)
print("Moyenne matrice : {}".format(m.mean()))
print("Ecart type : {}".format(m.std()))
print( (m-m.mean())/m.std() )


# Q19 : Créer une matrice random M 2x2 et donner sa transposer
m2 = np.random.rand(3,3)
print(m2)
m2_transposed = m2.transpose()
print(m2_transposed)


# Q20 : Écrire un petit script qui remplace un élément au hasard dans une matrice de dimension NxN
import random
def randomCellReplacer(matrix):
    matrixLines  = np.size(matrix, 0)
    matrixColumn = np.size(matrix, 1)
    
    matrix[random.randint(0, matrixLines)-1, random.randint(0, matrixLines)-1] = 5555

m3 = np.random.rand(3,4)
print(m3)
randomCellReplacer(m3)
print(m3)


# Q21 : Considérons une matrice de dimension (5,5,3), écrire un script qui multiplie cette
#  matrice par une matrice de dimension (5,5)
m4 = np.random.rand(5,5,3)
print(m4)