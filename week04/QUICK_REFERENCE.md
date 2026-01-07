# Lab 4 Quick Reference Card
## Functions and Web Data Processing - Cheat Sheet

⚠️ **TEMPLATE HAS INTENTIONAL ERRORS - FIX THEM!**

---

## 🔧 String Methods Cheat Sheet

```python
text = "  Hello World  "

text.strip()              # "Hello World" - remove edges
text.split()              # ["Hello", "World"] - split by space
text.split("/")           # Split by custom delimiter
text.replace("o", "0")    # "Hell0 W0rld" - replace
text.lower()              # "  hello world  " - lowercase
text.upper()              # "  HELLO WORLD  " - uppercase
"World" in text           # True - contains check
text.startswith("  H")    # True - starts with
text.endswith("  ")       # True - ends with
text.index("W")           # 8 - find position
text[:5]                  # "  Hel" - slice first 5 chars
text[5:]                  # "lo World  " - slice from 5 onward
```

---

## 📦 JSON Operations

```python
import json  # At top of file!

# Parse JSON string → Python dict
json_string = '{"name": "Alice", "age": 25}'
data = json.loads(json_string)

# Safe access (returns None if missing)
name = data.get("name")           # "Alice"
missing = data.get("missing")     # None (no error!)

# Unsafe access (crashes if missing)
name = data["name"]               # "Alice"
missing = data["missing"]         # KeyError!

# Check if key exists
if "name" in data:
    print(data["name"])

# Nested JSON
user = data.get("user", {})       # Get nested dict
name = user.get("name")           # Safe nested access
```

---

## 🔍 Common Patterns

### URL Parsing
```python
url = "https://www.example.com/page?q=test"

# Remove protocol
url.split("//")[1]           # "www.example.com/page?q=test"

# Get domain only
url.split("//")[1].split("/")[0]  # "www.example.com"

# Remove www
domain.replace("www.", "")   # "example.com"

# Get query string
url.split("?")[1]            # "q=test"

# Parse query params
for pair in query.split("&"):
    key, value = pair.split("=")
```

### JSON Array Processing
```python
data = '[{"name": "Alice", "score": 85}, {"name": "Bob", "score": 90}]'
items = json.loads(data)

# Extract all names
names = []
for item in items:
    if "name" in item:
        names.append(item["name"])

# Calculate average
total = 0
count = 0
for item in items:
    if "score" in item:
        total += item["score"]
        count += 1
average = total / count if count > 0 else 0.0
```

### Cleaning Strings
```python
# Remove extra whitespace
text = "  too   many    spaces  "
cleaned = " ".join(text.split())  # "too many spaces"

# Fix broken JSON
broken = "{'name': 'Alice',}"
fixed = broken.replace("'", '"').replace(",}", "}")
data = json.loads(fixed)
```

---

## ⚡ Quick Debugging

```python
# Print intermediate values
def my_function(param):
    print(f"Input: {param}")
    step1 = do_something(param)
    print(f"After step1: {step1}")
    return step1

# Check types
result = my_function()
print(f"Type: {type(result)}")  # int? str? dict?

# Test manually before running tests
result = extract_domain("https://example.com")
print(result)  # Should be "example.com"
```

---

## ⚠️ Common Mistakes to Avoid

```python
# ❌ WRONG - Returning string instead of int
def get_code(header):
    return header.split()[1]  # "200" (string!)

# ✅ CORRECT
def get_code(header):
    return int(header.split()[1])  # 200 (int!)

# ❌ WRONG - Unsafe dictionary access
def get_value(json_str, key):
    data = json.loads(json_str)
    return data[key]  # KeyError if missing!

# ✅ CORRECT
def get_value(json_str, key):
    data = json.loads(json_str)
    return data.get(key)  # None if missing

# ❌ WRONG - Forgetting to return
def process_data(data):
    result = data * 2
    # Missing return!

# ✅ CORRECT
def process_data(data):
    result = data * 2
    return result

# ❌ WRONG - Division by zero
def average(numbers):
    return sum(numbers) / len(numbers)  # Error if empty!

# ✅ CORRECT
def average(numbers):
    return sum(numbers) / len(numbers) if len(numbers) > 0 else 0.0
```

---

## 📝 Exercise Hints

### Section A (Easy - String Processing)
1. **Domain**: Remove "https://", remove path, remove "www."
2. **Query**: Split by "?", then "&", then "="
3. **Count**: Use `.lower()` and `.count()`
4. **Clean**: `.strip()` + `.split()` + `.join()`
5. **Status**: `.split()` and `int()` conversion
6. **Timestamp**: Split by "T", slice time part [:5]
7. **Email**: Check for "@" and "." after "@"

### Section B (Medium - JSON)
8. **Simple JSON**: `json.loads()` + `.get()`
9. **Nested**: Check outer exists, then inner
10. **Count**: Check if list, return `len()`
11. **Extract**: Loop and collect values
12. **Average**: Sum values, divide by count (watch for zero!)

### Section C (Hard - Cleaning)
13. **Fix JSON**: Replace quotes and commas, then parse
14. **Parse CSV**: Split lines, first is headers, map to dicts
15. **Mixed**: Split by " | ", process each part differently

---

## 🎯 Testing Strategy

```bash
# Run all tests
python test_lab4.py

# Expected output shows pass/fail for each
# Score calculated at the end

# If test fails:
# 1. Read the error message carefully
# 2. Check what the test expected
# 3. Print your actual output
# 4. Fix and test again
```

---

## ⏱️ Time Management

- **0-20 min**: Complete Section A (exercises 1-7)
- **20-55 min**: Complete Section B (exercises 8-12)
- **55-90 min**: Complete Section C (exercises 13-15)
- **90-100 min**: Review, test, submit

**Behind schedule?** Get Section A working first!

---

## 🆘 When You're Stuck

1. **Read the docstring** - it has examples!
2. **Check the README** - detailed explanations
3. **Print debug values** - see what you actually have
4. **Test simple cases** - does `extract_domain("https://example.com")` work?
5. **Ask your TA** - that's what they're here for!

---

## 📋 Submission Checklist

- [ ] All functions return correct types (int vs str vs dict)
- [ ] No syntax errors (code runs)
- [ ] Tests pass locally (`python test_lab4.py`)
- [ ] Code pushed to GitHub
- [ ] GitHub Actions shows green checkmark ✅
- [ ] Check your score in Actions tab

---

## 💡 Pro Tips

- **Start with easy** - Build confidence with Section A
- **Test frequently** - After every function, run tests
- **Use .get()** - Safer than [] for dictionaries
- **Return, don't print** - Functions return values
- **Read errors carefully** - They tell you exactly what's wrong
- **Break big problems into steps** - Don't try to do everything at once

---

**Remember**: The template has intentional errors. Fix them!

**Good luck!** 🚀

---

*Need more help? Check README_lab4.md for detailed examples and explanations.*
