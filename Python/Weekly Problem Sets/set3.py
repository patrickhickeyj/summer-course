import random
import math
import turtle

#Problem 1
def roll(sides):
    result = random.randint(1, sides)
    return result

def roll_many(num_dice, sides):
    result = []
    for i in range(num_dice):
        result.append(roll(sides))
    return result

def twod6():
    res_list = roll_many(2, 6)
    print('=== Movement check (2d6) ===')
    print(f'Roll 1: {res_list[0]}\tRoll 2: {res_list[1]}\tTotal: {res_list[0] + res_list[1]}')
    print()

# twod6()

def oned20():
    result = roll(20)
    message = ''
    if result == 1:
        message = 'Critical Miss!'
    elif result == 20:
        message = 'Critical Hit!'
    print('===Attack Check (1d20) ===')
    print(f'Roll: {result} {message}')
    print()

# oned20()

def threed8():
    result = roll_many(3, 8)
    total = sum(result)
    avg = total / len(result)
    print('==Damage Roll (3d8)===')
    print(f'Rolls:\t{result}\tTotal: {total}\tAverage: {avg}')

# threed8()

def sim1000():
    holder = []
    for i in range(1000):
        result = roll_many(3, 8)
        total = sum(result)
        holder.append(total)
    final_avg = sum(holder) / len(holder)
    print('===Simulation (1000 damage rolls) ===')
    print(f'Simulated average total:\t{final_avg}')
    print(f'Theoretical average:\t13.5')

# sim1000()

def chall1():
    print()
    quote_list = [
        'Quote 1',
        'Quote 2',
        'Quote 3',
        'Quote 4',
        'Quote 5'
    ]
    print(random.choice(quote_list))

# chall1()

#Problem 2
def distance(x1, y1, x2, y2):
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return round(distance, 2)

def orbit_circumference(radius):
    result = 2 * radius * math.pi
    return round(result, 2)

def fuel_need(mass, velocity):
    energy = 0.5 * mass * velocity ** 2
    return (math.floor(energy * 100)) / 100

ship_pos    = (0, 0)
station_pos = (143, 892)
orbit_radius = 6371        # km (Earth's radius)
ship_mass    = 50000       # kg
ship_velocity = 7800       # m/s

def bearing(x1, y1, x2, y2):
    res = math.atan2(y2 - y1, x2 - x1)
    return math.degrees(res)

def print_report():
    x1, y1 = ship_pos
    x2, y2 = station_pos
    dist = distance(x1, y1, x2, y2)

    print('===Navigation Report===')
    print(f'Distance to station: \t{dist}')
    print(f'Orbit circumference: \t {orbit_circumference(orbit_radius)}')
    print(f'Kinetic energy (fuel): \t {fuel_need(ship_mass, ship_velocity)} J')
    print(f'Log10 of velocity: {round(math.log(ship_velocity, 10), 2)}')
    print(f'Bearing is: \t {round(bearing(x1, y1, x2, y2), 2)} degrees')
    print(f'Ceiling:\t {math.ceil(dist)}')
    print(f'Floor: \t\t {math.floor(dist)}')

# print_report()


#Problem 3
def draw_sun(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.color('yellow')
    t.circle(25)
    t.end_fill()

def draw_grass(t, x, y):
    depth = 110
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.color('green')
    t.forward(abs(x) * 2)
    t.right(90)
    t.forward(depth)
    t.right(90)
    t.forward(abs(x) * 2)
    t.right(90)
    t.forward(depth)
    t.end_fill()

def draw_pond(t, x, y):
    r =40
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.color('blue')
    # t.shapesize(5, 2, 1)
    t.left(45)
    for loop in range(2):
        t.circle(r,90)
        t.circle(r/2,90)
    t.right(45)
    t.end_fill()
    t.penup()

def draw_trunk(t, x, y, height):
    width = 15
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.color('brown')
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.end_fill()

def draw_leaves(t, x, y, height):
    t.penup()
    t.goto(x + 30, y + height + 10)
    t.pendown()
    t.begin_fill()
    t.color('green')
    t.circle(25)
    t.end_fill()

def draw_tree(t, x, y, height):
    draw_trunk(t, x, y, height)
    draw_leaves(t, x, y, height)

def prob3():
    t = turtle.Turtle()
    t.speed(0)
    draw_sun(t, -250, 250)
    draw_grass(t, -400, -250)
    draw_pond(t, 0, -300)
    # draw_tree(t, 200, -300, 60)

    for i in range(10):
        tree_x = random.randint(-380, 380)
        tree_height = random.randint(40, 100)
        draw_tree(t, tree_x, -300, tree_height)

    turtle.done()

# prob3()

#Prob 4
def prob4():
    secret = random.randint(1, 100)
    guess = 0
    counter = 0
    guess_list = []

    while guess != secret:
        guess = int(input("Guess a number between 1 and 100: "))
        dif = math.fabs(secret - guess)
        if dif > 40:
            print("Ice cold")
        elif dif > 20:
            print("Cold")
        elif dif > 10:
            print("Warm")
        else:
            print('Hot')
        counter += 1
        guess_list.append(guess)

    print(f'It took {counter} guesses')
    print(f'Miminum possible guesses (optimal): {math.ceil(math.log2(100))}')
    print(f'Guess sum is {sum(guess_list)}')
    print(f'Guess mean is: {sum(guess_list) / len(guess_list)}')

# prob4()

#Prob 5

def spiral(t, laps, col = 'black'):
    color_list = ['red', 'green', 'blue', 'orange', 'yellow', 'purple']
    start_len = 10
    increment = 5
    t.penup()
    t.goto(0, 0)
    t.pendown()
    tempcol = col
    for i in range(laps * 4):
        t.forward(start_len + i * increment)
        t.right(90)
        if col == 'rainbow':
            tempcol = color_list[i % len(color_list)]
        t.color(tempcol)

        
def prob5():
    t = turtle.Turtle()
    t.speed(0)
    spiral(t, 10, 'rainbow')
    turtle.done()

prob5()