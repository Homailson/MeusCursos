class Book:
    TYPES = ("hardcover", "paperback") # em um método, quando definimos variáveis, elas se tornam propriedades daquela classe

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self): # A proposta do método repr é um representação do objeto criado que aprensenta todas as suas propriedades,
                        # o que torna possível construir um novo objeto a partir disso.
        return f"<Book {self.name} {self.book_type}, weighing {self.weight}g>"

    @classmethod # aqui nós utilizamos o método de classe para criar objetos com características específicas. Chamamos a classe dentro do método que está na própria classe.           
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)
    
    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)



print(Book.TYPES)

book1 = Book("Harry Potter", "hardcover", 1500)

print(book1.name)

print(book1)

book2 = Book.hardcover("Harry Potter", 1500)

print(book2)

book3 = Book.paperback("Lord of the Rings", 1900)

print(book3)


