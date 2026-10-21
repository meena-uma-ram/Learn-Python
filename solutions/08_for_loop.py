# Lesson 8: For loops (solution)
# Run:  python3 solutions/08_for_loop.py

# 1. Build a list of each fruit in uppercase
fruits = ["apple", "banana", "cherry"]
shouted = []
for fruit in fruits:
    shouted.append(fruit.upper())

# 2. Use range() to collect the numbers 1 to 10
one_to_ten = []
for i in range(1, 11):
    one_to_ten.append(i)

# 3. Add up all numbers from 1 to 100
total = 0
for n in range(1, 101):
    total = total + n

# 4. Collect the 5 times table: 5, 10, 15, ... 50
table = []
for i in range(1, 11):
    table.append(5 * i)

# 5. Count how many letters "s" are in the word
word = "mississippi"
s_count = 0
for letter in word:
    if letter == "s":
        s_count += 1

# 6. Even numbers from 0 to 20 using a step in range(start, stop, step)
evens = []
for e in range(0, 21, 2):
    evens.append(e)

# 7. Nested loops: build all pairs (row, col) for a 2 x 3 grid
pairs = []
for row in range(2):
    for col in range(3):
        pairs.append((row, col))

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
check("shouted", shouted, ["APPLE", "BANANA", "CHERRY"])
check("one_to_ten", one_to_ten, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
check("total", total, 5050)
check("table", table, [5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
check("s_count", s_count, 4)
check("evens", evens, [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
check("pairs", pairs, [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)])
if _failed == 0:
    print("All checks passed!")
