[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/FffQv2vy)
# Lab 3: Functions, Dictionaries, and Data Structures

## Overview
Master Python functions, dictionaries, and data structures! This lab introduces writing reusable code, working with key-value data, and building complete programs from scratch.

**Time Limit:** 100 minutes  
**Total Points:** 35 (from autograding)

## 📋 Instructions

### 1. Accept the Assignment
Click the assignment link provided by your instructor to create your personal repository.

### 2. Clone Your Repository
```bash
git clone <your-repository-url>
cd <repository-name>
```

### 3. Complete the Exercises

**Section A (Exercises 1-3):** Complete the function bodies where skeleton code is provided with detailed TODO comments.

**Section B & C (Exercises 4-12):** Write entire functions from scratch based on descriptions. Function names MUST match exactly!

### 4. Test Your Code Locally
```bash
python test_lab3.py
```

This will run all tests and show you which exercises pass/fail.

### 5. Submit Your Work
```bash
git add lab3_exercises.py
git commit -m "Complete Lab 3 exercises"
git push
```

### 6. Check Autograding Results
- Go to your repository on GitHub
- Click the "Actions" tab
- View the latest workflow run to see your score
- Green checkmark ✅ = All tests passed
- Red X ❌ = Some tests failed (click to see details)

## 📚 Exercises

| Exercise | Topic | Points | Type |
|----------|-------|--------|------|
| **Section A: Functions with Guidance** | | **6** | **Skeleton** |
| 1 | Temperature Converter | 2 | Skeleton |
| 2 | Dictionary Lookup | 2 | Skeleton |
| 3 | Format Person Info | 2 | Skeleton |
| **Section B: Write Complete Functions** | | **16** | **From Scratch** |
| 4 | Calculate Average | 2 | From Scratch |
| 5 | Clean Filename | 2 | From Scratch |
| 6 | Count File Extensions | 3 | From Scratch |
| 7 | Filter Passing Students | 3 | From Scratch |
| 8 | Analyze Numbers (Tuple) | 3 | From Scratch |
| 9 | Read Numbers from File | 3 | From Scratch |
| **Section C: Advanced Integration** | | **13** | **From Scratch** |
| 10 | Shopping Cart Total | 3 | From Scratch |
| 11 | Generate Grade Report | 5 | From Scratch |
| 12 | Analyze Log File | 5 | From Scratch |
| **TOTAL** | | **35** | |

## 🔑 Key Concepts

### Functions
Functions are reusable blocks of code that perform specific tasks.

```python
# Basic function
def greet(name):
    return f"Hello, {name}!"

# Function with default parameter
def calculate_total(price, tax_rate=0.08):
    return price * (1 + tax_rate)

# Function returning multiple values (tuple)
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

# Using the function
minimum, maximum, average = get_stats([10, 20, 30])
```

**Why Functions?**
- Write once, use many times
- Easier to test and debug
- Make code readable and organized
- Enable code reuse

### Dictionaries
Dictionaries store key-value pairs for fast lookups.

```python
# Creating dictionaries
grades = {"Alice": 85, "Bob": 92, "Charlie": 78}

# Accessing values
alice_grade = grades["Alice"]  # 85
dave_grade = grades.get("Dave", 0)  # 0 (default if not found)

# Adding/updating
grades["David"] = 88  # Add new
grades["Alice"] = 90  # Update existing

# Checking membership
if "Alice" in grades:
    print(f"Alice's grade: {grades['Alice']}")

# Looping through dictionary
for name, grade in grades.items():
    print(f"{name}: {grade}")
```

### Tuples
Tuples are immutable sequences - perfect for returning multiple values.

```python
# Creating tuples
point = (10, 20)
rgb = (255, 128, 0)

# Returning multiple values
def analyze(numbers):
    return min(numbers), max(numbers), sum(numbers)

# Unpacking
minimum, maximum, total = analyze([1, 2, 3, 4, 5])
```

### F-Strings
F-strings provide clean string formatting.

```python
name = "Alice"
age = 25
city = "Boston"

# F-string formatting
info = f"Name: {name}, Age: {age}, City: {city}"

# Expressions inside f-strings
print(f"Next year: {age + 1}")
print(f"Uppercase: {name.upper()}")

# Number formatting
price = 19.99
print(f"Price: ${price:.2f}")  # Price: $19.99
```

## 💡 Tips

