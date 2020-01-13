# Determinacion-de-mayor-entero-estricto-de-3-numeros
#El siguiente programa determinara el mayor entero estricto de entre 3 números sin el uso de operadores logico

A=int(input("Introduce el numero A:"))

B=int(input("Introduce el  numero B:"))

C=int(input("Introduce el  numero C:"))
#################################################################################################
#D=0
#if A>0:
	#D=1
#E=0	
#if B>0:
    #E=1
#F=0
#if C>0:
    #F=1
#if D+E+F==3:
   #print("Los numero introducidos son correctos")
##################################################################################################   

while A<=0:
	A=int(input("Introduce el primer numero:"))

while B<=0:
  
	B=int(input("Introduce el segundo numero:"))

while C<=0:
  
  C=int(input("Introduce el tercer numero:"))
   	

print("Los numero introducidos son correctos")

#A-B=U

#A-C=K

#B-C=L

i=1

if A-B>0:
  i=i+1

if A-C>0:
  i=i+1

if i==3:
  print("A es el mas grande")
else:
  t=1
  if A-B<0:
    t=t+1

  if B-C>0:
    t=t+1 

  if t==3:
    print("B es el mas grande")
  else:
    r=1

    if A-C<0:
      r=r+1

    if B-C<0:
      r=r+1 

    if r==3:
      print("C es el mas grande")


anio=int(input("Introduzca el año:"))

if isinstance((anio),int)==True:
  print("Hola")
  
contador=0  

if isinstance((anio/4),int)==True:
  contador==contador+1

if isinstance((anio/100),int)==True:
  contador==contador+1

if isinstance((anio/400),int)==True:
  contador==contador+1

print(contador)

if contador==1 or contador==3:
  print("El año no es bisiesto")  
else:
  print("El año es bisiesto")       

   
    


 













      











