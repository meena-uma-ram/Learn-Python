# Lesson 12: Strings (exercise)
# Replace every ____ with the right code, then run:  python3 exercises/12_strings.py

word = "Programming"

# 1. Length of word
length = ____

# 2. First letter and last letter
first_letter = word[____]
last_letter = word[____]

# 3. The first 3 letters ("Pro") using a slice
start = word[____]

# 4. Uppercase and lowercase versions
upper = word.____
lower = word.____

# 5. Remove the spaces around the text
messy = "   tidy me   "
clean = messy.____

# 6. Split a sentence into a list of words
sentence = "I love learning Python"
words = sentence.____

# 7. Join a list of words with "-" between them
joined = ____.join(["a", "b", "c"])

# 8. Replace "cats" with "dogs"
text = "I like cats"
new_text = text.replace(____)

# 9. Use an f-string to build "Sam scored 42 points"
player = "Sam"
points = 42
summary = f"____ scored ____ points"

# 10. Count the vowels in word using a loop
vowels = 0
for ch in word.lower():
    if ____:
        vowels += 1

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
check("length", length, 11)
check("first_letter", first_letter, "P")
check("last_letter", last_letter, "g")
check("start", start, "Pro")
check("upper", upper, "PROGRAMMING")
check("lower", lower, "programming")
check("clean", clean, "tidy me")
check("words", words, ["I", "love", "learning", "Python"])
check("joined", joined, "a-b-c")
check("new_text", new_text, "I like dogs")
check("summary", summary, "Sam scored 42 points")
check("vowels", vowels, 3)
if _failed == 0:
    print("All checks passed!")
