cantidadEstudiantes=float(input("Ingrese la cantidad de estudiantes: "))
contadorEstudiantes = 0
aprobaron = 0
reprobaron = 0
sumaDefinitiva = 0
notaDefinitiva = 0


while (contadorEstudiantes<cantidadEstudiantes):
    codigoEstudiantes = str(input("Ingrese el codigo del estudiante: "))
    notaDefinitiva = float(input("Ingrese la nota definitiva: "))
    if notaDefinitiva >= 3.0:
        aprobaron = aprobaron + 1
    else:
        reprobaron = reprobaron + 1
    
    sumaDefinitiva = sumaDefinitiva + notaDefinitiva
    contadorEstudiantes = contadorEstudiantes + 1


promedio = sumaDefinitiva/cantidadEstudiantes 
print(f"La cantidad de aprobados es: {aprobaron}")
print(f"la cantidad de reprobados es: {reprobaron}")
print(f"El promedio es: {promedio}")
 