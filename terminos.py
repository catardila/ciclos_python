cantidadTerminos=int(input("Ingrese la cantidad de terminos a generar: "))
contadorNumero=0
termino=1

while contadorNumero <= cantidadTerminos - 1:
    termino += 2
    contadorNumero += 1
    print (termino)