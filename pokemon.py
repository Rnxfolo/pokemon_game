#Pokemon Class

class Pokemon:

    def __init__(self,name,level,health):
        self.name = name
        self.level = level
        self.health = health
        
    
    def change_Name(self, name):
        self.name = name
    
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
