"""Implements the logic associated with a food fest"""


# PI create a class FoodFest
class FoodFest:
    
    # initializer
    def __init__(self, festName, regStallCount, premStallCount, revCost, tax, regRevCount, premRevCount):
        self.festName = festName
        self.regStallCount = regStallCount
        self.premStallCount = premStallCount
        self.revCost = revCost
        self.tax = tax
        self.regRevCount = regRevCount
        self.premRevCount = premRevCount
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

    
    


    
        


# PII create initailizer of FoodFest as per the instructions in print document
# PII define accessors and mutators as per the instructions in print document
# PII define method computeNetRegularCost as per the instructions in print document
# PII define method computeNetPremiumCost as per the instructions in print document
# PII define method requestReservation as per the instructions in print document
