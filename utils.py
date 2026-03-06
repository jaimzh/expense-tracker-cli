import json
import os

from expenses import Expense

# curr_dir = os.getcwd()
curr_dir = os.path.dirname(os.path.abspath(__file__))
json_file = "expenses.json"
filename = os.path.join(curr_dir, json_file)


#read and write functions for the json file 

def loaded_json():
    with open(filename, "r") as file:
        data = json.load(file)
    return data
    
def write_in_json( data):
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
    except Exception:
        return("error")
        
def display(response):
    
    if response == "help":
        #do somemthing 
        print("all the options")
    elif response == "add":
        #do something 
        print("call add function response")
        
        
def json_setup():
    
    preset = {
        "expenses": [], 
        "budget" : []
    }
    write_in_json(preset)




        
# crud functions 



def get_expense_list():
    try:
        json_data = loaded_json()
        return json_data["expenses"]
    except: 
        return ("Empty")

def get_budget_list():
    try:
        json_data = loaded_json()
        return json_data["budget"]
    except: 
        return ("Empty")




def add_expense(desc, amount, category = None):
    
    
    #if get expense list i
    
    if get_expense_list() == "Empty": 
        json_setup()
    
    else: 
        expenses = get_expense_list()
        data = loaded_json()
        
        expense = Expense(len(expenses) + 1, description=desc, amount=amount, category=category ) 
        new_expense = expense.get_json_obj()
    
    
        data["expenses"].append(new_expense)      
        write_in_json(data)
        print("written")
    


def get_expense_by_id(ex_id):
    expenses = get_expense_list()
    arr_index = ex_id - 1   
    return expenses[arr_index]
    
    
# print(get_expense_by_id(1))


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


def delete_expense(ex_id):
    
    expenses = get_expense_list()
    del expenses[ex_id - 1]

 
    for i, expense in enumerate(expenses[ex_id - 1: ]): 
        expense["id"] = ex_id + i 
         
    data = loaded_json() 
    data["expenses"] = expenses  
    write_in_json(data)
    print("deleted")
    
    
    

"""SUMmary hehe...get it, cuz it's the SUM of all the amounts
    but it's literally called summary with the SUM
    ....idk why i do this man 
"""
def sum_expenses():
    expenses = get_expense_list()
    total = 0
    for expense in expenses: 
        total = expense["amount"]  + total 
        
    return total 



#month SUMmary
def get_date_month(date):
    dates_arr = date.split("-")
    month_no =  dates_arr[1]
    return int(month_no)



# print("testing something ", get_date_month("2025-08-01"))


def set_month_budget(month, budget): 
    budget_list = get_budget_list()
    
    if budget_list == "Empty":
        json_setup()
    
    else: 
        budget_list = get_budget_list()
        data = loaded_json()
        
        new_budget = {
            "month": month,
            "budget": budget
        }
 
        data["budget"].append(new_budget)      
        write_in_json(data)
        print("written")
    
def get_month_budget(month):
    budget_list = get_budget_list()
    for budget in budget_list: 
        if budget["month"] == month: 
            return budget["budget"]
    return None

def warn_when_expenses_exceed_budget(month, budget):
    month_total = month_sum_expenses(month)
    if month_total > budget:
        print("Warning: You have exceeded your budget for this month.")


set_month_budget(8, 1000)   

def month_sum_expenses(month):
    expenses = get_expense_list()
    total = 0
    
    for expense in expenses: 
        if get_date_month(expense["date"]) == int(month) :
            total = expense["amount"]  + total 
        
    print("ready")
    return total 



# print(month_sum_expenses(8))

def category_filter(category):
    expenses = get_expense_list()
    filtered_list = []
    
    for expense in expenses: 
        if expense["category"] == category :
            filtered_list.append(expense)
            
    return filtered_list 



    
    


