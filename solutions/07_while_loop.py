# Lesson 7: While loops (solution)
# Run:  python3 solutions/07_while_loop.py
# (If your program never ends, press Ctrl + C. You've made an infinite loop!)

# 1. Collect the numbers 1 to 5 into the list counted
counted = []
i = 1
while i <= 5:
    counted.append(i)
    i = i + 1

# 2. Count DOWN from 10 to 1
countdown = []
n = 10
while n >= 1:
    countdown.append(n)
    n -= 1

# 3. Add numbers 1, 2, 3, ... until the total is MORE than 20.
#    How many numbers did it take? (store in steps)
total = 0
steps = 0
while total <= 20:
    steps += 1
    total += steps

# 4. Use break: stop as soon as you find the first number divisible by 7
k = 50
while True:
    if k % 7 == 0:
        break
    k += 1
first_multiple_of_7 = k

# 5. Use continue: collect 1 to 10 but SKIP the multiples of 3
kept = []
m = 0
while m < 10:
    m += 1
    if m % 3 == 0:
        continue
    kept.append(m)

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
check("counted", counted, [1, 2, 3, 4, 5])
check("countdown", countdown, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
check("steps", steps, 6)
check("first_multiple_of_7", first_multiple_of_7, 56)
check("kept", kept, [1, 2, 4, 5, 7, 8, 10])
if _failed == 0:
    print("All checks passed!")
