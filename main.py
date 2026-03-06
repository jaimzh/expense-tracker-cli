import argparse

from budget_manager import get_budget_list, get_month_budget
from expense_manager import add_expense, delete_expense, get_expense_list, month_sum_expenses, sum_expenses, update_expense
from view_manager import render_error, render_success, render_table, render_table_budget
from budget_manager import set_month_budget


def main():
    parser = argparse.ArgumentParser(description="Expense Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    #add command 
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("--description", required=True)
    add_parser.add_argument("--amount", required=True, type=float)
    add_parser.add_argument("--category", default="Misc")

    subparsers.add_parser("list")
    
    #delete command 
    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("--id", required=True, type=int)
    
    #update command 
    update_parser = subparsers.add_parser("update")
    update_parser.add_argument("--id", required=True, type=int)
    update_parser.add_argument("--description", default=None)
    update_parser.add_argument("--amount", default=None, type=float)
    update_parser.add_argument("--category", default=None)

    #summary command 
    summary_parser = subparsers.add_parser("summary")
    summary_parser.add_argument("--month", type=int)

    #budget command 
    budget_parser = subparsers.add_parser("budget")
    budget_parser.add_argument("--month", type=int)
    budget_parser.add_argument("--amount", type=float)
    budget_parser.add_argument("--view-all", action="store_true")
    budget_parser.add_argument("--view-month", type=int)
    #export command 
    # export_parser = subparsers.add_parser("export")
    # export_parser.add_argument("--file", type=str)

    args = parser.parse_args()

    if args.command == "add": 
        add_expense(desc= args.description , amount=args.amount, category=args.category)
        render_success("Expense added successfully")

    elif args.command == "list":
        render_table(get_expense_list())
    
    elif args.command == "delete":
        delete_expense(args.id)
        render_success("Expense deleted successfully")
    
    elif args.command == "update":
        update_expense(args.id, args.description, args.amount, args.category)
        render_success("Expense updated successfully")
    
    elif args.command == "summary":
        if args.month:
            total = month_sum_expenses(args.month)
            render_success(f"Total expenses for {args.month}: {total}")
        else:
            total = sum_expenses()
            render_success(f"Total expenses: {total}")
    
    elif args.command == "budget":
        if args.view_all:
            render_table_budget(get_budget_list())
        elif args.view_month:
            render_success(f"Budget for month {args.view_month}: {get_month_budget(args.view_month)}")
        elif args.month and args.amount:
            set_month_budget(args.month, args.amount)
            render_success(f"Budget of ${args.amount} set for month {args.month}")
        else:
            render_error("Please provide both month and amount")
    
    
    # elif args.command == "export":
    #     export_expense(args.file)
    
    


if __name__ == "__main__":
    main()