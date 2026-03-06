import json
import os



curr_dir = os.path.dirname(os.path.abspath(__file__))
json_file = "expenses.json"
filename = os.path.join(curr_dir, json_file)

def loaded_json():
    with open(filename, "r") as file:
        data = json.load(file)
    return data
    
def write_in_json(data):
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
    except Exception:
        return "error"

def json_setup():
    preset = {
        "expenses": [], 
        "budget" : []
    }
    write_in_json(preset)

def display(response):
    if response == "help":
        print("all the options")
    elif response == "add":
        print("call add function response")

def get_date_month(date):
    dates_arr = date.split("-")
    month_no = dates_arr[1]
    return int(month_no)



