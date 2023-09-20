# O símbolo **kwargs coleta keyword arguments
# no exemplo abaixo, os keyword arguments coletados
# são (name="Bob", age=25)

def named(**kwargs):
    print(kwargs)

named(name="Bob", age=25)


# O contrário também pode ser feito. Podemos desempacotar
# um dicionário para que key arguments sejam supridos

def named2(name, age):
    print(name, age)

details = {"name": "Bob", "age": 25}

named2(**details)


def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")

print_nicely(name="Bob", age=25)


def both(*args, **kwargs):
    print(args)
    print(kwargs)

both(1,3,5, name="Bob", age=25)