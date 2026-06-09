from datetime import datetime
class Transaction:
    def __init_(self,Amount:float,category:str,Description:str= ""):
        self.Amount = Amount
        self.category = category
        self.Description = Description 

    def To_dic(self) -> dic:
        return {
            "Amount":self.Amount,
            "category":self.category,
            "Description":self.Description

        } 



class Expense(Transaction):
    def __init_(self,Amount,category,Description):
        super().__init_(Amount,Description,category)  
        self.type='Expense' 



class Income(Transaction):
    def __init_(self,Amount,Description,category):
        super().__init_(Amount,category,Description)
        self.type='Income'
