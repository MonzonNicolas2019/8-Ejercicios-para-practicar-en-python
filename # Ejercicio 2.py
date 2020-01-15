# Determinacion-de-mayor-entero-estricto-de-3-numeros
#El siguiente programa determinara el mayor entero estricto de entre 3 números sin el uso de operadores logicos

A=int(input("Introduce el numero A:"))
B=int(input("Introduce el numero B:"))
C=int(input("Introduce el numero C:"))  

while A<=0:#No salia poner un print debajo de este y de los otros , porque?
	A=int(input("Introduce el numero A:"))

while B<=0:
	B=int(input("Introduce el numero B:"))

while C<=0:
	C=int(input("Introduce el numero C:"))
   	
print("Los numero introducidos son correctos")

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
