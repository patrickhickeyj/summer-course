# Error 1
student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science",
    # "grade" : 5
}

# Safer approach
grade = student.get("grade", "No grade available")
print(grade)


# Error 2
inventory = {
    "apples": 10,
    "bananas": 5,
    "oranges": 8
}
print(f"We have {inventory.get('apples', 'no apples')} apples")

