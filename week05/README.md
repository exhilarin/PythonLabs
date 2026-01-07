[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/J7yrNDFr)
Lab 5: SQLite3 Database Operations
==================================

In this lab, you will demonstrate your ability to interact with SQL databases using Python's `sqlite3` module. You will be acting as a Database Administrator (DBA).

Read `SQLITE_DATABASE_TUTORIAL` for Sqlite3 cheatsheet.

Overview
--------

Total Points: **40**

The lab is divided into two sections:

1.  **Mystery Database (20 pts):** You are given a file `library.db` (generated automatically when you run tests). You do not know the table names or columns. You must discover them and perform queries/updates.

2.  **New System (20 pts):** You must create a `finance.db` from scratch, design a schema, and handle complex Transactions (Commit/Rollback).

File Structure
--------------

-   `lab5_exercises.py`: **EDIT THIS FILE.** This is where you write your code.

-   `test_lab5.py`: Run this to check your score. DO NOT EDIT.

-   `SQLITE_DATABASE_TUTORIAL.md`: Use this as a reference guide.

How to Run Tests & Check Score
------------------------------

We use `pytest` to grade the lab. The testing script will automatically generate the database files required for the lab.

1.  Open your terminal.

2.  Run the following command:

    ```bash
    pytest -v -s

    ```

    *(The `-v` shows details, `-s` allows printed output to be seen)*

3.  At the end of the test run, you will see a **Score Summary** calculated out of 40 points.

Assignments
-----------

### Part 1: Exploration (Existing DB)

-   **Easy (2 pts each):** List items, Filter items, Count items, Get attribute.

-   **Medium (3 pts each):** Update stock, Add item, Delete item, Calculate Average.

### Part 2: Creation (New DB)

-   **Hard (5 pts each):** * Create Schema (Create table/db).

    -   Bulk Insert (Using `executemany`).

    -   Transaction (Money Transfer with `commit`).

    -   Undo (Simulate error and `rollback`).

Submission
----------

1.  Complete the functions in `lab5_exercises.py`.

2.  Ensure `pytest` shows 40/40.

3.  Commit and Push to GitHub Classroom:

    ```bash
    git add lab5_exercises.py
    git commit -m "Completed Lab 5"
    git push origin main

    ```