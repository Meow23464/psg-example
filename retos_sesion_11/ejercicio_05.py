# Crear un diccionario con las especies y la cantidad de animales que se guardarán en el arca
arca = {
    "perro": 2,
    "gato": 2,
    "tigre": 2,
    "mono": 2,
    "unicornio": 0,
    "jirafa": 1
}

# Añadir 2 especies más al arca usando update()
arca.update({"elefante": 2, "panda": 2})

# Tomar lista de los animales en el arca iterando el diccionario
animales_en_arca = []
for especie, cantidad in arca.items():
    for _ in range(cantidad):
        animales_en_arca.append(especie)

# ¿Existe en el arca la especie 'dragon'?
if 'dragon' in arca:
    print("Sí, la especie 'dragon' está en el arca.")
else:
    print("No, la especie 'dragon' no está en el arca.")

# Eliminar la especie 'unicornio' del arca
if 'unicornio' in arca:
    del arca['unicornio']

# Modificar el valor de la especie 'jirafa' por 2
arca['jirafa'] = 2

# Vaciar el arca después del diluvio
arca.clear()

# Mostrar el arca después del diluvio
print("El arca después del diluvio:", arca)
