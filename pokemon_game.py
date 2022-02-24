import random
import math
import keyboard


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

def selection_terminal(choices, message):
    def display_state(select):
        print(message)
        display_string = ""
        for i, row in enumerate(choices):
            if i == select:
                display_string += f"(^) {row}\n"
            else:
                display_string += f"( ) {row}\n"
        
        print(display_string)
        
    select = 0
    display_state(select)

    while True:
        # Wait for the next event.
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN and event.name == 'up':
            select -= 1
            if select < 0:
                select = len(choices) - 1
            display_state(select)
        if event.event_type == keyboard.KEY_DOWN and event.name == 'down':
            select += 1
            if select > len(choices) - 1:
                select = 0
            display_state(select)
        if event.event_type == keyboard.KEY_DOWN and event.name == 'space':
            return select
        if event.event_type == keyboard.KEY_DOWN and event.name == 'esc':
            return -1
        if keyboard.is_pressed("ctrl + c"):
            break


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
        bag_string = "Bag\n"
        for k, v in self.bag.items():
            bag_string += f"\t{k}: {v} \n"
        print(bag_string[:-1])
    def print_pokemon(self):
        print("Pokemon:")
        pokemon_string = ""
        for p in self.pokemon:
            pokemon_string += f"\n\t{p.name}\n\tHealth: {p.health}\n\tGender: {p.gender}\n\tNature: {p.nature}\n"
        print(pokemon_string)
        # print(",".join([x.name for x in self.pokemon]))
    def add_pokemon(self, pokemon):
        self.pokemon.append(pokemon)
    def add_item(self, item):
        if item in self.bag:
            self.bag[item] += 1


class CPU_Trainer:
    def __init__(self, name, money):
        self.name = name;
        self.money = money;
        self.pokemon = []



class Store:
    def __init__(self):
        self.items = [
            {"Health Potions": {
                "cost": 500,
                "stock": 5
            }},
            {"Pokeball": {
                "cost": 250,
                "stock": 10
            }}
        ]
    def __str__(self):
        return str(self.items)

    def buy(self, item, player):
        for inven in self.items:
            if item in inven:
                cost = inven[item]['cost']
                if player.money >= cost:
                    player.money -= cost
                    player.add_item(item)
                    inven[item]['stock']-= 1
                    print(f"Congrats, you have brought one {item}")
                else: 
                    print(f"You do not have enough money to buy {item}")

class Grid_Tiles:
    def __init__(self, terrain, gender):
        self.terrain_types = ['grass', 'store', 'trainer', 'pokemon', 'pokeball','player']
        self.terrain = self.terrain_types[terrain]
        self.gender = gender
    def convert_terrain_to_emoji(self):
        if self.terrain == 'grass':
            return "🌾"
        elif self.terrain == 'store':
            return "🏪"
        elif self.terrain == 'trainer':
            return "🦸"
        elif self.terrain == "pokemon":
            return "👹"
        elif self.terrain == "pokeball":
            return "🎈"
        elif self.terrain == "player":
            if self.gender == "M":
                return "[🏃]"
            else:
                return "[🏃]"
        else:
            return ""
    def __str__(self):
        return self.convert_terrain_to_emoji()
    def __repr__(self):
        return f"\nTerrain: {self.terrain}, Representation:{self.convert_terrain_to_emoji()}\n"




