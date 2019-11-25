from Card import Card
from Minion import Minion

def main():
    # create the townCrier Card
    # cost = 1 and name = 'Town Crier'
    townCrier = Minion(1, 'TownCrier', 1, 2)
    redbandWasp = Minion(2, 'Redband Wasp', 1, 3)
    warpath = Card(2, 'Warpath')

    townCrier.printMinionInfo()
    redbandWasp.printMinionInfo()

if __name__=="__main__":
    main()