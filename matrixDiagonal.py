import  numpy as np
A = [[1, 4, 5] ,
     [-5, 8, 9],
     [4, 3 , 2]]

B = [[2, 4, 5 , 6] ,
     [-5, 8, 9 , 4],
     [4, 3 , 2 , 2],
     [2, 3 , 2 , 1]]

C = [[2, 4, 5 , 6 , 3],
     [-5, 8, 9 , 4 ,2],
     [4, 3 , 2 , 2 ,1],
     [-5, 8, 9 , 4 ,2],
     [2, 3 , 2 , 1, 3]]

# print A[0] , A[1] , A[2]
# print A[-1] , A[-2]
#
# print A[0][0] ,  A[0][1]   # A[1][2])  3rd elemento de 2 nda fila   A[fila] [columna]
# print "4" , A[0][:] ,  A[::][::1]
#
# print A[::1] , A[::-1]

# obtener columnas

columnaA = [];        # empty list
for j in A:
  columnaA.append(j[0])
print  " columna " , columnaA


# encontrar dimensiones de la matriz

dimensionFila  = len( A[0] ) ; dimensionColumna =  len( columnaA )
print " es una matriz: ", dimensionFila , "x", dimensionColumna


#_______________________ diagonal principal

diagonalPrincipal = []

for i in range( len(A)):
    for j in range( len(A)):
        if i == j :
            diagonalPrincipal.append( A[i][j] )
        else:
            diagonalPrincipal.append( " * ")

np.reshape(diagonalPrincipal,(dimensionFila, dimensionColumna))
print "original: " , A
print " diagonal principal: " , diagonalPrincipal

#_______________________ diagonal secundaria
# se asume cuadrada
n = dimensionColumna + 1

# encontrar sumandos


enterosBase = [1,2,3,4,5,6,7,8,9]

# print range( 1, len(enterosBase) + 1)

sumandoA = []
sumandoB = []
# for i in enterosBase:
#     if i <= n :
#         for j in enterosBase:
#             if j <= n:
#                 if i + j == n:
#                     sumandoA.append(i)
#                     sumandoB.append(j)
#
#     else:
#         break


# i = 1
# while i <= n:
#     j = 1
#     sumandoA.append(i)
#     while j <= n:
#         if i + j == n:
#             sumandoB.append(j)
#             j = j + 1
#     i += 1
#
#
# print sumandoA , sumandoB

# _________________________ sumandos a lo fibonacho style
# a, b = 1, 1
# i = 1
#
# while i <= n :
#     a = b
#     b = a + 1
#     if a + b == n :
#         sumandoA.append(a)
#         sumandoB.append(b)
#     i = i + 1
#
# print sumandoA , sumandoB


diagonalSecundaria = []
orden = dimensionFila   # se asume cuadrada
for i in range( len(A)):
    for j in range( len(A)):
        if i + j == orden - 1 :
            diagonalSecundaria.append( A[i][j] )
        else:
            diagonalSecundaria.append( " * ")

print "original: " , A
print " diagonal secundaria : " , diagonalSecundaria


#______ matriz transpuesta ________________

transposedMatrix = []
print "______________________________________"
for i in range( len(A)):
   for j in range( len(A)):
       transposedMatrix.append( A[j][i] )

print "original: " , A
print " transpuesta: " , transposedMatrix






 # https://www.programiz.com/python-programming/matrix
 # https://www.mathworks.com/help/matlab/math/reshaping-and-rearranging-arrays.html;jsessionid=6d12af4a3fefde424eb5440f93f9
 # https://www.mathworks.com/help/matlab/ref/reshape.html
 # https://www.youtube.com/watch?v=Mz6-R53Yz2Q