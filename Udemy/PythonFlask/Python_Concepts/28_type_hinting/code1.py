# Podemos importar vários tipos de variáveis para suar com type hinting: Tuples, Set, ect...
from typing import List

# Na próxima linha, indicamos que os argumentos passados
# para a função será uma lista e que a função retornará
# um valor do tipo float
def list_avg(sequence: List) -> float:
    return sum(sequence) / len(sequence)

list_avg(123)

# Outro exemplo

class BookShelf:
    def __init__(self, books: List[Book]):
        self.books = books
    
    def __str_(self) -> str:
        return f"Bookshelf with {len(self.books)} books."

class Book:
    pass