import math
import matplotlib as plt

# _________________________________________________________

z = complex(2 , 3) ; w = complex( 1 , -1) ; print  z * w



# _________________________________________________________
def gradToradians(angulo):

    radian = angulo * math.pi / 180
    return radian

grados = 30 ; anguloZ = gradToradians( 30 )


# usando un sitema de coordenadas y aplicando rotacion
esquina =  complex(1 , -3)

za = complex( math.cos(  anguloZ ) , math.sin( anguloZ ) ) ; print za
laRotacion = za * esquina

print za * esquina         # aplicando la rotacion a ese detrminaod punto
complejosUsados = [esquina , za , laRotacion]


Re = [] ; Im = []
for i in range( len(complejosUsados) ):
    x = complejosUsados[i].real
    y = complejosUsados[i].imag

    Re.append(x)
    Im.append(y)

plt.scatter(Re, Im)
plt.xlabel('Re')
plt.ylabel('Im')
plt.title('Rotacion compleja')
plt.legend() ; plt.grid()
plt.show()





