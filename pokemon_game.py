import random
import math


starter_pokemon = [
    {
        "name": "Pikachu", 
        "nature": "electric", 
        "health": 100, 
        "gender": "male"
    }, 
    {
        "name": "Charmander", 
        "nature": "fire", 
        "health": 100, 
        "gender": "male"
    },
    {
        "name": "Bulbasaur", 
        "nature": "grass", 
        "health": 100, 
        "gender": "male"
    }, 
    {
        "name": "Squirtle", 
        "nature": "water", 
        "health": 100, 
        "gender": "female"
    }
]
game_pokemon = [{'name': 'Oshawott', 'nature': 'Water', 'gender': 'female', 'health': 100}, {'name': 'Seaking', 'nature': 'Water', 'gender': 'female', 'health': 100}, {'name': 'Furret', 'nature': 'Normal', 'gender': 'male', 'health': 75}, {'name': 'Shelmet', 'nature': 'Bug', 'gender': 'male', 'health': 100}, {'name': 'Pancham', 'nature': 'Fighting', 'gender': 'female', 'health': 75}, {'name': 'Geodude', 'nature': 'Rock', 'gender': 'female', 'health': 75}, {'name': 'Exploud', 'nature': 'Normal', 'gender': 'female', 'health': 75}, {'name': 'Tranquill', 'nature': 'Normal', 'gender': 'female', 'health': 75}, {'name': 'Porygon-Z', 'nature': 'Normal', 'gender': 'female', 'health': 100}, {'name': 'Seviper', 'nature': 'Poison', 'gender': 'male', 'health': 100}]

class Pokemon:
    def __init__(self, name, health, gender, nature):
        self.name = name
        self.health = health
        self.gender = gender
        self.nature = nature
    def __str__(self):
        return f"{self.name.capitalize()}\nHealth: {self.health}\nGender: {self.gender.capitalize()}\nNature: {self.nature.capitalize()}"
    def __repr__(self):
        return f"\n{self.name.capitalize()}\nHealth: {self.health}\nGender: {self.gender.capitalize()}\nNature: {self.nature.capitalize()}\n"
    def attack(self):
        value = math.floor(random.random() * 100)
        if value <= 40:
            return 25
        elif value <= 90:
            return 40
        else:
            return 100
    

class Player:
    def __init__(self, name, gender, nature, money):
        self.name = name;
        self.gender = gender
        self.nature = nature
        self.money = money
        self.bag = {"Health Potions": 0, "Pokeball":0}
        self.pokemon = []
    def __str__(self):
        return f"{self.name.capitalize()}\nGender: {self.gender.capitalize()}\nNature: {self.nature.capitalize()}\nMoney: ${self.money}"
    def print_bag(self):
        return str(self.bag)
    def print_pokemon(self):
        print(",".join([x.name for x in self.pokemon]))
    def add_pokemon(self, pokemon):
        self.pokemon.append(pokemon)

class CPU_Trainer:
    def __init__(self, name, money):
        self.name = name;
        self.money = money;
        self.pokemon = []



class Store:
    def __init__(self):
        self.items = {
            "Health Potions": {
                "cost": 500,
                "stock": 5
            },
            "Pokeball": {
                "cost": 250,
                "stock": 10
            }
        }
    def __str__(self):
        return str(self.items)

    def buy(self, item, player):
        if item in self.items:
            cost = self.items[item]['cost']
            if player.money >= cost:
                player.money -= cost
                player.bag[item] += 1
                self.items[item]['stock'] -= 1
            else: 
                print(f"You do not have enough money to buy {item}")
            return

class Grid_Tiles:
    def __init__(self, terrain):
        self.terrain_types = ['grass', 'store', 'trainer', 'pokemon', 'player']
        self.terrain = self.terrain_types[terrain]
    def convert_terrain_to_emoji(self):
        if self.terrain == 'grass':
            return "🌴"
        elif self.terrain == 'store':
            return "🏪"
        elif self.terrain == 'trainer':
            return "🦸"
        elif self.terrain == "pokemon":
            return "👹"
        elif self.terrain == "player":
            return "<🏃>"
        else:
            return ""
    def __str__(self):
        return self.convert_terrain_to_emoji()
    def __repr__(self):
        return f"\nTerrain: {self.terrain}, Representation:{self.convert_terrain_to_emoji()}\n"




class Grid:
    def __init__(self, row, col):
        trainer = math.floor(math.sqrt(row + col))
        pokemon = trainer * 2
        self.grid = self.create_grid(row, col, 1, trainer, pokemon, 1 )
    
    def create_grid(self, row, col, store, trainer, pokemon, player):
        #generates a random row and col
        def gen_rand_row_col(row, col):
            return [math.floor(random.random() * row), math.floor(random.random() * col)]

        def add_element(base, element):
            x, y = gen_rand_row_col(row, col)
            element_on_grid = {
                "store": 1,
                "trainer": 2, 
                "pokemon": 3, 
                "player": 4,
            }

            #makes sure the grid tile is grass
            while base[x][y] != 0:
                x, y = gen_rand_row_col(row, col)

            #places the element in a random place
            if x >= 0 and x < row and y >= 0 and y < col:
                base[x][y] = element_on_grid[element]
            return base

        
        base = [[0 for _ in range(row)] for _ in range(col)]
        for i in range(store):
            base = add_element(base, "store")
        for i in range(trainer):
            base = add_element(base, "trainer")
        for i in range(pokemon):
            base = add_element(base, "pokemon")
        base = add_element(base, "player")
    
        new_grid = []
        for row in base:
            temp_grid = []
            for col in row:
                tile = Grid_Tiles(col)
                temp_grid.append(tile)
            new_grid.append(temp_grid)
        return new_grid
    
    def __str__(self):
        top = " "+"".join(["---" for x in range(len(self.grid))])
        grid_string = top + "\n"
        for i, row in enumerate(self.grid):
            
            for j, col in enumerate(row):
                if j == 0:
                    grid_string += "|"
                grid_string += f" {col}"
                if j == len(self.grid[0]) - 1:
                    grid_string += "|"
            grid_string += "\n"
        
        return grid_string[:-1] + "\n" + top


def main():
    collection = [Pokemon(x["name"],x["health"],x["gender"] ,x["nature"]) for x in game_pokemon]
    alan = Player('Alan', 'male', 'angry', 1000)
    pika= starter_pokemon[0]
    alan.add_pokemon(Pokemon(pika['name'], pika['health'], pika['gender'], pika['nature']))
    grid = Grid(15, 15)
    print(grid)
    


if __name__ == '__main__':
    main()