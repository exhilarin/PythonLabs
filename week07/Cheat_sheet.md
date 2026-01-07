# 📑 Lab 7 – Functional Programming Quick Reference

## Purpose of This Document

This document is a **conceptual reference** for Lab 7.  
It summarizes **key functional programming ideas** used in the lab.

⚠️ This file is **NOT required** to complete the exercises and **does not contain solutions**.

---

## 1. Functional Programming – Core Concepts

Functional programming focuses on:

- Transforming data without modifying the original source
- Describing _what_ should happen, not _how_
- Using small, composable operations

In this lab, the main tools are:

- **map** → transformation
- **filter** → selection
- **reduce** → aggregation

---

## 2. map – Transformation

**Purpose:**  
Apply the same rule to every element in a sequence.

**Mental model:**

> “Take each item → transform it → keep the structure”

Common use cases:

- Converting values (currency, units)
- Formatting strings
- Extracting fields from dictionaries

---

## 3. filter – Selection

**Purpose:**  
Keep only elements that satisfy a condition.

**Mental model:**

> “Keep this? Yes or No.”

Common use cases:

- Threshold checks
- Removing invalid data
- Selecting items by category or status

---

## 4. reduce – Aggregation

**Purpose:**  
Combine many values into a single result.

**Mental model:**

> “Start with an initial value → combine step by step”

Important ideas:

- An **initializer** makes reduce safe for empty inputs
- The accumulator represents the partial result

Typical aggregations:

- Totals
- Flattening nested data
- Building summary values

---

## 5. The Functional Pipeline Pattern

Complex queries often follow this logical flow:

1. **FILTER** – narrow the dataset
2. **MAP** – extract or transform needed fields
3. **REDUCE** – aggregate results
4. **POLISH** – clean, sort, or deduplicate output

This pattern is used in the most advanced exercises.

---

## 6. Data Cleaning – Conceptual Tools

Common data issues handled in this lab:

- Extra whitespace
- Inconsistent casing
- Mixed data types
- Repeated values

Typical conceptual steps:

- Trim unnecessary characters
- Normalize formatting
- Convert data to consistent types
- Remove duplicates

---

## 7. Lambda Functions – When to Use Them

Lambdas are:

- Small
- Single-expression
- Temporary

They are best used when:

- The logic is simple
- The function is not reused
- Readability is preserved

If logic becomes complex, a named function is preferred.

---

## 8. Common Conceptual Mistakes

Be aware of these pitfalls:

- Forgetting that map/filter return iterators
- Omitting an initializer in reduce
- Returning nothing from a function
- Changing the original input data
- Mixing procedural loops with functional logic

---

## 9. Testing Expectations

The test system is strict by design:

- Missing functions or classes → FAIL
- Wrong return type → FAIL
- Incorrect logic → FAIL

This reflects real-world automated testing standards.

---

## Final Note

This cheat sheet is meant to support **understanding**, not replace problem-solving.

Focus on:

- Reading the TODO descriptions carefully
- Writing clear, minimal logic
- Keeping solutions functional and clean
