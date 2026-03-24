# Problem Set 1 — Python Basics

**Topics covered:** `print()`, `range()`, `type()`, `input()`, type casting (`int()`, `float()`, `str()`, `bool()`)

---

## Problem 1 — Introduction Card

Write a program that asks the user for their **name** and their **favorite number**, then prints a personalized card using `print()`.

Your output should look something like this (content will vary based on input):

```
*******************************
*  Hello, Ryan!               *
*  Your favorite number is 7  *
*******************************
```

**Requirements:**
- Use `input()` to collect the name and favorite number
- Use `print()` to display the card with a border made of `*` characters
- The border of '*' characters should always be based on the length of the favorite number line

**Advanced:**
Use `type()` to print the data type of the name and the favorite number as collected from `input()`. Then use type casting to convert the favorite number to an `int` and a `float`, and print those converted values along with their types. Your output should look like:

```
Raw input type: <class 'str'>
As int: 7  -->  <class 'int'>
As float: 7.0  -->  <class 'float'>
```

---

## Problem 2 — Sequence Explorer

Use `range()` to print each of the following sequences. Each sequence should be printed on a single line, with values separated by spaces.

1. All integers from **1 to 15** (inclusive)
2. All **even** numbers from **2 to 30** (inclusive)
3. A **countdown** from **20 down to 0**, counting by 2s

**Example output for sequence 1:**
```
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
```

> Hint: Look into the `end` parameter of `print()` and the `step` argument of `range()`.

**Advanced:**
Ask the user to enter a **start**, **stop**, and **step** value. Use `input()` to collect these, then use `range()` to print the resulting sequence on one line. 
---

## Problem 3 — Drill Sergeant Fitness Test
 
*ATTENTION, RECRUIT! The Army Physical Fitness Test is underway. Your program will collect a soldier's performance data and report their results — no excuses accepted.*
 
**Your task:**
 
- Ask the soldier for their name and rank using `input()`.
- Ask how many push-ups they completed and how long their 2-mile run took (in minutes).
- Print a formatted after-action report with their name, rank, and both scores. Also print the soldier's average pace per mile for the run.
 
> **Note:** `input()` always returns a *string*. You will need to convert numbers before doing any arithmetic.
 
**Example run:**
 
```
ENTER SOLDIER NAME: John Baker
ENTER RANK: Private
PUSH-UPS COMPLETED: 42
2-MILE RUN TIME (minutes): 16
 
=== AFTER-ACTION REPORT ===
Soldier: Private John Baker
Push-ups: 42
2-mile run: 16.0 minutes
Average pace: 8.0 minutes per mile
DISMISSED.
```
---

## Problem 4 — Road Trip Fuel Calculator

Write a program that helps a driver estimate the fuel cost for a road trip.

Ask the user for:
1. The **distance** of the trip in miles
2. Their car's **fuel efficiency** in miles per gallon (MPG)
3. The current **price of gas** per gallon in dollars

Calculate and print:
- The number of gallons needed (rounded to 2 decimal places)
- The total fuel cost (rounded to 2 decimal places)

**Example output:**
```
--- Road Trip Fuel Estimate ---
Distance:        350 miles
Fuel efficiency: 28 MPG
Gas price:       $3.45 / gallon

Gallons needed:  12.5
Total fuel cost: $43.13
```

**Requirements:**
- Use `input()` for all three inputs
- Cast inputs to `float` using `float()`
- Use `print()` with clear labels for all output values

**Advanced:**
Extend the program to also calculate the cost for **3 different gas price scenarios** using `range()`:
- The price the user entered
- That price plus $0.50
- That price plus $1.00

Print all three estimates in a table. Use `range()` to loop through the three scenarios rather than writing three separate calculations.

```
--- Price Scenarios ---
Gas @ $3.45/gal:  Total = $43.13
Gas @ $3.95/gal:  Total = $49.38
Gas @ $4.45/gal:  Total = $55.63
```

---

## References

- [Python `print()` documentation](https://docs.python.org/3/library/functions.html#print)
- [Python `range()` documentation](https://docs.python.org/3/library/stdtypes.html#range)
- [Python `type()` documentation](https://docs.python.org/3/library/functions.html#type)
- [Python `input()` documentation](https://docs.python.org/3/library/functions.html#input)
- [Python Built-in Types](https://docs.python.org/3/library/stdtypes.html)
