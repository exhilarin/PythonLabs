SQLite3 Quick Reference Guide
=============================

This document covers the essential commands and patterns for working with SQLite3 in Python. It does not provide the answers to your lab directly but provides the syntax blocks you will need to construct your solutions.

1\. Connecting and Cursors
--------------------------

To perform any action, you need a connection and a cursor. The connection represents the database file; the cursor is the tool used to execute queries.

```python
import sqlite3

# Opens file if exists, creates if not
connection = sqlite3.connect('my_database.db')

# The cursor allows us to run SQL commands
cursor = connection.cursor()

# ... perform work ...

# Always close the connection when done
connection.close()
```

2\. Exploring Metadata (The "Mystery" Tables)
---------------------------------------------

If you don't know what is inside a database, you can query the master table `sqlite_master`.

```SQL
-- Finds all table names
SELECT name FROM sqlite_master WHERE type='table';

-- Shows the SQL statement used to create the table (reveals columns)
SELECT sql FROM sqlite_master WHERE name='specific_table_name';

```

In Python:

```python
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()

```

3\. Retrieving Data (SELECT)
----------------------------

### Basic Fetch

```python
cursor.execute("SELECT * FROM my_table")

# Get one row (the next one in the queue)
one_row = cursor.fetchone()

# Get all remaining rows as a list of tuples
all_rows = cursor.fetchall()

```

### Filtering with Parameters (Security Best Practice)

Never use f-strings or string concatenation for values (prevents SQL Injection). Use the `?` placeholder.

```python
# GOOD:
target_year = 2020
cursor.execute("SELECT * FROM books WHERE year > ?", (target_year,))

# Tuple notation: (value,) is required even for one item.

```

4\. Modifying Data (INSERT, UPDATE, DELETE)
-------------------------------------------

**Important:** Modifications usually require a `commit()` to save the changes to the file.

### Insert

```python
# Inserting one row
cursor.execute("INSERT INTO books (title, qty) VALUES (?, ?)", ("My Book", 10))
connection.commit()

```

### Bulk Insert (Fast)

If you have a list of data, don't loop manually. Use `executemany`.

```python
data = [
    ("Book A", 5),
    ("Book B", 10)
]
cursor.executemany("INSERT INTO books (title, qty) VALUES (?, ?)", data)
connection.commit()

```

### Update

```python
cursor.execute("UPDATE books SET qty = ? WHERE id = ?", (50, 1))
connection.commit()

```

### Delete

```python
cursor.execute("DELETE FROM books WHERE id = ?", (1,))
connection.commit()

```

5\. Creating Tables
-------------------

```python
create_query = '''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT,
    balance REAL DEFAULT 0.0
)
'''
cursor.execute(create_query)

```

6\. Transactions and ACID Compliance
------------------------------------

SQLite treats individual `execute()` commands as atomic, but sometimes you need multiple steps to count as one action (e.g., Bank Transfer).

### The Commit/Rollback Pattern

```python
try:
    # 1. Start operations (Transaction starts automatically)
    cursor.execute("UPDATE accounts SET balance = balance - 100 WHERE id = 1")
    cursor.execute("UPDATE accounts SET balance = balance + 100 WHERE id = 2")

    # 2. Save everything if no errors occurred
    connection.commit()
    print("Transfer successful")

except Exception as e:
    # 3. If ANY error happened (e.g., Python crash, constraint violation)
    print("Error occurred, undoing changes...")
    connection.rollback()

```

### Undoing an Operation Explicitly

If you perform an action and want to reverse it purely for logic reasons (not just errors):

```python
cursor.execute("DELETE FROM users WHERE id=5")
# ... verification logic ...
# "Oops, shouldn't have done that."
connection.rollback()
# The delete is canceled, user 5 is back.

```