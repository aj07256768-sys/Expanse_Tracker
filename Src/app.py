import argparse
from storage import Data_base
from models import Expense, Income  # Imported your OOP models here!
from datetime import datetime 
from rich import print
from rich.console import Console
from rich.table import Table

def main():
    db = Data_base("Data/db.json")
    console = Console()

    parser = argparse.ArgumentParser(description="Financial Tracker: Track income, expenses, and balances.")
    subparsers = parser.add_subparsers(dest="command", required=True, help="Available subcommands")

    # Expense Parser
    expense_parser = subparsers.add_parser("expense", help="Add a new expense")
    expense_parser.add_argument("-a", "--amount", type=float, required=True, help="Expense amount")
    expense_parser.add_argument("-c", "--category", type=str, required=True, help="Category (e.g., Food, Rent)")
    expense_parser.add_argument("-d", "--description", type=str, default="", help="Optional description")

    # Income Parser
    income_parser = subparsers.add_parser("income", help="Add a new income source")
    income_parser.add_argument("-a", "--amount", type=float, required=True, help="Income amount")
    income_parser.add_argument("-c", "--category", type=str, required=True, help="Category (e.g., Salary, Gift)")
    income_parser.add_argument("-d", "--description", type=str, default="", help="Optional description")

    # View Parser
    subparsers.add_parser("view", help="View transaction history and current balance")

    # Delete Parser
    delete_parser = subparsers.add_parser("delete", help="Delete a transaction by index")
    delete_parser.add_argument("-i", "--index", type=int, required=True, help="Index of item to delete")

    # Update Parser (NEW)
    update_parser = subparsers.add_parser("update", help="Update an existing transaction by index")
    update_parser.add_argument("-i", "--index", type=int, required=True, help="Index of item to update")
    update_parser.add_argument("-a", "--amount", type=float, help="New amount (optional)")
    update_parser.add_argument("-c", "--category", type=str, help="New category (optional)")
    update_parser.add_argument("-d", "--description", type=str, help="New description (optional)")

    args = parser.parse_args()

    if args.command == "expense":
        # Using your model class now!
        expense_obj = Expense(args.amount, args.category, args.description)
        db.data_append(expense_obj.To_dic())
        print(f"[bold green]Expense of ${args.amount:.2f} saved successfully! :rocket:[/bold green]")

    elif args.command == "income":
        # Using your model class now!
        income_obj = Income(args.amount, args.category, args.description)
        db.data_append(income_obj.To_dic())
        print(f"[bold green]Income of ${args.amount:.2f} saved successfully! :rocket:[/bold green]")

    elif args.command == "view":
        history = db.load_data()
        
        table = Table(title="\n[bold cyan]--- Transaction History ---[/bold cyan]", title_justify="left")
        
        table.add_column("Index", style="dim", justify="center")
        table.add_column("Date", style="yellow")
        table.add_column("Type", justify="center")
        table.add_column("Amount", justify="right")
        table.add_column("Category", style="magenta")
        table.add_column("Description", style="italic dim")

        total_income = 0.0
        total_expense = 0.0
        
        for index, item in enumerate(history):
            amount_val = item['Amount']
            
            if item['type'] == 'Income':
                total_income += amount_val
                type_str = "[bold green]Income[/bold green]"
                amount_str = f"[bold green]${amount_val:.2f}[/bold green]"
            else:
                total_expense += amount_val
                type_str = "[bold red]Expense[/bold red]"
                amount_str = f"[bold red]${amount_val:.2f}[/bold red]"
                
            table.add_row(
                str(index),
                item['date'],
                type_str,
                amount_str,
                item['category'],
                item['Description'] or "-"
            )
        
        console.print(table)
        
        balance = total_income - total_expense
        balance_color = "green" if balance >= 0 else "red"
        
        print("\n[bold underline cyan]Financial Summary[/bold underline cyan]")
        print(f"Total Income:    [bold green]${total_income:.2f}[/bold green]")
        print(f"Total Expenses:  [bold red]${total_expense:.2f}[/bold red]")
        print(f"Current Balance: [bold {balance_color}]${balance:.2f}[/bold {balance_color}]")
        print("[cyan]" + "-" * 30 + "[/cyan]\n")

    elif args.command == "delete":
        deleted = db.data_delete(args.index)
        if deleted:
            print(f"[bold yellow]Deleted {deleted['type']} of ${deleted['Amount']:.2f} successfully![/bold yellow]")
        else:
            print("[bold red]Invalid index. No item was deleted.[/bold red]")

    elif args.command == "update":
        # Build payload of items the user actually wants to update
        update_payload = {}
        if args.amount is not None: update_payload["Amount"] = args.amount
        if args.category is not None: update_payload["category"] = args.category
        if args.description is not None: update_payload["Description"] = args.description
        
        if not update_payload:
            print("[bold red]Please specify at least one field to update using -a, -c, or -d.[/bold red]")
        else:
            updated_item = db.data_update(args.index, update_payload)
            if updated_item:
                print(f"[bold yellow]Successfully updated {updated_item['type']} at index {args.index}! :sparkles:[/bold yellow]")
            else:
                print("[bold red]Invalid index. No item was updated.[/bold red]")

if __name__ == "__main__":
    main()