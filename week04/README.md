[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/nUQxAZ4A)
# Lab 3: Functions and Web Data Processing

## Overview
Master function design while processing realistic web data! You'll write 15 functions that handle URLs, JSON responses, and messy real-world data formats - the core skills for Project 2's API monitoring.

**Time Limit:** 100 minutes  
**Total Points:** 44 (from autograding)

## Instructions

### 1. Accept the Assignment
Click the assignment link provided by your instructor to create your personal repository.

### 2. Clone Your Repository
```bash
git clone <your-repository-url>
cd <repository-name>
```

### 3. Complete the Exercises
Open `lab4_exercises.py` and complete each function. **The template has intentional errors** - don't just copy-paste!

### 4. Test Your Code Locally
```bash
python test_lab4.py
```

This will run all tests and show you which exercises pass/fail.

### 5. Submit Your Work
```bash
git add lab4_exercises.py
git commit -m "Complete Lab 3 exercises"
git push
```

### 6. Check Autograding Results
- Go to your repository on GitHub
- Click the "Actions" tab
- View the latest workflow run to see your score
- Green checkmark = All tests passed
- Red X = Some tests failed (click to see details)

## Exercises

| Exercise | Topic | Points | Difficulty |
|----------|-------|--------|------------|
| **Section A: String Processing** | | **14** | **Easy** |
| 1 | Extract Domain from URL | 2 | Easy |
| 2 | Parse Query Parameters | 2 | Easy |
| 3 | Count Keyword Occurrences | 2 | Easy |
| 4 | Clean Response Data | 2 | Easy |
| 5 | Extract Status Code | 2 | Easy |
| 6 | Format Timestamp | 2 | Easy |
| 7 | Simple Email Validation | 2 | Easy |
| **Section B: JSON Processing** | | **15** | **Medium** |
| 8 | Parse Simple JSON | 3 | Medium |
| 9 | Parse Nested JSON | 3 | Medium |
| 10 | Count JSON Array Items | 3 | Medium |
| 11 | Extract All Values for Key | 3 | Medium |
| 12 | Calculate Average from JSON | 3 | Medium |
| **Section C: Data Cleaning** | | **15** | **Hard** |
| 13 | Fix Broken JSON | 5 | Hard |
| 14 | Parse CSV-Like String | 5 | Hard |
| 15 | Process Mixed API Response | 5 | Hard |
| **TOTAL** | | **44** | |

## IMPORTANT: Template Has Intentional Errors!

The template code **will NOT run as-is**. This is intentional to encourage understanding:

```python
# TEMPLATE (BROKEN):
def extract_domain(url):
    wrong_variable = ""  # Wrong name!
    return domain  # Error - 'domain' not defined

# YOU MUST FIX:
def extract_domain(url):
    domain = url.split("//")[1].split("/")[0]
    domain = domain.replace("www.", "")
    return domain  # Now it works!
```

**Don't copy-paste blindly - understand and fix the template!**

## Tips by Section

### Section A: String Processing (Easy)

These build your foundation for web data handling:

**Exercise 1: Extract Domain**
```python
# Input: "https://www.example.com/page"
# Steps:
# 1. Remove "https://" or "http://"
# 2. Remove everything after first "/"
# 3. Remove "www." prefix
# Output: "example.com"

url = "https://www.example.com/page"
after_protocol = url.split("//")[1]  # "www.example.com/page"
before_path = after_protocol.split("/")[0]  # "www.example.com"
domain = before_path.replace("www.", "")  # "example.com"
```

**Exercise 2: Parse Query Parameters**
```python
# Input: "https://api.com/search?q=python&page=2"
# Steps:
# 1. Split by "?" to get query string
# 2. Split query by "&" to get pairs
# 3. Split each pair by "=" to get key and value
# Output: {"q": "python", "page": "2"}

url = "https://api.com/search?q=python&page=2"
if "?" in url:
    query_string = url.split("?")[1]  # "q=python&page=2"
    pairs = query_string.split("&")   # ["q=python", "page=2"]
    for pair in pairs:
        key, value = pair.split("=")  # "q", "python"
        params[key] = value
```

**Exercise 3: Count Keyword**
```python
# Case-insensitive counting
text = "Python is great. Python is powerful."
keyword = "python"

# Method 1: Using .lower() and .count()
count = text.lower().count(keyword.lower())

# Method 2: Using .split() and loop
words = text.lower().split()
count = 0
for word in words:
    if keyword.lower() in word:  # Contains keyword
        count += 1
```

**Exercise 4: Clean Whitespace**
```python
# Remove leading/trailing AND collapse internal spaces
text = "  Hello    World  "

# Step 1: Strip edges
text = text.strip()  # "Hello    World"

# Step 2: Collapse internal spaces
words = text.split()  # ["Hello", "World"]
result = " ".join(words)  # "Hello World"
```

**Exercise 7: Email Validation**
```python
# Check for @ and . in correct positions
def is_valid_email(email):
    # Must have @
    if "@" not in email:
        return False
    
    # Must have . after @
    at_position = email.index("@")
    after_at = email[at_position:]
    if "." not in after_at:
        return False
    
    # Must be reasonable length
    if len(email) < 5:
        return False
    
    return True
```

