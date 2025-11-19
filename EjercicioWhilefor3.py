a=int(input("Ingrese un número entero "))-1
b=1
c=0
while a!=0 and b!=0:
    if a<0 or b<0:
        b=0
    else:
        a+=b
    b=int(input("Ingrese otro número "))
print("La suma de los números es", a)
