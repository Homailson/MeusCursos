import functools

def idadeMaxima(func):    
    @functools.wraps(func)
    def testarIdade(*args, **kwargs):
        if bebe['idade'] <= 2:
            return func(*args, **kwargs)
        else:
            return f"A idade de {bebe['nome']} está avançada para mamar"
    return testarIdade

@idadeMaxima
def amamentar(tipo_de_leite):
    if tipo_de_leite == "leite materno":
        return "Mamãe amamentando criança com leite próprio"
    elif tipo_de_leite == "leite bovino":
        return "Mamãe amamentando criaça com leite de vaca"

bebe = {"nome":"Helena", "idade":1}

print(amamentar("leite bovino"))

