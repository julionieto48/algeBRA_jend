# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/113QtH4VHLepJCe3bJbAoqR-_itxST4nW
"""

# Matriz inversa
# A *A-1 = I  /A debe ser cuadrada
# proof : (AB)-1 = B-1 *A-1   //// (At)-1  = (A-1)T

a = [['a','b'],['c','d']]
b = [['x1','x2'],['y1','y2']]  # incognitas  b va a ser la inversa

# si es la inversa va resultar en la matriz identidad ... entonces crear la matriz identidad
aRows = len(a) ; aCol = len(a[0])
bRows = len(b) ; bCol = len(b[0])
# new dim

if aCol == bRows :
   fila = aRows ; col = bCol
identidad = []
for i in range(0,fila):
  identidad.append([])
  for j in range(0,col):
    if i == j :
      identidad[i].append(1)
    else:
      identidad[i].append(0)

c = []
for j in range(0,fila):
  c.append([0]*col)

for i in range(len(a)): # iterar sobre las filas de x
  for j in range(len(b[0])):
    #print(i,j)
    for k in range(len(b)): # iterar sobre las filas de b 
      #print(i,j,k)
      c[i][j] += a[i][k] + b[k][j]