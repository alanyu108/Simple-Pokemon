import random
import math
import keyboard


starter_pokemon = [
    {
        "name": "Pikachu ⚡", 
        "nature": "electric", 
        "health": 100, 
        "gender": "male"
    }, 
    {
        "name": "Charmander 🔥", 
        "nature": "fire", 
        "health": 100, 
        "gender": "male"
    },
    {
        "name": "Bulbasaur 🌾", 
        "nature": "grass", 
        "health": 100, 
        "gender": "male"
    }, 
    {
        "name": "Squirtle 🌊", 
        "nature": "water", 
        "health": 100, 
        "gender": "female"
    }
]

#list of all the pokemon that will be in the game
game_pokemon = [{'name': 'Oshawott', 'nature': 'Water', 'gender': 'female', 'health': 100}, {'name': 'Seaking', 'nature': 'Water', 'gender': 'female', 'health': 100}, {'name': 'Furret', 'nature': 'Normal', 'gender': 'male', 'health': 75}, {'name': 'Shelmet', 'nature': 'Bug', 'gender': 'male', 'health': 100}, {'name': 'Pancham', 'nature': 'Fighting', 'gender': 'female', 'health': 75}, {'name': 'Geodude', 'nature': 'Rock', 'gender': 'female', 'health': 75}, {'name': 'Exploud', 'nature': 'Normal', 'gender': 'female', 'health': 75}, {'name': 'Tranquill', 'nature': 'Normal', 'gender': 'female', 'health': 75}, {'name': 'Porygon-Z', 'nature': 'Normal', 'gender': 'female', 'health': 100}, {'name': 'Seviper', 'nature': 'Poison', 'gender': 'male', 'health': 100}]

#allows users to select a choice from a given prompt
def selection_terminal(choices, message):

    #displays the prompt
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
        self.battle_health = health
        self.gender = gender
        self.nature = nature
    def __str__(self):
        return f"{self.name.capitalize()}\nHealth: {self.health}\nGender: {self.gender.capitalize()}\nNature: {self.nature.capitalize()}"
    def __repr__(self):
        return f"\n{self.name.capitalize()}\nHealth: {self.health}\nGender: {self.gender.capitalize()}\nNature: {self.nature.capitalize()}\n"

    #each pokemon has the same attack ability with certain chances to deal more damage
    def attack(self):
        value = random.randint(0, 100)
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
        return f"{self.name.capitalize()}\nGender: {self.gender.capitalize()}\nNature: {self.nature.capitalize()}\nMoney: ${self.money}\n"


    def print_bag(self):
        bag_string = "Bag\n"
        for k, v in self.bag.items():
            bag_string += f"\t{k}: {v} \n"
        print(bag_string[:-1])

    def print_pokemon(self):
        print("Pokemon:")
        pokemon_string = ""
        for p in self.pokemon:
            pokemon_string += f"\n\t{p.name}\n\tHealth: {p.battle_health}\n\tGender: {p.gender}\n\tNature: {p.nature}\n"
        print(pokemon_string)

    #add pokemon to user's bag
    def add_pokemon(self, pokemon):
        self.pokemon.append(pokemon)

    #add item to user's bag
    def add_item(self, item):
        if item in self.bag:
            self.bag[item] += 1


class CPU_Trainer:
    def __init__(self, name):
        self.name = name;
        self.pokemon = []

        #the prize money is between 500 and 1500 randomly generated
        self.money = random.randint(500, 1500);
    def remove(self, name):
        self.pokemon = [x for x in self.pokemon if x.name != name]
    def __str__(self):
        print(f"\nTrainer {self.name.capitalize()}\nPrize: ${self.money}")
        print("Pokemon:")
        pokemon_string = ""
        for p in self.pokemon:
            pokemon_string += f"\t{p.name}\n\tHealth: {p.health}\n\tGender: {p.gender}\n\tNature: {p.nature}\n\n"
        print(pokemon_string[:-1])
        return ""
        
        

