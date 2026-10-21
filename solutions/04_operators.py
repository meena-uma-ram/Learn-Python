# Lesson 4: Operators (solution)
# Run:  python3 solutions/04_operators.py

a = 17
b = 5

# 1. Arithmetic
total = a + b            # a plus b
difference = a - b       # a minus b
product = a * b          # a times b
quotient = a / b         # a divided by b (decimal answer)
whole_part = a // b      # how many whole times b fits into a
remainder = a % b        # what's left over
squared = b ** 2         # b to the power of 2

# 2. Comparison (each answer is True or False)
a_is_bigger = a > b      # is a greater than b?
are_equal = a == b       # is a equal to b?

# 3. Use % to check whether n is even (True/False)
n = 14
n_is_even = n % 2 == 0

# 4. Logical: True only if BOTH a > 10 AND b < 10
both = a > 10 and b < 10

# 5. Increase score by 3 using the += shortcut
score = 7
score += 3

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
