def double(x):
    return x * 2

# Abaixo estamos usando list comprehension para criar
# outra lista, a qual será o dobro de uma primeira lista.

sequence = [1, 3, 5, 7, 9]

doubled = [x * 2 for x in sequence]

print(doubled)

# podemos também fazer uso da função map,
# aplicando a função double à primeira lista

double = map(double, sequence)
print(list(double))

# podemos também utilizar a função lambda em conjunto
# com a função map

double = list(map(lambda x: x * 2, sequence))
print(double)
