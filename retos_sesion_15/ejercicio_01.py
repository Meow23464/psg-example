# ejercicio_01.py

def solicitar_numero(mensaje):
    while True:
        entrada = input(mensaje)
        if entrada.lower() == "salir":
            return "salir"
        try:
            numero = float(entrada)
            return numero
        except ValueError:
            print("Entrada inválida, por favor ingrese un número válido o 'salir' para terminar.")

def calculadora():
    while True:
        print("\nCalculadora básica. Para salir, ingrese 'salir'.")
        
        numero1 = solicitar_numero("Ingrese el primer número: ")
        if numero1 == "salir":
            print("Saliendo de la calculadora...")
            break
        
        numero2 = solicitar_numero("Ingrese el segundo número: ")
        if numero2 == "salir":
            print("Saliendo de la calculadora...")
            break
        
        operacion = input("Ingrese la operación (suma, resta, multiplicacion, division): ").lower()
        if operacion == "salir":
            print("Saliendo de la calculadora...")
            break

        if operacion == "suma":
            resultado = numero1 + numero2
        elif operacion == "resta":
            resultado = numero1 - numero2
        elif operacion == "multiplicacion":
            resultado = numero1 * numero2
        elif operacion == "division":
            try:
                resultado = numero1 / numero2
            except ZeroDivisionError:
                resultado = "Error: División por cero no permitida."
        else:
            resultado = "Operación no válida."

        print(f"Resultado: {resultado}")

if __name__ == "__main__":
    calculadora()
