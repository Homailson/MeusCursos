from typing import List, Optional

# Observação importantíssima: nunca crie uma função que tenha um parâmetro como sendo
# um objeto mutável
# os parâmetros de uma função são valorados quando essa função é definida, não quando a função é chamada.
# Ou seja, quando criamos a função abaixo, self.grades faz referência à lista vazia e quando instanciamos
# os estudantes Bob e Rolf ambos fazem referência ao mesmo endereço de memória da lista vazia, ou seja,
# a ambos são atribuidos a mesma lista de grades, pois é apenas uma na memória.
# Evite o problema abaixo não utilzando listas como parâmetros de uma função.

class Student:
    def __init__(self, name: str, grades: List[int] = []): #this is bad!
        self.name = name
        self.grades = grades

    def take_exam(self, result):
        self.grades.append(result)


bob = Student("Bob")
rolf = Student("Rolf")
bob.take_exam(90)
print(bob.grades)
print(rolf.grades)

# Contornando o erro:
# Quando usar uma lista como parâmetro, defina-o dentro da função e não na lista de parâmetros

class Student:
    def __init__(self, name: str, grades: Optional[List[int]] = None): #this is bad!
        self.name = name
        self.grades = grades or []

    def take_exam(self, result):
        self.grades.append(result)


bob = Student("Bob")
rolf = Student("Rolf")
bob.take_exam(90)
print(bob.grades)
print(rolf.grades)