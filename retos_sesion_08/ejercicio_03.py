cadena = input("Ingresa una cadena: ")
tupla_cadena = tuple(cadena)
tupla_final = ('¡', ) + tupla_cadena + ('!', )
print("Resultado concatenado:", tupla_final)


tupla_repetida = tupla_final * 3
print("Tupla final repetida 3 veces:", tupla_repetida)