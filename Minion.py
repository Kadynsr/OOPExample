# This class needs to inherit the attributes and behaviors of the card class
# A Minion object is a Card
# Child Class -- derived class
from Card import Card
class Minion(Card):
    # attribute cots and name
    # inherits cost and name from parent class Card
    def __init__(self, cost, name, damage, life):
        Card.__init__(self, cost, name)
        #assign parameters to the object
        self.damage = damage
        self.life = life

    def printMinionInfo(self):
        print('The card name: ' + self.name)
        print('The card cost: ' + str(self.cost))
        print('damage: ' + str(self.damage))
        print('life: ' + str(self.life))