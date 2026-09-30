# 🐍 PythonLabs

![Course](https://img.shields.io/badge/İstinye%20University-COE203-blue?style=for-the-badge)
![Language](https://img.shields.io/badge/Language-Python-blue?style=for-the-badge)
![Concepts](https://img.shields.io/badge/Concepts-Data%20%26%20OOP-yellowgreen?style=for-the-badge)

## 📚 Project Summary

**PythonLabs** is a collection of weekly lab assignments from the **COE203 – Advanced Programming with Python** course at İstinye University.

Each week is a timed lab (100 minutes) with a set of exercises, automatically graded by `pytest` tests. Together they cover Python from the basics to OOP, working with databases and web data, functional programming and data visualization.

---

## 🧠 What I Learned in PythonLabs

| Week | Topic | Main Skills |
|---|---|---|
| **01** | Python Foundations | Variables, calculations, conditionals, debugging |
| **02** | Lists, Loops & File Operations | List processing, loops, reading and writing files |
| **03** | Functions, Dictionaries & Data Structures | Reusable functions, key-value data, building complete programs |
| **04** | Functions & Web Data Processing | URLs, JSON responses, cleaning messy real-world data |
| **05** | SQLite3 Database Operations | Exploring an unknown schema, queries, updates, transactions (commit/rollback) |
| **06** | Object-Oriented Programming | Classes, inheritance, polymorphism, encapsulation |
| **07** | Functional Programming | `map`, `filter`, `reduce`, aggregations without explicit loops |
| **08** | Visualization & Pandas DateTime | Matplotlib (OO API), Pandas plotting, datetime features, daily/weekly aggregation |

### 🔹 Testing and Code Quality
* Running automated tests with **pytest** and improving code until all tests pass
* Reading test failures to debug and fixing function contracts
* Writing clean, readable functions under time pressure

---

## 📁 Project Structure

```bash
PythonLabs/
├── week01/
│   ├── lab1_exercises.py    # My solutions
│   ├── test_lab1.py         # Autograding tests
│   └── README.md            # Lab instructions
├── week02/ ... week08/      # Same structure for each week
│   └── (extra reference files: cheat sheets, SQLite tutorial)
└── README.md
```

---

## 🚀 How to Run

```bash
git clone https://github.com/exhilarin/PythonLabs.git
cd PythonLabs/week03

pip install -r requirements.txt   # if the week has one
pytest test_lab3.py
```

---

## 🚀 Key Takeaways

These labs build Python skills step by step: from syntax and data structures to databases, OOP, functional style and data visualization.

---

> _“Small exercises every week add up to real skills.”_
