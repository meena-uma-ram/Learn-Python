# Lesson 14: Final project, a grade calculator (exercise)
# Replace every ____ with the right code, then run:  python3 exercises/14_project.py
# This uses everything: variables, lists, dictionaries, loops, if/else and functions.

students = {
    "Ana": [92, 88, 95],
    "Ben": [75, 80, 68],
    "Cai": [55, 62, 58],
    "Dee": [85, 90, 79],
}


# 1. Return the average of a list of marks
def average(marks):
    return ____ / ____


# 2. Turn an average into a letter: 90+ A, 80+ B, 70+ C, 60+ D, else F
def letter_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif ____:
        return "C"
    elif avg >= 60:
        return ____
    else:
        return "F"


# 3. Build a dictionary of name → letter grade by looping over students
report = {}
for name, marks in students.____:
    avg = average(marks)
    report[name] = ____

# 4. Find the student with the highest average
best_name = ""
best_avg = 0
for name, marks in students.items():
    avg = average(marks)
    if ____:
        best_avg = avg
        best_name = ____

# 5. Make a list of students who passed (grade is not "F")
passed = []
for name, grade in report.items():
    if ____:
        passed.append(name)

# 6. Print the report nicely
for name, marks in students.items():
    print(f"{name:<5} average {average(marks):5.1f}  grade {report[name]}")
print(f"Top student: {best_name}")

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
check("average([90, 80])", average([90, 80]), 85)
check("letter_grade(91)", letter_grade(91), "A")
check("letter_grade(72)", letter_grade(72), "C")
check("letter_grade(65)", letter_grade(65), "D")
check("report", report, {"Ana": "A", "Ben": "C", "Cai": "F", "Dee": "B"})
check("best_name", best_name, "Ana")
check("passed", passed, ["Ana", "Ben", "Dee"])
if _failed == 0:
    print("All checks passed!")
