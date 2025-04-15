from pakudex import Pakudex

pakudex: Pakudex
class MenuOption:
    def __init__(self, name: str, function = lambda : print("Function Not Implemented Yet")):
        self.name = name
        self.function = function

def listPakuri():
    global pakudex
    pakuris = pakudex.get_species_array()
    if(pakuris == None):
        print("No Pakuri in Pakudex yet!")
    else:
        print("Pakuri In Pakudex:")
        for i in range(len(pakuris)):
            print(str(i+1) + ". " + pakuris[i])

def showPakuri():
    speciesName: str = input("Enter the name of the species to display: ")
    stats = pakudex.get_stats(speciesName)
    if(stats == None):
        print("Error: No such Pakuri!")
    else:
        print("\nSpecies: " + speciesName)
        print("Attack: " + str(stats[0]))
        print("Defense: " + str(stats[1]))
        print("Speed: " + str(stats[2]))
def addPakuri():
    if (pakudex.get_size() == pakudex.get_capacity()):
        print("Error: Pakudex is full!")
        return
    speciesName: str = input("Enter the name of the species to add: ")
    if(pakudex.add_pakuri(speciesName)):
        print("Pakuri species " + speciesName + " successfully added!")
    else:
        if(pakudex.get_stats(speciesName) != None):
            print("Error: Pakudex already contains this species!")
def evolvePakuri():
    speciesName: str = input("Enter the name of the species to evolve: ")
    if(pakudex.evolve_species(speciesName)):
        print(speciesName + " has evolved!")
    else:
        print("Error: No such Pakuri!")
def sortPakuri():
    pakudex.sort_pakuri()
    print("Pakuri have been sorted!")

if __name__ == '__main__':
    print('Welcome to Pakudex: Tracker Extraordinaire!')
    maxCapacity = 0
    while(True):
        try:
            maxCapacity: int = int(input("Enter max capacity of the Pakudex: "))
            if(maxCapacity > 0):
                break
        except ValueError:
            None
        print("Please enter a valid size.")
    print("The Pakudex can hold " + str(maxCapacity) + " species of Pakuri.")

    pakudex = Pakudex(maxCapacity)

    Menu = [MenuOption("List Pakuri", listPakuri),
            MenuOption("Show Pakuri", showPakuri),
            MenuOption("Add Pakuri", addPakuri),
            MenuOption("Evolve Pakuri", evolvePakuri),
            MenuOption("Sort Pakuri", sortPakuri),
            MenuOption("Exit", lambda *args: None)]
    selectedOption = 1
    while (selectedOption != 5):
        print("\nPakudex Main Menu")
        print("-----------------")
        for i in range(len(Menu)):
            print(str(i+1) + ". " + Menu[i].name)

        try:
            selectedOption = int(input("\nWhat would you like to do? "))-1
            if (selectedOption in range(0, len(Menu))):
                Menu[selectedOption].function()
                continue
        except ValueError:
            None
        print("Unrecognized menu selection!")
    print("Thanks for using Pakudex! Bye!")