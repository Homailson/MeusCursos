# Entradas do usuário
nome = input("Digite seu nome: ")

print(nome)

# Calculando com entradas do usuário

area_construida = input("Qual a área construida da sua casa (em metros quadrados): ")

area_construida = int(area_construida)

pes_quadrados = area_construida*10.764

print(f"A área construida da sua casa, em pés quadrados, é: {pes_quadrados:.2f}")