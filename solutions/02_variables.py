# Lesson 2: Variables (solution)
# Run:  python3 solutions/02_variables.py

# 1. Create a variable called city that holds the text "London"
city = "London"

# 2. Create a variable called year that holds the number 2024
year = 2024

# 3. Change year so it holds 2025
year = 2025

# 4. Create points = 10, then increase it by 5 using points itself
points = 10
points = points + 5

# 5. Copy the value of city into a new variable called home
home = city

# 6. Swap a and b so that a becomes 2 and b becomes 1
a = 1
b = 2
temp = a
a = b
b = temp

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
check("city", city, "London")
check("year", year, 2025)
check("points", points, 15)
check("home", home, "London")
check("a after swap", a, 2)
check("b after swap", b, 1)
if _failed == 0:
    print("All checks passed!")