### General Tips
- **Test frequently**: Run tests after completing each exercise
- **Read docstrings carefully**: They contain exact requirements and examples
- **Function names must match exactly**: Typos will cause all tests to fail
- **Use print() for debugging**: Add print statements to see what your code is doing
- **Start with Section A**: Build confidence with guided exercises first

### Writing Functions from Scratch
```python
# 1. Read the description carefully
# 2. Look at the function signature and return type
# 3. Study the example
# 4. Write the function definition
# 5. Implement the logic
# 6. Test with the example

# Example: Write calculate_average(numbers)
def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count
```

### Working with Dictionaries
```python
# Building a dictionary from scratch
def count_items(items):
    counts = {}  # Start empty
    for item in items:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    # Or use .get() with default:
    # counts[item] = counts.get(item, 0) + 1
    return counts
```

### File Operations
```python
# Reading numbers from file
def read_numbers(filename):
    numbers = []
    with open(filename) as f:
        for line in f:
            number = int(line.strip())  # Remove \n, convert to int
            numbers.append(number)
    return numbers
```

## 🎯 Common Pitfalls

### Function Definition Errors
```python
# ❌ Wrong - Function name doesn't match
def calculateAverage(numbers):  # camelCase
    return sum(numbers) / len(numbers)

# ✅ Correct - Exact name from instructions
def calculate_average(numbers):  # snake_case
    return sum(numbers) / len(numbers)
```

### Dictionary Access Errors
```python
# ❌ Wrong - KeyError if key doesn't exist
grade = grades["Nonexistent"]

# ✅ Correct - Use .get() with default
grade = grades.get("Nonexistent", 0)
```

### Return vs Print
```python
# ❌ Wrong - Printing instead of returning
def calculate_average(numbers):
    avg = sum(numbers) / len(numbers)
    print(avg)  # Just prints, doesn't return!

# ✅ Correct - Return the value
def calculate_average(numbers):
    return sum(numbers) / len(numbers)
```

### File Reading Errors
```python
# ❌ Wrong - Forgetting to strip newlines
with open('file.txt') as f:
    for line in f:
        number = int(line)  # Error: "42\n" not valid int

# ✅ Correct - Strip first
with open('file.txt') as f:
    for line in f:
        number = int(line.strip())  # Remove \n first
```

### Tuple Unpacking
```python
# ❌ Wrong - Not unpacking correctly
result = analyze_numbers([1, 2, 3])
print(result[0])  # Works but awkward

# ✅ Correct - Unpack into variables
min_val, max_val, avg = analyze_numbers([1, 2, 3])
print(min_val)  # Clear and readable
```

## 🔍 Debugging Tips

### 1. Print Intermediate Values
```python
def calculate_cart_total(cart):
    total = 0
    for item, (price, quantity) in cart.items():
        cost = price * quantity
        print(f"{item}: ${price} × {quantity} = ${cost}")  # Debug line
        total += cost
    return total
```

### 2. Test with Simple Examples First
```python
# Before testing complex cases
result = calculate_average([10, 20, 30])
print(result)  # Should be 20.0

# Then test edge cases
result = calculate_average([5])
print(result)  # Should be 5.0
```

### 3. Check Return Types
```python
def analyze_numbers(numbers):
    result = min(numbers), max(numbers), sum(numbers) / len(numbers)
    print(type(result))  # Should be <class 'tuple'>
    return result
```

### 4. Verify Dictionary Operations
```python
def count_extensions(filenames):
    counts = {}
    for filename in filenames:
        ext = filename.split('.')[-1]
        print(f"File: {filename}, Extension: {ext}")  # Debug
        counts[ext] = counts.get(ext, 0) + 1
    print(f"Final counts: {counts}")  # Debug
    return counts
```

## 📖 Week 3 Concepts Review

### Functions
```python
# Definition
def function_name(parameter1, parameter2):
    # Do something
    return result

# Calling
output = function_name(arg1, arg2)

# Default parameters
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Alice")              # "Hello, Alice!"
greet("Bob", "Hi")          # "Hi, Bob!"
```

### Dictionaries
```python
# Creation
person = {"name": "Alice", "age": 25, "city": "Boston"}

# Access
name = person["name"]               # Direct access (error if missing)
age = person.get("age", 0)          # Safe access with default

# Modification
person["age"] = 26                  # Update
person["email"] = "a@b.com"         # Add new

# Iteration
for key, value in person.items():
    print(f"{key}: {value}")
```

