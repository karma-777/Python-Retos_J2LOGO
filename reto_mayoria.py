import random
def mayoria_absoluta(votos):
	ganador = ""
	for x in lista:
		num = lista.count(x)
		if num > mitad:
			ganador = "Voto -> " + str(x)+" <- " + "apareció " + str(num) + " Veces"

	if ganador != "":
		print(ganador)
	else:
		print("None")

lista = []

while True:
    r = str(input("Votos: "))
    if r == "":
        break
    else:
        lista.append(r)

'''
for n in range(10):
	n = random.randint(1,5)
	lista.append(n)
'''
print(str(lista))

counti = {}
mitad = int(len(lista))/2

mayoria_absoluta(lista)