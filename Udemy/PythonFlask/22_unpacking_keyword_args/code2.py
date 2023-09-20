def printGames(**kwargs):
    print(kwargs)


if __name__ == "__main__":
    
    # lista de tuplas
    games = [
    (0, "Phantasy Star", "Master System", 1987, "Sega"),
    (1, "World of Warcraft", "PC", 2004, "Blizzard Entertainment"),
    (2, "Resident Evil 3", "Playstation", 1996, "Capcom"),
    (3, "Metal Gear Solid", "Playstation", 1998, "Konami"),
    (4, "Wolfeinstein: Enemy Territory", 2003, "Activision")
    ]

    # criando um dicionário a partir da lista de tuplas
    # usando dict comprehension
    games_mapping = {game[1]: game for game in games}
    
    # chamando a função printGames fazendo o unpacking
    # do dicionário games_mapping. Interessante notar que
    # na definição da função, ela faz o packing dos valores
    # desempacotados quando ela foi chamada.        
    printGames(**games_mapping)