class Grid:
    def __init__(self, row, col, player):
        self.win = 0
        self.lose = 0


        self.store_position = []
        self.player_position = []
        self.store = Store()
        self.player = player
        self.pokemons = [Pokemon(x["name"],x["health"],x["gender"] ,x["nature"]) for x in game_pokemon]
        self.num = {
            "store": 1,
            "trainer": 2, 
            "pokemon": 3, 
            "pokeball": 4,
            "player": 5,
        }


        trainer = math.floor(math.sqrt(row + col))
        pokemon = trainer * 2
        self.grid = self.create_grid(row, col, 1, trainer, pokemon, pokemon - 2 ,1 )
    
    def create_grid(self, row, col, store, trainer, pokemon, pokeball, player):
        #generates a random row and col
        def gen_rand_row_col(row, col):
            return [math.floor(random.random() * row), math.floor(random.random() * col)]

        def add_element(base, element):
            x, y = gen_rand_row_col(row, col)
            
            #makes sure the grid tile is grass
            while base[x][y] != 0:
                x, y = gen_rand_row_col(row, col)

            #places the element in a random place
            if x >= 0 and x < row and y >= 0 and y < col:
                base[x][y] = self.num[element]
                if element == 'store':
                    self.store_position = [x,y]
                elif element == 'player':
                    self.player_position = [x,y]
            return base

        
        base = [[0 for _ in range(row)] for _ in range(col)]
        for _ in range(store):
            base = add_element(base, "store")
        for _ in range(trainer):
            base = add_element(base, "trainer")
        for _ in range(pokemon):
            base = add_element(base, "pokemon")
        for _ in range(pokeball):
            base = add_element(base, "pokeball")
        for _ in range(player):
            base = add_element(base, "player")  

        
        return base
    
    def __str__(self):
        top = " "+"".join(["---" for x in range(len(self.grid))])
        grid_string = top + "\n"
        for row in self.grid:
            for j, col in enumerate(row):
                tile = Grid_Tiles(col, self.player.gender)
                if j == 0:
                    grid_string += "|"
                grid_string += f"{tile} "
                if j == len(self.grid[0]) - 1:
                    grid_string += "|"
            grid_string += "\n"
        
        return grid_string[:-1] + "\n" + top

    

    def handle_terrain(self, row, col, player_num):
        position = self.grid[row][col]
        if position == self.num['pokeball']:
            self.player.add_item('Pokeball')
            self.grid[row][col] = player_num
            print("You have collected a pokeball!!!")
        elif position == self.num['store']:
            self.grid[row][col] = player_num
            enter = selection_terminal(["Yes", "No"], "Would you like to enter the store?")
            if enter == 0:
                print(self.player)
                items =[]
                for item in self.store.items:
                    item_name = list(item.keys())[0]
                    cost = item[item_name]['cost']
                    stock = item[item_name]['stock']
                    items.append([f"{item_name}, Cost: {cost}, Stock: {stock}", item_name])

                select_items = selection_terminal([x[0] for x in items], "What item would you like to buy?")
                if select_items != -1:
                    brought_item = items[select_items][1]
                    self.store.buy(brought_item, self.player)
                else: 
                    return
            elif enter == -1:
                return
        elif position == self.num['pokemon']:
            
            def battle_screen(enemy, pokemon, e_health, p_health):
                def health_bar(curr_health, max_health):
                    if curr_health <= max_health:
                        max_bar = math.floor((max_health / 10) * 2)
                        health_lost  = math.floor(((max_health - curr_health) / 10) * 2)
                        bar = ["=" for x in range(max_bar)]
                        for i in range(health_lost):
                            bar[i] = " "
                        bar = "".join(bar[::-1])
                        return f"({bar}) {curr_health} hp"
                    return ""

                if e_health >= 0 and p_health >= 0:
                    print(enemy.name)
                    print(health_bar(e_health, enemy.health))
                    print("\n")
                    print(health_bar(p_health, pokemon.health))
                    print(pokemon.name)
                    print("\n")
                pass;

                
            enemy_pokemon = self.pokemons.pop(math.floor(random.random() * len(self.pokemons)))
            print(f"A random {enemy_pokemon.name} appears!\n")
            print(enemy_pokemon)
            print()

            used_pokemon = []
            while True:
                player_pokemon = self.player.pokemon
                if len(player_pokemon) == len(used_pokemon):
                    self.lose +=1
                    print("You have lost this game. :(")
                    return 
                select_pokemon = selection_terminal([x.name for x in player_pokemon if x.name not in used_pokemon], "Select your pokemon.")
                if select_pokemon != -1:
                    battle_pokemon = player_pokemon[select_pokemon]
                    battle_screen(enemy_pokemon, battle_pokemon, enemy_pokemon.health, battle_pokemon.health)
                    battle_pokemon_health = battle_pokemon.health
                    enemy_pokemon_health = enemy_pokemon.health


                    while battle_pokemon_health > 0 or enemy_pokemon_health > 0:
                        player_action = selection_terminal(["Attack", "Items", "Run"], "Select Action")
                        if player_action != -1:
                            if player_action == 0:
                                battle_attack = battle_pokemon.attack()
                                print(f"{battle_pokemon.name} has attacked. It has dealt {battle_attack} damage.")
                                enemy_pokemon_health -= battle_attack
                                if enemy_pokemon_health <= 0:
                                    enemy_pokemon_health = 0
                                    print("You have won this battle!!!")
                                    battle_screen(enemy_pokemon, battle_pokemon, enemy_pokemon_health, battle_pokemon_health)
                                    return
                            elif player_action == 1:
                                items = [f"{k}, Stock: {v} \n" for k, v in list(self.player.bag.items())if v > 0]
                                if len(items) != 0:
                                    select_items = selection_terminal(items, "Select item you would like to use.")

                                    if select_items != -1:
                                        use_item = items[select_items].split(",")[0]
                                        if use_item == "Health Potions": #health potion
                                            self.player.bag[use_item] -= 1
                                            print(f"Used health potion. Restored hp to {battle_pokemon.health}")
                                            battle_pokemon_health = battle_pokemon.health
                                        elif use_item == 'Pokeball': #pokeball
                                            self.player.bag[use_item] -= 1
                                            chance_to_catch = math.floor(random.random() * 100)
                                            print("Using pokeball")
                                            if chance_to_catch <= 20:
                                                print("Congrats, you have captured the pokemon!!!")
                                                self.player.add_pokemon(enemy_pokemon)
                                                return
                                            else:
                                                print("The pokemon has escaped your pokeball. :(\n")
                                    else:
                                        return
                                else:
                                    print("You have no items. Go to the store if you would like to purchase some items.\n")
                            elif player_action == 2:
                                chance_to_run = math.floor(random.random() * 100)
                                if chance_to_run <= 20:
                                    print("You have fled this fight.")
                                    return;
                        else:
                            return
                        enemy_attack = enemy_pokemon.attack()
                        battle_pokemon_health -= enemy_attack
                        print(f"The wild {enemy_pokemon.name} attacks. It has dealt {enemy_attack} damage")
                        if battle_pokemon_health <= 0:
                            used_pokemon.append(battle_pokemon.name)
                            battle_pokemon_health = 0
                            battle_screen(enemy_pokemon, battle_pokemon, enemy_pokemon_health, battle_pokemon_health)
                            break;

                        battle_screen(enemy_pokemon, battle_pokemon, enemy_pokemon_health, battle_pokemon_health)
                else:
                    return
           


            self.grid[row][col] = player_num
        else:
            self.grid[row][col] = player_num


    def updatePosition(self, direction):
        x, y = self.player_position
        self.grid[x][y] = 0
        if direction == "up":
            x -= 1
            if x < 0 or x > len(self.grid[0]) - 1:
                x += 1
        if direction == "down":
            x += 1
            if x < 0 or x > len(self.grid[0]) - 1:
                x -= 1
        if direction == "left":
            y -= 1
            if y < 0 or y > len(self.grid) - 1:
                y += 1
        if direction == "right":
            y += 1
            if y < 0 or y > len(self.grid) - 1:
                y -= 1
        
        self.player_position = [x, y]
        if self.grid[x][y] != 0:
            self.handle_terrain(x, y, self.num['player'])
        else:
            self.grid[x][y] = self.num['player']

        store_x, store_y = self.store_position
        if self.grid[store_x][store_y] != self.num['player']:
            self.grid[store_x][store_y] = self.num['store']

            
