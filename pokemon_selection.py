import pokemon
import random

pokemon_list = ["Charmander","Squirtle","Bulbasaur"]

def pokemonSelection():
    user_Selection = []

    for p in pokemon_list:
        print(p)

    while len(user_Selection) < 2:
        user_choice = input("Make a selection: ")
        user_choice.capitalize
        
        if user_choice == "Charmander": 
            user_Pokemon = pokemon.FirePokemon(user_choice,random.randint(1,101),random.randint(20,255))
            user_Selection.append(user_Pokemon)
        
        if user_choice == "Squirtle":
            user_Pokemon = pokemon.WaterPokemon(user_choice,random.randint(1,101),random.randint(20,255))
            user_Selection.append(user_Pokemon)
        
        if user_choice == "Bulbasaur":
            user_Pokemon = pokemon.GrassPokemon(user_choice,random.randint(1,101),random.randint(20,255))
            user_Selection.append(user_Pokemon)

            
    print("Your team selection is: \n")

    for poke in user_Selection:
        print(f"Name: {poke.get_Name()} \nLVL: {poke.get_Level()} \nHP: {poke.get_Health()} \n")

def pokemonOpponentTeam():

    opponentTeam = []
    random_num = random.randint(0,len(pokemon_list)-1)

    while len(opponentTeam) < 2:
        opp_choice = pokemon_list[random_num]

        if opp_choice == "Charmander": 
            opp_Pokemon = pokemon.FirePokemon(opp_choice,random.randint(1,101),random.randint(20,255))
            opponentTeam.append(opp_Pokemon)
        
        if opp_choice == "Squirtle":
            opp_Pokemon = pokemon.WaterPokemon(opp_choice,random.randint(1,101),random.randint(20,255))
            opponentTeam.append(opp_Pokemon)
        
        if opp_choice == "Bulbasaur":
            opp_Pokemon = pokemon.GrassPokemon(opp_choice,random.randint(1,101),random.randint(20,255))
            opponentTeam.append(opp_Pokemon)

    for poke in opponentTeam:
        print(f"Name: {poke.get_Name()} \nLVL: {poke.get_Level()} \nHP: {poke.get_Health()} \n")

