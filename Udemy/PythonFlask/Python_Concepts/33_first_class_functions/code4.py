lados_triangulo = {
    "cateto1":6,
    "cateto2":8,
    "hipotenusa":10,
}

def eTrianguloRetangulo(cateto1, cateto2, hipotenusa, operacao):
    c1 = operacao(cateto1)
    c2 = operacao(cateto2)
    a2 = operacao(hipotenusa)

    if a2 == (c1 + c2):
        return "É triângulo retângulo"        
    else:
        return "Não é triângulo retângulo"    

def potenciacao(valor):
    return valor * valor

print(eTrianguloRetangulo(**lados_triangulo, operacao=potenciacao))
