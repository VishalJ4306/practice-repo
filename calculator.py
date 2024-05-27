# Creating calculator console base
num1 = eval(input("Please enter 1 st number:-"))
num2 = eval(input("Please enter 2 nd number:-"))

operation = input('''Please enter your operation
                  + for Addition
                  - for substraction
                  / for Division 
                  * for Multplication:- ''')
if operation == '+':
   print(num1+num2)

if operation == '-':
   print(num1+num2)   

if operation == '/':
   print(num1/num2)

if operation == '*':
   print(num1*num2) 