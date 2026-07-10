PI = 3.14
diameter = float(input("Choose a diameter for the pizza "))
radius = diameter / 2
area = PI * radius ** 2
print("Area is", area)

cost = float(input("What is the cost of the pizza? "))

ppa = cost / area
print("Cost per area: ", ppa)

