# Crear un diccionario que asocie especies animales en peligro de extinción con información sobre sus hábitats amenazados
habitats = {
    "polo norte": {"especies": {"oso polar", "morsa", "ballena"}},
    "amazonas": {"especies": {"tigre", "mono", "guacamayo"}}
}

# Añadir 2 habitats más usando update()
habitats.update({
    "Gran Barrera de Coral": {"especies": {"tortuga marina", "tiburón martillo"}},
    "Bosque Amazónico": {"especies": {"jaguar", "anaconda"}}
})

# ¿Existe en el diccionario de habitats el habitat 'amazonas'?
if 'amazonas' in habitats:
    print("Sí, el habitat 'amazonas' está en el diccionario de habitats.")

# Añadir al diccionario de amazonas la especie 'anaconda'
habitats['amazonas']['especies'].add('anaconda')

# Mostrar el diccionario de habitats actualizado
print(habitats)
