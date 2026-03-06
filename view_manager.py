from  rich.console import Console
from rich.table import Table

from expense_manager import get_expense_list


console = Console()
column_style = "dim bold"

def render_table(expenses): 
    table = Table(title = "My expenses", style = "bold blue")
    table.add_column("ID", style = column_style, width = 10)
    table.add_column("Date", style = column_style, width = 10)
    table.add_column("Description", style = column_style, width = 10)
    table.add_column("Amount", style = column_style, width = 10)
    table.add_column("Category", style = column_style, width = 10)


    for expense in expenses: 
           table.add_row(str(expense["id"]), expense["date"], expense["desc"], str(expense["amount"]), expense["category"])
     
    
    
    console.print(table) 



def render_table_budget(budget):
    table = Table(title = "My budget", style = "bold blue")
    table.add_column("Month", style = column_style, width = 10)
    table.add_column("Budget", style = column_style, width = 10)


    for budget in budget:
        table.add_row(str(budget["month"]), str(budget["budget"]))
    
    console.print(table)
        

def render_success(message):
    console.print(f"[bold green]Success[/bold green] {message}")

def render_error(message):
    console.print(f"[bold red]Error[/bold red] {message}")