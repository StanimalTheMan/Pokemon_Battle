from move import Move
from random import randint

class Pokemon():

    def __init__(self, pokemon_name, pokemon_type, pokemon_hp, moves):
        self._name = pokemon_name
        self._type = pokemon_type # will be a list in future as Pokemon can be both Water and Flying for example
        self._hp = pokemon_hp
        
        if moves is None:
            self._moves = [Move('Struggle', None, 'Pokemon attacks itself bc it doesn\'t know what to do.', 10, 1000)] # arbitrary large pp
        else:
            self._moves = moves
    
    def attack(self):
        move_num = randint(0, len(self._moves))
        print(self._name + " decided not to use " + self._moves[move_num] + " on other pokemon.")


class PlayerPokemon(Pokemon):

    def __init__(self, pokemon_name, pokemon_type, pokemon_hp, moves):
        super().__init__(pokemon_name, pokemon_type, pokemon_hp, moves)

    def attack(self, opponent):
        print("What will " + self._name + " do?")
        print()
        for move in self._moves:
            print(move.name)
        print()

        move = input()
        # Assume user enters right move
        print(self._name + " used " + move)
        opponent._hp -= move.base_damage
        
        if opponent._hp == 0:
            print(opponent._name + " fainted.")
            print("You won!")
        else:
            print(opponent._name + " has " + opponent._hp + " left.")

class EnemyPokemon(Pokemon):

    def __init__(self, pokemon_name, pokemon_type, pokemon_hp, moves):
        super().__init__(pokemon_name, pokemon_type, pokemon_hp, moves)
        


    

    
        


    