# ## Conditions / if

# ## Exercise 1
# user_num = int(input("Give me an int for positive "))

# if user_num > 0:
#     print ("Positive")
# else:
#     print ("Not positive")

# ## Exercise 2
# user_odd_even = int(input("Give me an int for odd/even "))

# if user_odd_even % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# ## Exercise 3
# user_age = int(input("Give me an age integer"))

# if user_age < 13:
#     print("Child")
# elif user_age < 20:
#     print("Teenage")
# elif user_age < 65:
#     print("Adult")
# else:
#     print("Senior")

# ## Exercise 4
# user_compare_a = int(input("Give me int a to compare"))
# user_compare_b = int(input("Give me int b to compare"))

# if user_compare_a > user_compare_b:
#     print("a is bigger")
# elif user_compare_b > user_compare_a:
#     print("b is bigger")
# else:
#     print("they are the same")

# ## Exercise 5
# user_grade = float(input("Give me a test score"))

# if user_grade >= 90:
#     print("A")
# elif user_grade >= 80:
#     print("B")
# elif user_grade >= 70:
#     print("C")
# elif user_grade >= 60:
#     print("D")
# else:
#     print("F")

# ## Exercise 6
# user_string = input("Give me a string")

# if len(user_string) > 10:
#     print("Long string")
# else:
#     print("Short string")


# for i in range (1, 11):
#     print(i)

# print(i)

# name_list = ["bob", "jack", "ryan"]
# name_list.append("app1")
# name_list.append("app2")

# for loop_var in name_list:
#     print(loop_var)

# user_int = 1

# while user_int %2 == 1:
#     user_int = int(input("Give me an even int"))

# print("Here's your even number: ", user_int)

secret = 55

user_guess = -1
counter = 0

while user_guess != secret:
    user_guess = int(input("Guess the number "))
    if user_guess > secret:
        print("Too high")
    else:
        print("too low")
    counter += 1

print("You got the right number ", user_guess, " in ", counter, " guesses")

