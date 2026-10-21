# Lesson 13: Handling errors (exercise)
# Replace every ____ with the right code, then run:  python3 exercises/13_errors.py


# 1. Turn text into an int. If that fails, return -1 instead of crashing
def to_number(text):
    try:
        return int(text)
    except ____:
        return -1


# 2. Divide a by b. If b is zero, return None
def safe_divide(a, b):
    try:
        return a / b
    except ____:
        return None


# 3. Get an item from a list. If the index doesn't exist, return "missing"
def get_item(items, index):
    try:
        return items[index]
    except ____:
        return "missing"


# 4. Look up a key in a dictionary. If the key isn't there, return "unknown"
def lookup(d, key):
    try:
        return d[key]
    except ____:
        return "unknown"


# 5. Add up only the entries that are valid numbers; skip the rest
entries = ["4", "x", "10", "", "6"]
good_total = 0
for e in entries:
    try:
        good_total += int(e)
    except ValueError:
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
check("to_number('12')", to_number("12"), 12)
check("to_number('abc')", to_number("abc"), -1)
check("safe_divide(10, 2)", safe_divide(10, 2), 5.0)
check("safe_divide(1, 0)", safe_divide(1, 0), None)
check("get_item([1, 2], 5)", get_item([1, 2], 5), "missing")
check("lookup({'a': 1}, 'b')", lookup({"a": 1}, "b"), "unknown")
check("good_total", good_total, 20)
if _failed == 0:
    print("All checks passed!")
