def multiply(*args):
    total = 1
    for arg in args:
        total = total * arg
    return total


# abaixo estamos coletando todos os argumentos
# posicionais através da tupla de argumentos
# e também temos um keyword argument, no caso,
# operator, que é compulsório. 
def apply(*args, operator):    
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "O operador provido não é válido à função apply"

nums = (1, 2, 3, 4, 5)

print(apply(*nums, operator="*"))