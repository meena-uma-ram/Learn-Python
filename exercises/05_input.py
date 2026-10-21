# Lesson 5: Input (exercise)
# Replace every ____ with the right code, then run:  python3 exercises/05_input.py
#
# NOTE: So this file can check itself, input() is replaced below with a
# pretend version that "types" the answers for you. In a real program,
# you'd type them yourself.
_pretend_answers = ["Maya", "12", "1.5"]


def input(prompt=""):
    answer = _pretend_answers.pop(0)
    print(prompt + answer)
    return answer


# 1. Ask "What is your name? " and store the answer in name
name = ____("What is your name? ")

# 2. Ask "How old are you? " and store the answer AS A NUMBER (int) in age
age = ____(input("How old are you? "))

# 3. Ask "Height in metres? " and store the answer as a decimal number (float)
height = ____

# 4. Build the greeting "Hi Maya, next year you'll be 13"
greeting = "Hi " + name + ", next year you'll be " + ____
print(greeting)

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
check("name", name, "Maya")
check("age", age, 12)
check("height", height, 1.5)
check("greeting", greeting, "Hi Maya, next year you'll be 13")
if _failed == 0:
    print("All checks passed!")
