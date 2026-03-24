# Problem Set 2 — Control Flow & Functions
 
**Topics covered:** conditional statements (`if`/`elif`/`else`), `for` loops, `while` loops, functions (`def`, parameters, return values)
 
---
 
## Problem 1 — Pizza Party Planner 🍕
 
*You're organising a pizza party and need to figure out how many pizzas to order. Write a program that helps the host plan for any group size.*
 
**Your task:**
 
- Write a function `pizzas_needed(people, slices_per_person, slices_per_pizza)` that calculates and returns how many whole pizzas to order (always round **up** — you never want to run short!).
- Write another function `leftover_slices(people, slices_per_person, slices_per_pizza` that returns how many slices will be leftover.
- Use input statements to ask how many guests, slices per person, and slices per pizza.
- Using your user defined functions, print the PARTY SUMMARY shown below.

**Example run:**
 
```
=== PIZZA PARTY PLANNER ===
How many guests? 14
Slices per person: 3
Slices per pizza: 8

 
=== PARTY SUMMARY ===
Guests:           14
Pizzas to order:  6
Total slices:     48
Leftover slices:  6
 
```
 
### Challenge
 
Extend `pizzas_needed()` to accept an optional `extra_percent` parameter (default `0`) that adds a percentage buffer to the guest count before calculating — useful for unexpected guests. For example, `extra_percent=10` would plan for 10% more people. Call the function with a 15% buffer and compare the result to the unbuffered version.
 
---
 
## Problem 2 — Space Station Oxygen Monitor 🚀
 
*Aboard the ISS, oxygen levels must be continuously monitored. Write a simulation that tracks O2 levels and triggers alerts.*
 
**Your task:**
 
- Write a function `o2_status(level)` that returns:
  - `"CRITICAL"` if level < 15
  - `"LOW"` if level is 15–18
  - `"NORMAL"` if level is 19–23
  - `"HIGH"` if level > 23
- You are given the following hourly O2 readings (as a percentage):
 
```python
readings = [21, 20, 19, 17, 16, 14, 13, 15, 18, 21, 22, 21]
```
 
- Use a `for` loop to process each reading, call your function, and print the hour and status.
- Use conditionals to print an extra `*** ALERT: TAKE ACTION IMMEDIATELY ***` line whenever the status is `CRITICAL`.
- After the loop, print a summary: how many hours were spent in each status category.
 
**Expected output (partial):**
 
```
Hour  1:  21%  —  NORMAL
Hour  2:  20%  —  NORMAL
Hour  3:  19%  —  NORMAL
Hour  4:  17%  —  LOW
Hour  5:  16%  —  LOW
Hour  6:  14%  —  CRITICAL
*** ALERT: TAKE ACTION IMMEDIATELY ***
...
 
=== STATUS SUMMARY ===
NORMAL:    6 hours
LOW:       3 hours
CRITICAL:  2 hours
HIGH:      1 hour
```
 
### Challenge
 
Add a second function `trend(readings)` that looks at the readings list and returns `"IMPROVING"`, `"DECLINING"`, or `"STABLE"` based on whether the last 3 readings are going up, going down, or neither. Print the trend at the end of the summary.
 
---
 
## Problem 3 — RPG Character Battle ⚔️
 
*You're simulating a turn-based battle between a hero and a monster. Each turn, the hero attacks the monster and then the monster strikes back — until one of them runs out of HP.*
 
**Your task:**
 
- Write a function `attack(defender_hp, damage)` that subtracts damage from defender HP and returns the new HP (minimum 0).
- Write a function `is_alive(hp)` that returns `True` if HP > 0.
- Use a `while` loop to simulate the battle. Each round:
  - The hero deals 18 damage to the monster.
  - If the monster is still alive, it deals 12 damage to the hero.
  - Print the round number and both HP values after each exchange.
  - End the loop when either combatant reaches 0 HP.
- Use conditionals after the loop to print who won.
 
**Starting values:**
 
```python
hero_hp = 100
monster_hp = 90
```
 
**Expected output (partial):**
 
