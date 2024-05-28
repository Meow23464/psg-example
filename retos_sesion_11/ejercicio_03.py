# Crear un diccionario con las siguientes tuplas de animales
tupla = (('perro', '🐶'), ('gato', '🐱'), ('aves', ['🐦', '🦅']))

# Convertir la tupla en un diccionario
diccionario = dict(tupla)

# Obtener y eliminar el valor de la clave 'aves'
valor_aves = diccionario.pop('aves')

# Modificar el valor de la clave 'gato'
diccionario['gato'] = '🐈'

# Cambiar la clave 'perro' por 'perros' y su valor por ['🐶', '🐕']
diccionario['perros'] = diccionario.pop('perro'), '🐕'

# Mostrar el diccionario resultante
print(diccionario)
