anita_platos = {"Sushi", "Pizza", "Tacos", "Hamburguesa", "Pasta", "Alitas"}
pepito_platos = {"Pizza", "Tacos", "Ensalada", "Pasta", "Helado", "Milanesa"}

# Encontrar los platos en común
platos_comunes = anita_platos & pepito_platos
print("Platos en común:", platos_comunes)

# Verificar si los platos en común son más del 50%
total_platos_anita = len(anita_platos)
porcentaje_comun = (len(platos_comunes) / total_platos_anita) * 100
print("Porcentaje de platos en común:", porcentaje_comun, "%")

if porcentaje_comun > 50:
    print("Ambos seguirán saliendo.")
else:
    print("Ambos no seguirán saliendo.")