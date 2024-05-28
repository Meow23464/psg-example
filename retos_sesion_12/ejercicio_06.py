def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return "Error: división por cero"
    else:
        return num1 / num2

print("Calculadora simple")
print("------------------")
numero1 = float(input("Número 1: "))
numero2 = float(input("Número 2: "))
operacion = input("Operación (+, -, *, /): ")

if operacion == '+':
    resultado = suma(numero1, numero2)
elif operacion == '-':
    resultado = resta(numero1, numero2)
elif operacion == '*':
    resultado = multiplicacion(numero1, numero2)
elif operacion == '/':
    resultado = division(numero1, numero2)
else:
    resultado = "Operación no válida"

print("-------------")
print("Resultado:", resultado)
