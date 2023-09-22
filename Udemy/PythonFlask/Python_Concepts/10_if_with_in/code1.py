filmes_que_ja_assisti = {"Forest Gump", "Gladiador", "O senhor dos Anéis", "Guardiões das Galáxias"}

filme_do_usuario = input("Digite o nome de algum filme que você já assistiu")

if filme_do_usuario in filmes_que_ja_assisti:
    print(f"Já assisti {filme_do_usuario} também!")
else:
    print(f"Ainda não assisti {filme_do_usuario}")