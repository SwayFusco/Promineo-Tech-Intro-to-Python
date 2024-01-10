# Sway (bryant)
# Fusco
# 2023-11-30-de-eastern
# submission date

# 1: Write the following list
lst1 = ['1', '2', [3]]

print('1: lst1 =', lst1)

# 2: Write the following list
lst2 = [('3', 4), '5', 6]

print('2: lst2 =', lst2)

# 3: Join lst1 and lst2 so only unique string or integer values remain in a
# new list, lst3.(i.e., ['1', '2', 3, '3', 4, 5, 6])
lst3 = lst1[0:2] + lst1[2:][0] + list(lst2[0]) + lst2[1:]

print('3: lst3 =', lst3)

# 4: Create an empty dictionary called odds_evens.
# Next, iterate through lst3. If a number (regardless of datatype) is even,
# add the value to a list that will be stored as a value for the key `even`
# in the dictionary, odds_evens. Do the same for the odds numbers. When you
# print the odds_evens dictionary the output should look like this:
# {'evens': ['2', 4, 6], 'odds': ['1', '3', 3, '5']}
odds_even = {}
odds_even['even'] = [i for i in lst3 if not int(i) % 2]
odds_even['odds'] = [i for i in lst3 if int(i) % 2]

print('4: even =', odds_even['even'])
print('4: odds =', odds_even['odds'])

# 5: Next, loop through lst3 and evaluate each item using a list
# comprehension. if it's not an integer, convert it to an integer. The
# resulting list should be called, numbers.
numbers = [i if isinstance(i, int) else int(i) for i in lst3]

print('5: numbers =', numbers)

# 6: Then, iterate through the values in the odds_evens dictionary. For each
# number, if it's a string, convert it to an int, otherwise ignore.
for key, values in odds_even.items():
    for i in range(len(values)):
        # Check if the element is a string and convert it to an integer
        if isinstance(values[i], str):
            values[i] = int(values[i])

print('6: odds_even = ', odds_even)

# 7: Find the maximum number in the numbers list. Then, for each item in the
# lists of the odds_evens dictionary, add this maximum number to the item and
# append the result to the numbers list. Try this using dictionary
# comprehension!
numbers.append(max(numbers))
print('7: numbers =', numbers)
# 8: Take the code you wrote to process #1 – 7 and add error handling with TRY-EXCEPT-FINALLY blocks. Print out any errors to the console. Print the numbers list to the console which should look like this: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# 9: Save your script. Run your script. Submit both the script and a screen shot of your IDE showing the resulting output from running your script.

# flat_list = []
# for i in lst1+lst2:
#     if isinstance(i, tuple) or isinstance(i, list):
#         for x in i:
#             flat_list.append(x)
#     else:
#         flat_list.append(i)

# ['1', '2', 3, '3', 4, '5', 6]
# print(flat_list)

# flat_2 = [i for i in [x for x in lst1+lst2 if not isinstance(x, tuple) and not isinstance(x, list)]]
# print(flat_2)

# flat_list = [i for i in lst1 + lst2 if type(i) is not tuple and type(i) is not list]
# flat_list = flat_list + [i for i in lst1 + lst2 if type(i) is list]
# flat_list = flat_list + [i for i in lst1 + lst2 if type(i) is list]
# print(set(flatten_list(lst1) + flatten_list(lst2)))
