productos = ["Leche", "Pan", "Huevo", "Queso", "Arroz"]
precios = [1.2, 0.5, 0.3, 2.0, 1.0]

productos_nuevos = ["Manzana", "Banana", "Yogur", "Zanahoria", "Tomate"]
precios_nuevos = [0.8, 0.6, 1.5, 0.4, 0.9]
productos.extend(productos_nuevos)
precios.extend(precios_nuevos)
print("Productos actualizados:", productos)
print("Precios actualizados:", precios)

if "Leche" in productos:
    indice_leche = productos.index("Leche")
    productos.pop(indice_leche)
    precios.pop(indice_leche)
print("Productos después de eliminar 'Leche':", productos)
print("Precios después de eliminar 'Leche':", precios)

precio_pan = precios[productos.index("Pan")]
precio_huevo = precios[productos.index("Huevo")]
print("Precio del Pan:", precio_pan)
print("Precio del Huevo:", precio_huevo)

producto_mas_caro = productos[precios.index(max(precios))]
producto_mas_barato = productos[precios.index(min(precios))]
print("Producto más caro:", producto_mas_caro)
print("Producto más barato:", producto_mas_barato)

total_productos = len(productos)
print("Total de productos:", total_productos)

total_precio_productos = sum(precios)
print("Costo total de los productos:", total_precio_productos)

productos_precios = sorted(zip(productos, precios))
productos_ordenados, precios_ordenados = zip(*productos_precios)
print("Productos ordenados alfabéticamente:", productos_ordenados)
print("Precios ordenados alfabéticamente:", precios_ordenados)

productos.clear()
precios.clear()
print("Productos después de eliminar todos:", productos)
print("Precios después de eliminar todos:", precios)