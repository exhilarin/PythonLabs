# ==========================================
# LAB 3: FUNCTIONS, DICTIONARIES, AND DATA STRUCTURES
# Advanced Python Course - Week 3
# ==========================================
#
# INSTRUCTIONS:
# - Section A: Complete the function bodies (skeleton provided)
# - Section B & C: Write entire functions from scratch
# - Function names MUST match exactly or tests will fail
# - Test your code by running: python test_lab3.py
# - Submit by pushing to your GitHub repository
# ==========================================

# ==========================================
# SECTION A: FUNCTIONS WITH GUIDANCE (6 points)
# Function skeleton provided - fill in the body
# ==========================================

# ==========================================
# EXERCISE 1: Temperature Converter (2 points)
# ==========================================
def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.

    Formula: Fahrenheit is Celsius x 9/5 + 32

    Args:
        Celsius (float): Temperature in Celsius

    Returns:
        float: Temperature in Fahrenheit

    Example:
        celsius_to_fahrenheit(0) returns 32.0
        celsius_to_fahrenheit(100) returns 212.0
    """
    fahrenheit = 0
    fahrenheit = (celsius * 9/5) + 32

    return fahrenheit


# ==========================================
# EXERCISE 2: Dictionary Lookup with Default (2 points)
# ==========================================
def get_student_grade(grades, student_name):
    """
    Get a student's grade from the grades' dictionary.
    If student not found, return 0.

    Args:
        grades (dict): Dictionary with student names as keys, grades as values
        student_name (str): Name of student to look up

    Returns:
        int: Student's grade, or 0 if not found

    Example:
        grades = {"Alice": 85, "Bob": 92}
        get_student_grade(grades, "Alice") returns 85
        get_student_grade(grades, "Charlie") returns 0
    """
    # HINT: dictionary.get(key, default_value)
    grade = grades.get(student_name, 0)
    return grade


# ==========================================
# EXERCISE 3: Format Person Information (2 points)
# ==========================================
def format_person(name, age, city):
    """
    Create a formatted string with person's information.

    Format: "Name: {name}, Age: {age}, City: {city}"

    Args:
        name (str): Person's name
        age (int): Person's age
        city (str): Person's city

    Returns:
        str: Formatted information string

    Example:
        format_person("Alice", 25, "Boston")
        returns "Name: Alice, Age: 25, City: Boston"
    """
    # HINT: f"{variable}"

    formatted = f"Name: {name}, Age: {age}, City: {city}"
    return formatted


# ==========================================
# SECTION B: WRITE COMPLETE FUNCTIONS (16 points)
# Write the entire function from scratch
# ==========================================

# ==========================================
# EXERCISE 4: Calculate Average (2 points)
# ==========================================
# Write a function called 'calculate_average' that:
# - Takes a list of numbers as parameter
# - Returns the average (sum divided by count)
#
# Function signature: def calculate_average(numbers):
# Parameter: numbers (list of int/float)
# Returns: float (the average)
#
# Example:
#   calculate_average([10, 20, 30]) returns 20.0
#   calculate_average([5, 10, 15, 20]) returns 12.5
#
# Hints:
# - Use sum() to add all numbers
# - Use len() to count numbers

# TODO: Write the complete calculate_average function here

def calculate_average(numbers):
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


# ==========================================
# EXERCISE 5: Clean Filename (2 points)
# ==========================================
# Write a function called 'clean_filename' that:
# - Takes a filename string as parameter
# - Strips whitespace from both ends
# - Converts to lowercase
# - Returns the cleaned filename
#
# Function signature: def clean_filename(filename):
# Parameter: filename (str)
# Returns: str (cleaned filename)
#
# Example:
#   clean_filename("  MyFile.TXT  ") returns "myfile.txt"
#   clean_filename("REPORT.PDF") returns "report.pdf"
#
# Hints:
# - Use .strip() to remove whitespace
# - Use .lower() to convert to lowercase

# TODO: Write the complete clean_filename function here

def clean_filename(filename):
    return filename.strip().lower()

# ==========================================
# EXERCISE 6: Count File Extensions (3 points)
# ==========================================
# Write a function called 'count_extensions' that:
# - Takes a list of filenames
# - Returns a dictionary counting how many files have each extension
# - Extension is the part after the last dot (e.g., "txt" from "file.txt")
#
# Function signature: def count_extensions(filenames):
# Parameter: filenames (list of str)
# Returns: dict with extensions as keys, counts as values
#
# Example:
#   count_extensions(["a.txt", "b.txt", "c.jpg"])
#   returns {"txt": 2, "jpg": 1}
#
# Hints:
# - Loop through each filename
# - Use .split([delimiter]) to split. for example "a-b-c".split("-") returns ['a', 'b', 'c']
# - Use an empty dictionary to store counts
# - Initialize count to 0 if extension was not in dictionary

# TODO: Write the complete count_extensions function here

def count_extensions(filenames):
    counts = {}
    for file in filenames:
        if "." in file:
            ext = file.split(".")[-1].lower()
            counts[ext] = counts.get(ext, 0) + 1
    return counts

# ==========================================
# EXERCISE 7: Filter Passing Students (3 points)
# ==========================================
# Write a function called 'filter_passing_students' that:
# - Takes a dictionary of student names and their scores
# - Returns a new dictionary with only students who scored 60 or above
#
# Function signature: def filter_passing_students(grades):
# Parameter: grades (dict with str keys, int values)
# Returns: dict with only passing students (score >= 60)
#
# Example:
#   filter_passing_students({"Alice": 85, "Bob": 45, "Charlie": 70})
#   returns {"Alice": 85, "Charlie": 70}

# TODO: Write the complete filter_passing_students function here

def filter_passing_students(grades):
    return {name: score for name, score in grades.items() if score >= 60}

# ==========================================
# EXERCISE 8: Analyze Numbers (3 points)
# ==========================================
# Write a function called 'analyze_numbers' that:
# - Takes a list of numbers
# - Returns a tuple containing (minimum, maximum, average)
#
# Function signature: def analyze_numbers(numbers):
# Parameter: numbers (list of int/float)
# Returns: tuple of (min, max, average)
#
# Example:
#   analyze_numbers([10, 50, 30, 70])
#   returns (10, 70, 40.0)

# TODO: Write the complete analyze_numbers function here

def analyze_numbers(numbers):
    if not numbers:
        return (None, None, None)
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)
    return (minimum, maximum, average)


# ==========================================
# EXERCISE 9: Read Numbers from File (3 points)
# ==========================================
# Write a function called 'read_numbers_from_file' that:
# - Takes a filename as parameter
# - Reads the file (one number per line)
# - Returns a list of integers
#
# Function signature: def read_numbers_from_file(filename):
# Parameter: filename (str)
# Returns: list of int
#
# Example:
#   If file contains:
#   5
#   10
#   15
#   Then read_numbers_from_file("file.txt") returns [5, 10, 15]
#
# Hints:
# - Use 'with open(filename) as f:' to open the file

# TODO: Write the complete read_numbers_from_file function here

def read_numbers_from_file(filename):
    numbers = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if line:
                numbers.append(int(line))
    return numbers

# ==========================================
# SECTION C: ADVANCED INTEGRATION (13 points)
# Complex functions combining multiple concepts
# ==========================================

# ==========================================
# EXERCISE 10: Shopping Cart Total (3 points)
# ==========================================
# Write a function called 'calculate_cart_total' that:
# - Takes a shopping cart dictionary
# - Each item in cart: key is item name, value is tuple of (price, quantity)
# - Returns the total cost (price × quantity for each item, summed)
#
# Function signature: def calculate_cart_total(cart):
# Parameter: cart (dict with str keys, tuple values of (float, int))
# Returns: float (total cost)
#
# Example:
#   cart = {
#       "apple": (1.5, 3),    # $1.50 each, quantity 3
#       "banana": (0.8, 5)    # $0.80 each, quantity 5
#   }
#   calculate_cart_total(cart) returns 8.5
#   Calculation: (1.5 × 3) + (0.8 × 5) = 4.5 + 4.0 = 8.5
#
# Hints:
# - Loop through cart.items() to get item name and (price, quantity) tuple
# - Unpack tuple: for item, (price, quantity) in cart.items():

# TODO: Write the complete calculate_cart_total function here

def calculate_cart_total(cart):
    total = 0.0
    for item, (price, quantity) in cart.items():
        total += price * quantity
    return total

# ==========================================
# EXERCISE 11: Generate Grade Report (5 points)
# ==========================================
# Write a function called 'generate_grade_report' that:
# - Takes a dictionary of student names and their numeric scores
# - Converts each score to a letter grade
# - Returns a formatted report string
#
# Grading scale:
#   A: 90-100
#   B: 80-89
#   C: 70-79
#   D: 60-69
#   F: below 60
#
# Function signature: def generate_grade_report(scores):
# Parameter: scores (dict with str keys, int values)
# Returns: str (formatted report with each student on a new line)
#
# Format for each line: "Student: {name}, Score: {score}, Grade: {letter}"
# Lines should be separated by newline character (\n)
#
# Example:
#   scores = {"Alice": 92, "Bob": 78, "Charlie": 85}
#   generate_grade_report(scores) returns:
#   "Student: Alice, Score: 92, Grade: A\nStudent: Bob, Score: 78, Grade: C\nStudent: Charlie, Score: 85, Grade: B"
#
# Hints:
# - You can use a list and .join() or build string with +=

# TODO: Write the complete generate_grade_report function here

def generate_grade_report(scores):
    def letter_grade(score):
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"

    report_lines = []
    for name, score in scores.items():
        report_lines.append(f"Student: {name}, Score: {score}, Grade: {letter_grade(score)}")
    return "\n".join(report_lines)

# ==========================================
# EXERCISE 12: Analyze Log File (5 points)
# ==========================================
# Write a function called 'analyze_log_file' that:
# - Reads a log file where each line is formatted as "LEVEL: message"
# - Returns a nested dictionary with statistics
#
# Function signature: def analyze_log_file(filename):
# Parameter: filename (str)
# Returns: dict with structure:
#   {
#       "total_lines": int,
#       "levels": {
#           "ERROR": count,
#           "WARNING": count,
#           "INFO": count
#       }
#   }
#
# Example:
#   If log.txt contains:
#   ERROR: Connection failed
#   INFO: Server started
#   ERROR: Timeout occurred
#   WARNING: Low memory
#
#   analyze_log_file("log.txt") returns:
#   {
#       "total_lines": 4,
#       "levels": {
#           "ERROR": 2,
#           "INFO": 1,
#           "WARNING": 1
#       }
#   }
#
# Hints:
# - Split each line by ": " to separate level and message
# - Some levels might not appear in file - keep count at 0

# TODO: Write the complete analyze_log_file function here

def analyze_log_file(filename):
    levels_count = {"ERROR": 0, "WARNING": 0, "INFO": 0}
    total_lines = 0
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            total_lines += 1
            if ": " in line:
                level, _ = line.split(": ", 1)
                level = level.upper()
                if level in levels_count:
                    levels_count[level] += 1
    return {"total_lines": total_lines, "levels": levels_count}

# ==========================================
# DO NOT MODIFY BELOW THIS LINE
# ==========================================
if __name__ == "__main__":
    print("Run 'python test_lab3.py' to test your solutions!")