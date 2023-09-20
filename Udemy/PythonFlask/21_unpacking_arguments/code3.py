def squared(*args):
    squared_list = list(map(lambda x: x**2, args))
    return squared_list


nums = (1, 2, 3, 4, 5, 6, 7, 8, 9)

if __name__ == '__main__':
    print(squared(*nums)) # Aqui nesta função ao usarmos o * em nums, estamos fazendo o unpacking (desempacontamento) da tupla nums,
                   # cujos valores serão passados como argumento para a função squared.
                   # Na chamada da função squared, os valores desempacotados são novamente empacotados em uma nova tupla denomidada
                   # args, pela qual fazemos iteração sobre seus elementos.