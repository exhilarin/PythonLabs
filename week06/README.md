[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/WEIjVhGU)
[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/kPvCFn2F)

# Lab 6: Object-Oriented Programming (OOP)

## Overview

Master Object-Oriented Programming concepts in Python! This lab introduces classes, inheritance, polymorphism, encapsulation, and advanced OOP patterns.

**⏱️ Time Limit:** 100 minutes | **📊 Total Points:** 44

---

## 📋 Instructions

### 1. Accept the Assignment

Click the assignment link provided by your instructor.

### 2. Clone Your Repository

```bash
git clone <your-repository-url>
cd <repository-name>
```

### 3. Complete the Exercises

Open `lab6_exercises.py` and implement each function/class.

### 4. Test Locally

```bash
python test_lab6.py
```

### 5. Submit Your Work

```bash
git add lab6_exercises.py
git commit -m "Complete Lab 6 exercises"
git push
```

### 6. Check Results on GitHub

- Go to **Actions** tab
- ✅ Green checkmark = All tests passed
- ❌ Red X = Tests failed (click for details)

---

## 📚 Exercises Overview

| Section | Topic                | Points | Difficulty |
| ------- | -------------------- | ------ | ---------- |
| **A**   | Basic Concepts (1-6) | 12     | Easy       |
| **B**   | OOP Concepts (7-12)  | 18     | Medium     |
| **C**   | Advanced OOP (13-16) | 20     | Hard       |
|         | **TOTAL**            | **44** |            |

---

## 🎯 Core OOP Concepts

### Classes & Objects

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

### Inheritance

```python
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
```

### Encapsulation

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private

    def get_balance(self):
        return self.__balance
```

### Polymorphism

```python
class Animal:
    def speak(self):
        return "Sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"
```

---

## ⏰ Time Management

| Time       | Section   | Exercises      |
| ---------- | --------- | -------------- |
| 0-25 min   | Section A | 1-6 (12 pts)   |
| 25-65 min  | Section B | 7-12 (18 pts)  |
| 65-100 min | Section C | 13-16 (20 pts) |

---

## 🔧 Common Patterns

**Constructor**

```python
def __init__(self, param1, param2):
    self.attr1 = param1
    self.attr2 = param2
```

**Method Overriding**

```python
class Child(Parent):
    def method(self):
        return "Child"
```

**Properties**

```python
@property
def fahrenheit(self):
    return self._celsius * 9/5 + 32

@celsius.setter
def celsius(self, value):
    self._celsius = value
```

**Composition**

```python
class Car:
    def __init__(self, engine):
        self.engine = engine
```

---

## 🚫 Restrictions

- ❌ No external libraries (built-in Python only)
- ❌ No advanced features unless specified
- ✅ Use proper OOP design

---

## 🏆 Success Checklist

- [ ] All classes have `__init__` methods
- [ ] Inheritance uses `super().__init__()`
- [ ] Private attributes use `__` prefix
- [ ] Methods properly overridden
- [ ] Tests pass locally
- [ ] Code follows OOP principles
- [ ] Changes pushed to GitHub
- [ ] GitHub Actions shows ✅

---

## 🎓 Learning Objectives

✅ Create and use classes  
✅ Implement inheritance  
✅ Apply encapsulation  
✅ Use polymorphism  
✅ Understand properties  
✅ Implement class/static methods  
✅ Create iterators  
✅ Apply composition

---

## 🆘 When Stuck

1. Review examples in this README
2. Check test output for failures
3. Test small parts incrementally
4. Use `print()` for debugging
5. Ask TAs during lab hours

---

## 💪 Final Advice

**OOP is a mindset!** Think in objects and interactions, not just functions.

- Keep classes focused
- Favor composition over inheritance
- Use private attributes
- Override meaningfully

**Pro Tip:** Master the Person/Student examples (4-6) before tackling advanced patterns!

Good luck! 🚀
