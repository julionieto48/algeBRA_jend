# -*- coding: utf-8 -*-
"""Untitled15.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lX536EmR_VPWe5NHokgDqe9cVknGG6oZ
"""



def transpose(x):

  transpuesta = []
  for i in range(len(x)):
    for j in range(i,len(x)):
      x[i][j] = x[j][i]
      #transpuesta.append(x[i][j])
  return x


def transposeA(x):

  transpuesta = []
  for i in range(len(x)):
    for j in range(i,len(x)):
       x[i][j],x[j][i] = x[j][i],x[i][j]
  return x

def reverseMatrix(x):
  N = len(x)
  for i in range(N/2):
    for j in range(N):
      x[j][i],x[j][N-1-i] = x[j][N-1-i],x[j][1]
  return x


m = [1,2,3,4,5]
mm = [[1,2,3,4,5],
      [1,2,3,4,5]]

a = transpose(mm)
print(a)

# https://www.geeksforgeeks.org/python-program-to-find-transpose-of-a-matrix/?ref=rp

def oneDim(x):
  flat = []
  for i in x: 
    for j in i:
      flat.append(j)
      # print(j)
  return flat




mm = [[1,2,3,4,5],
      [1,2,3,4,5]]

a = oneDim(mm)
print(a)

# reshape
l = [i for i in range(1,5)] # crear nums de 1  a 22

ll = [[1,2],
      [3,4]]
filas = len(ll)
columnas = len(ll[0])

#dimensiones deseadas

f = 1 ; c = 4
#output = []  # seria como int[][] out = new int[f][c]
output = [ [0 for x in range( f )] for y in range( c ) ]  


# debe tener la misma cantidad de elementos 
if (filas * columnas) != (f * c):
  print('no es vlaido')

else:
  numColumna = 0 ; numFila = 0
  # traversive para respetar el orden
  for i in range(0,filas-1):
    
    for j in range(0,columnas-1):
      output[numFila][numColumna] = ll[i][j] 
      numColumna = numColumna + 1  # voy a llenar columnas en este caso ... [,,,]
      if numColumna == c: # cuando alcanzo el numero deseado de columnas
        numColumna = 0
        numeroFila += 1  # empiezo a llenar filas

print(output)
 




# https://stackoverflow.com/questions/12575421/convert-a-1d-array-to-a-2d-array-in-numpy
