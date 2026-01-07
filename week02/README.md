[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/c3OTvfEe)
# Lab 2: Lists, Loops, and File Operations

## Overview
Complete 16 programming exercises covering lists, loops, and file operations - the building blocks of automation!

**Time Limit:** 100 minutes  
**Total Points:** 80 (from autograding)

## 📋 Instructions

### 1. Accept the Assignment
Click the assignment link provided by your instructor to create your personal repository.

### 2. Clone Your Repository
```bash
git clone <your-repository-url>
cd <repository-name>
```

### 3. Complete the Exercises
Open `lab2_exercises.py` and complete each function. Do not change function names or parameters.

### 4. Test Your Code Locally
```bash
python test_lab2.py
```

This will run all tests and show you which exercises pass/fail.

### 5. Submit Your Work
```bash
git add lab2_exercises.py
git commit -m "Complete Lab 2 exercises"
git push
```

### 6. Check Autograding Results
- Go to your repository on GitHub
- Click the "Actions" tab
- View the latest workflow run to see your score
- Green checkmark ✅ = All tests passed
- Red X ❌ = Some tests failed (click to see details)

## 📚 Exercises

| Exercise | Topic | Points |
|----------|-------|--------|
| **Section A: Lists Basics** | | **25** |
| 1 | Create a Shopping List | 4 |
| 2 | Access List Elements | 4 |
| 3 | List Length and Membership | 5 |
| 4 | Append Items | 6 |
| 5 | Insert at Position | 6 |
| **Section B: Loops with Lists** | | **25** |
| 6 | Collect All Items | 4 |
| 7 | Sum All Numbers | 5 |
| 8 | Count Specific Value | 5 |
| 9 | Filter by Threshold | 6 |
| 10 | Generate Number List | 5 |
| **Section C: File Operations** | | **20** |
| 11 | Read Entire File | 4 |
| 12 | Count Lines | 5 |
| 13 | Parse Numbers from File | 5 |
| 14 | Write List to File | 6 |
| **Section D: Integration** | | **10** |
| 15 | Filter File Numbers | 5 |
| 16 | Count Words Starting With Letter | 5 |
| **TOTAL** | | **80** |

## 📁 Test Files

The autograder automatically creates these files for testing:

- **numbers.txt** - Contains numbers: 42, 17, 93, 28, 55, 8, 76, 61, 34, 89
- **words.txt** - Contains words: apple, Apricot, banana, cherry, Avocado, date
- **shopping.txt** - Contains items: milk, eggs, bread, cheese, apples

Do not create or modify these files manually - they are generated automatically!

## 🔍 How Autograding Works

Every time you push code to GitHub:
1. GitHub Actions automatically runs your tests
2. Test data files are created automatically
3. Each exercise is graded separately
4. You receive immediate feedback
5. You can push multiple times to improve your score

## 💡 Tips

- **Test frequently**: Run `python test_lab2.py` after completing each exercise
- **Start with Section A**: Lists basics are foundational
- **Use print() for debugging**: Add print statements to see what your code is doing
- **Read error messages carefully**: They tell you exactly what's wrong
- **Remember zero-based indexing**: First item is at index 0, not 1!
- **Use .strip()**: Remove whitespace/newlines when reading files line by line
- **Ask for help**: If stuck for more than 5 minutes, ask your TA

## 🎯 Common Pitfalls

### Lists
```python
# ❌ Wrong - IndexError
my_list = ['a', 'b', 'c']
print(my_list[3])  # Only indices 0, 1, 2 exist!

# ✅ Correct
print(my_list[2])   # Gets 'c'
print(my_list[-1])  # Gets last item 'c'
```

### Loops
```python
# ❌ Wrong - Not using the loop variable
numbers = [1, 2, 3]
for num in numbers:
    total = total + numbers[0]  # Always adds first item!

# ✅ Correct
total = 0
for num in numbers:
    total = total + num  # Adds current item
```

