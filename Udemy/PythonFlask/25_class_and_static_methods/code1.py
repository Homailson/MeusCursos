# Método, em python, é uma chamada de um método de uma instância(objeto) porque nós os chamamos por meio de uma instância(objeto) da classe
class ClassTest:
    def instance_method(self): # Instance methods são todos os métodos da classe que têm como primeiro parâmetro self, ou seja, são relativos a um objeto
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls }")

    @staticmethod # Isto não é um método, é apenas uma função separada dentro da classe
    def static_method(): # métodos estáticos não recebem nenhum tipo de parâmetro especial
        print("Called static_method.")


test = ClassTest()
test.instance_method()
ClassTest.instance_method(test)

ClassTest.class_method()

ClassTest.static_method()

# Métodos de instâncias são úteis para muitas coisas, quando se quer produzir uma ação que utiliza dados
# dentro do objeto que você criou anteriormente, por exemplo. é quando métodos de instância são utilizados.
# Métodos de classe são utilizados como uma fábrica
# Métodos estáticos são utilizados para definir um método dentro de uma classe.