#pokemon store where players can buy items and heal pokemen as well
class Store:
    def __init__(self):
        self.items = [
            {"Health Potions": {
                "cost": 250,
                "stock": 3,
                "description":"When in battle, use this item to restore ur pokemon's health to full",
            }},
            {"Pokeball": {
                "cost": 250,
                "stock": 2,
                "description":"When in battle with a wild pokemon and not trainers, use this item and you will have a 20% chance of capturing the pokemon",
            }},
            {"Healing Center": {
                "cost": 100,
                "stock": "Infinite",
                "description":"Restore one of your pokemon's health to full",
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
                    print(f"You do not have enough money. :(")

    def healing_center(self, pokemons):
        select_pokemon = selection_terminal([x.name for x in pokemons], "Which pokemon would you like to heal?")
        if select_pokemon != -1:
            for pokemon in pokemons:
                if pokemon.name == pokemons[select_pokemon].name:
                    pokemon.battle_health = pokemon.health
                    print(f"{pokemon.name} has been healed to {pokemon.health} hp!!!")
            return pokemons
        else: 
            return   

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


def shuffle_arr(arr):
    random.shuffle(arr)
    return arr

class Grid:
    def __init__(self, row, col, player):
        #win and lose counters
        self.win = 0
        self.lose = 0

        self.store_position = []
        self.player_position = []
        self.trainer_position = []

        self.store = Store()
        self.player = player
        self.pokemons = shuffle_arr([Pokemon(x["name"],x["health"],x["gender"] ,x["nature"]) for x in game_pokemon])
        self.num = {
            "store": 1,
            "trainer": 2, 
            "pokemon": 3, 
            "pokeball": 4,
            "player": 5,
        }

        # number of trainers and pokemon that will be on the grid given the grid dimensions
        trainer = math.floor(math.sqrt(row + col))
        pokemon = trainer * 2
        self.grid = self.create_grid(row, col, 1, trainer, pokemon, pokemon - 2 ,1 )
    
    #generates all the terrain for the grid
    def create_grid(self, row, col, store, trainer, pokemon, pokeball, player):
        #generates a random row and col
        def gen_rand_row_col(row, col):
            return [random.randint(0, row - 1), random.randint(0, col - 1)]

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
                elif element == 'trainer':
                    self.trainer_position.append([x, y])
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
        win_counter = f"Win Counter: {self.win}\n"
        top = " "+"".join(["---" for x in range(len(self.grid))])
        grid_string = win_counter + top + "\n"
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

    #the battle sequence when the player encounters a trainer or wild pokemon
    def battle_stage(self, player_pokemon, enemy_pokemon, battle_type):
        #the standard display with hp and the pokemon's names
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

        print("".join(["---" for x in range(15)]))
        if battle_type == "pokemon":
            print(f"A random {enemy_pokemon.name} appears!\n")
            print(enemy_pokemon)
            print()
        elif battle_type == "trainer":
            print(f"The trainer summons {enemy_pokemon.name}!!!\n")
            print(enemy_pokemon)
            print()

        #keeps track of the number of pokemon the player uses
        used_pokemon = []
        while True:
            #if all of the player's pokemon have died, they lose
            if len(player_pokemon) == len(used_pokemon):
                return "lose" 

            #user selects their pokemon
            select_pokemon = selection_terminal([x.name for x in player_pokemon if x.name not in used_pokemon], "Select your pokemon.")
            if select_pokemon != -1:
                battle_pokemon = player_pokemon[select_pokemon]

                #battle start
                while battle_pokemon.battle_health > 0 or enemy_pokemon.battle_health > 0:
                    print("".join(["---" for x in range(15)]))
                    battle_screen(enemy_pokemon, battle_pokemon, enemy_pokemon.battle_health, battle_pokemon.battle_health)

                    #Selection menu for player to attack, use items, or try to flee
                    player_action = selection_terminal(["Attack", "Items", "Run"], "Select Action")
                    if player_action != -1:

                        #attack
                        if player_action == 0:
                            battle_attack = battle_pokemon.attack()
                            print(f"{battle_pokemon.name} has attacked. It has dealt {battle_attack} damage.")
                            enemy_pokemon.battle_health -= battle_attack
                            if enemy_pokemon.battle_health <= 0:
                                enemy_pokemon.battle_health = 0
                                print("You have won this battle!!!")
                                battle_screen(enemy_pokemon, battle_pokemon, enemy_pokemon.battle_health, battle_pokemon.battle_health)
                                return enemy_pokemon.name
                        #use items
                        elif player_action == 1:
                            items = [f"{k}, Stock: {v} \n" for k, v in list(self.player.bag.items())if v > 0]
                            if len(items) != 0:
                                select_items = selection_terminal(items, "Select item you would like to use.")

                                if select_items != -1:
                                    #retrieve all items in the player's pouch
                                    use_item = items[select_items].split(",")[0]
                                    if use_item == "Health Potions": #health potion
                                        self.player.bag[use_item] -= 1
                                        print(f"Used health potion. Restored hp to {battle_pokemon.health}")
                                        battle_pokemon.battle_health = battle_pokemon.health
                                    elif use_item == 'Pokeball': #pokeball
                                        #can only use pokeball on wild pokemon
                                        if battle_type != "trainer":
                                            self.player.bag[use_item] -= 1
                                            chance_to_catch = random.randint(0, 100)
                                            print(f"Using pokeball")
                                            if chance_to_catch <= 20:
                                                print("Congrats, you have captured the pokemon!!!")
                                                self.win += 1
                                                self.player.add_pokemon(enemy_pokemon)
                                                return
                                            else:
                                                print("The pokemon has escaped your pokeball. :(\n")
                                        else:
                                            print("Cannot use pokeballs in trainer battle.")
                                            continue;
                                else:
                                    return
                            else:
                                print("You have no items. Go to the store if you would like to purchase some items.\n")
                                continue

                        #flee or run
                        elif player_action == 2:
                            chance_to_run = random.randint(0, 100)
                            if chance_to_run <= 20:
                                print("You have fled this fight.")
                                return "fled";
                    else:
                        return
                    
                    #enemy's turn, default to just attack
                    enemy_attack = enemy_pokemon.attack()
                    battle_pokemon.battle_health -= enemy_attack
                    print(f"The wild {enemy_pokemon.name} attacks. It has dealt {enemy_attack} damage")
                    if battle_pokemon.battle_health <= 0:
                        used_pokemon.append(battle_pokemon.name)
                        battle_pokemon.battle_health = 0
                        battle_screen(enemy_pokemon, battle_pokemon, enemy_pokemon.battle_health, battle_pokemon.battle_health)
                        break;
            else:
                return
            
    #when user walks anywhere but grass
    def handle_terrain(self, row, col, player_num):
        position = self.grid[row][col]

        #player collecting pokeballs
        if position == self.num['pokeball']:
            self.player.add_item('Pokeball')
            self.grid[row][col] = player_num
            print("You have collected a pokeball!!!")
        #player heads to the store
        elif position == self.num['store']:
            self.grid[row][col] = player_num
            enter = selection_terminal(["Yes", "No"], "Would you like to enter the store?")
            if enter == 0:
                print("".join(["---" for x in range(15)]))
                print(self.player)

                #displays all the items that are in the store
                items =[]
                for item in self.store.items:
                    item_name = list(item.keys())[0]
                    cost = item[item_name]['cost']
                    stock = item[item_name]['stock']
                    items.append([f"{item_name}, Cost: {cost}, Stock: {stock}", item_name])

                #user buys items
                select_items = selection_terminal([x[0] for x in items], "What item would you like to buy?")
                print("".join(["---" for x in range(15)]))
                if select_items != -1:
                    brought_item = items[select_items][1]
                    if brought_item == "Healing Center":
                        self.player.pokemon = self.store.healing_center(self.player.pokemon)
                    else:
                        self.store.buy(brought_item, self.player)
                else: 
                    return
            elif enter == -1:
                return
        #player encounters a wild pokemon
        elif position == self.num['pokemon']:
            self.grid[row][col] = player_num
            enemy_pokemon = self.pokemons.pop()
            state = self.battle_stage(self.player.pokemon, enemy_pokemon, "pokemon")
            if state == "lose":
                self.lose += 1
            elif state == "flee":
                self.pokemons.append(enemy_pokemon)
            else:
                self.win += 1
        #player encounters a trainer        
        elif position == self.num['trainer']:
            trainer = CPU_Trainer("Bot")
            fight_trainer = selection_terminal(["Yes", "No"], f"Would you like to fight this trainer {trainer.name}?")
            if fight_trainer != -1:
                if fight_trainer == 0:
                    self.grid[row][col] = player_num

                    #the number of pokemon is dependent on the trainer's money or prize
                    pokemon_num = 0
                    if trainer.money <= 750:
                        pokemon_num += 1
                    elif trainer.money <= 1200:
                        pokemon_num += 2
                    else:
                        pokemon_num += 3
                    
                    for _ in range(pokemon_num):
                        trainer.pokemon.append(self.pokemons.pop())
                    print(trainer)

                    #fighting the trainer
                    while len(trainer.pokemon) != 0:
                        battle_state = self.battle_stage(self.player.pokemon, trainer.pokemon[-1], "trainer")
                        if battle_state == "lose":
                            print("You have been defeated by the trainer. :(")
                            self.lose += 1
                            return
                        else:
                            defeated_pokemon = battle_state
                            trainer.remove(defeated_pokemon)

                    #trainer is defeated
                    if len(trainer.pokemon) == 0:
                        print(f"Congrats, you have beaten trainer {trainer.name}.\n You have won ${trainer.money}.\n")
                        self.player.money += trainer.money
                        self.trainer_position = [ x for x in self.trainer_position if x[0] != row and x[1] != col ]
                        self.win += len(trainer.pokemon)
                else: 
                    self.grid[row][col] = player_num
                    return
            else:
                return
        else:
            self.grid[row][col] = player_num

    #updated the position of the player whenever they move
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

        for x, y in self.trainer_position:
            if self.grid[x][y] != self.num['player']:
                self.grid[x][y] = self.num['trainer']

#game loop
def run_game(player):
    #create grid
    grid = Grid(12, 12, player)
    print(grid)

    #game state
    while True:
        # Wait for the next event.
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN and event.name == 'up':
            grid.updatePosition("up")
            #lose condition
            if grid.lose >= 1:   
                print("You have lost this game :(")
                break;
            print(grid)
        if event.event_type == keyboard.KEY_DOWN and event.name == 'down':
            grid.updatePosition("down")
            if grid.lose >= 1:   
                print("You have lost this game :(")
                break;
            print(grid)
        if event.event_type == keyboard.KEY_DOWN and event.name == 'left':
            grid.updatePosition("left")
            if grid.lose >= 1:   
                print("You have lost this game :(")
                break;
            print(grid)
        if event.event_type == keyboard.KEY_DOWN and event.name == 'right':    
            grid.updatePosition("right")
            if grid.lose >= 1:   
                print("You have lost this game :(")
                break;
            print(grid)
        # if event.event_type == keyboard.KEY_DOWN and event.name == 'esc': 
        #     print(grid)    
        
        #win condition 
        if grid.win >= 4:   
            print("Congrats, you have won this game!!!!")
            break;
        
        #menu that displays player info
        if event.event_type == keyboard.KEY_DOWN and event.name == 'm':    
            current_player = grid.player
            print(current_player)
            current_player.print_bag()
            current_player.print_pokemon()
            
        if keyboard.is_pressed("ctrl + c"):
            break

#start of game to use player created            
def start_game():
    name = input("Enter your trainer name: ").strip()

    #user selects gender, male or female
    gender = ["Male", "Female"]
    gender_num = selection_terminal(gender, "Select your gender. Use [UP and DOWN arrow keys] to navigate and [SPACE] to select")
    if gender_num < 0:
        return 
  
    #user select their trainer's nature
    natures = ["kind", "mean", "funny", "sad", "quiet", "loud", "aggressive"]
    nature_num = selection_terminal(natures, "Select your trainer's nature. Use [UP and DOWN arrow keys] to navigate and [SPACE] to select")

    if nature_num < -1:
        return

    #add user data to pokemon class
    player = Player(name, gender[gender_num], natures[nature_num] , 500)
    
    #select starter pokemon and adds it to the user
    number = selection_terminal([x['name'] for x in starter_pokemon], "Select your starter pokemon. Use [UP and DOWN arrow keys] to navigate and [SPACE] to select")

    if number < -1:
        return
    first = starter_pokemon[number]
    player.add_pokemon(Pokemon(first['name'], first['health'], first['gender'], first['nature']))
    display_player = "[🏃]" if player.gender == "Male" else "[🏃]"
    print(f"Welcome to Simple Pokemon, {player.name} !!!")
    print("To navigate around the grid, use the arrow keys and press [M] to check player info.")
    print("Familiarize these symbols as they are pretty common on the playing grid. \n")
    print("🌾- grass         , player can move anywhere that has grass")
    print("🏪- pokemon store , contains purchasable items that can be useful in battle")
    print("🦸- trainer       , defeat trainers to obtain prizes, trainers may have one or more pokemon")
    print("👹- pokemon       , wild pokemon")
    print("🎈- pokeball      , item that can be found on the ground that can be used to capture wild pokemon")
    print(f"{display_player}- you, the player")
    print("\nTo win this game, defeat or catch four pokemon. \nIf all of your pokemon die in battle, I'm sorry but you have lost.\n")
    

    play = selection_terminal(["Yes", "No"], "Are you ready to start?")
    if play == 0:
        run_game(player)
    else: 
        return

def main():
     start_game()
     
 
if __name__ == '__main__':
    main()
