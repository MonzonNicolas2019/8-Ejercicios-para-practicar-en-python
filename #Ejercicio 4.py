#Determinacion de fecha gregoriana o no.py
#El siguiente programa es para determinar si cierta fecha introducida corresponde a el calendario gregoriano o no

dia=int(input("Introducir el dia de la fecha:"))
mes=int(input("Introducir el mes de la fecha:"))
anio=int(input("Introducir el año de la fecha:"))

		

def esBisiesto(a):
	
	contador=0
	
	if a % 4 == 0:
		contador++
	
	if a % 100 == 0:
		contador++
	
	if a % 400 == 0:
		contador++
	
	if contador==0 or contador==2:
		return False
	else:
		return True

i=1	

if not esBisiesto(anio):

	if 0<mes<=12:
	    
		if (mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12) and dia<=31:
			print("La fecha elegida corresponde a el calendario gregoriano")
		else:
			i=i+1#Probe con el i++ pero no funciono
		if  (mes==4 or mes==6 or mes==9 or mes==11) and dia<=30:
			print("La fecha elegida corresponde a el calendario gregoriano")
		else:
			i=i+1	
		if 	(mes==2 )and dia<=28:
			print("La fecha elegida corresponde a el calendario gregoriano")
		else:
			i=i+1
				

		if i==4:
			print("El dia introducio es incorrecto")	
	else:
		print("El mes introducido no es correcto")
else: #Equivale a que sea bisiesto
	if 0<mes<=12:
	    
		if (mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12) and dia<=31:
			print("La fecha elegida corresponde a el calendario gregoriano")
		else:
			i=i+1#Probe con el i++ pero no funciono
		if  (mes==4 or mes==6 or mes==9 or mes==11) and dia<=30:
			print("La fecha elegida corresponde a el calendario gregoriano")
		else:
			i=i+1	
		if 	(mes==2 )and dia<=29:
			print("La fecha elegida corresponde a el calendario gregoriano")
		else:
			i=i+1				

		if i==4:
			print("El dia introducio es incorrecto")	
	else:
		print("El mes introducido no es correcto")
