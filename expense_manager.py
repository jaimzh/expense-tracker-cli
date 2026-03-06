from expenses import Expense
from utils import loaded_json, write_in_json, json_setup, get_date_month

#CRUD functions for the most part

# #add functions
def add_expense(desc, amount, category = None):

    if get_expense_list() == []: 
        json_setup()
    
    else: 
        expenses = get_expense_list()
        data = loaded_json()
        
        expense = Expense(len(expenses) + 1, description=desc, amount=amount, category=category ) 
        new_expense = expense.get_json_obj()
    
        data["expenses"].append(new_expense)      
        write_in_json(data)
        print("written")

# #list functions
def get_expense_list():
    try:
        json_data = loaded_json()
        return json_data["expenses"]
    except: 
        return []

def get_expense_by_id(ex_id):
    expenses = get_expense_list()
    arr_index = ex_id - 1   
    return expenses[arr_index]

def sum_expenses():
    expenses = get_expense_list()
    total = 0
    for expense in expenses: 
        total = expense["amount"]  + total 
        
    return total

def month_sum_expenses(month):
    expenses = get_expense_list()
    total = 0
    
    for expense in expenses: 
        if get_date_month(expense["date"]) == int(month) :
            total = expense["amount"]  + total 
    return total

def category_filter(category):
    expenses = get_expense_list()
    filtered_list = []
    
    for expense in expenses: 
        if expense["category"] == category :
            filtered_list.append(expense)
            
    return filtered_list

# #update functions
def update_expense(ex_id, desc=None, amount=None, category=None):
    data = loaded_json()
    found = False
    
    for expense in data["expenses"]:
        if expense["id"] == ex_id:
            if desc: expense['desc'] = desc 
            if amount: expense['amount'] = amount
            if category: expense['category'] = category
            
            found = True
            break 
        
    if found:
        write_in_json(data)
        print(f"Expense {ex_id} updated successfully.")
    else:
        print(f"Error: Expense with ID {ex_id} not found.")

def update_expense(ex_id, desc=None, amount=None, category=None):
    old_expense = get_expense_by_id(ex_id)

    if old_expense:  
        if desc:
            old_expense['desc'] = desc
        if amount:
            old_expense['amount'] = amount
        if category:
            old_expense['category'] = category

        expenses = get_expense_list()
        expenses[ex_id - 1] = old_expense

        data = loaded_json()
        data["expenses"] = expenses
        write_in_json(data)
        print(f"Expense {ex_id} updated successfully.")
    else:
        print(f"Error: Expense with ID {ex_id} not found.")

def update_expense(ex_id, desc=None, amount=None, category=None):
    old_expense = get_expense_by_id(ex_id)

    if not old_expense:
        print(f"Error: Expense with ID {ex_id} not found.")
        return  
    if desc is not None:
        old_expense['desc'] = desc
    if amount is not None:
        old_expense['amount'] = amount
    if category is not None:
        old_expense['category'] = category

    expenses = get_expense_list() 
    expenses[ex_id - 1] = old_expense

    data = loaded_json()
    data["expenses"] = expenses
    write_in_json(data)
    
    print(f"Expense {ex_id} updated successfully.")

# #delete functions
def delete_expense(ex_id):
    expenses = get_expense_list()
    del expenses[ex_id - 1]

    for i, expense in enumerate(expenses[ex_id - 1: ]): 
        expense["id"] = ex_id + i 
         
    data = loaded_json() 
    data["expenses"] = expenses  
    write_in_json(data)
    print("deleted")
