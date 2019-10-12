# dictionaries and sets, unordered collections, no duplicates
# set is unordered so index is meaningless in context of a set

fruit = {'orange':'a sweet orange, citrus fruit',
    'apple':'good for cider',
    'lemon':'sour, yellow, citrus fruit',
    'grape':'small sweet fruit growing in bunches',
    'Lime':'sour green citrus fruit'}

# print(fruit)
# print(fruit['orange'])

# fruit['pear'] ='odd shaped apple'

# print(fruit)

# fruit['pear'] = 'great with tequila'

# print(fruit)

# del fruit['lemon']
# try:
#     if print(fruit['lemon']):
#         print('del')
# except:
#     print('BEEK')
# finally:
#     print('nonsense!')

# fruit.clear()
# print(fruit)

# # del fruit
# print(fruit)

# print("GRAPES")

# print('apple' in fruit)

# while True:
#     dict_key = input('Enter fruit: ')
#     if dict_key == 'quit':
#         break
#     description = fruit.get(dict_key, "we dont have a " + dict_key)
#     if dict_key in fruit:
#         description = fruit.get(dict_key)  #fruit[dict_key]
#         print(description)
#     else:
#         print("No fruit dict_key for you")
#     print(description)

# for snack in fruit:
#     print(fruit[snack])

# dict = {}

# dict['test'] = 'test'

# # for i in range(10):
# #     for snack in fruit:
# #         print(f"snack is {fruit[snack]}")

# # ordered dictionary is collections library
# # not as efficient

# # create a list from the dictionary keys
# # sort it
# # iterate over it to display ordered results


# # ordered_keys = list(fruit.keys())
# # ordered_keys.sort()

# ordered_keys = sorted(list(fruit.keys()))
# for key in sorted(list(fruit.keys())):
#     print(f"key {key} = {fruit[key]}")

# print('-' * 50)

# for key in sorted(fruit.keys()):
#     print(fruit[key])

# print('-' * 50)

# for key in fruit:
#     print(key)

# print('-' * 50)

# for val in fruit.values():
#     print(val)

# print('-' * 50)

# for key in fruit:
#     print(fruit[key]) # more efficient

# print('-' * 50)

# print(fruit.keys())  # returns dict_keys object
# print(fruit.values())  # dict_values  view object

# fruit_keys = fruit.keys()
# print(fruit_keys)

# fruit['tomato'] = 'not nice for ice cream, no?'

# print(fruit_keys)

# print(fruit.items())  # list of  key value pair tuples

f_tuple = tuple(fruit.items())
print(f_tuple)

for snack in f_tuple:
    item, description = snack
    print(item + " " + description)

print("+" * 90)

print(f_tuple)

print(dict(f_tuple))  # create a dictionary from a tuple of key value pair tuples



