while True:
    palabra = input("Ingresa una palabra: ")
    if palabra.lower() == "salir":
        break
    if palabra == palabra[::-1]:
        print("Es un palíndromo")
    else:
        print("No es un palíndromo")
