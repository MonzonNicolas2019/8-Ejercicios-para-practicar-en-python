#Nueva idea

import math

dia=int(input("Introducir el dia de la fecha:"))
mes=int(input("Introducir el mes de la fecha:"))
anio=int(input("Introducir el año de la fecha:"))
dias_a_sumar=int(input("Introduce una cantidad de dias a sumar:"))	

def fecha_gregoriana(dia,mes,anio):
	contador=0
	if anio%4==0:
		contador=contador+1
	if anio%100==0:
		contador=contador+1

	if anio%400==0:
		contador=contador+1

	if contador==0 or contador==2:
		print("El año no es bisiesto")	
	else:
		print("El año es bisiesto")

fecha_gregoriana(dia,mes,anio)

lista3=(31,59,90,120,151,181,212,243,273,304,334,365)
lista4=(31,60,91,121,152,182,213,244,274,305,335,366)

dian=0
mesn=0
anion=anio
r=0
c=0
d=math.floor(dias_a_sumar/364)
k=list(range(1,d+1))

if contador==0 or contador==2:
	if dias+lista3[mes+1]+dias_a_sumar-365>0:
		anion=anion+1
		c=dias_a_sumar-(365-dias+lista3[mes+1])
		for i in k:
			if fecha_gregoriana_incial(0,0,anion):
				dian=0
				if contador==0 or contador==2:
 					r=r+365	
 					if dias_a_sumar-c+r<365:
 						break			
 					if c-r>0:
	 					anio=anion+1
		 			else:
	 					anion=anion
            	else:	
	    			r=r+366
 					if dias_a_sumar-(c+r)<365:
 						break
	 				if c-r>0:
	 					anio=anion+1
	 				else:
	 					anion=anion
    	    	
		 					
	else:
		anion=anion	
else:
	if dias+lista3[mes+1]+dias_a_sumar-366>0:
		anion=anion+1
		c=dias_a_sumar-(366-dias+lista3[mes+1])
		for i in k:
			if fecha_gregoriana_incial(0,0,anion):
				if contador==0 or contador==2:
	 				r=r+365
 					if dias_a_sumar-(c+r)<365:
 						break	
	 				if c-r>0:
		 				anio=anion+1
		 			else:
		 			anionion=anion	
	    		else:
	    			r=r+366
 					if dias_a_sumar-(c+r)<366:
 						break
		 			if c-r>0:
	 					anio=anion+1
	 				else:
	 					anion=anion	
	else:
		anion=anion	


u=dias_a_sumar-(c+r)


if fecha_gregoriana_incial(0,0,anion):
	if contador==0 or contador==2:
		for i in lista3:
			if i-u>0:
				mesn=lista2.index(i)
				dian=lista2[mesn]-h
				break
	else:
		for i in lista3:
			if i-u>0:
				mesn=lista2.index(i)
				dian=lista2[mesn]-h
				break

print(dian)
print(mesn)
print(anion)
