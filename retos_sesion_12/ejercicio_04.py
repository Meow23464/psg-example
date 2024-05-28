def calcular_descuento(edad, monto_compra):
    if edad >= 18 and monto_compra > 1000:
        descuento = 0.1  # 10% de descuento
    elif edad < 18 and monto_compra > 500:
        descuento = 0.05  # 5% de descuento
    else:
        descuento = 0.02  # 2% de descuento
    
    return descuento

# Ejemplo de uso
edad_cliente = int(input("Ingrese la edad del cliente: "))
monto_compra_cliente = float(input("Ingrese el monto de la compra del cliente: "))

descuento_aplicado = calcular_descuento(edad_cliente, monto_compra_cliente)
monto_con_descuento = monto_compra_cliente * (1 - descuento_aplicado)

print(f"El cliente recibirá un descuento del {descuento_aplicado*100}%")
print(f"El monto a pagar con descuento es: ${monto_con_descuento:.2f}")
