# Basic Algorithms

# Exercise 1

# What is the output of this block of code?


def mut_example(list1, list2, list3):
    if len(list1) > 2:
        list1 = list1[:2]
    list2[0] = "hi"
    list3 = "".join(list2)

a_list = [1, 2, 3]
b_list = ["a", "b", "c"]
a_str = "do-re-mi"
mut_example(a_list, b_list, a_str)
print(a_list)
print(b_list)
print(a_str)




# Exercise 2

# What's the difference between sort and sorted?
#Sort modifies the list, sorted creates a new list
# Which one is a list method and which one is a function that works on lists?
#Sort is the method, sorted is a function

# Please explain



# Exercise 3

# Write a function that doubles the elements in a list.

test_list = list(range(5))

def doubling(listing):
    # dubbedlist = [2*item for item in listing]
    for item in range(len(listing)):
        listing[item] = listing[item] * 2

print(test_list)
doubling(test_list)
print(test_list)
# Do you need to return anything here?
# No


# Write a function that doubles the elements in a tuple.
test_tup = tuple(range(5))

def doubling(intuple):
    dubtuple = tuple([2*item for item in intuple])
    return dubtuple

print(test_tup)
print(doubling(test_tup))


# Do you need to return anything here?
#Yes


# Exercise 4

# Rewrite the pop, count, extend, reverse, and sort functions

tlist2 = list(range(10))
# tlist2 = []
print(tlist2)

def newpop(oldlist):
    if len(oldlist) > 0:
        retitem = oldlist[-1]
        oldlist = oldlist[0:-1]
    return oldlist

holder = newpop(tlist2)
print(holder)
print(tlist2)

print(tlist2.count(2))

def newcount(oldlist, num):
    count = 0
    for item in oldlist:
        if item == num:
            count += 1
    return count

print(newcount(tlist2, 2))

def newextend(oldlist, newlist):
    for item in newlist:
        oldlist.append(item)
    return oldlist

test_new = "table"

print(newextend(tlist2, test_new))

def newreverse(oldlist):
    retlist = []
    for item in oldlist[::-1]:
        retlist.append(item)
    return retlist

reversetest = newreverse(tlist2)

print(reversetest)



# Return the results in a new list and do not modify the original list

# (do not use the function you are rewriting)


# Exercise 5

# Fractions can be reprsented by the tuple (numerator, denominator)

# Write a function that adds two fractions



# Write a function that multiplies two fractions


# Write a function that simplifies a fraction


# Exercise 6

# write a function to calculate distance between two cartesian coordinates



# extension: make it work for more than two dimensions

