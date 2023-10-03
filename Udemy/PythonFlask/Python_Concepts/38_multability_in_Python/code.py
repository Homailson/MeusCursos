# Abaixo, podemos observar que a e b são nomes, o valor é a lista vazia.
# Nós teremos então dois nomes para o mesmo objeto

a = []
b = a

print(id(a))
print(id(b))

# Agora, a e b serão listas diferentes

a = []
b = []

a.append(12)

print(id(a))
print(id(b))

print(a)
print(b)

# Como podemos mudar uma lista após sua criação, dizemos que ela é mutável
# Em Python tudo é mutável, a menos que não haja forma de alterar as propriedades daquele objeto específico

# As tuplas são objetos imutáveis em Python
# Abaixo, mesmo adicionando um novo valor à c, estamos criando uma nova tupla

c = ()
c = c + (12,)

# Vejamos agora a imutabilidade com números
# Note que mesmo se alterarmos o valor de d, e não se altera


d = 4567
e = 4567

print(id(d))
print(id(e))

d = 4687

print(id(d))
print(id(e))

# muitos objetos em Python são mutáveis, exceto por tuplas, strings, inteiros, ponto flutuantes e booleanos

# Outro exemplo: No caso a seguir, não estamos alterando a string "hello" mas sim atribuindo a f o valor da concatenação de "hello" com " world"
# g permanece inalterado após a redefinição de f.

f = "hello"
g = f

print(id(f))
print(id(g))

f += " world"

print(g)
print(f)