import libs.mylib


def divide(dividend, divisor):
    return dividend / divisor

print("mymodule.py: ", __name__) ## __name__ é uma variável em python que muda dependendo do arquivo em que você está.
                                 ## através dela, podemos diferenciar o arquivo que você está rodando e o que está sendo importado.
                                 ## __name__ é a mesma coisa que __main__ no arquivo no qual estamos.