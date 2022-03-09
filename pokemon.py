#Pokemon Class

class Pokemon:

    def __init__(self,name,level,health):
        self.name = name
        self.level = level
        self.health = health
        
    def get_Name(self):
        return self.name
    
    def change_Name(self, name):
        self.name = name
    
    def get_Level(self):
        return self.level
        
    def level_Up(self):
        self.level +=1

    def get_Health(self):
        return self.health
    
    def set_Health(self, health):
        self.health = health

    def calculate_damage(self,damage):
        self.health -= damage


#Testing Pokemon class verifing functions
#pikachu = Pokemon("Pikachu",20,100)
#pikachu.calculate_damage(20)
#print(pikachu.get_Health())

class FirePokemon(Pokemon):

    def __init__(self, name, level, health):
        super().__init__(name, level, health)
        self.type = "Fire"
    
    def tackle(self):
        self.attack = 5
    
class WaterPokemon(Pokemon):

    def __init__(self, name, level, health):
        super().__init__(name, level, health)
        self.type = "Water"
    
    def tackle(self):
        self.attack = 5

class GrassPokemon(Pokemon):

    def __init__(self, name, level, health):
        super().__init__(name, level, health)
        self.type = "Grass"
    
    def tackle(self):
        self.attack = 5


#userPokemon_1 = FirePokemon("Charmander",10,50)
#oppPokemon_1 = WaterPokemon("Squirtle",10,50)
#userPokemon_1.tackle()
#print(userPokemon_1.attack)
#oppPokemon_1.calculate_damage(userPokemon_1.attack)
#print(oppPokemon_1.get_Health())