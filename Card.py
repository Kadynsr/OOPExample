#Card class is a blueprint of the Card object
class Card:

#Attributes
    def __init__ (self, cost, name):
        self.cost = cost
        self.name = name

    def printCardInfo(self):
        print('The card name: ' + self.name)
        print('The card cost: ' + str(self.cost))