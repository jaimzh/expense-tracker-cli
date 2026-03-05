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

