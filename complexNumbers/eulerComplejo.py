from __future__ import division


# serie x ^n / n!

tetha = []
for i in range(0,5):
    tetha.append(i)

print tetha


def factorialRecurs( numero ):
    if numero == 1:
        return 1
    else:
        return numero * factorialRecurs(numero - 1)

def factorial( numero ):
    elFactorial = 1
    for i in range(1, numero):
        elFactorial = elFactorial * i
    return elFactorial



# definir funcion exponencial
def exp( x ):
    orden = 10
    return sum( [x ** n / factorial(n)
                for n in range(1 , orden) ])  # ojo va desde 1 pq si es desde cero ccontaria le factorial de cero
print exp(3)



#__________________________________
# para mas valores de theta

exps = []
for i in range(len(tetha)):
    exps.append(exp(tetha[i]))

print exps
