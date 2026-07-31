import math
import random

#Problem 1

def pizzas_needed(people, slices_per_person, slices_per_pizza, extra_percent = 0):
    total_slices = math.ceil(people * slices_per_person * (1 + extra_percent))
    total_pizzas = math.ceil(total_slices / slices_per_pizza)
    return total_pizzas

def leftover_slices(people, slices_per_person, slices_per_pizza):
    pizza_num = pizzas_needed(people, slices_per_person, slices_per_pizza)
    actual_slices = pizza_num * slices_per_pizza
    slices_needed = people * slices_per_person
    leftover = actual_slices - slices_needed
    return leftover

def getinfo():
    print("=== Pizza Party Planner ===")
    guests = int(input("How many guests? "))
    slice_per_person = int(input("Slices per person: "))
    slice_per_pizza = int(input('Slices per pizza: '))
    return guests, slice_per_person, slice_per_pizza

def givesummary(extra = 0):
    guests, slices, slice_per_pizza = getinfo()
    total_pizzas = pizzas_needed(guests, slices, slice_per_pizza, extra)
    leftovers = leftover_slices(guests, slices, slice_per_pizza)
    print()
    print('=== Party Summary ===')
    print(f'Guests:           {guests}')
    print(f'Pizzas to order:  {total_pizzas}')
    print(f'Total slices:     {total_pizzas * slice_per_pizza}')
    print(f'Leftover slices:  {leftovers}')

# givesummary(0.15)

#Problem 2

def o2_status(level):
    if level < 15:
        return "Critical"
    elif level >=15 and level <= 18:
        return "Low"
    elif level >=19 and level <=23:
        return "Normal"
    else:
        return "High"

def trend(readings):
    if len(readings) > 2:
        readings_end = readings[-3:]
        if readings_end[0] < readings_end[1] and readings_end[1] < readings_end[2]:
            return "Increasing"
        elif readings_end[0] > readings_end[1] and readings_end[1] > readings_end[2]:
            return "Decreasing"
        else:
            return "No Trend"
    else:
        return "Insufficient data"

def prob2():
    readings = [21, 20, 19, 17, 16, 14, 13, 15, 18, 21, 22, 24]

    lowcount = 0
    normcount = 0
    highcount = 0
    critcount = 0

    for i in range(len(readings)):
        reading = readings[i]
        status = o2_status(reading)
        print(f'Hour {i + 1}: {reading} - {status}')
        if status == "Critical":
            print("*** Alert: take action immediately ***")
            critcount += 1
        elif status == "Low":
            lowcount += 1
        elif status == "Normal":
            normcount +=1
        elif status == "High":
            highcount +=1
        else:
            print("Bad status")

    print()
    print("===Status Summary===")
    print(f'Normal:    {normcount} hours')
    print(f'Low:       {lowcount} hours')
    print(f'Critical:  {critcount} hours')
    print(f'High:      {highcount} hours')

    print(trend(readings))

# prob2()

#Problem 3
def critical_hit(damage):
    roll = random.randint(1, 5)
    if roll == 3:
        damage = damage * 2
    return damage

def attack(defender_hp, damage):
    return max((defender_hp - damage), 0)

def is_alive(hp):
    return hp > 0

def prob3():
    hero_hp = 100
    hero_dmg = 18
    monster_hp = 90
    monster_dmg = 12
    round_count = 1

    while is_alive(hero_hp) and is_alive(monster_hp):
        actual_hero_dmg = critical_hit(hero_dmg)
        monster_hp = attack(monster_hp, actual_hero_dmg)
        if monster_hp > 0:
            hero_hp = attack(hero_hp, monster_dmg)
        print(f'Round {round_count}: Hero HP: {hero_hp}   |  Monster HP: {monster_hp}')
        if actual_hero_dmg > hero_dmg:
            print("*** CRITICAL HIT ***")
        round_count +=1

    if hero_hp > 0:
        print("Hero wins!")
    else:
        print("Monster wins!")

# prob3()


#Problem 4
def check_fitness(score):
    return score >= 70

def check_rank(rank):
    return rank == "Corporal" or rank == "Sergeant" or rank == 'Lieutenant'

def check_service_years(years):
    return years >= 2

def prob4():
    name = input("What is your name? ")
    fit_score = int(input("What is your fitness score? "))
    rank = input("What is your rank? ")
    tos = int(input("How many years of service? "))

    function_list = [check_fitness, check_rank, check_service_years]
    data_list = [fit_score, rank, tos]
    result_list = []

    for i in range(len(function_list)):
        result_list.append(function_list[i](data_list[i]))

    clearance = True
    for result in result_list:
        if result == False:
            clearance = False

    if clearance:
        final_stat = "Cleared for mission"
    else:
        final_stat = "Not cleared"

    print(f'Solder Name: {name}')
    print(f'Fitness score: {fit_score}')
    print(f'Rank: {rank}')
    print(f'Years of Service: {tos}')
    print()
    print("=== Mission Clearance Report ===")
    print(f'Solder: {name}')
    print()
    print(f'\tFitness check:   {result_list[0]}')
    print(f'\tRank check:       {result_list[1]}')
    print(f'\tService check:     {result_list[2]}')
    print()
    print(f'Final Status: {final_stat}')

    checks = [
        ("Fitness check", check_fitness, fit_score),
        ("Rank check", check_rank, rank),
        ("Service check", check_service_years, tos),
    ]

    new_result = True

    for title, func, data in checks:
        print(f'{title}: {func(data)}')
        if func(data) == False:
            new_result = False
    print(f"New result is {"Cleared" if new_result else "Not Cleared"}")

# prob4()

#Problem 5
athletes = [
    ("Jordan",  82, 15),   # (name, games_played, goals_scored)
    ("Patel",   78, 22),
    ("Okonkwo", 90, 18),
    ("Li",      65, 9),
    ("Reyes",   88, 31),
    ("Fischer", 72, 14),
]

def goals_per_game(goals, games):
    if games == 0:
        return 0
    gpg = round(goals / games, 2)
    return gpg

def mvp_candiate(gpg):
    return gpg >= 0.25

def grade(gpg):
    if gpg <= 0.15:
        return 'F'
    if gpg <= 0.18:
        return 'D'
    if gpg <= 0.2:
        return 'C'
    if gpg <= 0.3:
        return 'B'
    return 'A'

print("===Season Leaderboard===")
print('Athlete      Games   Goals   GPG     MVP?    Grade')
print('--------------------------------------------------')

top_scorer = ''
top_score = 0

grade_dict = {
    'A' : 0,
    'B' : 0,
    'C' : 0,
    'D' : 0,
    'F' : 0
}

for name, games, goals in athletes:
    gpg = goals_per_game(goals, games)
    grade_dict[grade(gpg)] += 1
    print(f'{name}\t\t{games}\t{goals}\t{gpg}\t{'*' if mvp_candiate(gpg) else ''}\t{grade(gpg)}')
    if goals > top_score:
        top_score = goals
        top_scorer = name

print(f'Top scorer: {top_scorer} ({top_score} goals)')

for key, value in grade_dict.items():
    print(f'{key}: {value}')