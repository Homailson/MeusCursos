numero = 7

while True:
    user_input = input("Você quer jogar? (S/n) ")
    
    if user_input == "n":
        break # break permite a saída do loop while true
    
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