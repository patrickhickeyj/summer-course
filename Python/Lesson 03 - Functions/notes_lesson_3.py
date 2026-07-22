import random

# Problem 1
# for i in range(1,101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# Problem 2
# person_holder = input("Give me rock, paper, or scissors")
# compchoice = random.randint(0, 2)

# name_holder = ["rock","paper","scissors"]

# if person_holder == name_holder[compchoice]:
#     print("You tie!")
# elif person_holder == "rock":
#     if compchoice == 1:
#         print("You lose")
#     else:
#         print("You win")
# elif person_holder == "paper":
#     if compchoice == 2:
#         print("You lose")
#     else:
#         print("You win")
# elif person_holder == "scissors":
#     if compchoice == 0:
#         print("You lose")
#     else:
#         print("You win")
# else:
#     print("Invalid choice")



# if compchoice == 0:
#     print("You win!")
# elif compchoice == 1:
#     print("You lose!")
# else:
#     print("You tie")

#Problem 3
# compchoice = random.randint(1, 100)
# userchoice = -1
# count = 0

# print("Don't cheat - number is ", compchoice)

# while userchoice != compchoice:
#     userchoice = int(input("Guess a number: "))
#     if userchoice > compchoice:
#         print("Too high!")
#     elif userchoice < compchoice:
#         print("Too low!")
#     count += 1

# print(f"Congrats! The number was {compchoice} and it took you {count} times")

#Problem 4


#Functions

# def area(num1: int, num2: int) -> int:
#     result = num1 * num2
#     return result

# def circ(num1: int, num2: int) -> int:
#     result = num1 * 2 + num2 * 2
#     return result

# length = int(input("Give me a length: "))
# width = int(input("Give me a width: "))

# x = area(length, width)
# y = circ(length, width)

# print(f"The area is: {x}")
# print(f"the circ is: {y}")

#In class 2

# def tip(total: float, percentage: float) -> float:
#     result = total * percentage / 100
#     return result

# print(f"{tip(200,20):.2f}")

#In class 4

def string_compare(s1: str, s2: str) -> str:
    if len(s1) > len(s2):
        return s1
    else:
        return s2
    
# string1 = "Have a nice day"
string2 = [1, 3, 4]
string1 = "Hello, it's very nice to meet you"

print(string_compare(string1, string2))

