# Amigos de Jhon y Jess
amigos_jhon = {"Alice", "Bob", "Charlie", "David", "Eve"}
amigos_jess = {"Alice", "Bob", "Frank", "Grace"}

# Calcular amigos en común
amigos_comunes = amigos_jhon.intersection(amigos_jess)

# Verificar si tienen amigos en común
if amigos_comunes:
    print("Jhon y Jess tienen amigos en común:")
    for amigo in amigos_comunes:
        print(amigo)
else:
    print("Jhon y Jess no tienen amigos en común.")
