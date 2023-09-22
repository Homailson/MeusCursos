numero = 7
user_input = input("Digite 'y' se você quiser jogar: ").lower()

if user_input in ("y", "Y"):
    user_number = int(input("Adivinhe nosso número: "))
    if user_number == numero:
        print("Você advinhou!")
    elif numero - user_number in (1, -1):
        print("Você errou por 1")
    elif abs(numero - user_number) == 2:
        print("Você errou por 2")
    else:
        print("Você errou!")
else:
    print("Tudo bem, até mais")