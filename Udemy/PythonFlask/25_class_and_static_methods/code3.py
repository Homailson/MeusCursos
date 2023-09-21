class Game:

    genre = ("Action", "RPG", "Puzzle", "Adventure", "Sports")
    
    def __init__(self, title, genre, launchement_year, owner_enterprise):
        self.title = title
        self.genre = genre
        self.lauchement_year = launchement_year
        self.owner_enterprise = owner_enterprise

    def __repr__(self):
        return f"<Game: {self.title}, {self.lauchement_year}, {self.genre}, {self.owner_enterprise} >"

    @classmethod
    def Action(cls, title, lauchement_year, owner_enterprise):
        return cls(title, cls.genre[0], lauchement_year, owner_enterprise)
    
    @classmethod
    def RPG(cls, title, lauchement_year, owner_enterprise):
        return cls(title, cls.genre[1], lauchement_year, owner_enterprise)

    @classmethod
    def Puzzle(cls, title, lauchement_year, owner_enterprise):
        return cls(title, cls.genre[2], lauchement_year, owner_enterprise)

    @classmethod
    def Adventure(cls, title, lauchement_year, owner_enterprise):
        return cls(title, cls.genre[3], lauchement_year, owner_enterprise)

    @classmethod
    def Sports(cls, title, lauchement_year, owner_enterprise):
        return cls(title, cls.genre[4], lauchement_year, owner_enterprise)

game1 = Game.Action("Grand Theft Auto V", 2013, "Rockstar")
game2 = Game.RPG("The Elder Scrolls", 1994, " Bethesda Softworks & ZeniMax Media")
game3 = Game.Puzzle("Tetris", 1984, "Alexey Pajitnov")
game4 = Game.Adventure("The Witcher", 2022, "Projekt RED")
game5 = Game.Sports("NBA 2K", 2013, "2K Sports")

print(game1)
print(game2)
print(game3)
print(game4)
print(game5)