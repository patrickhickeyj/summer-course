#Problem 1
def recursive_squares(n):
    if type(n) != int:
        return []
    if n < 1:
        return []
    if n == 1:
        return [1]
    else:
        return recursive_squares(n-1) + [n**2]

def palindrome_checker(word):
    cleaned = word.lower()
    if len(cleaned) < 2:
        return True
    elif cleaned[0] != cleaned[-1]:
        return False
    else:
        return palindrome_checker(cleaned[1:-1])

def length(tlist):
    if tlist:
        return length(tlist[:-1]) + 1
    return 0

def flatten(mixed_list):
    if len(mixed_list) < 1:
        return []
    elif type(mixed_list[0]) == int:
        return [mixed_list[0]] + flatten(mixed_list[1:])
    else:
        return flatten(mixed_list[0]) + flatten(mixed_list[1:])

#Problem 2

if __name__ == '__main__':
    def prob1():
        print(recursive_squares(5))
        print(recursive_squares([]))
        print(palindrome_checker('aab'))
        print(length([5, 6, 7, 8]))
        print(flatten([1, [2, 3], [4], 5]))

    def prob2():
        pass
    
    prob1()
    prob2()