### Files
```python
# ❌ Wrong - Forgetting to strip newlines
with open('file.txt') as f:
    for line in f:
        numbers.append(int(line))  # Error: "42\n" not a valid int

# ✅ Correct
with open('file.txt') as f:
    for line in f:
        numbers.append(int(line.strip()))  # Remove \n first
```

## 🛠️ Debugging Tips

If tests are failing:

1. **Print intermediate values**
```python
def exercise7(numbers):
    total = 0
    for num in numbers:
        print(f"Adding {num}, total now: {total}")  # Debug line
        total = total + num
    return total
```

2. **Test with simple examples first**
```python
# Test your function manually
result = exercise7([1, 2, 3])
print(result)  # Should be 6
```

3. **Check return types**
- Are you returning a list when you should return an int?
- Are you returning None (forgetting return statement)?
- Are you printing instead of returning?

4. **Read the docstring examples**
- Every function has an example showing expected behavior
- Test your function with the exact example given

## 📖 Key Concepts Review

### Lists
```python
# Creating lists
fruits = ['apple', 'banana', 'cherry']

# Accessing elements (zero-based!)
first = fruits[0]      # 'apple'
last = fruits[-1]      # 'cherry'
third = fruits[2]      # 'cherry'

# Modifying lists
fruits.append('date')        # Add to end
fruits.insert(1, 'apricot')  # Insert at position 1
fruits.remove('banana')      # Remove by value

# Checking
length = len(fruits)         # Count items
exists = 'apple' in fruits   # True or False
```

### Loops
```python
# Loop through list
for item in my_list:
    print(item)

# Accumulator pattern (very common!)
total = 0
for number in numbers:
    total = total + number

# Building new lists
results = []
for item in items:
    if item > 10:
        results.append(item)

# Using range()
for i in range(5):           # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):        # 1, 2, 3, 4, 5
    print(i)
```

### File Operations
```python
# Reading entire file
with open('file.txt') as f:
    content = f.read()

# Reading line by line
with open('file.txt') as f:
    for line in f:
        print(line.strip())  # Remove \n

# Writing to file
with open('output.txt', 'w') as f:
    f.write('Hello\n')
    f.write('World\n')

# Parsing numbers from file
numbers = []
with open('numbers.txt') as f:
    for line in f:
        num = int(line.strip())
        numbers.append(num)
```

## 🚀 Project 1 Connection

These skills directly enable Project 1:

- **Lists** → Store all files in a directory
- **Loops** → Process each file automatically
- **Files** → Read/move/organize actual files
- **Filtering** → Categorize files by extension

Example Project 1 logic:
```python
# Get all files
files = os.listdir('folder')

# Filter image files
images = []
for file in files:
    if file.endswith('.jpg'):
        images.append(file)

# Move them to organized folders
for image in images:
    move_file(image, 'Images/')
```

## 📚 Resources

- [Python Lists Documentation](https://docs.python.org/3/tutorial/introduction.html#lists)
- [Python Loops Tutorial](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [Python File I/O](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [range() Function](https://docs.python.org/3/library/functions.html#func-range)

## ⚠️ Important Notes

- Do **NOT** modify `test_lab2.py` or the test files will not work
- Do **NOT** change function names or parameters in `lab2_exercises.py`
- Do **NOT** use `print()` statements inside functions (return values instead)
- Do **NOT** use built-in functions when exercise says not to (like `sum()` or `.count()`)
- Protected files (tests and workflows) cannot be modified

## 🎯 Grading

Your grade is automatically calculated based on passed tests:
- Each exercise has multiple test cases
- Partial credit is awarded for partially correct solutions
- Final score = (Passed Tests / Total Tests) × 100

## Need Help?

- Check the GitHub Actions log for detailed error messages
- Review the function docstrings for requirements and examples
- Ask your TA during lab hours
- Refer to course materials on the LMS
- Review the Week 2 lecture slides

Good luck! 🚀