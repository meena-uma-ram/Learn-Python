# Lesson 11: Functions (solution)
# Run:  python3 solutions/11_functions.py


# 1. A function that returns the square of n
def square(n):
    return n * n


# 2. A function that adds two numbers and returns the result
def add(a, b):
    return a + b


# 3. Return True if age is 18 or more, else False
def is_adult(age):
    if age >= 18:
        return True
    return False


# 4. Return a greeting. greeting defaults to "Hello" if not given
def greet(name, greeting="Hello"):
    return greeting + ", " + name + "!"


# 5. Return the bigger of two numbers (don't use max)
def bigger(x, y):
    if x > y:
        return x
    else:
        return y


# 6. Return the sum of all numbers in a list, using a loop
def total(numbers):
    result = 0
    for n in numbers:
        result += n
    return result


# 7. Convert Celsius to Fahrenheit:  F = C * 9 / 5 + 32
def to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


# 8. Call your functions: store the square of 7 in seven_squared
seven_squared = square(7)

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
check("square(4)", square(4), 16)
check("add(2, 3)", add(2, 3), 5)
check("is_adult(20)", is_adult(20), True)
check("is_adult(12)", is_adult(12), False)
check("greet('Zoe')", greet("Zoe"), "Hello, Zoe!")
check("greet('Zoe', 'Hi')", greet("Zoe", "Hi"), "Hi, Zoe!")
check("bigger(3, 9)", bigger(3, 9), 9)
check("bigger(10, 2)", bigger(10, 2), 10)
check("total([1, 2, 3, 4])", total([1, 2, 3, 4]), 10)
check("to_fahrenheit(100)", to_fahrenheit(100), 212)
check("seven_squared", seven_squared, 49)
if _failed == 0:
    print("All checks passed!")
