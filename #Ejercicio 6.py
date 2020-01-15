#Ejercicio 6

tipo_de_video=input("Introduce el tipo de video:")
dias=int(input("Introduce la cantidad de dias desfasados:"))
pago=0

def funcion(tipo_de_video,dias):
	global pago
	if tipo_de_video=="Dibujo" and dias>0:
		pago = 2

	if tipo_de_video=="Estrenos" and dias>0:
		pago = 3

	if tipo_de_video=="Otros" and dias>0:
		pago = 2.5

	if dias >= 1:
		pago += 1 + 0.5*(dias-1)

	#El siguiente If lo podes poner mas arriba para que programa se termine si llega a ser el caso y no haga nada, porque los if tambien tienen coste de ejecucion
	if (tipo_de_video != "Otros" and tipo_de_video != "Estrenos" and tipo_de_video!="Dibujo") or dias < 0:
		print("El tipo de video introducido es incorrecto o la cantidad de dias es incorrecta")
		return -1 #No siempre, pero para algunos informaticos mas a la antigua, derivando de C++, ponen return -1 cuando el programa ejecuto algo incorrecto

	print("Pago: " + pago)
	print("La cantidad de dias desfasados son " + (dias - 1))

funcion(tipo_de_video,dias)	







