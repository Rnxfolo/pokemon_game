from cmath import e
import pokemon
import random

pokemon_list = ["Charmander","Squirtle","Bulbasaur"]
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

        
print("Your team selection is: ")

for poke in user_Selection:
    print(f"Name: {poke.get_Name()} \nLVL: {poke.get_Level()} \nHP: {poke.get_Health()} \n")