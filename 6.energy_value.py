"""
6. Calcular el total del servicio de energía de los usuarios, si se conocen los siguientes 
datos:
Cargo fijo 1500.00
Alumbrado público 1200.00
El valor del Kws consumido depende del estrato, así:
$ 150.00 para el estrato 1, $ 200.00 para el estrato 2, $ 250.00 para el estrato 3, $ 300.00 
para el estrato 4, $ 350.00 para los estratos 5 y 6, si el usuario digita un número de 
estrato diferente a los indicados, se debe imprimir un mensaje de error.
Téngase en cuenta, además, que los usuarios del estrato uno tienen derecho a un subsidio 
del estado correspondiente al 40% sobre el consumo si el consumo no excede de 200 
kws y del 25% para consumo entre 201 a 300 kws mensuales, y, los del estrato dos 
tienen derecho a un subsidio del 25% para un consumo de hasta 250 Kws mensuales.
"""

print(f'-> Bienvenido <-')

extract_value = int(input('Hola, por favor ingresa tu extracto: '))
value_kws = int(input('Ingresa el consumo de los kws: '))

if extract_value == 1 and value_kws <= 200:
    print(f'Hola, eres extracto 1 y tienes un subsidio del 40%, valor a pagar: {}')

elif extract_value == 2:
    print(f'Hola, eres extracto 2 y tienes un subsidio del 25%, valor a pagar: {}')

elif extract_value == 3:
    print(f'Hola, eres extracto 3 ')

elif extract_value == 4:
    print(f'Hola, eres extracto 4 ')

elif extract_value == 5 or extract_value == 6:
    print(f'Hola, eres extracto 4 ')


