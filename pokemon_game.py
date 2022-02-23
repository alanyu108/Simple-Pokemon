class Pokemon:
    def __init__(self, name, health, gender, nature):
        self.name = name
        self.health = health
        self.gender = gender
        self.nature = nature
        self.moves = {"Attack": 25}
    def __str__(self):
        return f"{self.name.capitalize()}\nHealth: {self.health}\nGender: {self.gender}\nNature: {self.nature}"
    
class Player:
    def __init__(self, name, gender, nature, money):
        self.name = name;
        self.gender = gender
        self.nature = nature
        self.money = money
        self.bag = []
        self.pokemon = []
    def __str__(self):
        return f"{self.name.capitalize()}\nGender: {self.gender.capitalize()}\nNature: {self.nature.capitalize()}\nMoney: ${self.money}"

class CPU_Trainer:
    def __init__(self, name, money):
        self.name = name;
        self.money = money;
        self.pokemon = []

class Grid_Tiles:
    def __init__(self, terrain):
        self.terrain = terrain
        



def main():
    player = CPU_Trainer('alan',  1000000)
    print()

if __name__ == '__main__':
    main()