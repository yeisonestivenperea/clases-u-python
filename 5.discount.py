"""
5. Un almacén se encuentra en promoción por lo que hace un descuento del 20% a todos 
los clientes sobre el total de sus compras que sean mayores que 5000.00.
Se pide imprimir el valor de la venta, el descuento correspondiente y el neto a pagar.
"""

price_total = float(input('-> Valor de la compra: '))
discount = 0.20
if price_total > 0 and price_total > 5000:
    total =  price_total - (price_total * discount)
    print(f'Valor de la venta: ${price_total}')
    print(f'Se aplico un descuento de: ${discount}')
    print(f'Total a pagar: ${total}')
elif price_total > 0 and price_total <= 5000:
    print(f'Tu compra no tiene descuento, valor a pagar: ${price_total}')
else:
     print(f'El valor ingresado es incorrecto')
