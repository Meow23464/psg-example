lista_personas = ["Alice", "Bob", "Catherine", "David", "Eva", "Frank", "Grace", "Hannah", "Isaac", "Jhon"]

sub_lista_personas = lista_personas[2:8]
print("Sub lista de 2 a 7:", sub_lista_personas)

existe_jhon = "Jhon" in lista_personas
print("Existe 'Jhon' en la lista original:", existe_jhon)

sub_lista_personas_ordenada = sorted(sub_lista_personas)
print("Sub lista ordenada alfabéticamente:", sub_lista_personas_ordenada)

lista_personas_descendente = sorted(lista_personas, reverse=True)
print("Lista original ordenada alfabéticamente de forma descendente:", lista_personas_descendente)