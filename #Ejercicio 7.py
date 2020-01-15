#Ejercicio 7

numero_de_paginas=int(input("Introduce la cantidad de paginas que tiene el libro:"))

costo=0

def calcularCosto(numero_de_paginas):
	if Numero_de_paginas<=300:
		costo=5+numero_de_paginas*0.02

	if 300<Numero_de_paginas<=600:
		costo=8+numero_de_paginas*0.02

	if Numero_de_paginas>600:
		costo=16+numero_de_paginas*0.02

	print(costo)

calcularCosto(numero_de_paginas)
