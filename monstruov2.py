#Javier Juarez Jimenez
#16/08/18
s=12
p=input("Teclea un número: ")
while p%2==0:
    p=p+1
    a=2
    while a<p:
        r=p%a
        b=1
        if r!=0:  #si el residuo da cero en algun momento, no es primo, no hace el if y se queda b=1
            a=a+1
            b=0
    while b==1:  #no es primo
        p=p+2
        break
    while b==0: # es primo
        if p<s:
            s=s-p
            p=p+2
        else:
            s=s-1
            if S==0:
                print(P)
            else:
                p=p+2
while p%2!=0:
      a=2
    while a<p:
        r=p%a
        b=1
        if r!=0:  #si el residuo da cero en algun momento, no es primo, no hace el if y se queda b=1
            a=a+1
            b=0
    while b==1:  #no es primo
        p=p+2
        break
    while b==0: # es primo
        if p<s:
            s=s-p
            p=p+2
        else:
            s=s-1
            if S==0:
                print(P)
            else:
                p=p+2
    
        
    
