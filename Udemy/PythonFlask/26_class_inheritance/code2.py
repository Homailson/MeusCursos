class Character:
    def __init__(self, name, gender, age, classe):
        self.name = name
        self.gender = gender
        self.age = age
        self.classe = classe
        self.awakened = True
        self.hungry = False
        self.thirsty = False
        self.walk = False

    def __str__(self):
        return f"Character: {self.name}, {self.gender}, {self.age} and {self.classe}"
    
    def wakeupSleep(self):
        if self.awakened == True:            
            print(f"{self.name} is awake")        
        else:
            print(f"{self.name} is sleeping")
    
    def eat(self):
        if self.hungry:
            print(f"{self.name} is not hungry")
        print(f"{self.name} is eating")
    
    def drink(self):
        if self.thirsty:
            print(f"{self.name} is not thirsty")
        print("{self.name} is drinking")

    def walk(self):
        if self.walk:
            print(f"{self.name} is stoped")
        print(f"{self.name} is walking")
    
class Mage(Character):
    def __init__(self, name, gender, age, classe, mana):
        super().__init__(name, gender, age, classe)
        self.mana = mana
        self.remaing_mana = mana
    
    def fireball(self):
        if self.awakened:
            if self.remaing_mana < 100:
                print("Not enough mana")            
            self.remaing_mana -= 100
            print(f"{self.name} casted Fireball.\nNow {self.name}'s mana is {self.remaing_mana}.")
        else:
            print(f"{self.name} can not cast spells when sleeping!")

mage1 = Mage("Morgana", "female", 32, "firemage", 500)

print(mage1)

mage1.awakened = True

mage1.wakeupSleep()

mage1.fireball()
        
