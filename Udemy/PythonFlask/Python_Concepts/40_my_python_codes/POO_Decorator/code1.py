import functools

class Personagem:
    def __init__(self, nome, classe, estamina, mana):
        self.nome = nome
        self.classe = classe
        self.estamina = estamina
        self.mana = mana

    # este é um método de representação do objeto em string, mais amigável
    # ao usuário
    def __str__(self):
        return f"{self.nome} é um {self.classe}"


class Guerreiro(Personagem):
    def __init__(self, nome, classe, estamina, mana, arquetipo_de_batalha):
        super().__init__(nome, classe, estamina, mana)
        self.arquetipo_de_batalha = arquetipo_de_batalha

    # este é um método que retorna uma representação mais canônica do objeto em string,
    # voltada aos desenvolvedores
    def __repr__(self):
        return f"<Personagem: nome: {self.nome}, classe: {self.classe}, arquetipo de batalha: {self.arquetipo_de_batalha}, estamina: {self.estamina}, mana: {self.mana}>"


class Mago(Personagem):
    def __init__(self, nome, classe, estamina, mana, escola_de_magia):
        super().__init__(nome, classe, estamina, mana)
        self.escola_de_magia = escola_de_magia

    def __repr__(self):
        return f"<Personagem: nome: {self.nome}, classe: {self.classe}, escola de magia: {self.escola_de_magia}, estamina: {self.estamina}, mana: {self.mana}>"


def verificadorDeClasse(classe):
    def decorator(funcao):
        @functools.wraps(funcao)
        def verificaClasse(personagem):
            if personagem.classe == classe:
                return funcao(personagem)
            else:
                return f"{personagem.nome} é um {personagem.classe} e não possui essa habilidade"
        
        return verificaClasse

    return decorator

@verificadorDeClasse("Guerreiro")
def ataquePoderoso(personagem):
    return f"{personagem.nome} desfere um golpe poderoso com toda sua força"

@verificadorDeClasse("Mago")
def raioCongelante(personagem):
    return f"{personagem.nome} paraliza o inimigo ao atingí-lo com seu raio congelante"


mago1 = Mago("Presto", "Mago", 50, 100, "Transmutação")

guerreiro1 = Guerreiro("Erik", "Guerreiro", 100, 50, "Campeão")

print(repr(mago1))

print(repr(guerreiro1))

print(raioCongelante(guerreiro1))

print(raioCongelante(mago1))