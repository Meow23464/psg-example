# conversion_temperaturas.py
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temperaturas_celsius = [30, -273.99, 100]
for temp in temperaturas_celsius:
    temp_fahrenheit = celsius_a_fahrenheit(temp)
    print(f"{temp} ºC es equivalente a {temp_fahrenheit} ºF")
