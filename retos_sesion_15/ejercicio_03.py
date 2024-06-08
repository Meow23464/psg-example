# ejercicio_03.py

class SaldoInsuficienteError(Exception):
    def __init__(self, saldo, monto):
        super().__init__(f"Saldo insuficiente: {saldo} - Monto solicitado: {monto}")

def cajero_automatico(saldo):
    while True:
        print(f"\nSaldo disponible: {saldo}")
        entrada = input("Ingrese el monto a retirar (o 'salir' para terminar): ")
        
        if entrada.lower() == "salir":
            print("Saliendo del cajero automático...")
            break
        
        try:
            monto = float(entrada)
            if monto > 1000:
                raise Exception("No se pueden retirar montos superiores a 1000.")
            if monto > saldo:
                raise SaldoInsuficienteError(saldo, monto)
            saldo -= monto
            print(f"Retiro exitoso. Nuevo saldo: {saldo}")
        except ValueError:
            print("Entrada inválida, por favor ingrese un número válido.")
        except SaldoInsuficienteError as e:
            print(e)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    saldo_inicial = 500  # Puedes ajustar el saldo inicial según sea necesario
    cajero_automatico(saldo_inicial)
