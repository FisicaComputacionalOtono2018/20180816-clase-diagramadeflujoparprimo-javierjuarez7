#Javier Juarez Jimenez
#17/ago/2018
#Programa que verifica si un numero es primo o no usando for y funciones

def isPrimeFor(num):      #True es primo False no es primo
	flag=True
	if num==1:
		flag=False
	if num==2:
		flag=True
	if num==3:
		flag=True
	if num==4:
		flag=False
	if num>4:
		for i in range (2, num/2):
			if num%i==0:
				flag=False
				break
	return flag

num=input("Introduce un numero: ")
if isPrimeFor(num):
	print("El numero es primo")
else:
	print("EL numero no es primo")
		
