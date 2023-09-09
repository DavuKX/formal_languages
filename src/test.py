import random

a = set([1, 2, 3, 4, 5])
b = set([4, 5, 6, 7, 8])

## Intersection
print(a | b)

## Union
print(a & b)

## Difference
print(a - b)


def cerradura_estrella(alfabeto, num_palabras, longitud_max):
    cerradura = set()
    for _ in range(num_palabras):
        palabra = ''.join(random.choice(alfabeto) for _ in range(random.randint(0, longitud_max)))
        cerradura.add(palabra)
    
    return cerradura

# Alfabeto
alfabeto = ['a', 'b', 'c', 'd']

# Obtener entrada del usuario
num_palabras = 5
longitud_max = 20

# Generar la cerradura estrella
resultado = cerradura_estrella(alfabeto, num_palabras, longitud_max)

# Imprimir el resultado
for palabra in resultado:
    print(palabra)