### String Operations
```python
# Cleaning
text = "  Hello  ".strip()          # "Hello"
text = "HELLO".lower()               # "hello"

# Formatting
name = "Alice"
message = f"Hello, {name}!"          # f-strings

# Splitting
parts = "file.txt".split('.')        # ["file", "txt"]
extension = parts[-1]                # "txt"
```

### File Operations
```python
# Reading
with open('file.txt') as f:
    content = f.read()               # Entire file
    
with open('file.txt') as f:
    for line in f:                   # Line by line
        clean = line.strip()

# Writing
with open('output.txt', 'w') as f:
    f.write("Hello\n")
```

## 🚀 Project 1 Connection

Lab 3 skills directly enable Project 1:

**Functions:**
```python
def get_file_extension(filename):
    return filename.split('.')[-1].lower()

def categorize_file(filename):
    ext = get_file_extension(filename)
    categories = {
        "jpg": "Images",
        "pdf": "Documents",
        "mp3": "Music"
    }
    return categories.get(ext, "Other")
```

**Dictionaries for Categories:**
```python
file_counts = {}
for file in files:
    category = categorize_file(file)
    file_counts[category] = file_counts.get(category, 0) + 1
```

**Putting It Together:**
```python
def organize_files(source_dir):
    files = get_all_files(source_dir)
    for file in files:
        category = categorize_file(file)
        move_to_category(file, category)
    generate_report(file_counts)
```

## 🧪 Test Data Files

The autograder automatically creates these files for testing:

**numbers.txt** - Contains:
```
10
20
30
40
50
```

**log.txt** - Contains:
```
ERROR: Connection failed
INFO: Server started
ERROR: Timeout occurred
WARNING: Low memory
INFO: Request processed
ERROR: Database error
```

Do not create or modify these files manually - they are generated automatically during testing!

## 📝 How Autograding Works

Every time you push code to GitHub:
1. GitHub Actions automatically runs your tests
2. Test data files are created automatically
3. Each exercise is graded separately
4. You receive immediate feedback
5. You can push multiple times to improve your score

## 📚 Resources

### Python Documentation
- [Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [String Formatting](https://docs.python.org/3/tutorial/inputoutput.html#fancier-output-formatting)
- [File I/O](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)

### Tutorials
- [Real Python - Functions](https://realpython.com/defining-your-own-python-function/)
- [Real Python - Dictionaries](https://realpython.com/python-dicts/)
- [F-strings Guide](https://realpython.com/python-f-strings/)

### Week 3 Lecture Materials
Review your Week 3 lecture slides for:
- Function design patterns
- Dictionary operations
- String methods
- F-string formatting

## ⚙️ Grading

Your grade is automatically calculated based on passed tests:
- Each exercise has multiple test cases
- Partial credit is awarded for partially correct solutions
- Final score = (Passed Tests / Total Tests) × 100

**Score Breakdown:**
- Section A (Skeleton): 6 points
- Section B (Complete): 16 points
- Section C (Advanced): 13 points
- **Total: 35 points**

## ❓ Need Help?

1. **Check the error messages**: GitHub Actions log shows exactly which tests fail
2. **Review the docstrings**: Function descriptions contain all requirements
3. **Test locally first**: Run `python test_lab3.py` before pushing
4. **Ask your TA**: During lab hours for guidance
5. **Review lecture materials**: Week 3 slides cover all concepts

## 🎓 Learning Objectives

By completing this lab, you will:
- ✅ Write reusable functions with clear purposes
- ✅ Use dictionaries for efficient data storage and lookup
- ✅ Return multiple values using tuples
- ✅ Format strings professionally with f-strings
- ✅ Read and process data from files
- ✅ Combine concepts into complete solutions
- ✅ Write functions from scratch based on specifications

## 🏆 Success Checklist

Before submitting, verify:
- [ ] All function names match exactly
- [ ] Section A functions have completed bodies
- [ ] Section B & C have complete function definitions
- [ ] All functions return values (not just print)
- [ ] File operations use `with open()` pattern
- [ ] Dictionary lookups use `.get()` for safety
- [ ] Local tests pass: `python test_lab3.py`
- [ ] Code is pushed to GitHub
- [ ] GitHub Actions shows green checkmark

Good luck! 🚀

---

**Remember**: Functions are the building blocks of all software. Master them now, and you'll be able to build anything! 💪