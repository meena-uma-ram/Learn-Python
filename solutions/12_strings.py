# Lesson 12: Strings (solution)
# Run:  python3 solutions/12_strings.py

word = "Programming"

# 1. Length of word
length = len(word)

# 2. First letter and last letter
first_letter = word[0]
last_letter = word[-1]

# 3. The first 3 letters ("Pro") using a slice
start = word[0:3]

# 4. Uppercase and lowercase versions
upper = word.upper()
lower = word.lower()

# 5. Remove the spaces around the text
messy = "   tidy me   "
clean = messy.strip()

# 6. Split a sentence into a list of words
sentence = "I love learning Python"
words = sentence.split()

# 7. Join a list of words with "-" between them
joined = "-".join(["a", "b", "c"])

# 8. Replace "cats" with "dogs"
text = "I like cats"
new_text = text.replace("cats", "dogs")

# 9. Use an f-string to build "Sam scored 42 points"
player = "Sam"
points = 42
summary = f"{player} scored {points} points"

# 10. Count the vowels in word using a loop
vowels = 0
for ch in word.lower():
    if ch in "aeiou":
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
