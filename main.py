import argparse

from utils import add_expense, get_expense_list 

def main():
    parser = argparse.ArgumentParser(description="Expense Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    #add command 
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("--description", required=True)
    add_parser.add_argument("--amount", required=True, type=float)
    add_parser.add_argument("--category", default="Misc")


    subparsers.add_parser("list")

    summary_parser = subparsers.add_parser("summary")
    summary_parser.add_argument("--month", type=int)

    args = parser.parse_args()

    if args.command == "add": 
        add_expense(desc= args.description , amount=args.amount, category=args.category)

    elif args.command == "list":
        print(get_expense_list())



if __name__ == "__main__":
    main()