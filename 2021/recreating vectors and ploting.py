# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uNN6N7cuja1IkxSxWgZYJhGZ8sGpTabw
"""

import numpy as np
import matplotlib.pyplot as plt



plt.quiver([0, 0], [0, 0], [1, 0], [0, 1,])



plt.xlim(-5, 5) , plt.ylim(-5, 5)
plt.grid(); plt.show()

#_____________________________________________________________________________________
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_xlim3d(-3, 3)
ax.set_ylim3d(-3, 3)
ax.set_zlim3d(-3, 3)
#ax.quiver(0, 0, 0, 1, 1, 1, length = 0.5, normalize = True)


X = [0,0,0] ; Y = [0,0,0] ; Z = X = [0,0,0]

escalonada =         [[1,5,3],
                      [0,1,2],
                      [0,0,1]] 

A = escalonadaReducida[:][0]
B = escalonadaReducida[:][1]
C = escalonadaReducida[:][2]

ax.quiver(X,Y,Z,A,B,C)


plt.grid(); plt.show()

#_____________________________________________________________________________________
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_xlim3d(-3, 3)
ax.set_ylim3d(-3, 3)
ax.set_zlim3d(-3, 3)
#ax.quiver(0, 0, 0, 1, 1, 1, length = 0.5, normalize = True)


X = [0,0,0,0] ; Y = [0,0,0,0] ; Z = X = [0,0,0,0]

m =         [[ 1, 5,-1,-2],
             [ 2,-1, 2, 5],
             [-1, 2, 2, 1] ] 

A = m[:][0]
B = m[:][1]
C = m[:][2]

ax.quiver(X,Y,Z,A,B,C)

plt.grid(); plt.show()

filas = len(m)
column = len(m[0])

print(filas,column)
print(m)

# froward elimination 

for i in range(column-1): # i = range(column-1) -> 0 1 2  j = print(i+1,filas) -> 13 13 23
  for j in range(i+1,filas):
    #print(m[j][:])              # iterar sobre las filas m[j][:] -> [2, -1, 2, 5] [-1, 2, 2, 1] [-1, 2, 2, 1]
    #print(m[j][i] , m[i][i])    # 2 1    -1 1    2 -1 
    #print(m[i][:] , m[j][:])    # [1, 5, -1, -2] [2, -1, 2, 5] // [1, 5, -1, -2] [-1, 2, 2, 1] // [2, -1, 2, 5] [-1, 2, 2, 1]

    m[j][:] =  float(-1( m[j][i] / m[i][i] ) * ( m[i][:] + m[j][:]) )

a = [1,2,3,4]
b = [1,2,3,4]

# print len(b) 4
filas = len(a)
columnas = len(b)


matrizP = []


for i in range(filas):
    matrizP.append([])
    for j in range(columnas):
        valor = [a[i] ,b[j] ]
        matrizP[i].append( valor )

print(matrizP) 

for i in range(filas):
    for j in range(columnas):
        if i <= j :
          matrizP[i][j] = 5
            
        else:
          matrizP[i][j] = 0

print (matrizP)

