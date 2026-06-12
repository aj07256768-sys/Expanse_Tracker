from datetime import datetime

class Transaction:
    def __init__(self, Amount: float, category: str, Description: str = ""):
        self.Amount = Amount
        self.category = category
        self.Description = Description
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def To_dic(self) -> dict:
        return {
            "Amount": self.Amount,
            "category": self.category,
            "Description": self.Description,
            "date": self.date,
            "type": getattr(self, 'type', 'Unknown')  
        }  


class Expense(Transaction):
    def __init__(self, Amount, category, Description):
        super().__init__(Amount, category, Description)  
        self.type = 'Expense' 


class Income(Transaction):
    def __init__(self, Amount, category, Description):
        super().__init__(Amount, category, Description)  
        self.type = 'Income'  