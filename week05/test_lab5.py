import pytest
import sqlite3
import os
import lab5_exercises as lab


# --- SETUP: GENERATE MYSTERY DB ---
# This runs before any tests to ensure the student has the DB to work with.
@pytest.fixture(scope="session", autouse=True)
def setup_mystery_db():
    db_name = lab.EXISTING_DB_NAME
    if os.path.exists(db_name):
        os.remove(db_name)

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Hidden schema for student to discover
    cursor.execute('''
                   CREATE TABLE books
                   (
                       id        INTEGER PRIMARY KEY AUTOINCREMENT,
                       title     TEXT NOT NULL,
                       author    TEXT NOT NULL,
                       pub_year  INTEGER,
                       stock_qty INTEGER
                   )
                   ''')

    data = [
        ('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 5),
        ('To Kill a Mockingbird', 'Harper Lee', 1960, 3),
        ('1984', 'George Orwell', 1949, 10),
        ('Pride and Prejudice', 'Jane Austen', 1813, 2),
        ('The Catcher in the Rye', 'J.D. Salinger', 1951, 0)
    ]
    cursor.executemany('INSERT INTO books (title, author, pub_year, stock_qty) VALUES (?, ?, ?, ?)', data)
    conn.commit()
    conn.close()

    yield db_name

    # Cleanup
    if os.path.exists(db_name):
        os.remove(db_name)
    if os.path.exists(lab.NEW_DB_NAME):
        os.remove(lab.NEW_DB_NAME)


# --- HELPER ---
def check_func(func_name):
    if not hasattr(lab, func_name):
        pytest.fail(f"Function '{func_name}' not defined in lab5_exercises.py. Check spelling!")


# --- EASY TESTS (2 PTS) ---

@pytest.mark.easy
def test_task_1_list_all(setup_mystery_db):
    check_func('task_1_list_all_items')
    results = lab.task_1_list_all_items(setup_mystery_db)
    assert results is not None, "Function returned None"
    assert len(results) == 5, "Should return all 5 rows"
    assert results[0][1] == 'The Great Gatsby', "First item title mismatch"


@pytest.mark.easy
def test_task_2_condition(setup_mystery_db):
    check_func('task_2_find_items_by_condition')
    # Books after 1950: Mockingbird (1960) and Catcher (1951)
    results = lab.task_2_find_items_by_condition(setup_mystery_db, 1950)
    assert results is not None
    assert len(results) == 2, "Should find exactly 2 books published after 1950"
    titles = [r[1] for r in results]
    assert 'To Kill a Mockingbird' in titles


@pytest.mark.easy
def test_task_3_count(setup_mystery_db):
    check_func('task_3_count_items')
    count = lab.task_3_count_items(setup_mystery_db)
    assert count == 5


@pytest.mark.easy
def test_task_4_attribute(setup_mystery_db):
    check_func('task_4_get_specific_attribute')
    author = lab.task_4_get_specific_attribute(setup_mystery_db, '1984')
    assert author == 'George Orwell'

    missing = lab.task_4_get_specific_attribute(setup_mystery_db, 'Harry Potter')
    assert missing is None


# --- MEDIUM TESTS (3 PTS) ---

@pytest.mark.medium
def test_task_5_update(setup_mystery_db):
    check_func('task_5_update_quantity')
    # ID 1 has 5 copies. Set to 20.
    lab.task_5_update_quantity(setup_mystery_db, 1, 20)

    # Verify
    conn = sqlite3.connect(setup_mystery_db)
    cur = conn.cursor()
    cur.execute("SELECT stock_qty FROM books WHERE id=1")
    val = cur.fetchone()[0]
    conn.close()
    assert val == 20


@pytest.mark.medium
def test_task_6_insert(setup_mystery_db):
    check_func('task_6_add_new_item')
    lab.task_6_add_new_item(setup_mystery_db, 'Dune', 'Frank Herbert', 1965, 7)

    conn = sqlite3.connect(setup_mystery_db)
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE title='Dune'")
    row = cur.fetchone()
    conn.close()

    assert row is not None
    assert row[2] == 'Frank Herbert'


@pytest.mark.medium
def test_task_7_delete(setup_mystery_db):
    check_func('task_7_delete_item')
    # Delete ID 3 (1984)
    lab.task_7_delete_item(setup_mystery_db, 3)

    conn = sqlite3.connect(setup_mystery_db)
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE id=3")
    row = cur.fetchone()
    conn.close()

    assert row is None, "Item ID 3 should be deleted"


@pytest.mark.medium
def test_task_8_avg(setup_mystery_db):
    check_func('task_8_calculate_average')
    # Current DB state:
    # Gatsby (1925), Mockingbird (1960), P&P (1813), Catcher (1951), Dune (1965)
    # Sum: 7714. Count: 5. Avg: 1542.8
    # Note: 1984 was deleted in previous test

    avg = lab.task_8_calculate_average(setup_mystery_db)
    # Allow small float error
    assert 1540 < avg < 1545


# --- HARD TESTS (5 PTS) ---

@pytest.mark.hard
def test_task_9_create_schema():
    check_func('task_9_create_schema')
    db_name = lab.NEW_DB_NAME
    if os.path.exists(db_name):
        os.remove(db_name)

    lab.task_9_create_schema(db_name)

    assert os.path.exists(db_name), "Database file not created"

    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    # Check table exists
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='accounts'")
    assert cur.fetchone() is not None, "Table 'accounts' not created"

    # Check columns roughly
    cur.execute("PRAGMA table_info(accounts)")
    cols = [info[1] for info in cur.fetchall()]
    assert 'owner' in cols
    assert 'balance' in cols
    conn.close()


@pytest.mark.hard
def test_task_10_bulk_insert():
    check_func('task_10_bulk_insert')
    db_name = lab.NEW_DB_NAME
    data = [('Alice', 1000.0), ('Bob', 500.0), ('Charlie', 200.0)]
    lab.task_10_bulk_insert(db_name, data)

    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute("SELECT count(*) FROM accounts")
    count = cur.fetchone()[0]
    conn.close()
    assert count == 3


@pytest.mark.hard
def test_task_11_transaction_transfer():
    check_func('task_11_transaction_transfer')
    db_name = lab.NEW_DB_NAME
    # Assume IDs: Alice=1 (1000), Bob=2 (500)

    # 1. Valid Transfer
    success = lab.task_11_transaction_transfer(db_name, 1, 2, 100.0)
    assert success is True

    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute("SELECT balance FROM accounts WHERE id=1")
    alice_bal = cur.fetchone()[0]
    cur.execute("SELECT balance FROM accounts WHERE id=2")
    bob_bal = cur.fetchone()[0]
    conn.close()

    assert alice_bal == 900.0
    assert bob_bal == 600.0

    # 2. Invalid Transfer (Overdraft)
    success = lab.task_11_transaction_transfer(db_name, 1, 2, 9000.0)
    assert success is False


@pytest.mark.hard
def test_task_12_undo():
    check_func('task_12_transaction_undo')
    db_name = lab.NEW_DB_NAME
    # Try to delete Alice (id=1), but rollback

    exists_after_rollback = lab.task_12_transaction_undo(db_name, 1)

    assert exists_after_rollback is True

    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute("SELECT * FROM accounts WHERE id=1")
    row = cur.fetchone()
    conn.close()

    assert row is not None, "Alice should still exist after rollback"