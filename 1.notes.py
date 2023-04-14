"""
1. Capture el nombre y tres notas de un estudiante e imprimir el nombre y la nota
promedio, así como un mensaje que indique si el alumno aprobó o reprobó, sabiendo
que la materia se aprueba con un promedio mínimo de 3.5 (nota de 1 a 5).
"""

name = input('-> Hola, por favor ingresa tu nombre: ')

note_1 = int(input('-> ingresa la primera nota: '))
note_2 = int(input('-> ingresa la segunda nota: '))
note_3 = int(input('-> ingresa la tercera nota: '))

average = (note_1 + note_2 + note_3) / 3
passing_average = 3.5
if average >= passing_average:
    print(f'Felicitaciones aprobaste')
else:
    print(f'Reprobaste, por favor estudia un poco más')