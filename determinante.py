from copy import deepcopy
import numpy as np


A = [[2,3,2],[1,2,2],[4,4,5]]

def matrizReducida(matrizOriginal , fila , columna):                 # funcion usada en hola perrito
    nuevaMatriz = deepcopy(matrizOriginal)                           # copio la matriz original, la nueva matriz no puede afectar original
    nuevaMatriz.remove(matrizOriginal[fila])                         # elimino fila en el ejemplo seria 2,3,2

    for i in range( len(nuevaMatriz)):                              #  range( len(nuevaMatriz)) -> [0,1]  i -> 01 01 01 , sale 01 3 veces
        nuevaMatriz[i].remove( nuevaMatriz[i][columna])             # recorro cada fila y elimino las columnas por elemento ...ojoelemento por elemento
    return  nuevaMatriz

def determinant(matriz):

    filasNumero = len(matriz)

    # coincidencia de dimensiones
    for fila in matriz:

        if len(fila) != filasNumero :                                    # len(fila) = 3  len(matriz ) = 3
            print "no es una matriz cuadrada"
            return None

    # caso base
    if len(matriz) == 2 :
        determinanteBase = matriz[0][0] * \
                           matriz[1][1] - \
                           matriz[1][0] * \
                           matriz[0][1]
        return  determinanteBase
    else:
        # detemrinante teniendo encuenta la expansion de cofactores
        respuesta = 0                                                      # suma acumulada
        columnasnumero = filasNumero                                       # pq es cuadrada

        for j in range(columnasnumero):                                    # puede ser un j o un i
            cofactor = ((-1) ** (0 + j) ) * matriz[0][j]           \
                                         * determinant(matrizReducida( matriz , 0 , j )) # hola perrito quiero reducir la fila 0 y columna especificada ver la func

            respuesta = cofactor
        return respuesta


print "el determinante es : " , determinant(A)
print "el determinante segun numpy es : ", np.linalg.det(A)










# _________-


# # el chequeo d ematriz cuadrada este es el reusltado de recorrer el for
# for fila in matriz:
#     print matriz
#     print fila
#     print "________"
#
# A = [[2,3],[1,2],[4,5]] -> no cuadrada
# [[2, 3], [1, 2], [4, 5]]
# [2, 3]
# ________
# [[2, 3], [1, 2], [4, 5]]
# [1, 2]
# ________
# [[2, 3], [1, 2], [4, 5]]
# [4, 5]
# ________



# determinanteBase = matriz[0][0] * \
#                    matriz[1][1] - \
#                    matriz[1][0] * \
#                    matriz[0][1]
#
# a00 a01    base  ... a00 * a11  -  a01 * a11
# a10 a11


# en la iteracion para el caso no basestring
#
# print columnasnumero  -> 3
#
#         for j in range(columnasnumero):
#             print j  -> 0 1 2
#
#         ((-1) ** (0 + j) ) * matriz[0][j]  * determinant(matrizReducida( matriz , 0 , j ))
           # se debe expresar la funcion matriz reducida   matrizReducida( matriz , 0 , j ) -> eliminando la fila 0

           # fila cero columna j matriz[0][j]
#


# resultaod de matriz reducida para el ejemplo
#
# A =
#      2 3 2
#      1 2 2
#      4 4 5
# print matrizReducida(A , 0 , j)   en el ecodigo i = j
#
#          i = 0     matrizReducida = 2 2
#                                     4 5
#          i = 1     matrizReducida = 1 2
#                                     4 5
#          i = 2    matrizReducida =  1 2
#                                     4 4

# https://scriptverse.academy/tutorials/python-determinant.html