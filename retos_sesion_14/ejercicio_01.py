def calcular_promedio(calificaciones):
    return sum(calificaciones) / len(calificaciones)

calificaciones = [20, 40, 60, 51, 13]
promedio = calcular_promedio(calificaciones)
print(f"El promedio de las calificaciones es: {promedio}")
