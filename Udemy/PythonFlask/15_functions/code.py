def hello():
    print("Hello world!") # Interessante, aqui "hello" é uma callabe variable. É uma variável cujo valor é uma função.and
                          # Quando se declara uma função em python se cria uma callabe variable.abs

def user_age_in_seconds():
    user_age = int(input("Digite a sua idade:"))
    user_age_in_seconds = user_age*365*24*60*60
    print(f"Sua idade em segundos é {user_age_in_seconds}")


friends = ["Rolf", "Bob"]

def add_friend():    
    friend_name = input("Digite o nome de um amigo seu: ")
    friends.append(friend_name)
    print(friends)


if __name__ == "__main__":
    hello()
    user_age_in_seconds()
    add_friend()





 

