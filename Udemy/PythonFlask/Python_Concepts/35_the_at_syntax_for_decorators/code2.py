
mage = {"nome": "Presto", "classe": "Mago", "Mana": 90}
cleric = {"nome": "Berem", "classe": "Clerigo", "Mana": 20}
warrior1 = {"nome": "Erik", "classe": "Guerreiro", "Stamina": 100}
warrior2 = {"nome": "Artur", "classe": "Guerreiro", "Stamina": 150}


# ##########
# Decoradores
# ##########
def WarriorValidator(skill):
    def wrapper(character, atributo):
        if character["classe"] == "Guerreiro":
            print(f"Eu sou um {character['classe']}, meu nome é {character['nome']}!")
            return skill(character[atributo])
        else:
            return f"Este personagem é um {character['classe']} e não possui esta habilidade"
    
    return wrapper


def MageValidator(skill):
    def wrapper(character, atributo):
        if character["classe"] == "Mago":
            print(f"Eu sou um {character['classe']}, meu nome é {character['nome']}!")
            return skill(character[atributo])
        else:
            return f"Este personagem é um {character['classe']} e não possui esta habilidade"
    
    return wrapper


# #################
# Funções decoradas
# #################
@WarriorValidator
def PowerAttack(character_stamina):
    if character_stamina >= 48:
        print("O guerreiro começa a girar rapidamente com suas armas afiadas, causando 30 de dano a cada inimigo em um raio de 1,5 metros.")
        character_stamina -= 48
        return f"A Stamina agora é {character_stamina}"
    else:
        print("Não há stamina o suficiente para usar esta habilidade")
        return f"Sua Stamina é {character_stamina}"


@MageValidator
def Fireball(character_mana):
    if character_mana >= 70:
        print("As mãos do mago começam a formar uma imensa bola de fogo que é lançada contra um grupo de inimigos causando 40 de dano a cada um deles")
        character_mana -= 70
        return f"A Stamina agora é {character_mana}"
    else:
        print("Não há mana o suficiente para usar esta habilidade")
        return f"Sua mana agora é {character_mana}"


##################################
# Execução das funções decoradas
##################################


# Evento 01
#################################################################

personagem1 = mage
atributo1 = "Mana"

print(Fireball(personagem1, atributo1))


# Evento 02
#################################################################

personagem2 = warrior1
atributo2 = "Stamina"

print(PowerAttack(personagem2, atributo2))