"""Implements the logic associated with a food fest"""


# PI create a class FoodFest
class FoodFest:
    
    # initializer
    def __init__(self, festName, regStallCount, premStallCount, revCost, tax, regRevCount, premRevCount, revCategory):
        self.festName = festName
        self.regStallCount = regStallCount
        self.premStallCount = premStallCount
        self.revCost = revCost
        self.tax = tax
        self.regRevCount = regRevCount
        self.premRevCount = premRevCount
        self.revCategory = revCategory
        regRevCount = 0
        premRevCount = 0

    # accessor methods
    def getFestName(self):
        return self.festName
    
    def getRevCost(self):
        return self.revCost
    
    def getPremStallCount(self):
        return self.premStallCount
    
    # mutator method

    def getRevCost(self, newValue):
        self.revCost = newValue
        self.revCost >= 0


    # method to compute net REGULAR cost

    def computeNetRegularCost(self):
        self.tax = self.revCost / 100
        return self.revCost + self.tax
    


    # method to compute net PREMIUM cost

    def computeNetPremiumCost(self):
        self.revCost * 2
        return self.revCost
    
    
    # method to request reservation
    def requestReservation(self):
        self.regStallCount = int(input("Enter the stall count for reservation: "))
        self.regStallCount = str(input("Enter category of reservation: "))

        if self.regStallCount < 0:
            return False
        
        if self.revCategory == "regular":
            return True


        if self.revCategory == "premium":
            return True
        
        else:
            return False
        
        

        



    


    
    


    
        


# PII create initailizer of FoodFest as per the instructions in print document
# PII define accessors and mutators as per the instructions in print document
# PII define method computeNetRegularCost as per the instructions in print document
# PII define method computeNetPremiumCost as per the instructions in print document
# PII define method requestReservation as per the instructions in print document
