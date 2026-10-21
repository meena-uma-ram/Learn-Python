# Lesson 6: Decisions with if / else (solution)
# Run:  python3 solutions/06_if_else.py

# 1. Set result to "even" if n is even, otherwise "odd"
n = 9
if n % 2 == 0:
    result = "even"
else:
    result = "odd"

# 2. Set grade using: 90+ → "A", 80-89 → "B", 70-79 → "C", else "F"
score = 84
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

# 3. Can enter only if age is 18 or more AND has_ticket is True
age = 20
has_ticket = False
if age >= 18 and has_ticket:
    can_enter = True
else:
    can_enter = False

# 4. Set sign to "positive", "negative" or "zero"
x = -4
if x > 0:
    sign = "positive"
elif x < 0:
    sign = "negative"
else:
    sign = "zero"

# 5. Nested if: describe a temperature t
#    above 25 → "hot"; 15 to 25 → "warm"; below 15: if raining "wet and cold", else "cold"
t = 10
raining = True
if t > 25:
    weather = "hot"
elif t >= 15:
    weather = "warm"
else:
    if raining:
        weather = "wet and cold"
    else:
        weather = "cold"

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
check("result", result, "odd")
check("grade", grade, "B")
check("can_enter", can_enter, False)
check("sign", sign, "negative")
check("weather", weather, "wet and cold")
if _failed == 0:
    print("All checks passed!")
