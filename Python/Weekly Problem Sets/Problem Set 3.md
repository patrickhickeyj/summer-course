# Problem Set 3 — Data Structures, String Methods & List Methods

**Topics covered:** dictionaries, sets, string methods (`.lower()`, `.split()`, `.strip()`, `.replace()`, `.join()`, etc.), list methods (`.append()`, `.sort()`, `.count()`, `.remove()`, etc.)

---

## Problem 1 — Soldier Roster & Dispatch System 🪖

*HQ needs a searchable roster of available soldiers. Your program will parse incoming personnel reports, build a roster, and process dispatch orders.*

**You are given the following personnel reports as raw strings:**

```python
reports = [
    "SANTOS | Private | Fitness:91 | Status:available",
    "KOWALSKI | Corporal | Fitness:74 | Status:deployed",
    "OKAFOR | Sergeant | Fitness:88 | Status:available",
    "BRIGGS | Private | Fitness:55 | Status:available",
    "NAKAMURA | Corporal | Fitness:82 | Status:deployed",
    "REYES | Sergeant | Fitness:79 | Status:available",
]
```

**Your task:**

- Use a `for` loop to parse each report string. Use `.split("|")`, `.strip()`, and `.split(":")` to extract each field.
- Use `.title()` on names and `.lower()` on status values to normalise the data.
- Build a dictionary called `roster` where each key is a soldier's name and the value is a dictionary with keys `rank`, `fitness`, and `status`.
- Use a set to collect all unique ranks in the roster and print them.
- Build and print a list of all **available** soldiers, sorted alphabetically by name using `.sort()`.
- Write a function `dispatch(roster, name)` that sets a soldier's status to `"deployed"` if they are currently `"available"`, or prints a message if they are already deployed or not found.
- Call `dispatch()` on `"Santos"` and `"Kowalski"`, then print the updated roster status for both.

**Expected output (partial):**

```
=== ROSTER LOADED ===
6 soldiers on record.
Ranks on file: {'Private', 'Corporal', 'Sergeant'}

Available soldiers: ['Briggs', 'Okafor', 'Reyes', 'Santos']

Dispatching Santos...   Done. Status set to deployed.
Dispatching Kowalski... Kowalski is already deployed.

Updated status:
  Santos   : deployed
  Kowalski : deployed
```

### Challenge

Write a function `fitness_report(roster)` that builds and returns a dictionary with three keys — `"high"`, `"medium"`, and `"low"` — each mapping to a list of soldier names in that fitness band (high ≥ 80, medium 60–79, low < 60). Use `.append()` to build each list and `.sort()` to sort the names. Print the full report.

---

## Problem 2 — Recipe Ingredient Checker 🍳

*You're building a tool that helps cooks figure out what they can make with what's in their kitchen, and what they're missing.*

**You are given the following recipes and pantry:**

```python
recipes = {
    "omelette":        ["eggs", "butter", "salt", "pepper", "cheese"],
    "pancakes":        ["flour", "eggs", "milk", "butter", "sugar", "salt"],
    "tomato pasta":    ["pasta", "tomatoes", "garlic", "olive oil", "salt", "pepper"],
    "grilled cheese":  ["bread", "cheese", "butter"],
}

pantry = ["eggs", "butter", "salt", "pepper", "cheese", "milk", "bread", "garlic"]
```

**Your task:**

- Convert `pantry` to a set for efficient lookups.
- Write a function `can_make(recipe_ingredients, pantry_set)` that returns `True` if every ingredient is in the pantry, `False` otherwise.
- Write a function `missing_ingredients(recipe_ingredients, pantry_set)` that returns a **sorted list** of any ingredients not in the pantry. Use `.sort()` or `sorted()`.
- Use a `for` loop to go through each recipe, call both functions, and print whether it can be made and — if not — what's missing.
- At the end, print a list of all **unique ingredients** across all recipes, sorted alphabetically. Use a set and `.sort()`.

**Expected output:**