def start_game():
    name = input("Enter your trainer name: ").strip()

    #user selects gender, male or female
    gender = ""
    while True:
        gender = input("Select the gender of your trainer (M for male and F for female):").capitalize().strip()
        if gender == "M" or  gender == "F":
            break;
  
    #user select their trainer's nature
    natures = ["kind", "mean", "funny", "sad", "quiet", "loud", "aggressive"]
    nature_num = selection_terminal(natures, "Select your trainer's nature. Use [up and down arrow keys] to navigate and [space] to select")

    if nature_num == -1:
        return

    #add user data to pokemon class
    player = Player(name, gender, natures[nature_num] , 500)
    
    #select starter pokemon and adds it to the user
    number = selection_terminal([x['name'] for x in starter_pokemon], "Select your starter pokemon. Use [up and down arrow keys] to navigate and [space] to select")

    if number == -1:
        return
    first = starter_pokemon[number]
    player.add_pokemon(Pokemon(first['name'], first['health'], first['gender'], first['nature']))
    
    #create grid
    grid = Grid(12, 12, player)
    print(grid)

    while grid.win + grid.lose == 0:
        # Wait for the next event.
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN and event.name == 'up':
            grid.updatePosition("up")
            print(grid)
        if event.event_type == keyboard.KEY_DOWN and event.name == 'down':
            grid.updatePosition("down")
            print(grid)
        if event.event_type == keyboard.KEY_DOWN and event.name == 'left':
            grid.updatePosition("left")
            print(grid)
        if event.event_type == keyboard.KEY_DOWN and event.name == 'right':    
            grid.updatePosition("right")
            print(grid)
        if event.event_type == keyboard.KEY_DOWN and event.name == 'm':    
            current_player = grid.player
            print(current_player)
            current_player.print_bag()
            current_player.print_pokemon()
        if event.event_type == keyboard.KEY_DOWN and event.name == 'esc': 
            print(grid)       
            
        if keyboard.is_pressed("ctrl + c"):
            break


    


def main():
    start_game()
   

if __name__ == '__main__':
    main()