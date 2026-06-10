from storage import Data_base
from models import Expense,Income 


db= Data_base('data/db.json')


new_expense = Expense(Amount=50.9,Category="water",Description="planting water")


db.data_append(new_expense.To_dic())
print("The expense object was automatically processed and saved!")