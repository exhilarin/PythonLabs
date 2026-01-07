[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Dg0i-74P)
# 🐍 Lab 7: Functional Programming & Advanced Aggregations

## 📖 Overview

This lab focuses on **functional programming techniques in Python**, including `map`, `filter`, and `reduce`, as well as **data formatting, cleaning, and complex querying**. You are expected to write clean, functional-style solutions **without explicit loops**.

⏱️ **Time Limit:** 100 minutes  
📊 **Total Points:** 44

---

## 📋 Instructions

### 1. Setup Environment

```bash
git clone <your-repository-url>
cd <repository-name>
```

## 📝 2. Complete Exercises

Open **`lab7_exercises.py`**.

⚠️ **IMPORTANT FORMAT RULE (READ CAREFULLY):**

- The starter file **DOES NOT** contain any function or class implementations.
- You must write **every required `def` and `class` from scratch**.
- Only the **TODO descriptions** define what you should implement.
- **Do NOT change** function names, parameter names, or return types.
- Each exercise is **independent**.
- If a function or class is missing or misspelled, related tests will **FAIL**.

## 🧪 3. Test Locally

Run the autograder:

```bash
python test_lab7.py
```

**Expected behaviors:**

- ❌ **FAILED** → Logic is incorrect or item is missing
- ✅ **SUCCESSFUL** → Exercise implemented correctly
- ⚠️ **ERROR (NoneType)** → Missing return statement or wrong return type

> **Note:** In the starter state, all tests are expected to **FAIL**.

## 📤 4. Submission

```bash
git add lab7_exercises.py
git commit -m "Complete Lab 7: Functional Programming"
git push origin main
```

## 📚 Exercises Overview

| Section   | Topic                          | Points | Difficulty |
| --------- | ------------------------------ | ------ | ---------- |
| A         | Map, Filter, Data Cleaning     | 14     | Easy       |
| B         | Reduce & Aggregations          | 15     | Medium     |
| C         | Complex Queries (MP VR) & Logs | 15     | Hard       |
| **TOTAL** |                                | **44** |            |

## 🎯 Core Learning Goals

By completing this lab, you should be able to:

- Write pure functions using `lambda`
- Transform collections using `map`
- Filter datasets using `filter`
- Aggregate values safely using `functools.reduce`
- Perform multi-stage functional pipelines
- Clean and normalize messy real-world data
- Query structured data without side effects

## ⚠️ Common Mistakes to Avoid

- Forgetting to **return a value**
- Returning an **iterator instead of a list**
- **Misspelling** function or class names
- Using **explicit `for` loops** instead of functional tools
- Omitting the **initializer** in `reduce`
- Modifying the **original input data**

## 🧪 Testing Philosophy

- Tests are **strict by design**
- Missing functions/classes cause **FAIL**, not SKIP
- **Hidden checks** ensure:
  - Correct return types
  - Proper use of functional patterns
  - No reliance on side effects
- This mirrors real-world code review and production constraints

## 🎓 Final Notes

- Follow the **TODO instructions exactly**
- Do **not add helper code** outside the required functions
- Keep solutions **simple, readable, and functional**
- When in doubt, **re-read the TODO description**

> **Good luck 🚀**  
> _Focus on clarity over cleverness._
