estudiantes = [('Juan', 51), ('Pedro', 80), ('Maria', 90), ('Ana', 40), ('Luis', 30)]
aprobados = [nombre for nombre, nota in estudiantes if nota >= 50]

# Dar las felicitaciones a los estudiantes que aprobaron el curso
for nombre in aprobados:
    print(f"Felicidades {nombre} por aprobar el curso!")
