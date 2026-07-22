# my_list = ['c', 'a', 't']
# my_string = 'cat'

# # Looping
# for item in my_list:
#     print(item)

# for char in my_string:
#     print(char)

# #Index / slicing

# print(my_list[0], my_string[0])
# print(my_list[-1], my_string[-1])
# print(my_string[0:2])

# # len(), in, and membership
# print(len(my_list), len(my_string))
# print('a' in my_list, 'a' in my_string)

# # big reveal
# print(list("cat"))


# def validate_name(namevar: str) -> bool:
#     boolreturn = True #Start here, check for disqualifiers
#     if len(namevar) < 5 or len(namevar) > 15:
#         boolreturn = False
#     if not namevar.replace('_','t').isalnum():
#         boolreturn = False
#     if not namevar[0].isalpha():
#         boolreturn = False
#     if namevar[-1] == "_":
#         boolreturn = False
    
#     digittest = False
#     for char in namevar:
#         if char.isdigit():
#             digittest = True
#     if not digittest:
#         boolreturn = False

#     return boolreturn

# # print(validate_name("gg5test"))

# assert validate_name("ryan2360") == True #Will give errors if it doesn't agree

#-----------------Imports-------------------

from area import circle_area, rectangle_area, tri_area

# print(rectangle_area(10, 10))
# print(tri_area(10, 10))
# print(circle_area(10))

#------------default values in functions-------------
def greet(name, greeting="Hello"):
    print(f'{greeting}, {name}!')

# greet("Pat")

#------------enumerate function-------

passengers = ["Lopez", "Chen", "Okafor", "Smith", "Patel"]

def print_boarding_list(list):
    for index, item in enumerate(list, 1):
        print(f'Seat {index}: {item}')

print_boarding_list(passengers)

print(list(enumerate(passengers))[1])
