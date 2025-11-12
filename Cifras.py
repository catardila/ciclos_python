import math

num = int(input("Ingrese un numero entero"))
sum = 0
contador = 0
hola = num

while hola > 0:
    if hola > 0:
        cifra = hola%10
        sum = sum + cifra
        contador = contador + 1
        hola = math.trunc(hola/10)
    else:
        print("El numero no es positivo")
        hola = 0

if num > 0:
    print("El numero es positivo")
    print(f"tiene {contador} cifras")
    print(f"La suma de sus cifras es: {sum}")


    


