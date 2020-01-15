#Ejercicio 8 

Dinero_a_retirar=int(input("Introduce una cantidad de dinero a retirar:"))

def Billetes(Dinero_a_retirar):
	c=0
	contador=0
	Cant100=0
	Cant50=0
	Cant10=0
	Cant5=0
	Cant1=0
	for i in list(str(Dinero_a_retirar)): #Aca queda mas prolijo si reescribis parte del programa usando un while Dinero_a_retirar > 0
		
		contador=contador+1
		c=len(list(str(Dinero_a_retirar)))-contador+1
		if c-2>0:
			Cant100=Cant100+(int(i)*10**(c-1))/100	
		if c-2==0:
			if int(i)>=5:
				Cant50=1
				Cant10=(int(i)-5)*10
				print("La cantidad de billetes de 50 es" + str(Cant50))
				print("La cantidad de billetes de 10 es" + str(Cant10))
			else:
				Cant10=int(i)*10
				print("La cantidad de billetes de 50 es" + str(Cant50))
				print("La cantidad de billetes de 10 es" + str(Cant10))
				
		
		if c-2==-1:
			if int(i)>=5:
				Cant5=1
				Cant1=int(i)-5
				print("La cantidad de billetes de 5 es" + str(Cant5))
				print("La cantidad de billetes de 1 es" + str(Cant1))
			else:
				Cant1=int(i)
				print("La cantidad de billetes de 5 es" + str(Cant5))
				print("La cantidad de billetes de 1 es" + str(Cant1))
	print("La cantidad de billetes de 100 es" + str(Cant100))			


Billetes(Dinero_a_retirar)		
		
