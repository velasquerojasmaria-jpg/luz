promedio = float(input("Ingrese el promedio del estudiante: "))
if promedio >= 18:
    print("Beca completa")
elif promedio >= 15:
    print("Media beca")
elif promedio >= 11:
    print("Sin beca")
else:
    print("Desaprobado")