# Programa-para-determinar-si-un-a-o-es-bisiesto-o-no
#El siguiente programa sirve para determinar si un año es o fue bisiesto o no
anio=int(input("Introduzca el año:"))


contador=0


if isinstance((anio/4),int)==True:
	print("Hola")
else:
	print("Chau")	

print(contador)	

if isinstance((anio/4),int)==True:
	contador=contador+1
	print("h")

if isinstance((anio/100),int)==True:
	contador=contador+1
	print("J")

if isinstance((anio/400),int)==True:
	contador=contador+1
	print("L")

print(contador)

if contador==1 or contador==3:
	print("El año no es bisiesto")	
else:
	print("El año es bisiesto")			



