# The Most Basic Python Tutorial

A from-zero tutorial. Each lesson has four parts:

1. **The idea**: the concept in plain words, with no programming language involved. These ideas exist in every language.
2. **In Python**: the same idea written as Python code.
3. **Fill in the blanks**: a practice file in `exercises/` where you complete the missing pieces (`____`).
4. **Questions**: check your understanding. The answers are in [`ANSWERS.md`](ANSWERS.md).

---

## How to use this tutorial

1. Install Python 3 from <https://www.python.org/downloads/>. Check that it works:
   ```
   python3 --version
   ```
2. Read one lesson below.
3. Open the matching file in `exercises/`, replace every `____` with the right code, and run it:
   ```
   python3 exercises/01_print.py
   ```
   If you got it right, you'll see `All checks passed!`. If not, the error message tells you which check failed.
4. Answer the questions for that lesson, then compare with [`ANSWERS.md`](ANSWERS.md).
5. Stuck? Peek at the `solutions/` folder, but try first.

> **Tip:** Errors are normal. Every programmer sees them all day. Read the last line of an error message first: it usually says what went wrong.

---

## Table of contents

| #  | Lesson | Exercise file |
|----|--------|---------------|
| 1  | [Instructions and output](#lesson-1--instructions-and-output) | `exercises/01_print.py` |
| 2  | [Variables](#lesson-2--variables) | `exercises/02_variables.py` |
| 3  | [Data types](#lesson-3--data-types) | `exercises/03_data_types.py` |
| 4  | [Operators](#lesson-4--operators) | `exercises/04_operators.py` |
| 5  | [Input](#lesson-5--input) | `exercises/05_input.py` |
| 6  | [Decisions: if / else](#lesson-6--decisions-if--else) | `exercises/06_if_else.py` |
| 7  | [Loops: while](#lesson-7--loops-while) | `exercises/07_while_loop.py` |
| 8  | [Loops: for](#lesson-8--loops-for) | `exercises/08_for_loop.py` |
| 9  | [Lists](#lesson-9--lists) | `exercises/09_lists.py` |
| 10 | [Dictionaries](#lesson-10--dictionaries) | `exercises/10_dictionaries.py` |
| 11 | [Functions](#lesson-11--functions) | `exercises/11_functions.py` |
| 12 | [Strings in depth](#lesson-12--strings-in-depth) | `exercises/12_strings.py` |
| 13 | [Handling errors](#lesson-13--handling-errors) | `exercises/13_errors.py` |
| 14 | [Final project: a grade calculator](#lesson-14--final-project-a-grade-calculator) | `exercises/14_project.py` |

---

## Lesson 1: Instructions and output

### The idea
A **program** is a list of instructions that a computer follows **in order, top to bottom**, one step at a time. It's like a recipe: step 1, then step 2, then step 3.

The simplest thing a program can do is **show something** to the person using it. This is called **output**.

A **comment** is a note written for humans. The computer ignores it.

### In Python
```python
# This is a comment. Python ignores everything after the # sign.
print("Hello, world!")      # shows: Hello, world!
print("I am learning.")     # shows: I am learning.
print(5)                    # shows: 5
print("Age:", 30)           # shows: Age: 30   (a comma puts a space between items)
print()                     # shows an empty line
```

Key points:
- `print(...)` shows whatever is inside the brackets.
- Text must be inside quotes: `"like this"` or `'like this'`.
- Numbers don't need quotes.
- Lines run in order, top to bottom.

### Fill in the blanks → `exercises/01_print.py`

### Questions
1. In what order does a computer run the instructions in a program?
2. What does a comment do? How do you write one in Python?
3. What does `print("3 + 4")` show? What about `print(3 + 4)`?
4. Write one line of Python that shows `My name is Sam`.
5. What is wrong with `print(Hello)`?

---

## Lesson 2: Variables

### The idea
A **variable** is a **labelled box** that holds a value. You give the box a name, put something in it, and later use the name to get the value back. You can also replace what's in the box.

Putting a value into a variable is called **assignment**.

### In Python
```python
name = "Asha"         # put "Asha" into a box called name
age = 25              # put 25 into a box called age

print(name)           # Asha
print(age)            # 25

age = 26              # replace the value: age is now 26
print(age)            # 26

age = age + 1         # take the current value, add 1, store it back
print(age)            # 27
```

Rules for variable names:
- Use letters, numbers and `_`. Don't start with a number. ✅ `score_1` ❌ `1score`
- No spaces. ✅ `first_name` ❌ `first name`
- Case matters: `Age` and `age` are two different variables.
- `=` means "store into", **not** "is equal to".

### Fill in the blanks → `exercises/02_variables.py`

### Questions
1. Explain a variable using the "box" idea.
2. After running `x = 5` then `x = 10`, what is in `x`?
3. Which of these names are allowed: `my_score`, `2nd_place`, `total`, `first name`?
4. What does `count = count + 1` do?
5. Write code that stores your favourite food in a variable and prints it.

---

## Lesson 3: Data types

### The idea
Values come in different **kinds**, called **types**. The type decides what you can do with a value. You can do maths with numbers but not with words.

The four most basic types:
| Type | What it is | Example |
|------|------------|---------|
| Whole number | A number with no decimal point | 42 |
| Decimal number | A number with a decimal point | 3.14 |
| Text | Letters, words, sentences | "hello" |
| True/False | Only two possible values: yes or no | True |

You can often **convert** a value from one type to another.

### In Python
```python
count = 42            # int    (integer, a whole number)
price = 9.99          # float  (decimal number)
city = "Paris"        # str    (string, which means text)
is_open = True        # bool   (boolean: True or False)

print(type(count))    # <class 'int'>
print(type(price))    # <class 'float'>
print(type(city))     # <class 'str'>
print(type(is_open))  # <class 'bool'>

# Converting between types
print(int("7") + 1)   # 8      text "7" → number 7
print(str(7) + "1")   # 71     number 7 → text "7", then joined with "1"
print(float(3))       # 3.0
print(int(3.9))       # 3      (int() cuts off the decimal, it does not round)
```

### Fill in the blanks → `exercises/03_data_types.py`

### Questions
1. Name the four basic types and give a Python example of each.
2. What is the type of `"123"`? What is the type of `123`?
3. What does `int("10") + 5` give? What about `"10" + "5"`?
4. What does `int(7.8)` give?
5. Why does `"Age: " + 30` cause an error? How would you fix it?

---

## Lesson 4: Operators

### The idea
**Operators** are symbols that do something with values: add them, compare them, or combine yes/no answers.

- **Arithmetic** operators do maths.
- **Comparison** operators ask a question and answer **True** or **False**.
- **Logical** operators combine True/False answers: *and* (both must be true), *or* (at least one true), *not* (flip it).

### In Python
```python
# Arithmetic
print(7 + 2)    # 9    add
print(7 - 2)    # 5    subtract
print(7 * 2)    # 14   multiply
print(7 / 2)    # 3.5  divide (always gives a float)
print(7 // 2)   # 3    whole-number division (drops the remainder)
print(7 % 2)    # 1    remainder ("modulo")
print(7 ** 2)   # 49   power (7 squared)

# Comparison: the answer is always True or False
print(5 > 3)    # True
print(5 < 3)    # False
print(5 == 5)   # True   (== means "is equal to?")
print(5 != 5)   # False  (!= means "is not equal to?")
print(5 >= 5)   # True
print(4 <= 3)   # False

# Logical
print(True and False)   # False  (both must be True)
print(True or False)    # True   (at least one True)
print(not True)         # False  (flips it)

# Shortcut assignment
score = 10
score += 5      # same as score = score + 5  → 15
score -= 2      # same as score = score - 2  → 13
```

> **Remember:** `=` stores a value. `==` compares two values.

### Fill in the blanks → `exercises/04_operators.py`

### Questions
1. What is the difference between `=` and `==`?
2. What do `17 // 5` and `17 % 5` give?
3. How can you use `%` to check if a number is even?
4. What does `(5 > 3) and (2 > 4)` give? What about `or` instead of `and`?
5. If `x = 8`, what is `x` after `x *= 3`?

---

## Lesson 5: Input

### The idea
**Input** is information the user gives to the program while it runs, such as typing their name. The program waits, reads what was typed, and can store it in a variable.

What the user types always arrives as **text**, even if they type digits. To do maths with it, you first convert it to a number.

### In Python
```python
name = input("What is your name? ")     # program waits for the user to type
print("Hello,", name)

age_text = input("How old are you? ")   # e.g. user types 20 → "20" (text!)
age = int(age_text)                     # convert to a number
print("Next year you will be", age + 1)

# Short version: convert straight away
height = float(input("Your height in metres: "))
```

### Fill in the blanks → `exercises/05_input.py`
(This exercise uses a pretend input so it can check itself.)

### Questions
1. What type is the value returned by `input()`?
2. Why does `input("Number: ") + 1` cause an error?
3. Write one line that asks for a number and stores it as an `int` in a variable `n`.
4. What does the text inside `input("...")` do?

---

## Lesson 6: Decisions: if / else

### The idea
Programs often need to **choose** what to do. "**If** it is raining, take an umbrella; **otherwise**, wear sunglasses."

A **condition** is a question whose answer is True or False. If it's True, one block of steps runs. If it's False, a different block runs (or nothing). You can check several conditions in order. The **first** one that is True wins.

### In Python
```python
temperature = 30

if temperature > 25:
    print("It's hot")             # runs only when the condition is True
elif temperature > 15:            # "else if": checked only if the one above was False
    print("It's warm")
else:
    print("It's cold")            # runs when none of the above were True
```

Key points:
- End the `if`, `elif` and `else` lines with a colon `:`.
- The lines **inside** each branch are **indented** (4 spaces). Indentation is how Python knows which lines belong to the branch.
- You can have any number of `elif`s, and `else` is optional.

```python
age = 16
has_ticket = True

if age >= 18 and has_ticket:
    print("You may enter")
else:
    print("Sorry, no entry")

# Nested if (an if inside an if)
number = 7
if number > 0:
    if number % 2 == 0:
        print("positive and even")
    else:
        print("positive and odd")
```

### Fill in the blanks → `exercises/06_if_else.py`

### Questions
1. In your own words, what does `if / elif / else` do?
2. What is printed if `temperature = 20` in the first example above? And `10`?
3. Why is indentation important in Python?
4. Write an `if/else` that prints `"even"` or `"odd"` for a variable `n`.
5. Given `score = 85`, write code that prints `"A"` for 90+, `"B"` for 80–89, `"C"` for 70–79, otherwise `"F"`.
6. What's the bug? `if x = 5: print("five")`

---

## Lesson 7: Loops: while

### The idea
A **loop** repeats steps so you don't have to write them over and over.

A **while loop** keeps repeating **as long as** a condition is True. "While the kettle isn't boiling, keep waiting." Something inside the loop must eventually make the condition False, or it repeats forever (an **infinite loop**).

### In Python
```python
count = 1
while count <= 5:
    print("Count is", count)
    count = count + 1       # without this line, the loop would never stop!
print("Done")
# Count is 1 ... Count is 5, then Done
```

Two special words work inside any loop:
- `break` stops the loop immediately.
- `continue` skips the rest of this round and goes to the next one.

```python
n = 0
while True:              # "forever"... until break
    n += 1
    if n == 3:
        continue         # skip printing 3
    if n > 5:
        break            # leave the loop
    print(n)             # prints 1 2 4 5
```

> If you accidentally make an infinite loop, press **Ctrl + C** to stop the program.

### Fill in the blanks → `exercises/07_while_loop.py`

### Questions
1. When does a while loop stop?
2. What is an infinite loop and how do you avoid one?
3. What does `break` do? What does `continue` do?
4. Write a while loop that prints 10, 9, 8, …, 1.
5. How many times does this print "hi"? `i = 0` / `while i < 3: print("hi"); i += 1`

---

## Lesson 8: Loops: for

### The idea
A **for loop** goes through a collection **one item at a time**: "**for each** apple in the basket, wash it." You use it when you know what you're going through (a list of things, or a range of numbers).

### In Python
```python
# Go through each item in a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("I like", fruit)

# Go through each letter of a string
for letter in "hi!":
    print(letter)

# range() makes a sequence of numbers
for i in range(5):          # 0, 1, 2, 3, 4   (stops BEFORE 5)
    print(i)

for i in range(1, 6):       # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):   # 0, 2, 4, 6, 8   (start, stop, step)
    print(i)

# Adding things up with a loop
total = 0
for n in range(1, 101):
    total += n
print(total)                # 5050

# A loop inside a loop
for row in range(3):
    for col in range(3):
        print(row, col)
```

**while or for?** Use `for` when you know what to go through or how many times. Use `while` when you repeat *until something happens*.

### Fill in the blanks → `exercises/08_for_loop.py`

### Questions
1. What numbers does `range(3)` produce? What about `range(2, 8, 3)`?
2. When would you choose a `for` loop instead of a `while` loop?
3. Write a for loop that prints the 5 times table (5, 10, …, 50).
4. Write a for loop that adds up all even numbers from 1 to 20.
5. How many times does the inner `print` run in the nested loop example above?

---

## Lesson 9: Lists

### The idea
A **list** is an **ordered collection** of values kept in one variable, like a shopping list. Each item has a **position number** called an **index**. Counting starts at **0**, not 1. You can add, remove, and change items.

### In Python
```python
colors = ["red", "green", "blue"]

print(colors[0])        # red     (first item, index 0)
print(colors[2])        # blue
print(colors[-1])       # blue    (negative counts from the end)
print(len(colors))      # 3       (how many items)

colors[1] = "yellow"    # change an item  → ["red", "yellow", "blue"]
colors.append("pink")   # add to the end  → ["red", "yellow", "blue", "pink"]
colors.remove("red")    # remove by value → ["yellow", "blue", "pink"]
print("blue" in colors) # True    (is it in the list?)

numbers = [4, 1, 3]
numbers.sort()          # → [1, 3, 4]
print(sum(numbers), max(numbers), min(numbers))   # 8 4 1

# Slicing: take part of a list  [start:stop]  (stop not included)
letters = ["a", "b", "c", "d", "e"]
print(letters[1:3])     # ['b', 'c']
print(letters[:2])      # ['a', 'b']

# Looping over a list
for c in colors:
    print(c)
```

### Fill in the blanks → `exercises/09_lists.py`

### Questions
1. What index does the first item of a list have?
2. Given `pets = ["cat", "dog", "fish"]`, what is `pets[1]`? `pets[-1]`? `len(pets)`?
3. How do you add `"bird"` to the end of `pets`?
4. What does `[10, 20, 30, 40][1:3]` give?
5. Write code that finds the largest number in a list **using a loop** (without `max`).

---

## Lesson 10: Dictionaries

### The idea
A **dictionary** stores **pairs**: a **key** and its **value**, like a real dictionary (word → meaning) or a phone book (name → number). You look things up by key, not by position.

### In Python
```python
person = {"name": "Leo", "age": 30, "city": "Rome"}

print(person["name"])        # Leo
person["age"] = 31           # change a value
person["job"] = "chef"       # add a new key-value pair
del person["city"]           # remove a pair

print("age" in person)       # True   (is this key present?)
print(person.get("email", "none"))  # none   (safe lookup with a default)

# Loop through key-value pairs
for key, value in person.items():
    print(key, "→", value)

# Counting with a dictionary
counts = {}
for word in ["a", "b", "a", "c", "a"]:
    counts[word] = counts.get(word, 0) + 1
print(counts)                # {'a': 3, 'b': 1, 'c': 1}
```

### Fill in the blanks → `exercises/10_dictionaries.py`

### Questions
1. How is a dictionary different from a list?
2. Given `d = {"x": 1, "y": 2}`, how do you get the value `2`?
3. How do you add the pair `"z": 3` to `d`?
4. What happens with `d["w"]` if `"w"` isn't a key? What's a safer way?
5. Write a dictionary of 3 countries and their capitals, then loop through it and print each pair.

---

## Lesson 11: Functions

### The idea
A **function** is a **named, reusable set of steps**. You define it once, then **call** it whenever you need it. Like a recipe card titled "make tea" that you can follow any time.

A function can take **inputs** (called **parameters**) and give back a **result** (a **return value**).

### In Python
```python
def greet():                     # define a function with no inputs
    print("Hello!")

greet()                          # call it → Hello!
greet()                          # call it again → Hello!

def greet_person(name):          # one parameter
    print("Hello,", name)

greet_person("Mia")              # Hello, Mia

def add(a, b):                   # two parameters, and it returns a result
    return a + b

result = add(3, 4)
print(result)                    # 7

def power(base, exponent=2):     # a default value for a parameter
    return base ** exponent

print(power(5))                  # 25  (uses exponent=2)
print(power(2, 3))               # 8
```

Key points:
- `def` starts a function definition. The body is indented.
- `return` sends a value back **and ends the function**.
- `print` only shows something. `return` gives a value you can store and use later.
- Variables made inside a function exist only inside it (this is called **scope**).

### Fill in the blanks → `exercises/11_functions.py`

### Questions
1. Why are functions useful?
2. What is the difference between a parameter and a return value?
3. What is the difference between `print` and `return` inside a function?
4. Write a function `square(n)` that returns `n * n`.
5. Write a function `is_adult(age)` that returns `True` if age is 18 or more, otherwise `False`.

---

## Lesson 12: Strings in depth

### The idea
Text is really a **sequence of characters** in order, a bit like a list of letters. You can measure it, pick out pieces, search it, and change its form (for example to uppercase).

### In Python
```python
word = "Python"
print(len(word))          # 6
print(word[0])            # P
print(word[-1])           # n
print(word[0:3])          # Pyt

msg = "  Hello World  "
print(msg.strip())        # "Hello World"   (removes outer spaces)
print(msg.upper())        # "  HELLO WORLD  "
print(msg.lower())        # "  hello world  "
print("World" in msg)     # True
print(msg.replace("World", "There"))   # "  Hello There  "

print("a,b,c".split(","))     # ['a', 'b', 'c']   text → list
print("-".join(["a", "b"]))   # a-b               list → text

# f-strings: put variables directly into text
name = "Ana"
age = 9
print(f"{name} is {age} years old")    # Ana is 9 years old
print(f"Next year: {age + 1}")         # Next year: 10
```

### Fill in the blanks → `exercises/12_strings.py`

### Questions
1. What does `len("hello")` return?
2. What is `"banana"[1:4]`?
3. How do you turn `"Hi"` into `"HI"`?
4. What does `"red green blue".split()` give?
5. Using an f-string, print `Total: 15` where `15` comes from a variable `total`.

---

## Lesson 13: Handling errors

### The idea
Sometimes something goes wrong while a program runs: the user types letters where a number was expected, or you divide by zero. Instead of crashing, a program can **try** something risky and **catch** the problem, then react calmly.

### In Python
```python
try:
    number = int("abc")           # this fails: "abc" isn't a number
    print("This line is skipped")
except ValueError:
    print("That was not a number!")

try:
    print(10 / 0)
except ZeroDivisionError:
    print("You can't divide by zero")

# Keep asking until the input is valid
while True:
    text = input("Enter a number: ")
    try:
        n = int(text)
        break                     # success → leave the loop
    except ValueError:
        print("Try again.")
print("You entered", n)
```

Common error types:
| Error | When it happens |
|-------|-----------------|
| `SyntaxError` | The code is written wrongly (missing `:` or bracket) |
| `NameError` | Using a variable that doesn't exist |
| `TypeError` | Mixing types wrongly, e.g. `"a" + 1` |
| `ValueError` | Right type, bad value, e.g. `int("abc")` |
| `IndexError` | List position doesn't exist |
| `KeyError` | Dictionary key doesn't exist |
| `ZeroDivisionError` | Dividing by zero |

### Fill in the blanks → `exercises/13_errors.py`

### Questions
1. What is the purpose of `try / except`?
2. Which error do you get from `[1, 2, 3][5]`?
3. Which error do you get from `int("hello")`?
4. Write a function `safe_divide(a, b)` that returns `a / b`, or `None` if `b` is zero.

---

## Lesson 14: Final project: a grade calculator

### The idea
Real programs combine everything: variables, lists, dictionaries, loops, decisions and functions all working together.

In this project you'll build a small program that:
1. Stores students and their marks in a dictionary.
2. Uses a function to calculate each student's average.
3. Uses `if/elif/else` to turn the average into a letter grade.
4. Loops over all students and prints a report.

### In Python (the shape of the solution)
```python
students = {
    "Ana": [90, 85, 100],
    "Ben": [70, 65, 80],
}

def average(marks):
    return sum(marks) / len(marks)

def letter_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    ...

for name, marks in students.items():
    avg = average(marks)
    print(f"{name}: {avg:.1f} → {letter_grade(avg)}")
```

### Fill in the blanks → `exercises/14_project.py`

### Questions (stretch goals)
1. Add a new student to the dictionary. Does your report update automatically? Why?
2. Change the program to also print the class's best student.
3. Change it to ask the user for a student's name with `input()` and print only their result.
4. What happens if a student has an empty list of marks? How could you prevent the crash?

---

## What next?

You now know the core building blocks that every programming language shares: **output, variables, types, operators, input, decisions, loops, collections, functions and error handling**.

Good next topics:
- Reading and writing files (`open()`)
- Modules and `import` (e.g. `import random`, `import math`)
- Classes and objects
- Small projects: a number-guessing game, a to-do list, a quiz program
