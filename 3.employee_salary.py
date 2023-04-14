"""
Pedir el nombre y sueldo de un empleado y calcular su devengado.
Además, si su sueldo no es superior a dos salarios mínimos tiene derecho a una prima
de alimentación de $ 12,000.00 y subsidio de transporte por $ 9,500.00, y si su sueldo
es superior a dos salarios mínimos y no mayor que cinco salarios mínimos, tendrá
derecho a una prima de representación correspondiente al 7% de su sueldo básico.
Finalmente, los empleados que ganen más de seis salarios mínimos tendrán un
descuento del 1.5% por concepto de retención en la fuente.
Cada concepto se paga proporcional al número de días trabajados.
"""

name = input('-> Hola, por favor ingresa tu nombre: ')
salary = float(input('-> ingresa tu salario: '))
minimum_salary = 1,300,606
price_alimentation = 12,000.00
price_transport = 9,500.00

final_salary = 0
if salary < salary * 2:
    final_salary = 