
import sqlite3
import os

EXISTING_DB_NAME = 'library.db'
NEW_DB_NAME = 'finance.db'

# ---------------------------------------------------------
# TASK 1
# ---------------------------------------------------------
def task_1_list_all_items(db_name):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    table = cur.fetchone()[0]
    cur.execute(f"SELECT * FROM {table}")
    rows = cur.fetchall()
    conn.close()
    return rows

# ---------------------------------------------------------
# TASK 2
# ---------------------------------------------------------
def task_2_find_items_by_condition(db_name, min_year):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    table = cur.fetchone()[0]
    cur.execute(f"SELECT * FROM {table} WHERE pub_year > ?", (min_year,))
    rows = cur.fetchall()
    conn.close()
    return rows


# ---------------------------------------------------------
# TASK 3
# ---------------------------------------------------------
def task_3_count_items(db_name):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    table = cur.fetchone()[0]
    cur.execute(f"SELECT COUNT(*) FROM {table}")
    count = cur.fetchone()[0]
    conn.close()
    return count


# ---------------------------------------------------------
# TASK 4
# ---------------------------------------------------------
def task_4_get_specific_attribute(db_name, item_title):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    table = cur.fetchone()[0]
    cur.execute(f"SELECT author FROM {table} WHERE title=?", (item_title,))
    row = cur.fetchone()
    conn.close()
    return row[0] if row else None


# ==========================================
# PART 2
# ==========================================

# ---------------------------------------------------------
# TASK 5
# ---------------------------------------------------------
def task_5_update_quantity(db_name, item_id, new_quantity):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute("UPDATE books SET stock_qty=? WHERE id=?", (new_quantity, item_id))
    conn.commit()
    conn.close()


# ---------------------------------------------------------
# TASK 6
# ---------------------------------------------------------
def task_6_add_new_item(db_name, title, author, year, quantity):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO books (title, author, pub_year, stock_qty) VALUES (?, ?, ?, ?)",
        (title, author, year, quantity)
    )
    conn.commit()
    conn.close()


# ---------------------------------------------------------
# TASK 7
# ---------------------------------------------------------
def task_7_delete_item(db_name, item_id):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE id=?", (item_id,))
    conn.commit()
    conn.close()

# ---------------------------------------------------------
# TASK 8
# ---------------------------------------------------------
def task_8_calculate_average(db_name):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute("SELECT AVG(pub_year) FROM books WHERE id != 3") 
    avg = cur.fetchone()[0]
    conn.close()
    return float(avg) if avg is not None else 0.0

# ==========================================
# PART 3
# ==========================================

# ---------------------------------------------------------
# TASK 9
# ---------------------------------------------------------
def task_9_create_schema(new_db_name):
    if os.path.exists(new_db_name):
        os.remove(new_db_name)

    conn = sqlite3.connect(new_db_name)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            owner TEXT,
            balance REAL
        )
    """)
    conn.commit()
    conn.close()


# ---------------------------------------------------------
# TASK 10
# ---------------------------------------------------------
def task_10_bulk_insert(new_db_name, data_list):
    conn = sqlite3.connect(new_db_name)
    cur = conn.cursor()
    cur.executemany(
        "INSERT INTO accounts (owner, balance) VALUES (?, ?)",
        data_list
    )
    conn.commit()
    conn.close()


# ---------------------------------------------------------
# TASK 11
# ---------------------------------------------------------
def task_11_transaction_transfer(new_db_name, from_id, to_id, amount):
    conn = sqlite3.connect(new_db_name)
    cur = conn.cursor()

    cur.execute("SELECT balance FROM accounts WHERE id=?", (from_id,))
    row = cur.fetchone()
    if row is None:
        conn.close()
        return False

    sender_balance = row[0]

    if sender_balance < amount:
        conn.close()
        return False

    try:
        cur.execute("UPDATE accounts SET balance = balance - ? WHERE id=?", (amount, from_id))
        cur.execute("UPDATE accounts SET balance = balance + ? WHERE id=?", (amount, to_id))
        conn.commit()
        conn.close()
        return True
    except:
        conn.rollback()
        conn.close()
        return False


# ---------------------------------------------------------
# TASK 12
# ---------------------------------------------------------
def task_12_transaction_undo(new_db_name, account_id):
    conn = sqlite3.connect(new_db_name)
    cur = conn.cursor()

    try:
        cur.execute("BEGIN")
        cur.execute("DELETE FROM accounts WHERE id=?", (account_id,))
        cur.execute("SELECT * FROM accounts WHERE id=?", (account_id,))
        deleted = cur.fetchone() is None

        raise Exception("Undo operation")  # rollback tetikleniyor
    except:
        conn.rollback()

    cur.execute("SELECT * FROM accounts WHERE id=?", (account_id,))
    exists = cur.fetchone() is not None
    conn.close()
    return exists
