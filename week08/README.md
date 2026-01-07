[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/8RuvOwzs)
# 🐍 LAB 8: Visualization & Pandas DateTime

## 📌 Overview

This lab focuses on **data visualization with Matplotlib** and **date/time operations with Pandas**.  
You will practice working with `datetime` data, basic aggregations, and creating different types of plots using both
Matplotlib’s object-oriented API and Pandas plotting.

Each exercise is **independent** and must be implemented exactly where `pass` is indicated.

---

## 🎯 Learning Objectives

By completing this lab, you should be able to:

- Parse date strings into Pandas datetime objects
- Extract datetime-based features (year, month, day, etc.)
- Perform daily and weekly aggregations
- Create plots using:
  - Matplotlib (object-oriented API)
  - Pandas built-in plotting
- Work with multiple subplots and simple dashboards
- Save figures to files programmatically

---

## 🧪 Structure

The lab consists of **15 exercises** divided into three sections:

### 🟢 Section A — Easy (2 pts each)

- Datetime parsing and feature extraction
- Basic line plots, histograms, and bar plots
- Simple Pandas plotting

### 🟡 Section B — Medium (3 pts each)

- Daily aggregation with dates
- Plotting on existing axes
- Saving plots to files
- Working with subplots

### 🔴 Section C — Hard (5 pts each)

- Multi-plot dashboards
- Weekly aggregation with `DateTimeIndex`
- Ranking days by aggregated values
- Comparing multiple metrics
- Filtering by date range and plotting

---

## ⚠️ Important Rules

- **Function names must match exactly** as specified.
- **Do not change function signatures**.
- **Do not call `plt.show()`** in any function.
- Return values must match the expected type exactly.
- Column names (and order, where specified) must be respected.
- Input date strings may include **mixed formats** (with or without time).

---

## 🧩 Files

- `lab8_exercises.py` → Your solutions go here
- `lab8_test.py` → Autograder / test file (do not modify unless instructed)

---

## 🛠️ Installation

Before running the tests, install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## 🧠 Tips

- Prefer Pandas datetime utilities (`pd.to_datetime`, `.dt` accessor).
- Use Matplotlib’s **object-oriented API** (`fig, ax = plt.subplots()`).
- When working with dates, always convert to datetime **before** grouping or filtering.
- Read function docstrings and comments carefully — they describe grading expectations.

---

## ✅ Submission

Make sure:

- All functions are implemented
- The test file runs without errors
- Your code executes without printing unnecessary output

Good luck! 🚀
