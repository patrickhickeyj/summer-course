# # Notes

# Don't have to declare variables

#  Data type casting - 
#     - int()
#     - float()
#     - str()
#     - bool()

# Operators
#  // - integer/floor
# % - modulo

# Assignment
#  x += 5
# -=
# *=

# Comparison - always evaluate to boolean
# x<y
# x==y
# x!=y

# Logical
# x or y
# x and y
# not x

# Variables Names
# - descriptive
# - snake_case_for_variables
# - UseCapWords for class names
# - use ALLCAPs for constants

# name = input('What is your name ') - allows you to interact with the script

# note to myself about stuff that's happenig

u_name = input('What is your name? ')
u_number = float(input('What is your favorite number? '))
print("Hello " + u_name)
print("Your favorite number is " + str(u_number))
print("Your favorite number minus 10 is " + str(u_number - 10))

# fstrings - inline variable stuff
print(f'fstring test {u_name}')

#by default "print" has a new line character at the end
#can add argument print("Pat", end="") which will remove that (add \n to add more)
# can add sep argument to change how things are done

