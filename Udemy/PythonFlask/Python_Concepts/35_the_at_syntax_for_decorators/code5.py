import functools

jogador = {"Nome": "Roberto Carlos", "posicao": "lateral"}

def taticaDeJogo(funcao):
    @functools.wraps(funcao)
    def verificaTatitca():
        if jogador["posicao"] == "lateral":
            return funcao()
        else:
            print("Essa tática não é válida para esse jogador.")
    return verificaTatitca

@taticaDeJogo
def cruzarNaLinhaDeFundo():
    return "Cruzando a bola da linha de fundo para a área."

#cruzarNaLinhaDeFundo = taticaDeJogo(cruzarNaLinhaDeFundo)

print(cruzarNaLinhaDeFundo.__name__)

print(cruzarNaLinhaDeFundo())

