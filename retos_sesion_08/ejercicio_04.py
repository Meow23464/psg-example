notas = (34, 61, 80, 20, 12, 69, 32, 60, 61, 51, 90, 23, 15)
promedio = sum(notas) / len(notas)
print("Promedio del semestre:", promedio)
if promedio >= 60:
    print("El estudiante aprobó el semestre.")
else:
    print("El estudiante no aprobó el semestre.")