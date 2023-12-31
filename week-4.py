"""
Author:  Sway (bryant) Fusco
Project: Week 4 Technical Assignment
Version: 20231231-115339
Cohort:  2023-11-30-de-eastern
Teacher: Tiago Basil
School:  Promineo Tech/ACC Data Engineering
"""
import json

# Part 1: Lists
# 1.1 Create a list called shopping_list that contains
# at least 5 items you need to buy at the grocery store
shopping_list = ['Potatoes', 'Steak', 'Broccoli', 'Wine', 'Coffee']

# 1.2 Print out the third item in shopping_list
print(shopping_list[2])

# 1.3 Add two more items to the end of shopping_list
shopping_list.extend(['Cheese Cake', 'Ice Cream'])

# 1.4 Remove the first item from shopping_list
del shopping_list[0]

# 1.5 Print out the final version of shopping_list
print(shopping_list)

# Part 2: Dictionaries
# 2.1 Create a dictionary called my_info that contains
# your name, age, and favorite hobby
my_info = {'name': 'Sway Fusco', 'age': 47, 'favorite_hobby': 'Fencing'}

# 2.2 Print out your name from the my_info dictionary
print(my_info['name'])

# 2.3 Update the value of your favorite hobby in the
# my_info dictionary
my_info['favorite_hobby'] = 'Playing Ukulele'

# 2.4 Add a new key-value pair top the my_info dictionary
# that contains your favorite food
my_info['favorite_food'] = shopping_list[0]

# 2.5 Print out the final version of the my_info dictionary
print(my_info)

# Part 3: Loops
# 3.1 Create a list called numbers that contains the numbers
# 1-10
numbers = list(range(1, 11))

# 3.2 using a for loop, print out each number in the numbers
# list
for this_number in numbers:
    print(this_number)

# 3.3 using a while loop print out each number in the
# numbers list
index = 0
while index < len(numbers):
    print(numbers[index])
    index += 1

# 3.4 Create a dictionary called squares that contains the
# squares of the numbers 1 through 5
# (e.g. 1: 1, 2: 4, 3: 9, 4: 16, 5: 25)
squares = {}
for key in range(1, 6):
    squares[key] = key * key

# 3.5 Using a for loop, print out each key-value pair in
# the squares dictionary
for key in squares:
    print(f'{key}: {squares[key]}')

# Part 4: Conditional Logic
# 4.1 Create a variable called temperature and set it to
# a number representing the current temperature (in degrees
# Celsius)
temperature = 2  # current temperature in Loveland, CO @ Now

# 4.2 Using an if statement, print out a message telling the
# user whether they should wear a coat or not based on the
# current temperature. If the temperature is below 10 degrees
# Celsius, print out a message telling the user to wear a coat.
# If the temperature is 10 degrees Celsius or above, print out a
# message telling the user that they do not need to wear a coat.
if temperature < 10:
    print(f"Wear a coat —it's {temperature}° Celsius outside")
else:
    print(f"You do not need to wear a coat —it's {temperature}° Celsius outside")

# 4.3 Create a variable called username and set it to a string
# representing the user's username
username = 'MyUsernameisTooLong'

# 4.4 Using an if statement, print out a message telling the
# user whether their username is too long or not. If the username
# is more than 10 characters long, print out a message telling the
# user that their username is too long. If the username is 10
# characters or less, print out a message telling the user that
# their username is okay.
if len(username) > 10:
    print(f'{username} is {len(username) - 11} characters too long (max 10)')
else:
    print(f'The username: {username} is ok to use')

# 4.5 Create a list called numbers_2 that contains the
# numbers 1 through 5.
numbers_2 = list(range(1, 6))

# 4.6 Using a for loop and an if statement, print out only the
# even numbers in the numbers_2 list.
for index in range(1, len(numbers_2), 2):
    print(numbers_2[index])

# Part 5: Data Wrangling
# 5.1 Read the 'new_families.txt' file (included in your materials)
# into memory and assign the variable, “file” to the object.
file = open('new_families.txt', 'r')  # for reading

# 5.2 Print(file) # Can you read the data in the file?
print(file)  # No, you can't

# 5.3 What is the datatype of the file variable?
print(type(file)) # <class '_io.TextIOWrapper'>

# 5.4 Write a FOR loop to iterate over the Text IO object referenced
# by the file variable and print each iteration of the text. How many
# results did you get back? #HINT shouldn't be a very large number ;)
for line in file:
    print(line.strip())

# 5.5 What is the datatype of the object returned in the iteration?
print(type(line)) # <class 'str'>

# 5.6 What happens when you try to parse the first item in the list?
# first_family = json.loads(families_list[0]) # errors: needs string not dict
try:
    json.loads(line)
except:
    print('Error! json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes')

# 5.7 Change the string variable into a list of dictionaries type
# so you can work with it. #HINT: import json
family_list = json.loads(line.replace("'",'"'))

# 5.8 Now that you have a list, print only the second item from the
# list. What is its type?
print(f"{family_list[1]} (type:{type(family_list[1])})")