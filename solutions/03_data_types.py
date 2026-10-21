# Lesson 3: Data types (solution)
# Run:  python3 solutions/03_data_types.py

# 1. Store a whole number (int), a decimal (float), text (str) and a boolean
my_int = 10
my_float = 2.5
my_text = "hello"
my_bool = True

# 2. Convert the text "25" into a number so the addition works
age_text = "25"
age = int(age_text)
next_age = age + 1

# 3. Convert the number 99 into text so it can be joined to other text
label = "Score: " + str(99)

# 4. Convert the text "3.75" into a decimal number
price = float("3.75")

# 5. What type is "100"?  Write the type name: int, float, str or bool
type_of_text_100 = str

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
check("my_int is an int", type(my_int), int)
check("my_float is a float", type(my_float), float)
check("my_text is a str", type(my_text), str)
check("my_bool is a bool", type(my_bool), bool)
check("next_age", next_age, 26)
check("label", label, "Score: 99")
check("price", price, 3.75)
check("type of \"100\"", type_of_text_100, type("100"))
if _failed == 0:
    print("All checks passed!")
