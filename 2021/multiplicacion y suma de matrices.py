# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11ujc2WQWhr-vTmUF-9LcWzmN9-KrZGvc
"""

# adicion y multiplicacion de matrices 

# suma 
A = [[1,2,3],
     [4,5,6],
     [7,8,9]]
B = [[9,8,7],
     [6,5,4],
     [3,2,1]]


def suma(A,B):
  filasA = len(A) ; filasB = len(B)
  colA = len(A[0]) ; colB = len(B[0])

  if filasA * colA == filasB * colB:

    C = []   # creanto la matrix 
    for i in range(filasA):
      C.append([])
      for j in range(colA):
        C[i].append(0)
    print(C)

    # operando dentro dE LA MATRIX
    for i in range(0, filasA):
      for j in range(0 , colA):
        C[i][j] = (A[i][j] + B[i][j] )  # lo amo no tuve que usar appends
        

  return C

print(suma(A,B))
#________________________________________________________________________________________

# multiplicacion 
A = [[1,2],
     [3,4]]

B = [[4,3],
     [2,1]]

def multiplicacion(A,B):
  filasA = len(A) ; filasB = len(B)
  colA = len(A[0]) ; colB = len(B[0])
  
  # (mxn)*(nxp)  el numero de columnas de A debe ser igial al numero de filas de B y se acaba con una matriz mxp
  if colA == filasB:
     C = []   # creanto la matrix 
     for i in range(filasA):
       C.append([])
       for j in range(colB):
         C[i].append(0)
     print(C)
     filasC = len(C) ; colC = len(C[0])
     


     for i in range(0, filasC):
       for j in range(0 , colC):
         C[i][j] = A[i][colA - 1] + B[filasB - 1][j]
    
  else : 
    print("dimensiones no aceptadas")
  return C


multiplicacion(A,B)


# http://es.onlinemschool.com/math/assistance/matrix/multiply/
#mostrar que A*B != B*A