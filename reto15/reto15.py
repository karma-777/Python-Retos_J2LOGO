'''
Implementa una funciÃ³n final_comun_mayor(str1, str2), a la que se le pase como argumento dos
cadenas de caracteres y devuelva el final comÃºn a ambas mÃ¡s largo.
'''
def final_comun_mayor(str1, str2):
    str1 = ''.join(reversed(str1))
    str2 = ''.join(reversed(str2))
    comprobador = False
    cadena = ""
    for x in range(len(str1)):
        if str2[x] == str1[x]:
            cadena += str2[x]
            comprobador = True
        else:
            break
    if comprobador == True:
        cadena = ''.join(reversed(cadena))
        print(cadena)
    else:
        print("")