### Section B: JSON Processing (Medium)

Learn to work with structured data from APIs:

**Exercise 8: Parse Simple JSON**
```python
import json

json_string = '{"name": "Alice", "age": 25}'

# Parse JSON
data = json.loads(json_string)  # Returns dict

# Safely get value (use .get() to return None if missing)
value = data.get("name")  # "Alice"
missing = data.get("missing_key")  # None (not error!)
```

**Exercise 9: Nested JSON**
```python
json_string = '{"user": {"name": "Bob", "age": 30}}'
data = json.loads(json_string)

# Unsafe way (crashes if keys missing):
name = data["user"]["name"]  # Error if "user" or "name" missing

# Safe way:
if "user" in data:
    if "name" in data["user"]:
        name = data["user"]["name"]
    else:
        name = None
else:
    name = None

# Or using .get() chaining:
user = data.get("user", {})
name = user.get("name")
```

**Exercise 11: Extract All Values**
```python
# From array of objects, collect all values for one key
json_string = '[{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]'
data = json.loads(json_string)

# Extract all names
names = []
for item in data:
    if "name" in item:  # Check key exists
        names.append(item["name"])
# Result: ["Alice", "Bob"]
```

**Exercise 12: Calculate Average**
```python
json_string = '[{"score": 85}, {"score": 90}, {"score": 78}]'
data = json.loads(json_string)

total = 0
count = 0
for item in data:
    if "score" in item:
        total += item["score"]
        count += 1

average = total / count if count > 0 else 0.0
```

### Section C: Data Cleaning (Hard)

Handle messy real-world data:

**Exercise 13: Fix Broken JSON**
```python
# Common issues:
# 1. Single quotes instead of double quotes
# 2. Trailing commas before closing braces

broken = "{'name': 'Alice', 'age': 25,}"

# Fix quotes
fixed = broken.replace("'", '"')
# Now: {"name": "Alice", "age": 25,}

# Fix trailing commas
fixed = fixed.replace(",}", "}")
fixed = fixed.replace(",]", "]")
# Now: {"name": "Alice", "age": 25}

# Parse it
data = json.loads(fixed)
return data  # Return the dict, not string!
```

**Exercise 14: Parse CSV**
```python
csv_string = "name,age,city\nAlice,25,NYC\nBob,30,LA"

# Split into lines
lines = csv_string.split('\n')
# ["name,age,city", "Alice,25,NYC", "Bob,30,LA"]

# First line is headers
headers = lines[0].split(',')  # ["name", "age", "city"]

# Process data rows
results = []
for i in range(1, len(lines)):  # Skip header
    values = lines[i].split(',')  # ["Alice", "25", "NYC"]
    
    # Create dict mapping headers to values
    row = {}
    for j in range(len(headers)):
        row[headers[j]] = values[j]
    
    results.append(row)

# Result: [{"name": "Alice", "age": "25", "city": "NYC"}, ...]
```

**Exercise 15: Mixed API Response**
```python
response = 'STATUS: 200 | DATA: {"success": true} | COUNT: 5'

# Split by delimiter
parts = response.split(" | ")
# ["STATUS: 200", "DATA: {...}", "COUNT: 5"]

result = {}

# Process each part
for part in parts:
    if part.startswith("STATUS:"):
        code = part.replace("STATUS: ", "")
        result["status"] = int(code)
    
    elif part.startswith("DATA:"):
        json_str = part.replace("DATA: ", "")
        result["data"] = json.loads(json_str)
    
    elif part.startswith("COUNT:"):
        count = part.replace("COUNT: ", "")
        result["count"] = int(count)

return result
```

## Common Pitfalls

### String Operations
```python
# WRONG - Not handling all cases
def extract_domain(url):
    return url.split("//")[1]  # Still has path!

# CORRECT - Complete processing
def extract_domain(url):
    after_protocol = url.split("//")[1]
    before_path = after_protocol.split("/")[0]
    clean = before_path.replace("www.", "")
    return clean
```

### JSON Parsing
```python
# WRONG - Crashes if key missing
def get_value(json_str, key):
    data = json.loads(json_str)
    return data[key]  # KeyError if key doesn't exist!

# CORRECT - Safe access
def get_value(json_str, key):
    data = json.loads(json_str)
    return data.get(key)  # Returns None if missing
```

### Type Conversion
```python
# WRONG - Returning wrong type
def extract_status_code(header):
    parts = header.split()
    return parts[1]  # Returns "200" (string!)

# CORRECT - Convert to int
def extract_status_code(header):
    parts = header.split()
    return int(parts[1])  # Returns 200 (int!)
```

### Return Statements
```python
# WRONG - Missing return
def process_data(data):
    result = do_something(data)
    # Forgot return! Function returns None

# CORRECT - Always return
def process_data(data):
    result = do_something(data)
    return result  # Returns the value
```

## Debugging Tips

