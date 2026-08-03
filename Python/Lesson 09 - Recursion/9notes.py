def factorial(n):
    if n == 1 or n ==0:
        return 1
    return n * factorial(n-1)

print(factorial(7))

def palindrome(input_str):
    if input_str == '' or len(input_str) == 1:
        return True
    if input_str[0] != input_str[-1]:
        return False
    return(palindrome(input_str[1:-1]))

print(palindrome('chicken'))

def getsum(list):
    if len(list) == 0:
        return 0
    if len(list) == 1:
        return list[0]
    hold = list.pop()
    list[-1] += hold
    return getsum(list)

print(getsum([1, 2, 3, 4, 5]))

