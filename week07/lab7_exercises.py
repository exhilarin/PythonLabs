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
# TODO:
#   Function Name: get_high_balance_users
#   Parameters:
#       db_name (str): Path to the SQLite database
#       threshold (float): Minimum balance
#   Returns:
#       list of strings
#   Description:
#       Connect to the SQLite database.
#       Select and return the names of users whose balance
#       is strictly greater than the given threshold.
#       Assume the table name is 'accounts' with columns
#       'owner' and 'balance'.
#   IMPORTANT:
#       Function name MUST be exactly 'get_high_balance_users'.
def get_high_balance_users(db_name, threshold):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute("SELECT owner FROM accounts WHERE balance > ?", (threshold,))
    owners = cur.fetchall()
    ret = []
    for owner in owners:
        ret.append(owner[0])
    conn.close()
    return ret

# ==========================================
# EXERCISE 2: Week 6 Reminder - OOP Basics (2 points)
# ==========================================
# TODO:
#   Create a class named 'DataPoint'.
#   Requirements:
#       1. __init__(self, label, value) must store instance attributes.
#       2. Implement a method named 'as_tuple'
#          that returns a tuple (label, value).
#   IMPORTANT:
#       Class name MUST be exactly 'DataPoint'.
class DataPoint:
    def __init__(self, label, value):
        self.label = label
        self.value = value
    
    def as_tuple(self):
        return (self.label, self.value)

# ==========================================
# EXERCISE 3: Simple Map - Price Conversion (2 points)
# ==========================================
# TODO:
#   Function Name: convert_to_usd
#   Parameters:
#       prices_in_try (list): List of float values
#       exchange_rate (float): Conversion rate
#   Returns:
#       list of floats
#   Description:
#       Convert each price from TRY to USD using map().
#       Round each converted value to 2 decimal places.
#   IMPORTANT:
#       The function MUST return a list.
def convert_to_usd(prices_in_try, exchange_rate):
    return list(map(lambda x: round(x * exchange_rate, 2), prices_in_try))


# ==========================================
# EXERCISE 4: Simple Filter - High Rating Only (2 points)
# ==========================================
# TODO:
#   Function Name: filter_high_ratings
#   Parameters:
#       products (list): List of dictionaries with 'rating' key
#       threshold (float): Minimum rating (default is 4.5)
#   Returns:
#       list of dictionaries
#   Description:
#       Filter and return only the products whose rating
#       is strictly greater than the threshold.
#       Use filter().
def filter_high_ratings(products, threshold=4.5):
    return list(filter(lambda p: p['rating'] > threshold, products))


# ==========================================
# EXERCISE 5: Data Cleaning - Name Normalization (2 points)
# ==========================================
# TODO:
#   Function Name: normalize_names
#   Parameters:
#       raw_names (list): List of raw name strings
#   Returns:
#       list of strings
#   Description:
#       Clean each name by:
#           - Removing extra spaces
#           - Capitalizing the first letter of each word
#       Use map() for transformation.
def normalize_names(raw_names):
    return list(map(lambda x: x.strip().title(), raw_names))

# ==========================================
# EXERCISE 6: Simple Map - Power of Two (2 points)
# ==========================================
# TODO:
#   Function Name: square_numbers
#   Parameters:
#       numbers (list): List of integers
#   Returns:
#       list: List of integers
#   Description:
#       Use map() to calculate the square of each number in the input list.
#       Return the result as a list.
#   IMPORTANT:
#       Function name MUST be exactly "square_numbers".
def square_numbers(numbers):
    return list(map(lambda x: x**2, numbers))


# ==========================================
# SECTION B: MEDIUM - DATA FORMATTING & REDUCE (12 points)
# Grouping, aggregating and complex transformations (3 points each)
# ==========================================

# ==========================================
# EXERCISE 7: Map & Filter - Bonus Calculation (3 points)
# ==========================================
# TODO:
#   Function Name: calculate_bonuses
#   Parameters:
#       employees (list): List of dictionaries with keys:
#           - "name" (str)
#           - "salary" (int/float)
#           - "performance_score" (int)
#   Returns:
#       list: List of strings
#   Description:
#       1) Filter out employees whose "performance_score" is below 70.
#       2) For remaining employees, compute bonus as salary * 0.10.
#       3) Return a list of strings in the EXACT format:
#          "{name} bonus: {bonus_amount}"
#   IMPORTANT:
#       Output string format must match exactly.
#       Function name MUST be exactly "calculate_bonuses".
def calculate_bonuses(employees):
    filtered = filter(lambda e: e['performance_score'] >= 70, employees)
    return list(map(lambda e: f"{e['name']} bonus: {e['salary']*0.1}", filtered))

# ==========================================
# EXERCISE 8: Reduce - Total Order Value (3 points)
# ==========================================
# TODO:
#   Function Name: total_order_value
#   Parameters:
#       cart_items (list): List of dictionaries with keys:
#           - "price" (int/float)
#           - "quantity" (int)
#   Returns:
#       int or float
#   Description:
#       Use functools.reduce() to calculate the total value of the cart.
#       Total is the sum of (price * quantity) for all items.
#   IMPORTANT:
#       Function name MUST be exactly "total_order_value".
def total_order_value(cart_items):
    return functools.reduce(lambda acc, item: acc + item['price'] * item['quantity'], cart_items, 0)


