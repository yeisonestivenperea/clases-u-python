"""
4. Calcular el valor de la comisión de un asesor de ventas que recibe la siguiente 
bonificación sobre total de sus ventas mensuales:
10 % por ventas hasta 3’000,000.
14 % por ventas mayor que 3'000,000.00 y menor o igual que 5'000,000.
18 % por ventas mayor que 5'000,000.00 y menor o igual que 7'000,000.
20 % por ventas hasta superior a 7'000,000.
"""

total_sales = float(input('-> Hola, por favor ingresa el valor de tus ventas este mes: '))

if total_sales > 0 and total_sales <= 3000000:
    print(f'Felicidades tú comision es del 10%')
elif total_sales > 3000000 and total_sales <= 5000000:
    print(f'Felicidades tú comision es del 14%')
elif total_sales > 5000000 and total_sales <= 7000000:
    print(f'Felicidades tú comision es del 18%')
elif total_sales > 7000000:
    print(f'Felicidades tú comision es del 20%')
else:
    print(f'Lo siento, el valor ingresado no corresponde')
