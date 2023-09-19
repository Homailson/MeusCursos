# Funções lambda não têm um nome e retornam apenas valores.
# Elas são usadas para operar entradas e retornar saídas
# São quase nunca usadas para performar ações


# Esta abaixo é uma função de soma simples
def add(x, y):
    return x + y

print(add(5,7))

# Podemos reescrever essa função soma utilizando
# uma função lambda. Veja abaixo

# Antes dos dois pontos vai a lista de parâmetros e depois
# o retorno da função, que no caso não está explícito, mas
# corresponde a x + y, que é a operação com os parâmetros.

lambda x, y: x + y

# Podemos dar um nome para a função

add = lambda x, y: x + y

# Caso não queiramos nomeá-la, temos de usá-la na mesma linha
# em que a definimos

print((lambda x, y: x + y)(5,7))