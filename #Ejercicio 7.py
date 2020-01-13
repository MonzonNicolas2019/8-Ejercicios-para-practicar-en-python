#Ejercicio 7

Numero_de_paginas=int(input("Introduce la cantidad de paginas que tiene el libro:"))

Costo=0

def Costo(Numero_de_paginas):
	if Numero_de_paginas<=300:
		Costo=5+Numero_de_paginas*0.02

	if 300<Numero_de_paginas<=600:
		Costo=8+Numero_de_paginas*0.02

	if Numero_de_paginas>600:
		Costo=16+Numero_de_paginas*0.02

	print(Costo)

Costo(Numero_de_paginas)	
				



