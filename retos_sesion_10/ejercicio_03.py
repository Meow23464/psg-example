mochilero_a = {"París", "Londres", "Nueva York", "Tokio", "Peru", "Chile", "Colombia", "Bolivia"}
mochilero_b = {"Londres", "Roma", "Nueva York", "Sidney", "Argentina", "Brasil", "Panama", "Bolivia"}

lugares_unicos_a = mochilero_a - mochilero_b
print("Lugares visitados por mochilero_a que mochilero_b no ha visitado:", lugares_unicos_a)

lugares_unicos_b = mochilero_b - mochilero_a
print("Lugares visitados por mochilero_b que mochilero_a no ha visitado:", lugares_unicos_b)

lugares_comunes = mochilero_a & mochilero_b
print("Lugares visitados por ambos mochileros:", lugares_comunes)