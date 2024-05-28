# Obtener la entrada del usuario
entrada_usuario = input("Ingrese su nombre y gustos musicales separados por coma: ")

# Separar el nombre y los gustos musicales
datos_usuario = entrada_usuario.split(',')

# Verificar si se ingresó un nombre válido (no vacío)
nombre_usuario = datos_usuario[0].strip() if datos_usuario else None
if nombre_usuario:
    print("Nombre válido:", nombre_usuario)
else:
    print("Nombre inválido. Por favor ingrese un nombre válido.")

# Convertir los gustos musicales en una lista
gustos_musicales = datos_usuario[1:] if len(datos_usuario) > 1 else []
print("Gustos musicales:", gustos_musicales)

# Verificar si el usuario tiene el gusto "rock" en su lista de gustos musicales
if 'rock' in gustos_musicales:
    print("El usuario disfruta del género musical rock.")
else:
    print("El usuario no disfruta del género musical rock.")
