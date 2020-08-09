'''
Implementa una función acumulado(lista), a la que se le pase como argumento una lista de números enteros y devuelva una lista de la suma acumulada.
Consideraciones a tener en cuenta

    Si se pasa como argumento una lista vacía ([]), la función devolverá una lista vacía.
    Imagina la siguiente lista [1, 2, 3, 4]. La función acumulado([1, 2, 3, 4]) devolverá [1, 3, 6, 10]. Como ves, cada elemento de la lista devuelta es [1, 1 + 2, 1 + 2 + 3, 1 + 2 + 3 + 4].
'''

def acumulado(lista):
    resultado = []
    contador = 1
    for n in range(len(lista)):
        suma = 0
        for x in range(contador):
            suma += lista[x]
        resultado.append(suma)
        contador += 1
    print(resultado)
        
