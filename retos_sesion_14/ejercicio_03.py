def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = 10  # Cambiar este valor para obtener un número diferente en la serie
print(f"El {n}-ésimo número de la serie de Fibonacci es: {fibonacci(n)}")
