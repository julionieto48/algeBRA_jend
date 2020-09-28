from copy import deepcopy
import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# import mayavi.mlab as m




# determinante
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


#_________________________________________________________________________________________
def transpuesta(mtrx):
    mtrx
    # for i in range(len(mtrx)):
    #     for j in range(len(mtrx)):
    #         mtrx[i][j] = mtrx[j][i]

    mtrx = [[mtrx[j][i] for j in range(len(mtrx))] for i in range(len(mtrx[0]))]
    # print('\n')
    # for row in rez:
    #     print(row)

    return mtrx

def cramer(matriz,v):

    denominador = np.linalg.det(A)#determinant(A)

    Ax = deepcopy(matriz)
    #Ax[:,0] = 1 #Ax[:][0] =  v
    Axtrans = transpuesta(Ax)
    Axtrans[0][:] = v  # reemplazar filas si funciona y columnas no pues hago transpuesta
    Ax_x = transpuesta(Axtrans)

    x = np.linalg.det(Ax_x)/denominador

    return x

def plot(matriz ,v):
    Ax = deepcopy(matriz) ; Axtrans = transpuesta(Ax)

    i = Axtrans[0][:] ; j =  Axtrans[1][:]  ; k = Axtrans[2][:]

    origen = [0, 0, 0]
    X, Y, Z  = zip(origen, origen, origen)
    U, V, W  = zip(i, j, k )

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.quiver(X, Y, Z, U, V, W, arrow_length_ratio=0.01)
    plt.show()

    #m.quiver3d(X, Y, Z, U, V, W)





A = [[1,2,3] ,
     [4,5,6],
     [7,8,9]]

v = [ 7,-8,3 ]

plot(A,v)

print 'Transformacion'
for fila in A:
     print(fila)

print 'vector', v

x = cramer(A,v) ; print 'solucion x :' , x








# https://stackoverflow.com/questions/28952946/how-to-replace-one-column-by-a-value-in-a-numpy-array
# https://www.geeksforgeeks.org/transpose-matrix-single-line-python/
# https://stackoverflow.com/questions/47319238/python-plot-3d-vectors