import sympy

sympy.init_printing()              # definicion simbolica
x,y = sympy.symbols('x,y')

#P1 = input("Primer Polinomio: ")
pUno = 7*x**3 + 2*x**2 + x - 7
#P2 = input("Segundo Polinomio: ")
pDos = x**2 + 3
print("\n")


polinomioUno = sympy.Poly(pUno)
polinomioDos = sympy.Poly(pDos)

# funciones de las operaciones
def mult(p1, p2):
	return p1 * p2

def suma(p1, p2):
	return p1 + p2

def res(p1, p2):
	return p1 - p2

def div(p1, p2):
	return p1 / p2

resultMult = mult(polinomioUno, polinomioDos)
resultSuma = suma(polinomioUno, polinomioDos)
resultDiv = div(polinomioUno, polinomioDos)
resultRes = res(polinomioUno, polinomioDos)

print("Resultado: ", resultMult)