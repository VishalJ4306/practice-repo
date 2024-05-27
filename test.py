a="Hello, India!"
print(a[:2])

h="Spiderman"
print(h[3:9])
print(h[:2])
print(h[2:9])

b = "Hello, World!"
print(b[-5:-2])

#The upper() method returns the string in upper case:

print(a.upper())
print(a.lower())

#The strip() method removes any whitespace from the beginning or the end:
d = " Hello, TingTong! "
print(d.strip())

p = "Hello"
q = "World"
r = p + " " + q
print(r)
# As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
age = 45
txt1 ="My name is John, I am " + age
print(txt1)

#But we can combine strings and numbers by using f-strings or the format() method!
age = 35
txt =f"My name is John, I am {age}"
print(txt)