# ==========================================
# EXERCISE 9: Data Formatting - CSV to Dict (3 points)
# ==========================================
# TODO:
#   Function Name: format_sensor_data
#   Parameters:
#       raw_data (list): List of strings in CSV-like format: "id,type,value"
#   Returns:
#       list: List of dictionaries
#   Description:
#       Convert each string into a dictionary:
#           {"id": <int>, "type": <str>, "value": <float>}
#       Use map() for the transformation.
#   IMPORTANT:
#       Numeric conversion rules:
#           - "id" must be int
#           - "value" must be float
#       Function name MUST be exactly "format_sensor_data".
def format_sensor_data(raw_data):
    return list(map(lambda s: {"id": int(s.split(',')[0]),
                               "type": s.split(',')[1],
                               "value": float(s.split(',')[2])}, raw_data))


# ==========================================
# EXERCISE 10: Dictionary Formatting - Map (3 points)
# ==========================================
# TODO:
#   Function Name: extract_emails
#   Parameters:
#       user_dicts (list): List of dictionaries containing key "email"
#   Returns:
#       list: List of strings
#   Description:
#       Use map() to extract only the "email" values from each dictionary.
#       Return emails in lowercase.
#   IMPORTANT:
#       Function name MUST be exactly "extract_emails".
def extract_emails(user_dicts):
    return list(map(lambda u: u['email'].lower(), user_dicts))


# ==========================================
# SECTION C: HARD - QUERIES (MP VR) (20 points)
# Complex data querying and multi-step processing (5 points each)
# ==========================================

# ==========================================
# EXERCISE 11: The "MP VR" Query - Nested Project Stats (5 points)
# ==========================================
# TODO:
#   Function Name: get_department_projects
#   Parameters:
#       staff_data (list): List of dictionaries with keys:
#           - "name" (str)
#           - "dept" (str)
#           - "projects" (list of str)
#       target_dept (str): Department name to query
#   Returns:
#       list: List of unique project names (strings)
#   Description:
#       1) Filter staff_data to include only records where "dept" == target_dept.
#       2) Use map() to extract only the "projects" lists.
#       3) Use reduce() to flatten the list of lists into a single list.
#       4) Remove duplicates (unique projects only).
#       5) Return the unique projects sorted alphabetically (ascending).
#   IMPORTANT:
#       The returned list must be sorted.
#       Function name MUST be exactly "get_department_projects".
def get_department_projects(staff_data, target_dept):
    filtered = filter(lambda s: s['dept'] == target_dept, staff_data)
    projects_lists = map(lambda s: s['projects'], filtered)
    flattened = functools.reduce(lambda acc, x: acc + x, projects_lists, [])
    return sorted(set(flattened))



# ==========================================
# EXERCISE 12: Advanced Data Cleaning - Faulty Logs (5 points)
# ==========================================
# TODO:
#   Function Name: clean_and_query_logs
#   Parameters:
#       log_strings (list): List of log entry strings
#   Returns:
#       list: List of integers
#   Description:
#       1) Keep only logs that contain the keyword "ERROR".
#       2) Extract the error code from each ERROR log.
#          The code always appears after "CODE:" and ends at the next space.
#       3) Remove duplicate error codes.
#       4) Return the unique codes as integers, sorted in DESCENDING order.
#   IMPORTANT:
#       Output must be list of int.
#       Sorting order must be descending.
#       Function name MUST be exactly "clean_and_query_logs".
def clean_and_query_logs(log_strings):
    error_logs = filter(lambda s: "ERROR" in s, log_strings)
    codes = map(lambda s: int(s.split("CODE:")[1].split()[0]), error_logs)
    return sorted(set(codes), reverse=True)


# ==========================================
# EXERCISE 13: MP VR - Aggregating Sales (5 points)
# ==========================================
# TODO:
#   Function Name: total_revenue_by_category
#   Parameters:
#       sales_data (list): List of dictionaries with keys:
#           - "cat" (str)
#           - "p" (int/float)  price
#           - "q" (int)        quantity
#       category_name (str): Category to filter by
#   Returns:
#       int or float
#   Description:
#       1) Filter sales_data where "cat" == category_name.
#       2) Use map() to compute (p * q) for each filtered sale.
#       3) Use reduce() to sum these values into a total revenue.
#   IMPORTANT:
#       Function name MUST be exactly "total_revenue_by_category".
def total_revenue_by_category(sales_data, category_name):
    filtered = filter(lambda s: s['cat'] == category_name, sales_data)
    revenues = map(lambda s: s['p'] * s['q'], filtered)
    return functools.reduce(lambda acc, x: acc + x, revenues, 0)


# ==========================================
# EXERCISE 14: Complex Formatting - Nested Data (5 points)
# ==========================================
# TODO:
#   Function Name: summarize_inventory
#   Parameters:
#       warehouse_data (list): List of dictionaries with keys:
#           - "id" (str)
#           - "stock" (list of int)
#   Returns:
#       list: List of strings
#   Description:
#       For each warehouse, compute the sum of quantities in "stock".
#       Return a list of strings in EXACT format:
#           "Warehouse {id}: Total Items = {sum_of_quantities}"
#       Use map() and sum().
#   IMPORTANT:
#       Output string format must match exactly.
#       Function name MUST be exactly "summarize_inventory".
def summarize_inventory(warehouse_data):
    return list(map(lambda w: f"Warehouse {w['id']}: Total Items = {sum(w['stock'])}", warehouse_data))


# ==========================================
# DO NOT MODIFY BELOW THIS LINE
# ==========================================
if __name__ == "__main__":
    print("Run 'python test_lab7.py' to test your solutions!")
