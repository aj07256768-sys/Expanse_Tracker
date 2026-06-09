from datetime import datetime
class Transaction:
    def __init_(self,Amount:float,category:str,Description:str= ""):
        self.Amount = Amount
        self.category = category
        self.Description = Description