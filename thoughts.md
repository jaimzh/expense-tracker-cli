# My thoughts

Alright so my plan is to first of all set up schema's for the finance tracker so the best way to do it it so make a class, we'll call it **Expenses**, 

## Expenses class
- constructor to define, id , date, descriptiion and amount
- function to return the constuctor as a dictionary or json string
- class function for date


## Expense List Functions

### Crud functions
- add an axpense: you pass d
- update an expense: you pass the id and then modify either the amount and/or description 
- delete an expense: pass an id and then deletes it from the list, make sure we set automatic id updates 
- view all expenses: function w/ no arguments that returns just the entire list 

### View functions 
- view summary: function w/ no arguments which just takes all the amounts and sums them
- view month summary:  pass in month number and it returns the sum of all amounts in that year


## helper functions
- write to csv/json 
- read from csv or json 
- print or display response



## Additional features 
- set buget for each month: you specify the month and the limit and if the total amount in that month surpasses the limit you print warning 
- add category so that we can return based on category as well, so that is add category function and view by category funtion
- allow users to export expenses to a csv or even a json 



# Notes: 
hmm so something i have noticed, is that when it commes to crud api's/functions i usually make the read(list all) api first then add... i mean it only makes sense, test if it can hold something in the right format and then testiing if you can add somethign

For cli handling in the main.py we have parsers, sub parsers and then arguments 

- Parser that is like git or python main.py //the main stuff 
- Subparser that is the command git **commit** or **add** or  **list**
- Argument flaag that is -m or --desciption, more or less kwarg
- The value is well the value something like args.description 

Alright so now to add the features 








--- 
1. Add Expenses
First, let's populate the tracker with some data across different categories.

bash
python main.py add --description "Lunch at McDonald's" --amount 12.50 --category "Food"
python main.py add --description "Movie tickets" --amount 25.00 --category "Entertainment"
python main.py add --description "Internet Bill" --amount 60.00 --category "Utilities"
python main.py add --description "Random snacks" --amount 5.25
2. View All Expenses
Check to make sure everything was added correctly. Take note of the ID numbers generated here!

bash
python main.py list
3. Check Summaries
Test the total summary and the month-specific summary (Assuming we are in month 3 for March).

bash
python main.py summary
python main.py summary --month 3
4. Update an Expense
Let's modify the "Random snacks" entry (assuming it was assigned ID 4).

bash
python main.py update --id 4 --description "Gummy Bears" --amount 6.50
python main.py list
5. Test Budgets
Set a budget for the current month and the next month.

bash
python main.py budget --month 3 --amount 500.00
python main.py budget --month 4 --amount 450.00
6. View Budgets
Test both the "view-all" flag and the specific "view-month" flag.

bash
python main.py budget --view-all
python main.py budget --view-month 3
7. Delete an Expense
Finally, delete the "Internet Bill" (assuming it was assigned ID 3) and verify it's gone.

bash
python main.py delete --id 3
python main.py list
(Note: Depending on how your ID generation works, the IDs might be 1, 2, 3, 4. If you get an error that an ID doesn't exist during the Update/Delete steps, just check the output of the list command and adjust the --id flag accordingly!)

