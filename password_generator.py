#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


lenght = nr_letters + nr_numbers + nr_symbols
password = ""
x = 0 
y = 0

for i in range(0, lenght):
  random_char = random.choice(letters)
  random_sym = random.choice(symbols)
  random_num = random.choice(numbers)
  if i < nr_letters:
    password = password + random_char

  elif x < nr_symbols:
    password = password + random_sym
    x += 1

  else:
    password = password + random_num


print(f"Your First option is: {password}")

list_password = ( list(password) )

list_password_2 = random.sample(list_password, len(list_password))

password_2 = ""

for z in range(0, lenght):
  password_2 = password_2 + list_password_2[z]
  z += 1

print(f"Your Second option is: {password_2}")






