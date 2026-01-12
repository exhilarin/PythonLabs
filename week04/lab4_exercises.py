# ==========================================
# LAB 4: FUNCTIONS AND WEB DATA PROCESSING
# Advanced Python Course - Week 7
# ==========================================
# 
# INSTRUCTIONS:
# - Complete each exercise function below
# - Do not change function names or parameters
# - Test your code by running: python test_lab4.py
# - Submit by pushing to your GitHub repository
# 
# SKILLS PRACTICED:
# - Writing reusable functions
# - Processing string data from web sources
# - Parsing JSON responses
# - Data cleaning and validation
# ==========================================

import json

# ==========================================
# SECTION A: STRING PROCESSING BASICS (14 points)
# Easy exercises - building blocks for web data processing
# ==========================================

# ==========================================
# EXERCISE 1: Extract Domain from URL (2 points)
# ==========================================
def extract_domain(url):
    """
    Extract the domain name from a URL.
    
    Args:
        url (str): A URL string like "https://www.example.com/page"
    
    Returns:
        str: Just the domain, e.g., "example.com"
    
    Example:
        extract_domain("https://www.example.com/page") returns "example.com"
        extract_domain("http://api.github.com/users") returns "api.github.com"
    
    Hint: Use .split() to break the URL into parts
    """
    # TODO: Remove protocol (http:// or https://), remove www., remove path
    # HINT: Split by "//" first, then by "/", handle "www." prefix
    
    # This template is intentionally incomplete - you need to add logic
    wrong_variable = ""  # Intentional: wrong variable name
    without_protocol = url.split("://")[-1]
    domain = without_protocol.split("/")[0]
    return domain  # This will error - you need to define 'domain'


# ==========================================
# EXERCISE 2: Parse Query Parameters (2 points)
# ==========================================
def parse_query_params(url):
    """
    Extract query parameters from a URL as a dictionary.
    
    Args:
        url (str): URL with query string like "https://api.com/search?q=python&page=2"
    
    Returns:
        dict: Query parameters, e.g., {"q": "python", "page": "2"}
    
    Example:
        parse_query_params("https://api.com/search?q=python&page=2")
        returns {"q": "python", "page": "2"}
    
    Hint: Split by "?" to separate query string, then split by "&" and "="
    """
    # TODO: Extract everything after "?", split by "&", then split each by "="
    params = {}
    if "?" in url:
        query = url.split("?")[-1]
        pair = query.split("&")
        for param in pair:
            if "=" in param:
                params[param.split("=")[0]] = param.split("=")[-1]
    return params


# ==========================================
# EXERCISE 3: Count Keyword Occurrences (2 points)
# ==========================================
def count_keyword(text, keyword):
    """
    Count how many times a keyword appears in text (case-insensitive).
    
    Args:
        text (str): Text to search in
        keyword (str): Word to count
    
    Returns:
        int: Number of occurrences
    
    Example:
        count_keyword("Python is great. Python is powerful.", "python") returns 2
        count_keyword("Hello world", "goodbye") returns 0
    
    Hint: Convert both to lowercase, use .count() or loop through .split()
    """
    # TODO: Make case-insensitive comparison
    counter = 0
    keyword = keyword.lower()
    text = text.lower()
    counter = text.count(keyword)
    return counter


# ==========================================
# EXERCISE 4: Clean Response Data (2 points)
# ==========================================
def clean_response(response_text):
    """
    Clean whitespace from API response text.
    Remove leading/trailing spaces and normalize internal whitespace.
    
    Args:
        response_text (str): Raw response with extra whitespace
    
    Returns:
        str: Cleaned text with single spaces
    
    Example:
        clean_response("  Hello    World  ") returns "Hello World"
        clean_response("Too   many    spaces") returns "Too many spaces"
    
    Hint: .strip() for edges, .split() and .join() for internal spaces
    """
    # TODO: Remove leading/trailing whitespace and collapse multiple spaces
    return (" ".join(response_text.strip().split()))


# ==========================================
# EXERCISE 5: Extract Status Code (2 points)
# ==========================================
def extract_status_code(response_header):
    """
    Extract HTTP status code from a response header string.
    
    Args:
        response_header (str): Header like "HTTP/1.1 200 OK" or "HTTP/1.1 404 Not Found"
    
    Returns:
        int: The status code (200, 404, etc.)
    
    Example:
        extract_status_code("HTTP/1.1 200 OK") returns 200
        extract_status_code("HTTP/1.1 404 Not Found") returns 404
    
    Hint: Split by spaces, the code is usually the second element
    """
    # TODO: Split the header and extract the numeric code
    parts = response_header.split()
    code = int(parts[1])
    
    return code


