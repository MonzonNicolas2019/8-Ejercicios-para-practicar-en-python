#Ejercicio 6

tipo_de_video=input("Introduce el tipo de video:")
dias=int(input("Introduce la cantidad de dias desfasados:"))
pago=0

def funcion(tipo_de_video,dias):
	if tipo_de_video=="Dibujo" and dias>0:
		global pago
		pago=1+0.5*(dias-1)

	if tipo_de_video=="Estrenos" and dias>0:
		pago=1+0.5*(dias-1)


	if tipo_de_video=="Otros" and dias>0:
		pago=1+0.5*(dias-1)

	if dias<0:
		pago=-1

	if (tipo_de_video!="Otros" or tipo_de_video!="Estrenos" or tipo_de_video!="Dibujo") and dias>0:
		print("El tipo de video introducido es incorrecto")		


	print(pago)	

funcion(tipo_de_video,dias)	







