import math

class ACanNotBeZero(ValueError):
    pass

coeficientes = {"a": 1, "b": 5, "c": -24}

def bhaskara(a, b, c, function):    
    x1 = (-b + math.sqrt(function(a, b, c)))/2*a
    x2 = (-b - math.sqrt(function(a, b, c)))/2*a
    
    return f"A solução da equação de grau 2 com os parâmetros {a, b, c} é S = [{x1, x2}]"

def delta(a, b, c):
    if a == 0:
        raise ACanNotBeZero(
            "ERRO! Em uma equação quadrática o parâmetro 'a' não pode ser zero"
        )
    delta = b**2 - 4*a*c
    return delta

try:
    print(bhaskara(**coeficientes, function = delta))
except ACanNotBeZero as e:
    print(e)
