# Lesson 4: Operators (exercise)
# Replace every ____ with the right code, then run:  python3 exercises/04_operators.py

a = 17
b = 5

# 1. Arithmetic
total = ____            # a plus b
difference = ____       # a minus b
product = ____          # a times b
quotient = ____         # a divided by b (decimal answer)
whole_part = ____      # how many whole times b fits into a
remainder = ____        # what's left over
squared = ____         # b to the power of 2

# 2. Comparison (each answer is True or False)
a_is_bigger = ____      # is a greater than b?
are_equal = ____       # is a equal to b?

# 3. Use % to check whether n is even (True/False)
n = 14
n_is_even = ____

# 4. Logical: True only if BOTH a > 10 AND b < 10
both = ____

# 5. Increase score by 3 using the += shortcut
score = 7
score += ____

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
check("total", total, 22)
check("difference", difference, 12)
check("product", product, 85)
check("quotient", quotient, 3.4)
check("whole_part", whole_part, 3)
check("remainder", remainder, 2)
check("squared", squared, 25)
check("a_is_bigger", a_is_bigger, True)
check("are_equal", are_equal, False)
check("n_is_even", n_is_even, True)
check("both", both, True)
check("score", score, 10)
if _failed == 0:
    print("All checks passed!")