```
=== RECIPE CHECKER ===
omelette       : CAN MAKE ✓
pancakes       : MISSING — ['flour', 'sugar']
tomato pasta   : MISSING — ['olive oil', 'pasta', 'tomatoes']
grilled cheese : CAN MAKE ✓

All unique ingredients (12): ['bread', 'butter', 'cheese', 'eggs', ...]
```

### Challenge

Ask the user to type in a comma-separated list of extra ingredients they have on hand (e.g. `"flour, pasta, tomatoes"`). Use `.split(",")` and `.strip()` to parse the input, add the new items to the pantry set, and re-run the recipe checker. Print which recipes became newly available.

---

## Problem 3 — Song Lyric Word Counter 🎵

*Pick your favourite song and paste a few verses as a string in your code. Your program will analyse the lyrics and report word frequency statistics.*

**Your task:**

- Assign your chosen lyrics to a variable called `lyrics` as a multi-line string. Here is an example you can use if you prefer:

```python
lyrics = """
we will we will rock you
we will we will rock you
buddy youre a boy make a big noise
playing in the street gonna be a big man someday
you got mud on your face you big disgrace
kicking your can all over the place singing
we will we will rock you
"""
```

- Use `.lower()` to normalise the lyrics, then `.split()` to get a list of words.
- Use `.replace()` to strip out any punctuation characters you want to ignore (e.g. commas, apostrophes).
- Use a `for` loop and a dictionary to count how many times each word appears.
- Use `.sort()` on a list of the dictionary's keys to print every word and its count alphabetically.
- Use a set to find and print the number of **unique** words.
- Use `.count()` on the words list to verify the count of your most frequent word.
- Print the most frequently used word and its count.

**Expected output (partial, using example lyrics):**

```
=== WORD COUNT ===
a          : 4
all        : 1
be         : 1
big        : 3
...
we         : 6
will       : 6
...

Unique words: 26
Most common word: 'we' — 6 times
Verified with .count(): 6
```

### Challenge

Define a set of stop words to filter out common filler words before counting:

```python
stop_words = {"a", "the", "you", "your", "in", "on", "we", "be", "got"}
```

Use a `for` loop to build a filtered word list that excludes any word in `stop_words`. Re-run your word count on the filtered list and print the most common *meaningful* word.

---

## Problem 4 — Zoo Animal Registry 🦁

*You've just been hired as the data manager for a city zoo. Your job is to build and query a registry of animals currently in residence.*

**You are given the following raw data as a list of comma-separated strings:**

```python
raw_data = [
    "Simba, lion, 7, Africa",
    "Pebbles, penguin, 3, Antarctica",
    "Kovu, lion, 4, Africa",
    "Bubbles, dolphin, 12, Ocean",
    "Mango, parrot, 6, South America",
    "Nala, lion, 5, Africa",
    "Splash, dolphin, 8, Ocean",
    "Crackers, parrot, 2, South America",
]
```

**Your task:**

- Use a `for` loop to process each string. Use `.split(",")` and `.strip()` to parse each entry into its four fields: name, species, age, and origin.
- Build a dictionary called `registry` where each key is an animal's name and the value is another dictionary with keys `species`, `age`, and `origin`.
- Use a set to find all **unique species** in the zoo and print them.
- Use a set to find all **unique origins** and print how many distinct regions the zoo's animals come from.
- Ask the user to enter an animal's name. Use `.strip()` and `.title()` to clean the input, then look it up in the registry and print the result.

**Example output (partial):**

```
=== ZOO REGISTRY BUILT ===
8 animals registered.

Unique species: {'lion', 'penguin', 'dolphin', 'parrot'}
Animals come from 4 distinct regions.

Enter an animal name to look up: bubbles

Name:    Bubbles
Species: dolphin
Age:     12
Origin:  Ocean
```

### Challenge

Build a second dictionary called `by_species` where each key is a species name and the value is a list of animal names of that species. Use `.append()` to build each list. Then use `", ".join()` to print each species and its animals on one line, like:

```
lion    : Simba, Kovu, Nala
dolphin : Bubbles, Splash
...
```

---

## References

- [Python dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Python sets](https://docs.python.org/3/tutorial/datastructures.html#sets)
- [Python list methods](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [Python string methods](https://docs.python.org/3/library/stdtypes.html#string-methods)