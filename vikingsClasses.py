import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health   #initializes the attribute health with the given value
        self.strength = strength #initializes the attribute strength with the given value
    
    def attack(self):   
        return self.strength #returns the strength of the given soldier as the attack power

    def receiveDamage(self, damage):     
        self.health -= damage #reduces the soldier's health by the damage amount received
        

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.health = health
        self.strength = strength #inherits attributes health and strength from Soldier class 
        self.name = name #initializes the name attribute with the given value
    
    def battleCry(self):
        return "Odin Owns You All!" #returns the Battle Cry of the viking

    def receiveDamage(self, damage): 
        self.health -= damage #reduces the viking's health by the damage amount received
        if self.health <= 0:  #if the vikings's health drops to 0 or below, it returns "{self.name} has died in act of combat." where {self.name} is the name of the affected viking
            return f"{self.name} has died in act of combat"
        else:
            return f"{self.name} has received {damage} points of damage"  #else, it returns a message indicating the damage received
# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength  #inherits attributes health and strength from super class Soldier

    def receiveDamage(self, damage):
        self.health -= damage #reduces the saxon's health by the damage amount received
        if self.health > 0: 
            return f"A Saxon has received {damage} points of damage"  #if the saxon is still alive, it returns a message indicating the damage receivedd
        else:
           return f"A Saxon has died in combat" #if the saxon's health drops to 0 or below, it returns "Saxon has died in act of combat."
        
# Davicente

class War():
    def __init__(self):
        self.vikingArmy = []  #initializes the vikingArmy list as empty
        self.saxonArmy = []   #initializes the saxonArmy list as empty

    def addViking(self, viking):
        self.vikingArmy.append(viking) #adds a Viking soldier to the vikingArmy
    
    def addSaxon(self, saxon): 
        self.saxonArmy.append(saxon) #adds a Saxon soldier to the saxonArmy
    
    def vikingAttack(self):
        attack_viking = random.choice(self.vikingArmy) #selects a random Viking from the vikingArmy
        attacked_saxon = random.choice(self.saxonArmy) #selects a random Saxon from the saxonArmy
        
        result = attacked_saxon.receiveDamage(attack_viking.strength)  #the saxon receives damage equal to the viking's attack power
        if attacked_saxon.health <= 0:
            self.saxonArmy.remove(attacked_saxon)                #if the result is 0 or less, the saxon is removed from the saxonArmy
        return result    

    def saxonAttack(self):
        attacked_viking = random.choice(self.vikingArmy) #selects a random Viking from the vikingArmy
        attack_saxon = random.choice(self.saxonArmy) #selects a random Saxon from the saxonArmy
        
        result = attacked_viking.receiveDamage(attack_saxon.strength)  #the viking receives damage equal to the saxon's attack power
        if attacked_viking.health <= 0:
            self.vikingArmy.remove(attacked_viking)  #if the result is 0 or less, the viking is removed from the vikingArmy
        return result   

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        if len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."

    pass
 

# #yop
# class War2:

#     def __init__(self):
#         # your code here

#     def addViking(self, Viking):
#         # your code here
    
#     def addSaxon(self, Saxon):
#         # your code here
    
#     def vikingAttack(self):
#         # your code here

#     def saxonAttack(self):
#         # your code here

#     def showStatus(self):
#         # your code here

#     pass


