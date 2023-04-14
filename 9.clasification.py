""""
9. Clasificar el grupo al que pertenecen los estudiantes de un plantel educativo si se sabe 
que los menores de 10 años pertenecen al grupo A, entre 10 y menores que 18 al grupo 
B y de 18 en adelante al grupo C.
"""

age = int(input('Hola, por favor ingresa tu edad: '))

if age > 0 and age <= 10:
    print(f'Hola, perteneces al grupo A')
elif age > 10 and age <= 17:
    print(f'Hola, perteneces al grupo B')
elif age >= 18:
    print(f'Hola, perteneces al grupo C')
else:
    print(f'La edad ingresada es incorrecta')