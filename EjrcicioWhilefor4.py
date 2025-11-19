print("1=Sumar")
print("2=Restar")
print("3=Salir")
c=0
while c!=3:
    a=int(input("Ingrese el primer número "))
    b=int(input("Ingrese el segundo número "))
    c=int(input("Elige 1, 2 o 3: "))
    if c==1:
        d=a+b
        print("La suma de los dos números es", d)
    elif c==2:
        d=a-b
        print("La resta de los dos números es", d)
    a=0
    b=0
print("Finalización")