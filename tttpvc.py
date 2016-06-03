#Made by TechnoWizX 2016
#More comments
#Oooooh look! Some imports!


#Now some variables!!! #Yas!
Yes = ("yes", "y", "true", "yep", "yas")
No = ("no", "n", "nah", "false", "nope")

class pvc():
    def helpPage():
        print('''
''')

    def startGame():
        first = input("Would you like to go first? (Y/N)\n").lower()
        if first in Yes:
            first = True
            print("You are going first")
                        
        elif first in No:
            first = False
            print("You are going seccond")
