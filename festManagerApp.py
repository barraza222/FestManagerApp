"""The entry point of the application. Implements UI related code"""
import foodFest

class FestManagerApp:
    
    # PI create method main with the functionality described in the print document
    def main():
        print("Food Fest Manager - Aaron Santiago")

    # PIII write the code to implement the User Interaction as described in print document

    def getUserInput(self):
        regStallCount = int(input("Enter the stall count for reservation: "))
        revCategory = str(input("Enter category of reservation: "))
        return regStallCount, revCategory


    def printUserInput(self):
        var = self.getUserInput()
        print(var[0], var[1])

# PI create instance of FestManagerApp

# PI call the method main using the instance of FestManagerApp
    main()
    getUserInput()
    printUserInput()