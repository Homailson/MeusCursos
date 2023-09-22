def add(x, y =8):
    print(x + y)


# Observação interessante: ao definir uma função na forma abaixo,
# ao se criar uma variável fora da definição que será usada como
# key argument, esse valor não mudará dentro da função, mesmo que
# ele seja modificado posteriormente. Veja a seguir:

default_y = 10

def minus(x, y=default_y):
    minus = x - y
    print(minus)


if __name__ == "__main__":
    # Apesar de a função add demandar 2 parâmetros, abaixo,
    # 
    add(5)
    add(x=6)
    # testando minus 
    minus(15)
    default_y = 15
    minus(15)