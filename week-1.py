"""
Author:  Sway (bryant) Fusco
Project: Week 3 Technical Assignment
Version: 20231218-231533
Cohort:  2023-11-30-de-eastern
Teacher: Tiago Basil
School:  Promineo Tech/ACC Data Engineering
"""

# Exercise 1 : A program that declares a variable
# and assigns a string to it, then prints the variable.
ex_1_variable = 'Exercise One!'
print(ex_1_variable)

# Exercise 2 : Write a program that declares two
# variables and concatenates them into a single
# string, then prints the result.
ex_2_foo = 'Exercise'
ex_2_bar = 'Two!'
ex_2_foo_bar = ex_2_foo + ' ' + ex_2_bar
print(ex_2_foo_bar)

# Exercise 3 : Write a program that declares a
# variable and prints the length of the string
# assigned to the variable.
ex_3_variable = 'This string length is 24'
print(len(ex_3_variable))

# Exercise 4 : Write a program that a variable
# and prints the first letter of the string
# assigned to the variable.
ex_4_variable = 'A is the first letter of this string'
print(ex_4_variable[:1])

# Exercise 5 : Write a program that declares a
# variable and prints the last letter of the
# string assigned to the variable
ex_5_variable = 'The last letter of this string is R'
print(ex_5_variable[-1])  # the last character

# Exercise 6 : Write a program that declares a variable
# and prints a slice of the string assigned to the
# variable, from the 2nd to the 5th character.
ex_6_variable = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(ex_6_variable[1:5])

# Exercise 7 : Write a program that declares a variable
# and prints a slice of the string assigned to the
# variable, from the 5th character to the end.
ex_7_variable = 'the BEGINNING to the END'
print(ex_7_variable[4:])

# Exercise 8 : Write a program that declares a variable
# and prints a slice of string assigned to the variable,
# from the 2nd to the 5th character in reverse order.
ex_8_variable = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# print(ex_8_variable[-22:-4])
print(ex_8_variable[-25:-21])

# Exercise 9 : Write a program that declares a variable and
# prints a slice of the string assigned to the variable, ever
# other character
ex_9_variable = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(ex_9_variable[2:12:2])

# Exercise 10 : Write a program that declares a variable and
# prints a slice of the string assigned to the variable,
# skipping the first two characters.
ex_10_variable = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(ex_10_variable[2:])

# Exercise 11 : Write a program that declares a variable and
# prints a slice of the string assigned to the variable,
# skipping the last 2 characters.
ex_11_variable = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(ex_11_variable[:-2])

# Exercise 12 : Write a program that declares a variable
# and prints a slice of the string assigned to the variable,
# skipping the first and last 2 characters.
ex_12_variable = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(ex_12_variable[1:-2])

# Exercise 13 : Write a program that declares a variable
# and converts the string assigned to the variable to
# all uppercase.
ex_13_variable = 'this string should be in all uppercase'
print(ex_13_variable.upper())

# Exercise 14 : Write a program that declares a variable
# and converts the string assigned to the variable to
# all lowercase letters.
ex_14_variable = 'This StRiNg SHOULD Be In ALL LowerCase'
print(ex_14_variable.lower())

# Exercise 15 : Write a program that declares a variable
# replaces a portion of the string assigned to the
# variable with a new string.
ex_15_variable = "Comparing Apples to Oranges"
print(ex_15_variable.replace('Oranges', 'Apples'))

# Chores
del ex_1_variable
del ex_2_foo
del ex_2_bar
del ex_2_foo_bar
del ex_3_variable
del ex_4_variable
del ex_5_variable
del ex_6_variable
del ex_7_variable
del ex_8_variable
del ex_9_variable
del ex_10_variable
del ex_11_variable
del ex_12_variable
del ex_13_variable
del ex_14_variable
del ex_15_variable
