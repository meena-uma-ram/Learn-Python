# Lesson 10: Dictionaries (exercise)
# Replace every ____ with the right code, then run:  python3 exercises/10_dictionaries.py

book = {"title": "Matilda", "author": "Roald Dahl", "pages": 240}

# 1. Get the author
author = book[____]

# 2. Change pages to 250
book["pages"] = ____

# 3. Add a new key "year" with value 1988
book[____] = 1988

# 4. Is the key "title" in the dictionary? (True/False)
has_title = ____

# 5. Safely get "price". If it's missing, use 0
price = book.get(____)

# 6. Build a list of all the keys by looping over book.items()
keys = []
for key, value in book.____:
    keys.append(key)

# 7. Count how many times each word appears
words = ["sun", "rain", "sun", "snow", "sun", "rain"]
counts = {}
for w in words:
    counts[w] = counts.get(w, ____) + 1

# 8. Phone book: look up Bob's number
phone_book = {"Alice": "555-1234", "Bob": "555-9876"}
bobs_number = ____

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
check("author", author, "Roald Dahl")
check("pages", book["pages"], 250)
check("year", book.get("year"), 1988)
check("has_title", has_title, True)
check("price", price, 0)
check("keys", keys, ["title", "author", "pages", "year"])
check("counts", counts, {"sun": 3, "rain": 2, "snow": 1})
check("bobs_number", bobs_number, "555-9876")
if _failed == 0:
    print("All checks passed!")
