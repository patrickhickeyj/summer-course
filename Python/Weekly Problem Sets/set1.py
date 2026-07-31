#Problem 1
def prob1():
    name = input("What is your name?")
    number = input("What is your favorite number?")

    response = f'Your favorite number is {number}'
    baselength = len(response)

    border = '*' * (baselength + 4)
    namelen = len(name)

    print(border)
    print(f'* Hello, {name}! {" " * (baselength - namelen - 8)}*')
    print(f'* {response} *')
    print(border)

    print(f'Raw input type: {type(number)}')
    print(f'As int: {int(number)} --> {type(int(number))}')
    print(f'As float: {float(number)} --> {type(float(number))}')

# prob1()

#Problem 2
def prob2():
    for i in range(1, 16):
        print(i, end = ' ')
    # print([i in range(1, 15)])
    print()
    for i in range(2, 31, 2):
        print(i, end = ' ')
    print()
    for i in range(20, -1, -2):
        print(i, end = ' ')
    print()

    use_start = int(input("Choose a start number"))
    use_stop = int(input("Choose an end number"))
    use_step = int(input("Choose a step"))

    for i in range(use_start, use_stop, use_step):
        print(i, end = ' ')

# prob2()

#Problem 3
def prob3():
    solname = input("Enter Soldier Name: ")
    solrank = input("Enter Rank: ")
    pushups = float(input("Pushups Completed: "))
    runmin = float(input("2-mile run time (minutes): "))
    pace = runmin / 2


    print("=== After-Action Report ===")
    print(f'Solder: {solrank} {solname}')
    print(f'Push-pups: {pushups}')
    print(f'2-mile run: {runmin}')
    print(f'Average pace: {pace:.2f} minutes per mile')
    print('Dismissed')

# prob3()

#Problem 4
def prob4():
    dist = float(input("What is the trip distance? "))
    efficiency = float(input("What is the efficiency in mpg? "))
    price = float(input("What is the current gas price? "))

    needed = dist / efficiency
    cost = needed * price

    print('--- Road Trip Fuel Estimate ---')
    print(f'Distance:        {dist} miles')
    print(f'Fuel Efficiency: {efficiency} mpg')
    print(f'Gas price:       ${price} / gallon')
    print()
    print(f'Gallons needed {needed:.2f}')
    print(f'Total fuel cost: ${cost:.2f}')

    print()
    print('--Price Scenarios--')
    for i in range(-1, 2):
        cost = needed * (price + (i * 0.5))
        print(f'Gas @ ${price + (i * 0.5):.2f}/gal: Total = ${cost:.2f}')

prob4()