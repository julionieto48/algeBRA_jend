
def tijeraMetodo(b,c):
    divisores = []
    cocientes = []

    for entero in range(1, c + 1):
        if c % entero == 0:               # cumplir con el criterio de divisibilidad del coeficiente c
            divisores.append(entero)      # colocar en una lista los divisors de dicho divisor

            cocienteI = c / entero        # cociente  = dividendo / divisor
            cocientes.append(cocienteI)   # guardar en lista los resultados o cociente
    print (divisores)
    print (cocientes)

    if c > 0 :                            # si c e spositivo
        operacionA = []                   # operacion a es (r + s )
        for i in range(len(divisores)):  # recorrer el tamano de dicho arreglo ya que coincide en tamano divisores y cocientes
            operacionAi = (divisores[i] + cocientes[i])
            operacionA.append(operacionAi)
        print operacionA

        indexA = linBusqueda(b , operacionA)      # indices donde se encuentra el numero b
        print ("en estos indices esta el num b despues d ela operacion ", indexA)
        solPositivos = []

        if len( indexA) > 0 :                     # si la lista de indices no esta len( indexA) > 0 / vacia len( indexA) == 0  -> if not a

            for i in range(len(indexA)):

                solPositivos.append(  [ divisores[indexA[i]] , cocientes[indexA[i]] ] )


        # la opcion en cuando ambos son negativos ya que - y - = +
        operacionB = []
        for i in range(len(divisores)):  # recorrer el tamano de dicho arreglo ya que coincide en tamano divisores y cocientes
            operacionBi = (- divisores[i] - cocientes[i])
            operacionB.append(operacionBi)
        print operacionB

        indexB = linBusqueda(b , operacionB)      # indices donde se encuentra el numero b

        solPositivos = []
        if len( indexB) > 0 :                     # si la lista de indices no esta len( indexA) > 0 / vacia len( indexA) == 0  -> if not a

            for i in range(len(indexB)):

                solPositivos.append(  [ divisores[indexB[i]] , cocientes[indexB[i]] ] )

        print (solPositivos)





    elif c < 0 :                                    # si c e spositivo
        operacionA = []  # operacion a es (- r + s )

    else:
        print " el coeficiente c no puede ser cero"


def linBusqueda(numeroBuscar , lista):
    indicesEncontrados = []
    for  i in range( len(lista)):
        if lista[i] == numeroBuscar :
            indicesEncontrados.append(i) # si se encuentra el numero retornar la posicion en la que se encontro
    return  indicesEncontrados



tijeraMetodo(9,20)



# https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?codigo=32
# https://code.i-harness.com/es/q/d109
# https://www.tutorialpython.com/listas-en-python/
# https://www.learnbyexample.org/python-nested-list/