

deltaMes = 1
porcentaje = 12
valorInicial = 100

#jajaja se usaorn dos formas d eprogramar una con cambiios de estado la cual tiene mas lineas de code

def valorPorPorcentaje( porcentajeDeterminado, valorInicial):
    x = valorInicial * porcentajeDeterminado / 100  # es el valor en dinero correspondiente al porcentaje establecido
    return x

def generadorAhorro( periodoTiempo, porcentajeDeterminado, valorInicial):

    actualDeltaM = 0
    ultimoDeltaM = valorPorPorcentaje(porcentajeDeterminado, valorInicial)

    tiempoReferencia = 12                                    # 12 meses
    listaMes = [] ; listaValores = [] ; mes = 0

    for i in range(tiempoReferencia):  # va del 0 al 11

        valor = valorInicial + ultimoDeltaM
        actualDeltaM = valorPorPorcentaje(porcentajeDeterminado, valor)

        mes =  mes + periodoTiempo

        listaMes.append(mes) ; listaValores.append(valor)

        ultimoDeltaM = actualDeltaM
        valorInicial = valor


    print listaValores , listaMes




#generadorAhorro(deltaMes,porcentaje,valorInicial)




#
def generadorAhorroVersion( periodoTiempo, porcentajeDeterminado, valor):

    # deltaM = valorPorPorcentaje(porcentajeDeterminado , valor )  # es el valor monetario que aumentara en el tiempo

    tiempoReferencia = 12                                    # 12 meses de evaluacion
    listaMes = [] ; listaValores = [] ; mes = 0

    for i in range(tiempoReferencia ):
        deltaM = valorPorPorcentaje(porcentajeDeterminado , valor )  # es el valor monetario que aumentara en el tiempo
        valor = valor + deltaM
        mes =  mes + periodoTiempo

        listaMes.append(mes) ; listaValores.append(valor)


    print listaValores , listaMes

#generadorAhorroVersion(deltaMes,porcentaje,valorInicial)


# convertir anos en meses


def anotoMes(ano):
    return  ano * 12
#m = anotoMes(24) ; print m , "meses"

#____________________________________________________-
# que sucede al cambiar valores de tiempo y taza de interes

initialValue = 100
bancoA = [12 , anotoMes(1) ]
bancoB = [1  , 1 ]
bancoC = [6  , 6 ]

generadorAhorroVersion(bancoA[1], bancoA[0], initialValue)
generadorAhorroVersion(bancoB[1], bancoB[0], initialValue)
generadorAhorroVersion(bancoC[1], bancoC[0], initialValue)
