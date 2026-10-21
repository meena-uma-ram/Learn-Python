# Answers to the Questions

Try each question yourself before reading these answers. For the fill-in-the-blank code, see the `solutions/` folder.

---

## Lesson 1: Instructions and output
1. In order, from top to bottom, one instruction at a time.
2. A comment is a note for humans that the computer ignores. In Python, it starts with `#`.
3. `print("3 + 4")` shows the text `3 + 4`. `print(3 + 4)` shows `7`.
4. `print("My name is Sam")`
5. `Hello` has no quotes, so Python thinks it's a variable name. That variable doesn't exist, so you get a `NameError`. Fix it with `print("Hello")`.

## Lesson 2: Variables
1. A variable is a labelled box. The label is the name and the contents are the value. You can look inside (use the value) or replace the contents (assign a new value).
2. `10`. The new value replaces the old one.
3. Allowed: `my_score`, `total`. Not allowed: `2nd_place` (starts with a number) and `first name` (has a space).
4. It reads the current value of `count`, adds 1, and stores the result back into `count`.
5. ```python
   food = "pizza"
   print(food)
   ```

## Lesson 3: Data types
1. `int` (e.g. `42`), `float` (e.g. `3.14`), `str` (e.g. `"hello"`), `bool` (`True` / `False`).
2. `"123"` is a `str` (it's in quotes). `123` is an `int`.
3. `int("10") + 5` gives `15`. `"10" + "5"` gives `"105"`, because joining two pieces of text just sticks them together.
4. `7`. `int()` cuts off the decimal part. It doesn't round.
5. You can't add text and a number. Fix: `"Age: " + str(30)`, or `print("Age:", 30)`, or `f"Age: {30}"`.

## Lesson 4: Operators
1. `=` stores a value in a variable. `==` asks "are these two values equal?" and gives `True` or `False`.
2. `17 // 5` is `3`. `17 % 5` is `2`.
3. A number is even if dividing it by 2 leaves no remainder: `n % 2 == 0`.
4. `(5 > 3) and (2 > 4)` → `True and False` → `False`. With `or` → `True`.
5. `24`.

## Lesson 5: Input
1. Always `str` (text).
2. `input()` returns text, and you can't add the number `1` to text, so you get a `TypeError`. Convert first: `int(input("Number: ")) + 1`.
3. `n = int(input("Enter a number: "))`
4. It's the **prompt**: the message shown to the user before they type.

## Lesson 6: if / else
1. It checks conditions from top to bottom and runs the block of the **first** condition that is `True`. If none are true, it runs the `else` block (if there is one).
2. `20` → `It's warm`. `10` → `It's cold`.
3. Indentation tells Python which lines belong inside the `if` / `elif` / `else` block. Wrong indentation changes the meaning or causes an `IndentationError`.
4. ```python
   if n % 2 == 0:
       print("even")
   else:
       print("odd")
   ```
5. ```python
   score = 85
   if score >= 90:
       print("A")
   elif score >= 80:
       print("B")
   elif score >= 70:
       print("C")
   else:
       print("F")
   ```
   This prints `B`.
6. It uses `=` (store) instead of `==` (compare), and the `print` should go on its own indented line:
   ```python
   if x == 5:
       print("five")
   ```

## Lesson 7: while loops
1. When its condition becomes `False` (or when `break` runs).
2. A loop whose condition never becomes `False`, so it runs forever. Avoid it by making sure something inside the loop changes the condition, such as increasing a counter.
3. `break` exits the loop immediately. `continue` skips the rest of the current round and jumps to the next one.
4. ```python
   n = 10
   while n >= 1:
       print(n)
       n -= 1
   ```
5. 3 times (when `i` is 0, 1 and 2).

## Lesson 8: for loops
1. `range(3)` → `0, 1, 2`. `range(2, 8, 3)` → `2, 5`.
2. When you know what you're going through (each item in a list, each letter in a string) or exactly how many times to repeat.
3. ```python
   for i in range(1, 11):
       print(5 * i)
   ```
4. ```python
   total = 0
   for n in range(2, 21, 2):
       total += n
   print(total)   # 110
   ```
5. 9 times (3 rows × 3 columns).

## Lesson 9: Lists
1. `0`.
2. `pets[1]` is `"dog"`, `pets[-1]` is `"fish"`, and `len(pets)` is `3`.
3. `pets.append("bird")`
4. `[20, 30]` (index 1 up to, but not including, index 3).
5. ```python
   numbers = [4, 17, 9, 2]
   largest = numbers[0]
   for n in numbers:
       if n > largest:
           largest = n
   print(largest)   # 17
   ```

## Lesson 10: Dictionaries
1. A list stores items in order and you find them by position (index). A dictionary stores key → value pairs and you find values by their key.
2. `d["y"]`
3. `d["z"] = 3`
4. You get a `KeyError`. A safer way is `d.get("w")`, which returns `None`, or `d.get("w", default)`. You can also check first with `if "w" in d:`.
5. ```python
   capitals = {"France": "Paris", "Japan": "Tokyo", "India": "New Delhi"}
   for country, capital in capitals.items():
       print(country, "→", capital)
   ```

## Lesson 11: Functions
1. You write the steps once and reuse them many times. Functions also make code shorter, easier to read, and easier to fix in one place.
2. A **parameter** is an input the function receives. A **return value** is the output it sends back.
3. `print` only shows a value on screen. `return` hands the value back to the code that called the function, so it can be stored or used.
4. ```python
   def square(n):
       return n * n
   ```
5. ```python
   def is_adult(age):
       return age >= 18
   ```

## Lesson 12: Strings
1. `5`
2. `"ana"` (indexes 1, 2, 3)
3. `"Hi".upper()`
4. `["red", "green", "blue"]`
5. `print(f"Total: {total}")`

## Lesson 13: Handling errors
1. It lets the program try something that might fail and handle the failure calmly instead of crashing.
2. `IndexError`
3. `ValueError`
4. ```python
   def safe_divide(a, b):
       if b == 0:
           return None
       return a / b
   ```
   or, using `try/except`:
   ```python
   def safe_divide(a, b):
       try:
           return a / b
       except ZeroDivisionError:
           return None
   ```

## Lesson 14: Final project (stretch goals)
1. Yes. The report loops over everything in the dictionary, so any new student is included automatically.
2. This is already in the exercise (step 4: `best_name`). Print it with `print("Top student:", best_name)`.
3. ```python
   name = input("Student name: ")
   if name in students:
       avg = average(students[name])
       print(f"{name}: {avg:.1f} → {letter_grade(avg)}")
   else:
       print("No such student")
   ```
4. `len(marks)` would be `0`, so dividing causes a `ZeroDivisionError`. Prevent it by checking first:
   ```python
   def average(marks):
       if len(marks) == 0:
           return 0
       return sum(marks) / len(marks)
   ```
