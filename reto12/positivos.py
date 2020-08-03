'''
Escribe una función ordena_positivos(lista), que dada una lista de números enteros, 
devuelva una nueva lista con los números positivos ordenados de menor a mayor, y mantenga 
los números negativos en la misma posición que la lista original.
'''

def ordena_positivos(lista):
    newlista = []
    for x in range(len(lista)):
        if lista[x] > 0:
            newlista.append(lista[x])
    newlista.sort()
    for x in range(len(lista)):
        if lista[x] < 0:
            newlista.insert(x,lista[x])
    print(newlista)

    

ordena_positivos()
