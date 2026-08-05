#Problem 1
def recursive_squares(n):
    if n == 1:
        return [1]
    else:
        return recursive_squares(n-1) + [n ** 2]

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

if __name__ == '__main__':
    def prob1():
        print(recursive_squares(5))
        print(palindrome_checker('aab'))
        print(length([5, 6, 7, 8]))
    prob1()