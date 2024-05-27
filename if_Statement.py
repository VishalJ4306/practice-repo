# If statement exaples
a = 15  
b = 10
if a > b:
 print("a is greater than b")

if a >= b:
 print("a is greater than or equal to b") 

if a == b:
  print("a equal to b") 

if a <=b:
 print("a less than or equal to b")

if a != b:
 print("a is not eaual to b")  

# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

c = 12
d = 15
if d > c:
 print("d is greater than c")
elif c == d:
 print("c and d are equal")
else:
 print("c is greater than d") 

# else without the elif: 

if a > b:
 print("a is greater than b")
else:
 print("a is less than b") 