**1. Print intermediate values:**
```python
def extract_domain(url):
    print(f"Input: {url}")
    
    after_protocol = url.split("//")[1]
    print(f"After protocol: {after_protocol}")
    
    domain = after_protocol.split("/")[0]
    print(f"Final domain: {domain}")
    
    return domain
```

**2. Test with simple cases first:**
```python
# Before running tests, try manually:
result = extract_domain("https://example.com/page")
print(result)  # Should be "example.com"
```

**3. Check function signatures:**
- Are you accepting the right parameters?
- Are you returning the right type?
- Are you handling all cases?

**4. Read error messages carefully:**
```python
# NameError: name 'domain' is not defined
# -> You're returning a variable you never created

# KeyError: 'missing_key'
# -> Use .get() instead of [] for dictionary access

# TypeError: 'NoneType' object is not subscriptable
# -> Check if value exists before using it
```

## Project 2 Connection

These skills directly enable Project 2 (API Monitoring):

**Lab 3 Skill** -> **Project 2 Application**
- **Extract domain** -> Validate API endpoints
- **Parse query params** -> Build dynamic API requests
- **Parse JSON** -> Process API responses
- **Data cleaning** -> Handle inconsistent data
- **Extract values** -> Track specific metrics
- **Calculate averages** -> Detect trends

Example Project 2 workflow:
```python
# 1. Make API request (you'll learn requests library)
response = requests.get("https://api.weather.com/current?city=Istanbul")

# 2. Parse JSON response (Lab 3 Exercise 8)
data = json.loads(response.text)
temperature = data.get("temperature")

# 3. Compare to previous state (Lab 3 Exercise 12)
if temperature > previous_temp + 5:
    send_notification("Temperature spike detected!")

# 4. Store current state for next check
save_state({"temperature": temperature, "timestamp": now()})
```

## Key Concepts

### Functions
```python
# Function with parameters and return value
def function_name(param1, param2):
    """Docstring explaining what function does"""
    result = param1 + param2
    return result  # Send value back

# Calling the function
answer = function_name(5, 10)  # answer = 15
```

### String Methods
```python
text = "  Hello World  "

text.strip()           # Remove edges: "Hello World"
text.split()           # Split by whitespace: ["Hello", "World"]
text.replace("o", "0") # Replace: "Hell0 W0rld"
text.lower()           # Lowercase: "hello world"
text.upper()           # Uppercase: "HELLO WORLD"
"x" in text            # Contains: False
text.startswith("H")   # Starts with: True
text.endswith("d")     # Ends with: True
text.index("W")        # Find position: 8
```

### JSON Operations
```python
import json

# Parse JSON string to Python dict
json_string = '{"key": "value"}'
data = json.loads(json_string)

# Convert Python dict to JSON string
python_dict = {"key": "value"}
json_string = json.dumps(python_dict)

# Safe access
value = data.get("key", "default")  # Returns "default" if key missing
```

### List Comprehensions (Optional)
```python
# Extract names from list of dicts
users = [{"name": "Alice"}, {"name": "Bob"}]

# Traditional way:
names = []
for user in users:
    names.append(user["name"])

# List comprehension (more concise):
names = [user["name"] for user in users]
```

## Resources

- [Python String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Python JSON Module](https://docs.python.org/3/library/json.html)
- [Working with JSON in Python](https://realpython.com/python-json/)
- [String Formatting](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals)

## Grading

Your grade is calculated based on passed tests:
- **Section A** (Easy): 14 points - String processing basics
- **Section B** (Medium): 15 points - JSON data handling
- **Section C** (Hard): 15 points - Complex data cleaning
- **Total**: 44 points

Each exercise has multiple test cases - partial credit for partially correct solutions!

## Strategy for Success

### 1. Start with Easy Exercises (Section A)
- Build confidence with string operations
- Test each function immediately after writing
- Don't move on until tests pass

### 2. Progress to Medium (Section B)
- Understand JSON structure first
- Use print() to see what json.loads() returns
- Always use .get() for safe access

### 3. Tackle Hard Last (Section C)
- Break complex problems into steps
- Test each step independently
- Don't try to do everything at once

### 4. Time Management
- Easy exercises: 3-5 minutes each (~35 min total)
- Medium exercises: 5-8 minutes each (~35 min total)
- Hard exercises: 8-10 minutes each (~30 min total)
- **Total: 100 minutes**

## Need Help?

- **Stuck on easy exercises?** Review Week 2 string methods
- **Struggling with JSON?** Check the examples in this README
- **Hard exercises too hard?** Break them into smaller steps
- **Tests failing?** Read the error messages - they tell you exactly what's wrong
- **Still stuck?** Ask your TA - that's what they're here for!

## Final Reminders

- **Fix the template** - It has intentional errors
- **Test frequently** - After every function
- **Read docstrings** - They have examples
- **Return, don't print** - Functions should return values
- **Handle edge cases** - What if key doesn't exist?
- **Use .get()** - Safer than [] for dictionaries

Good luck! These skills will power your API monitoring in Project 2!