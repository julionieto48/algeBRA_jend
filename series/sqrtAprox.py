import math
import random
area = 34
cantidadDivisores = 0
for x in range(1,area + 1):  # secuencia hasta dicho numero
    if area % x == 0:      # si la division es exacta
        cantidadDivisores += 1

#divisores = [] * cantidadDivisores
divs = []
for x in range(1, area + 1):  # secuencia hasta dicho numero
    if area % x == 0:  # si la division es exacta
        divs.append(x)
        divisorTrue = x
    #divisores[].append(divisorTrue)


# revDivs = divs[::-1]
revDivs = [0]*len(divs)    # divs = [1, 2, 4, 8, 16] len(divs ) = 5

i = len(revDivs) - 1  #  apunta a iltimo elemnto 0 1 2 3 4 osea  = 4
while i >= 0 :
    revDivs.append(divs[i])
    i -= 1

#quitar ceros
# print revDivs, len(revDivs)
# for i in range(0,6):
#     if revDivs[i] == 0 :
#         revDivs.pop(i)
# print revDivs

while 0 in revDivs: revDivs.remove(0)
#_________________________________________________________________
# en este punto tengo dos listas de divisores una e sla version reversada... aora debo escoger por posiciones
pos =  random.randint(1,len(divs)-1)          #pos = 1              # puede ser random entre 1 len(divs) -1
print pos
ladoA = float(divs[pos]) ; ladoB = float(revDivs[pos])   # evito escoger lado donde divido en 1 osea pos  = 0
iter = 6
i = 0

while i <= iter:

    ladoA = (ladoA + ladoB) / 2
    ladoB = area / ladoA

    i += 1
print ladoA

# evaluar hasta que sean iguales si es perfecto ;)
# while ladoA != ladoB:
#
#     ladoA = (ladoA + ladoB) / 2
#     ladoB = area / ladoA
#     i += 1
#
# print ladoA , 'num iteraciones :' , i

print math.sqrt(area)

# https://thispointer.com/python-different-ways-to-iterate-over-a-list-in-reverse-order/
# https://www.geeksforgeeks.org/python-reversing-list/
# https://stackoverflow.com/questions/1157106/remove-all-occurrences-of-a-value-from-a-list




