from models import Expense, Income
from storage import Data_base

db = Data_base("Data/db.json")

while True:
    print("\n=== EXPENSE TRACKER MENU ===")
    print("1. Add Expense")
    print("2. View All Transactions")
    print("3. Exit")
    
    choice = input("Choose an option (1-3): ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        desc = input("Enter description: ")
        
        # Fixed: Passed 'desc' instead of 'description'
        new_expense = Expense(amount, category, desc) 
        
        db.data_append(new_expense.To_dic())
        print("Expense saved successfully!")

    elif choice == "2":
        history = db.load_data()
        print("\n--- Transaction History ---")
        for item in history:
            print(f"[{item['date']}] {item['type']}: ${item['Amount']} | {item['category']} ({item['Description']})")

    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")