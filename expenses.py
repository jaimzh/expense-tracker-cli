from datetime import date
import json 


class Expense:
    def __init__(self, expense_id, description, amount, category=None):
        self.id = expense_id 
        self.date = self.get_date()
        self.desc = description
        self.amount = amount 
        if category: self.category = category
        
    def get_json_obj(self):
        return self.__dict__   
    
    @classmethod  
    def get_date(cls):
        today = date.today()
        date_string = today.isoformat()
        return date_string
    
 