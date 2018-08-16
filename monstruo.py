#Javier Juarez Jimenez
#16-08-18
#Programa que hace muchas cosas

S=12
p=input("Introduce un numero: ")
if p%2==0:	
	p=p+1
else:
	a=2
	b=1
	while a<p:
		r=p%a
		if r==0:
			break
			p=p+2
		else:
			a=a+1
		if p<5:
			S=S-p
			p=p+2
		else:
			S=S-1
		if S==0:
			print(p)
			break
		else:
			p=p+2

	
	
	

