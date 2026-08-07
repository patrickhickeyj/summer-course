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

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def count_ways(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return count_ways(n-2) + count_ways(n-1)

def grid_paths(m, n):
    if m == 1 or n ==1:
        return 1
    else:
        return grid_paths(m, n-1) + grid_paths(m-1, n)

def permutation(perm_list):
    if not perm_list:
        return []
    else:
        holder = []
        for i in range(len(perm_list)):
            hold = perm_list[i]
            clone = perm_list[:]
            del clone[i]
            holder.append([hold] + permutation(clone))
        return holder


if __name__ == '__main__':
    def prob1():
        print(recursive_squares(5))
        print(recursive_squares([]))
        print(palindrome_checker('aab'))
        print(length([5, 6, 7, 8]))
        print(flatten([1, [2, 3], [4], 5]))

    def prob2():
        print(fibonacci(7))
        print(count_ways(4))
        print(grid_paths(3, 3))
        print(permutation([1, 2, 3]))
    prob1()
    prob2()