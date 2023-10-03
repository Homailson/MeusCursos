import functools

def verificadorDeClasse(classe):
    def decorator(funcao):
        @functools.wraps(funcao)
        def testaClasse(personagem):
            if personagem['classe'] == classe:
                return funcao(personagem)
            else:
                return f"{personagem['nome']} tenta, mas nada acontece"
    
        return testaClasse
    
    return decorator


@verificadorDeClasse("Guerreiro")
def arrombarPorta(personagem):    
    return f"{personagem['nome']} arromba a porta com sucesso"


@verificadorDeClasse("Mago")
def lancarBolaDeFogo(personagem):    
    return f"{personagem['nome']} lança Bola de Fogo com sucesso"

personagem1 = {"nome": "Erik", "classe": "Guerreiro"}

personagem2 = {"nome": "Presto", "classe": "Mago"}

print(arrombarPorta(personagem1))

print(arrombarPorta(personagem2))

print(lancarBolaDeFogo(personagem1))

print(lancarBolaDeFogo(personagem2))