import argparse
from storage import Data_base
from datetime import datetime

def main():
    db = Data_base("Data/db.json")

    parser = argparse.ArgumentParser(description="Financial Tracker: Track income, expenses, and balances.")
    subparsers = parser.add_subparsers(dest="command", required=True, help="Available subcommands")

    expense_parser = subparsers.add_parser("expense", help="Add a new expense")
    expense_parser.add_argument("-a", "--amount", type=float, required=True, help="Expense amount")
    expense_parser.add_argument("-c", "--category", type=str, required=True, help="Category (e.g., Food, Rent)")
    expense_parser.add_argument("-d", "--description", type=str, default="", help="Optional description")

    income_parser = subparsers.add_parser("income", help="Add a new income source")
    income_parser.add_argument("-a", "--amount", type=float, required=True, help="Income amount")
    income_parser.add_argument("-c", "--category", type=str, required=True, help="Category (e.g., Salary, Gift)")
    income_parser.add_argument("-d", "--description", type=str, default="", help="Optional description")

    subparsers.add_parser("view", help="View transaction history and current balance")

    delete_parser = subparsers.add_parser("delete", help="Delete a transaction by index")
    delete_parser.add_argument("-i", "--index", type=int, required=True, help="Index of item to delete")

    args = parser.parse_args()

    if args.command == "expense":
        date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_expense = {"type": "Expense", "Amount": args.amount, "category": args.category, "Description": args.description, "date": date_str}
        db.data_append(new_expense)
        print(f"Expense of ${args.amount:.2f} saved successfully!")

    elif args.command == "income":
        date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_income = {"type": "Income", "Amount": args.amount, "category": args.category, "Description": args.description, "date": date_str}
        db.data_append(new_income)
        print(f"Income of ${args.amount:.2f} saved successfully!")

    elif args.command == "view":
        history = db.load_data()
        print("\n--- Transaction History ---")
        total_income = 0.0
        total_expense = 0.0
        
        for index, item in enumerate(history):
            print(f"[{index}] [{item['date']}] {item['type']}: ${item['Amount']:.2f} | {item['category']} ({item['Description']})")
            if item['type'] == 'Income':
                total_income += item['Amount']
            elif item['type'] == 'Expense':
                total_expense += item['Amount']
        
        print("-" * 50)
        print(f"Total Income:   ${total_income:.2f}")
        print(f"Total Expenses: ${total_expense:.2f}")
        print(f"Current Balance: ${total_income - total_expense:.2f}")
        print("-" * 50)

    elif args.command == "delete":
        deleted = db.data_delete(args.index)
        if deleted:
            print(f"Deleted {deleted['type']} of ${deleted['Amount']:.2f} successfully!")
        else:
            print("Invalid index. No item was deleted.")

if __name__ == "__main__":
    main()