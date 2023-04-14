"""
2. Pedir un número y calcular el cuadrado, si el número es menor o igual que 100, el
cubo si es mayor que 100 y menor o igual que 200 y un mensaje de error si es mayor que
200.
"""

number = int(input('-> Hola, por favor ingresa un número: '))

if number <= 100:
    cube = number * number * number
    print(f'El cubo de {number} es: {cube}')
elif number > 100 and number <= 200:
    square = number * number
    print(f'El cuadrado del {number} es: {square}')
else:
    print(f'El número {number} es invalido')
