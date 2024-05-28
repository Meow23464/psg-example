comidas = {
    "carne": {"animales": ["león", "tigre"]},
    "frutas": {"animales": ["mono", "elefante"]}
}

# Añadir al diccionario de comidas 4 alimentos más usando update(clave=valor)
comidas.update(
    vegetales={"animales": ["conejo", "elefante"]},
    pescado={"animales": ["oso", "gato"]},
    insectos={"animales": ["lagartija", "rana"]},
    semillas={"animales": ["pájaro", "ardilla"]}
)

# Verificar si existe en el diccionario de comidas la comida 'meat'
existe_meat = 'meat' in comidas

# Eliminar la comida 'frutas' del diccionario de comidas
if 'frutas' in comidas:
    del comidas['frutas']

# Imprimir los resultados
print("Diccionario de comidas actualizado:")
for comida, info in comidas.items():
    print(f"{comida}: {info}")

print(f"\n¿Existe la comida 'meat' en el diccionario? {existe_meat}")