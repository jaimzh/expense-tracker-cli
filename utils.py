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
        print("json updated")
    except Exception:
        print("we have a problem while writing json", Exception)
        
def display(response):
    
    if response == "help":
        #do somemthing 
        print("all the options")
    elif response == "add":
        #do something 
        print("call add function response")
        
        
def json_setup():
    
    preset = {
        "expenses": []
    }
    write_in_json(preset)




        
# crud functions 



def get_expense_list():
    json_data = loaded_json()
    return json_data["expenses"]





def add_expense(desc, amount, category = None):
    expenses = get_expense_list()
    data = loaded_json()
    
    expense = Expense(len(expenses) + 1, description=desc, amount=amount, category=category ) 
    new_expense = expense.get_json_obj()
 
   
    data["expenses"].append(new_expense)      
    write_in_json(data)
    print("written")
    
add_expense("heyyyy", 20, )


def update_expense(id, desc, amount, category=None):
    pass


