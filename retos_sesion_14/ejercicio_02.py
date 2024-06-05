def calculadora_flexible(**kwargs):
    resultado = None
    if 'suma' in kwargs:
        resultado = sum(kwargs['suma'])
    elif 'resta' in kwargs:
        resultado = kwargs['resta'][0]
        for num in kwargs['resta'][1:]:
            resultado -= num
    elif 'multiplicacion' in kwargs:
        resultado = 1
        for num in kwargs['multiplicacion']:
            resultado *= num
    elif 'division' in kwargs:
        resultado = kwargs['division'][0]
        for num in kwargs['division'][1:]:
            resultado /= num
    return resultado

print(calculadora_flexible(suma=[1, 2, 3, 4]))  # Output: 10
print(calculadora_flexible(resta=[10, 2, 3]))   # Output: 5
print(calculadora_flexible(multiplicacion=[2, 3, 4]))  # Output: 24
print(calculadora_flexible(division=[20, 2, 2]))   # Output: 5
