# Hello World
print("Hello World")

# Variables
x = 5
y = "John"
print(x)
print(y)

x = int(3) # 3
y = str(3) # '3'
z = float(3) # 3.0 



x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = 10
print(x + y)

x = 5
y = "John"
print(x, y)

# Function 

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

# Integers:

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

 # Floats:

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

# Complex:

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

# Multiline Strings

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Strings are Arrays
a = "Hello, World!"
print(a[1])

# Looping Through a String

for x in "banana":
  print(x)

# Check String 1
txt = "the best thing in life are free"
print("free" in txt)


# Check String 2

txt = "the best thing in life are free"
if "free" in txt:
    print("Yes")

# Slicing

b = "Hello, World!"
print(b[2:5])

# Upper Case

a = "Hello, World!"
print(a.upper())

# Lower Case

a = "Hello, World!"
print(a.lower())

# Remove Whitespace

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# String Format

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
# OR
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# Escape Character

txt = "We are the so-called \"Vikings\" from the north."
print(txt) 

# Boolean Values 1

print(10 > 9)
print(10 == 9)
print(10 < 9)

# Boolean Values 2

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

  