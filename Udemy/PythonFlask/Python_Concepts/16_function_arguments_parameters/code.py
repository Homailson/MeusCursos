def add(x, y): # x e y são chamados parâmetros
    result = x + y
    print(result)
    
# Na função abaixo, estamos utlizando argumentos posicionais, onde
# a ordem dos mesmos importa, ou seja, primeiro vem o nome e depois
# o sobrenome
def say_hello(name, surname):
    print(f"Hello! {name} {surname}")

# Na função abaixo, estamos utlizando argumentos nomeados, onde
# cada argumento recebe uma palavra-chave como nome

def say_goodbye(name = "Marcus", surname="Aurélios"):
    print(f"Goodbye! {name} {surname}")


def divide(dividend, divisor):
    if divisor != 0:
        print(dividend /  divisor)
    else:
        print("You fool!")


if __name__ == '__main__':
    add(5, 3) # 5 e 3 são chamados argumentos
    say_hello("Carol", "Darge")
    say_hello(name="Artur", surname="Argélius")
    say_goodbye()
    divide(dividend=5,divisor=2)

# É recomendado fazer uso dos key arguments para deixar o código mais intelegível