# ==========================================
# EXERCISE 6: Format Timestamp (2 points)
# ==========================================
def format_timestamp(timestamp_str):
    """
    Convert timestamp string from "2024-03-15T14:30:00" to "2024-03-15 14:30".
    
    Args:
        timestamp_str (str): ISO format timestamp
    
    Returns:
        str: Formatted as "YYYY-MM-DD HH:MM"
    
    Example:
        format_timestamp("2024-03-15T14:30:00") returns "2024-03-15 14:30"
        format_timestamp("2024-12-25T09:15:30") returns "2024-12-25 09:15"
    
    Hint: Use .split() to separate date and time, then rejoin
    """
    # TODO: Split by "T", split time by ":", reconstruct format
    
    # Intentional: overly complex template
    date_part = timestamp_str.strip().split("T")[0]
    time_part = ":".join((timestamp_str.strip().split("T")[-1]).split(":")[:2])

    return (f"{date_part} {time_part}")


# ==========================================
# EXERCISE 7: Simple Email Validation (2 points)
# ==========================================
def is_valid_email(email):
    """
    Check if email string has basic valid format (contains @ and .).
    
    Args:
        email (str): Email address to validate
    
    Returns:
        bool: True if valid format, False otherwise
    
    Example:
        is_valid_email("user@example.com") returns True
        is_valid_email("invalid.email") returns False
        is_valid_email("no@domain") returns False
    
    Hint: Check for "@", check for "." after "@", check length > 5
    """
    # TODO: Validate email has @ and . in correct positions
    if len(email) <= 5:
        return False
    if "@" not in email:
        return False
    at_index = email.index(".", 0)
    if "." not in email[at_index:]:
        return False
    return True


# ==========================================
# SECTION B: JSON DATA PROCESSING (15 points)
# Medium exercises - working with structured data
# ==========================================

# ==========================================
# EXERCISE 8: Parse Simple JSON (3 points)
# ==========================================
def get_json_value(json_string, key):
    """
    Parse JSON string and return the value for a given key.
    
    Args:
        json_string (str): JSON formatted string
        key (str): Key to look up
    
    Returns:
        any: Value associated with key, or None if key not found
    
    Example:
        get_json_value('{"name": "Alice", "age": 25}', "name") returns "Alice"
        get_json_value('{"status": "success"}', "status") returns "success"
        get_json_value('{"x": 10}', "y") returns None
    
    Hint: Use json.loads() to parse, then dictionary access with .get()
    """
    # TODO: Parse JSON and extract value safely
    data = json.loads(json_string)
    if key in data.keys():
        return data[key]
    else:
        return None

# ==========================================
# EXERCISE 9: Parse Nested JSON (3 points)
# ==========================================
def get_nested_value(json_string, outer_key, inner_key):
    """
    Extract value from nested JSON structure.
    
    Args:
        json_string (str): JSON with nested objects
        outer_key (str): First level key
        inner_key (str): Second level key
    
    Returns:
        any: Value at nested location, or None if path doesn't exist
    
    Example:
        get_nested_value('{"user": {"name": "Bob", "age": 30}}', "user", "name")
        returns "Bob"
    
    Hint: Parse JSON, check outer_key exists, check inner_key exists in nested dict
    """
    # TODO: Safely navigate nested structure
    data = json.loads(json_string)
    if outer_key in data.keys():
        if inner_key in data.get(outer_key):
            return data[outer_key][inner_key]
    return None


# ==========================================
# EXERCISE 10: Count JSON Array Items (3 points)
# ==========================================
def count_json_items(json_string, array_key):
    """
    Count the number of items in a JSON array.
    
    Args:
        json_string (str): JSON with an array
        array_key (str): Key that contains the array
    
    Returns:
        int: Number of items in array, or 0 if key not found or not an array
    
    Example:
        count_json_items('{"users": ["Alice", "Bob", "Charlie"]}', "users") returns 3
        count_json_items('{"items": [1, 2, 3, 4, 5]}', "items") returns 5
    
    Hint: Parse JSON, check key exists, check value is list, return len()
    """
    # TODO: Parse JSON, validate array, count items
    
    data = json.loads(json_string)
    if array_key in data.keys():
        return len(data[array_key])
    return 0


# ==========================================
# EXERCISE 11: Extract All Values for Key (3 points)
# ==========================================
def extract_all_values(json_string, key):
    """
    From a JSON array of objects, extract all values for a specific key.
    
    Args:
        json_string (str): JSON array of objects
        key (str): Key to extract from each object
    
    Returns:
        list: All values for that key from all objects
    
    Example:
        extract_all_values('[{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]', "name")
        returns ["Alice", "Bob"]
    
    Hint: Parse JSON array, loop through objects, collect values for key
    """
    # TODO: Parse JSON array and extract key from each object
    
    data = json.loads(json_string)
    results = []
    for item in data:
        if key in item.keys():
            results.append(item[key])
    return results


