# Lesson 9: Lists (exercise)
# Replace every ____ with the right code, then run:  python3 exercises/09_lists.py

animals = ["cat", "dog", "fish", "bird"]

# 1. Get the first and the last item
first = animals[____]
last = animals[____]

# 2. How many items are in the list?
how_many = ____

# 3. Add "hamster" to the end
animals.____("hamster")

# 4. Replace "fish" (index 2) with "turtle"
animals[____] = "turtle"

# 5. Remove "dog"
animals.____("dog")

# 6. Is "cat" in the list? (True/False)
has_cat = ____

# 7. Take a slice: the 2nd and 3rd numbers (indexes 1 and 2)
numbers = [10, 20, 30, 40, 50]
middle = numbers[____]

# 8. Find the biggest number WITHOUT using max(), using a loop
scores = [12, 45, 7, 33, 45, 2]
biggest = scores[0]
for s in scores:
    if ____:
        biggest = s

# 9. Build a new list containing only the scores above 10
high = []
for s in scores:
    if s > 10:
        ____

# ---------------------------------------------------------------
# Checks: don't edit below this line.
# ---------------------------------------------------------------
_failed = 0


def check(label, got, expected):
    global _failed
    if got == expected:
        print(f"  ✓ {label}")
    else:
        _failed += 1
        print(f"  ✗ {label}: expected {expected!r}, but got {got!r}")


print("\nChecking your answers...")
check("first", first, "cat")
check("last", last, "bird")
check("how_many", how_many, 4)
check("animals", animals, ["cat", "turtle", "bird", "hamster"])
check("has_cat", has_cat, True)
check("middle", middle, [20, 30])
check("biggest", biggest, 45)
check("high", high, [12, 45, 33, 45])
if _failed == 0:
    print("All checks passed!")
