# O símbolo * diz respeito à ação de unpacking
# args correspondem aos valores que serão desempacotados


# Na função abaixo, a função recebe como
# argumento uma tupla de elementos que são
# atribuídos à variável args, então são impressos
# no console
def pringArgs(*args):
    print(args)

pringArgs(1, 2, 3, 4, 5)


# Outra aplicação (packing)

def multiply(*args):
    total = 1
    for arg in args:
        total = total * arg
    return total

print(multiply(1, 2, 3, 4, 5))

# Outra aplicação (agora de unpacking)

def add(x, y):
    return x + y

nums = [3, 6]

print(add(*nums))

# Outra aplicação (usando keyword arguments)

# Note que abaixo temos um dicionário contendo
# dois elementos, x e y, com seus respectivos valores.
# Podemos passar esses elementos como elementos nomeados
# para a função add. 

nums = {"x": 15, "y": 25}

# aqui não estamos usando unpacking
print(add(x=nums["x"], y = nums["y"]))

# mas podemos usar como a seguir, porque
# como o nome dos argumentos correspondem
# às chaves dos dicionários, o python já
# entende essa sintaxe, aceitando as chaves
# do dicionário como os nomes dos argumentos
# e seus valores como os valores dos argumentos

print(add(**nums))

