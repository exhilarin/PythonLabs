# ==========================================
# LAB 7: FUNCTIONAL PROGRAMMING & DATA PROCESSING
# Advanced Python Course - Week 7
# ==========================================
# 
# INSTRUCTIONS:
# - Use functional programming tools: map(), filter(), and functools.reduce()
# - Practice data cleaning, formatting, and complex querying
# - NO external libraries like pandas or numpy (use built-in functions)
# - Complete each exercise below
# - Test your code by running: python test_lab7.py
#
# TOTAL POINTS: 44
# ==========================================

import functools
import sqlite3

# ==========================================
# SECTION A: EASY - BASIC FUNCTIONAL TOOLS (12 points)
# map, filter, and simple cleaning (2 points each)
# ==========================================


# ==========================================
# EXERCISE 1: Week 5 Reminder - SQL Query (2 points)
# ==========================================
def get_high_balance_users(db_name: str, threshold: float) -> list:
    """
    Connect to the SQLite database and return the names of users whose balance
    is strictly greater than the given threshold.
    """
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Execute the query
    cursor.execute("SELECT owner FROM accounts WHERE balance > ?", (threshold,))
    results = [row[0] for row in cursor.fetchall()]

    # Close the connection
    conn.close()
    return results

# ==========================================
# EXERCISE 2: Week 6 Reminder - OOP Basics (2 points)
# ==========================================
class DataPoint:
    """
    A class to represent a data point with x and y coordinates.
    """
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance_from_origin(self) -> float:
        """
        Calculate and return the distance of the data point from the origin (0, 0).
        """
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def as_tuple(self):
        """
        Return the data point as a tuple (label, value).
        """
        return (self.x, self.y)

# ==========================================
# EXERCISE 3: Convert to USD (2 points)
# ==========================================
def convert_to_usd(amounts: list, rate: float) -> list:
    """
    Convert a list of amounts to USD using the given exchange rate.
    """
    return list(map(lambda x: round(x * rate, 2), amounts))

# ==========================================
# EXERCISE 4: Filter High Ratings (2 points)
# ==========================================
def filter_high_ratings(ratings: list, threshold: float) -> list:
    """
    Filter and return ratings that are strictly above the given threshold.
    """
    return list(filter(lambda x: x['rating'] > threshold, ratings))

# ==========================================
# EXERCISE 5: Data Cleaning - Name Normalization (2 points)
# ==========================================
def normalize_names(raw_names: list) -> list:
    """
    Clean each name by removing extra spaces and capitalizing the first letter of each word.
    """
    return list(map(lambda name: " ".join(word.capitalize() for word in name.split()), raw_names))

# ==========================================
# EXERCISE 6: Simple Map - Power of Two (2 points)
# ==========================================
def square_numbers(numbers: list) -> list:
    """
    Use map() to calculate the square of each number in the input list.
    """
    return list(map(lambda x: x ** 2, numbers))

# ==========================================
# SECTION B: MEDIUM - DATA FORMATTING & REDUCE (12 points)
# Grouping, aggregating and complex transformations (3 points each)
# ==========================================

# ==========================================
# EXERCISE 7: Map & Filter - Bonus Calculation (3 points)
# ==========================================
def calculate_bonuses(employees: list) -> list:
    """
    Calculate bonuses for employees with performance scores above 70.
    """
    filtered_employees = filter(lambda e: e["performance_score"] >= 70, employees)
    return [f"{e['name']} bonus: {round(e['salary'] * 0.10, 2)}" for e in filtered_employees]

# ==========================================
# EXERCISE 8: Reduce - Total Order Value (3 points)
# ==========================================
def total_order_value(cart_items: list) -> float:
    """
    Calculate the total value of the cart using reduce.
    """
    return functools.reduce(lambda acc, item: acc + item["price"] * item["quantity"], cart_items, 0)

# ==========================================
# EXERCISE 9: Data Formatting - CSV to Dict (3 points)
# ==========================================
def format_sensor_data(raw_data: list) -> list:
    """
    Convert each CSV-like string into a dictionary.
    """
    return list(map(lambda row: {"id": int(row.split(",")[0]), "type": row.split(",")[1], "value": float(row.split(",")[2])}, raw_data))

# ==========================================
# EXERCISE 10: Dictionary Formatting - Map (3 points)
# ==========================================
def extract_emails(user_dicts: list) -> list:
    """
    Extract and return emails in lowercase from a list of dictionaries.
    """
    return list(map(lambda user: user["email"].lower(), user_dicts))

# ==========================================
# SECTION C: HARD - QUERIES (MP VR) (20 points)
# Complex data querying and multi-step processing (5 points each)
# ==========================================

# ==========================================
# EXERCISE 11: The "MP VR" Query - Nested Project Stats (5 points)
# ==========================================
def get_department_projects(staff_data: list, target_dept: str) -> list:
    """
    Get unique project names for a specific department.
    """
    filtered = filter(lambda staff: staff["dept"] == target_dept, staff_data)
    projects = functools.reduce(lambda acc, staff: acc + staff["projects"], filtered, [])
    return sorted(set(projects))

# ==========================================
# EXERCISE 12: Advanced Data Cleaning - Faulty Logs (5 points)
# ==========================================
def clean_and_query_logs(log_strings: list) -> list:
    """
    Extract unique error codes from logs containing "ERROR".
    """
    error_logs = filter(lambda log: "ERROR" in log, log_strings)
    error_codes = set(map(lambda log: int(log.split("CODE:")[1].split()[0]), error_logs))
    return sorted(error_codes, reverse=True)

# ==========================================
# EXERCISE 13: MP VR - Aggregating Sales (5 points)
# ==========================================
def total_revenue_by_category(sales_data: list, category_name: str) -> float:
    """
    Calculate total revenue for a specific category.
    """
    filtered_sales = filter(lambda sale: sale["cat"] == category_name, sales_data)
    revenues = map(lambda sale: sale["p"] * sale["q"], filtered_sales)
    return functools.reduce(lambda acc, revenue: acc + revenue, revenues, 0)

# ==========================================
# EXERCISE 14: Complex Formatting - Nested Data (5 points)
# ==========================================
def summarize_inventory(warehouse_data: list) -> list:
    """
    Summarize inventory for each warehouse.
    """
    return list(map(lambda warehouse: f"Warehouse {warehouse['id']}: Total Items = {sum(warehouse['stock'])}", warehouse_data))

# ==========================================
# DO NOT MODIFY BELOW THIS LINE
# ==========================================
if __name__ == "__main__":
    print("Run 'python test_lab7.py' to test your solutions!")