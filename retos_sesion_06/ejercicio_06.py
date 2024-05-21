numero = 123
cuadrado = numero ** 2
esta_en_rango = cuadrado > 0 and cuadrado < 20000

print(f"El cuadrado de 123 ({cuadrado}) {'sí' if esta_en_rango else 'no'} se encuentra en el rango [1, 20000]")