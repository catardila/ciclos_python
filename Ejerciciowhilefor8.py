a=int(input("Ingrese un número positivo: "))+1
b=1
c=0
d=0
for i in range(1, a):
    d+=1
    b=1/d
    c+=b
print("La sumatoria de los números es:", c)