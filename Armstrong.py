import math

num = float(input("Ingrese el numero entero positivo: "))
cont=0
sum=0
a=num
b=num
c=0
d=0

while num>=1:
    num=num/10
    cont+=1


while a>0:
    c=a%10
    a=math.trunc(a/10)
    d=c**cont
    sum+=d
if sum==b:
        print("Si es un numero de Armstrong")
else:
        print("No es un número de Armstrong")






