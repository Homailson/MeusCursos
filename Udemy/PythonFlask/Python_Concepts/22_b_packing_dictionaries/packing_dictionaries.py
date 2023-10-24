def empacotar_dados(a, b, c):
    return {'a': a, 'b': b, 'c': c}

# Dados para empacotar
dados_para_empacotar = {'a': 2, 'b': 4, 'c': 10}

# Chamada da função para realizar o packing
resultado_empacotado = empacotar_dados(**dados_para_empacotar)

# Exibindo o resultado empacotado
print(resultado_empacotado)