```
=== BATTLE START ===
Round 1:  Hero HP: 88   |  Monster HP: 72
Round 2:  Hero HP: 76   |  Monster HP: 54
Round 3:  Hero HP: 64   |  Monster HP: 36
...
HERO WINS! The monster has been defeated.
```
 
### Challenge
 
Add a `critical_hit(damage)` function that returns double damage 20% of the time (hint: use `random.randint(1, 10)` — import `random` at the top). Apply it to the hero's attack each round and print `*** CRITICAL HIT! ***` when it triggers.
 
---
 
## Problem 4 — Mission Clearance System 🪖
 
*A soldier must pass a series of automated checks before being cleared for a mission. Your program will run each check and produce a final clearance report.*
 
**Your task:**
 
Define a function for each of the following checks — each should return `True` (cleared) or `False` (denied):
 
```python
def check_fitness(score):
    """Cleared if score >= 70."""
 
def check_rank(rank):
    """Cleared if rank is 'Corporal', 'Sergeant', or 'Lieutenant'."""
 
def check_service_years(years):
    """Cleared if years >= 2."""
```
 
Then write a main program that:
- Collects the soldier's name, fitness score, rank, and years of service using `input()`.
- Uses a `for` loop to run all three checks and store each result.
- Uses conditionals to determine overall clearance: the soldier is cleared only if **all three checks pass**.
- Prints a full clearance report showing each individual check and the final decision.
 
**Example run:**
 
```
SOLDIER NAME: James Okafor
FITNESS SCORE: 83
RANK: Corporal
YEARS OF SERVICE: 3
 
=== MISSION CLEARANCE REPORT ===
Soldier: James Okafor
 
  Fitness check:    PASS
  Rank check:       PASS
  Service check:    PASS
 
FINAL STATUS: CLEARED FOR MISSION.
```
 
### Challenge
 
Store the three check functions in a list of tuples alongside their labels and input values:
 
```python
checks = [
    ("Fitness check", check_fitness, fitness_score),
    ("Rank check", check_rank, rank),
    ("Service check", check_service_years, years),
]
```
 
Then use a single `for` loop to run all checks, print each result, and determine the final clearance — without any repeated `if` statements for individual checks.
 
---
 
## Problem 5 — Sports Leaderboard 🏆
 
*The season is over and it's time to crunch the numbers. Write a program that processes a list of athletes and generates a leaderboard.*
 
**You are given the following data:**
 
```python
athletes = [
    ("Jordan",  82, 15),   # (name, games_played, goals_scored)
    ("Patel",   78, 22),
    ("Okonkwo", 90, 18),
    ("Li",      65, 9),
    ("Reyes",   88, 31),
    ("Fischer", 72, 14),
]
```
 
**Your task:**
 
- Write a function `goals_per_game(goals, games)` that returns goals per game rounded to 2 decimal places. Return `0.0` if games played is 0.
- Write a function `mvp_candidate(gpg)` that returns `True` if the rate is 0.25 or higher.
- Use a `for` loop to process each athlete, call both functions, and print a formatted leaderboard. Use a conditional to mark MVP candidates with a `*`.
- After the loop, print the name of the top scorer (most total goals).
 
**Expected output:**
 
```
=== SEASON LEADERBOARD ===
  Athlete       Games   Goals   GPG     MVP?
  ------------------------------------------
  Jordan        82      15      0.18
  Patel         78      22      0.28    *
  Okonkwo       90      18      0.20
  Li            65      9       0.14
  Reyes         88      31      0.35    *
  Fischer       72      14      0.19
 
Top scorer: Reyes (31 goals)
```
 
### Challenge
 
Add a `grade(gpg)` function that returns a letter grade (`A`, `B`, `C`, `D`, or `F`) based on the GPG rate. Define your own grading scale, add the grade to each row, and print a grade distribution summary after the leaderboard using a `for` loop and a dictionary to count grades.
 
---
 
## References
 
- [Python `if` statements](https://docs.python.org/3/tutorial/controlflow.html#if-statements)
- [Python `for` loops](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [Python `while` loops](https://docs.python.org/3/reference/compound_stmts.html#while)
- [Python functions (`def`)](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Python `break` and `continue`](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops)