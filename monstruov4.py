#Javier Juarez Jimenez
#16/08/18
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

s=12
p=input("Teclea un numero: ")
while s!=0:
	if p%2==0:
		p=p+1
	while not isPrimeFor(p):
		p=p+2
		if p%2==0:
			p=p+1
	while p<s:
		s=s-p
		p=p+2
		while not isPrimeFor(p):
			p=p+2
			if p%2==0:
				p=p+1
	s=s-1
	if s!=0:
		p=p+2
print(p)
		
