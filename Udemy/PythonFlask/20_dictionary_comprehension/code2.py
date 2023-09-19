# Outra aplicação de dictionary comprehension

games = [
    (0, "Phantasy Star", "Master System", 1987, "Sega"),
    (1, "World of Warcraft", "PC", 2004, "Blizzard Entertainment"),
    (2, "Resident Evil 3", "Playstation", 1996, "Capcom"),
    (3, "Metal Gear Solid", "Playstation", 1998, "Konami"),
    (4, "Wolfeinstein: Enemy Territory", 2003, "Activision")
]

games_mapping = {game[1]: game for game in games}

print(games_mapping)

usergame_input = input("Digite o nome do jogo que você quer consultar: ")

_, title, platform, year, enterprise = games_mapping[usergame_input]

print(f"O título {title} foi lançado em {year} para {platform} pela {enterprise}")