# ==========================================
# EXERCISE 12: Calculate Average from JSON (3 points)
# ==========================================
def calculate_json_average(json_string, key):
    """
    Calculate the average of numeric values for a key across JSON array of objects.
    
    Args:
        json_string (str): JSON array of objects with numeric values
        key (str): Key containing numbers to average
    
    Returns:
        float: Average value, or 0.0 if no valid numbers
    
    Example:
        calculate_json_average('[{"score": 85}, {"score": 90}, {"score": 78}]', "score")
        returns 84.33 (approximately)
    
    Hint: Extract all values for key, sum them, divide by count
    """
    # TODO: Extract numeric values and calculate average
    data = json.loads(json_string)
    total = 0
    count = 0
    for item in data:
        if key in item:
            total += item[key]
            count += 1
    return total / count


# ==========================================
# SECTION C: DATA CLEANING & INTEGRATION (15 points)
# Hard exercises - handling messy real-world data
# ==========================================

# ==========================================
# EXERCISE 13: Fix Broken JSON (5 points)
# ==========================================
def fix_json(broken_json):
    """
    Fix common JSON formatting errors:
    - Remove trailing commas before closing braces/brackets
    - Handle single quotes instead of double quotes for keys
    
    Args:
        broken_json (str): JSON with common formatting issues
    
    Returns:
        dict: Parsed JSON object (return the actual dict, not string)
    
    Example:
        fix_json("{'name': 'Alice', 'age': 25,}") 
        returns {"name": "Alice", "age": 25}
    
    Hint: Use .replace() for fixing quotes and commas before parsing
    """
    # TODO: Fix common JSON issues before parsing
    fixed = broken_json.replace("'", '"')
    fixed = fixed.replace(",}", "}")
    fixed = fixed.replace(",]", "]")
    return json.loads(fixed)


# ==========================================
# EXERCISE 14: Parse CSV-Like String (5 points)
# ==========================================
def parse_csv_string(csv_string):
    """
    Parse a CSV-formatted string into a list of dictionaries.
    First line is headers, subsequent lines are data.
    
    Args:
        csv_string (str): CSV formatted data with headers
    
    Returns:
        list: List of dictionaries, each representing one row
    
    Example:
        parse_csv_string("name,age,city\nAlice,25,NYC\nBob,30,LA")
        returns [
            {"name": "Alice", "age": "25", "city": "NYC"},
            {"name": "Bob", "age": "30", "city": "LA"}
        ]
    
    Hint: Split by newlines, first line is headers, map remaining lines to dicts
    """
    # TODO: Parse CSV format into structured data
    lines = csv_string.split('\n')
    headers = lines[0].split(',')
    results = []
    
    for line in lines[1:]:
        if not line.strip():
            continue
        values = line.split(',')
        row_dict = {}
        for i in range(len(headers)):
            row_dict[headers[i]] = values[i]
        results.append(row_dict)
    
    return results


# ==========================================
# EXERCISE 15: Process Mixed API Response (5 points)
# ==========================================
def process_api_response(response_string):
    """
    Process a complex API response containing multiple data types.
    Response format: "STATUS: 200 | DATA: {json_here} | COUNT: 42"
    
    Args:
        response_string (str): Mixed format response string
    
    Returns:
        dict: {
            "status": int (the status code),
            "data": dict (parsed JSON),
            "count": int (the count value)
        }
    
    Example:
        process_api_response('STATUS: 200 | DATA: {"success": true} | COUNT: 5')
        returns {
            "status": 200,
            "data": {"success": True},
            "count": 5
        }
    
    Hint: Split by " | ", process each part separately, combine results
    """
    # TODO: Parse complex mixed-format response
    result = {
        "status": None,
        "data": None,
        "count": None
    }
    parts = response_string.split(" | ")
    for part in parts:
        key, value = part.split(": ", 1)
        if key == "STATUS":
            result["status"] = int(value)
        elif key == "DATA":
            result["data"] = json.loads(value)
        elif key == "COUNT":
            result["count"] = int(value)
    return result


# ==========================================
# DO NOT MODIFY BELOW THIS LINE
# ==========================================
if __name__ == "__main__":
    print("Run 'python test_lab4.py' to test your solutions!")
    print("\nQuick self-test examples:")
    print("=" * 50)
    
    # Test Exercise 1
    try:
        domain = extract_domain("https://www.example.com/page")
        print(f"Exercise 1: {domain}")
    except Exception as e:
        print(f"Exercise 1 Error: {e}")
    
    # Test Exercise 8
    try:
        value = get_json_value('{"name": "Alice"}', "name")
        print(f"Exercise 8: {value}")
    except Exception as e:
        print(f"Exercise 8 Error: {e}")
    
    print("=" * 50)
    print("\nFix the errors above, then run: python test_lab4.py")
