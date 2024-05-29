def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

while True:
    numero = int(input("Ingresa un número: "))
    if numero == 0:
        break
    if is_prime(numero):
        print("Es un número primo")
    else:
        print("No es un número primo")
