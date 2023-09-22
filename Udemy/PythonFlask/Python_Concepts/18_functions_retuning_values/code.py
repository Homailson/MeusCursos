# Por padrão, funções retornam o valor None
# Return é a última coisa que acontece dentro
# da função, após isso, nada mais será excutado
# nela

def add(x, y):
    return x + y


# Na função abaixo, estamos retornando dois tipos de
# variáveis, uma numérica (inteira) e outra literal (string)
# Isso não é uma prática recomendada

def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "You Fool!"

if __name__ == '__main__':
    result_f1 = add(9,5)
    print(result_f1)
    result_f2 = divide(10,5)
    print(result_f2)