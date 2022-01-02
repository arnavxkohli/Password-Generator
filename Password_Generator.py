#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
a = len (letters) - 1
b = len (numbers) - 1
c = len (symbols) - 1

i = 0 
password = [letters[random.randint(0,a)]]

while i < (nr_letters - 1):
  password.append (letters[random.randint (0,a)])
  i += 1

i = 0

while i < (nr_symbols):
  password.append (str (symbols [random.randint (0,c)]))
  i += 1

i = 0

while i < (nr_numbers):
  password.append (str (numbers [random.randint (0,b)]))
  i += 1

d = len (password)

#print (password)

first = random.randint (0,d - 1)

#print (first)

actual_password = password [first]

password.pop (first)

d -= 1

while d>0:
  n = random.randint (0,d-1)
  actual_password += password [n]
  password.pop (n)
  d -= 1

print (actual_password)

#print (password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


