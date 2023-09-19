# F string não muda dinamicamente

nome = "Homailson"

saudacao = f"Olá {nome}!"

print(saudacao)

nome = "Carolina"

print(saudacao)


# Contornando a situação

nome = "Homailson"

print(f"Hello, {nome}")

nome = "Carolina"

print(f"Hello, {nome}")


# Fazendo uso de templates com formatting

nome1 = "Homailson"
nome2 = "Carolina"

greeting = "Hello, {}"

with_nome1 = greeting.format(nome1)
with_nome2 = greeting.format(nome2)

print(with_nome1)
print(with_nome2)


# Usando formatting para frases longas

frase_longa = "Olá, {}. Hoje é {}."

nome = "Homailson"
dia = "Sábado"

fomatted = frase_longa.format(nome, dia)

print(fomatted)