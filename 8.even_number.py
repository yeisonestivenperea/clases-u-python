"""
8. Capturar un número entero e imprimir un mensaje indicando si es par o impar
"""

number = int(input('Hola, por favor ingresa un número: '))

if number == 0:
    print(f'El numero: {number} no se considera par ni impar')
elif number != 0 and number % 2 == 0:
    print(f'El numero: {number} es par')
else:
    print(f'El numero: {number} es impar')