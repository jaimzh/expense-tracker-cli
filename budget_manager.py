from utils import loaded_json, write_in_json, json_setup
from expense_manager import month_sum_expenses

def get_budget_list():
    try:
        json_data = loaded_json()
        return json_data["budget"]
    except: 
        return []


def get_month_budget(month):
    budget_list = get_budget_list()
    for budget in budget_list: 
        if budget["month"] == month: 
            return budget["budget"]
    return None


    
def set_month_budget(month, budget): 
    budget_list = get_budget_list()
    
    if budget_list == []:
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
    


def warn_when_expenses_exceed_budget(month, budget):
    month_total = month_sum_expenses(month)
    if month_total > budget:
        print("Warning: You have exceeded your budget for this month.")

