# ==========================================
# LAB 2: LISTS, LOOPS, AND FILE OPERATIONS
# Advanced Python Course - Week 2
# ==========================================
# 
# INSTRUCTIONS:
# - Complete each exercise function below
# - Do not change function names or parameters
# - Test your code by running: python test_lab2.py
# - Submit by pushing to your GitHub repository
# ==========================================

# ==========================================
# SECTION A: LISTS BASICS (25 points)
# ==========================================

# ==========================================
# EXERCISE 1: Create a Shopping List (4 points)
# ==========================================
def exercise1():
    """
    Create a list containing exactly 5 shopping items (strings).
    
    Returns:
        list: A list with 5 string items
    
    Example:
        ['milk', 'eggs', 'bread', 'cheese', 'apples']
    """
    # TODO: Create any list with 5 shopping items
    # HINT: Make sure that the list contains exactly 5 "string" elements not integers.
    shopping_list = ["milk", "eggs", "bread", "cheese", "apples"]
    
    return shopping_list


# ==========================================
# EXERCISE 2: Access List Elements (4 points)
# ==========================================
def exercise2(items):
    """
    Given a list, return the first element, last element, and third element.
    
    Args:
        items (list): A list with at least 3 elements
    
    Returns:
        list: [first_element, last_element, third_element]
    
    Example:
        exercise2(['a', 'b', 'c', 'd', 'e']) returns ['a', 'e', 'c']
    """
    # TODO: Access the correct elements using indexing
    # HINT: Remember you return a list with the three elements in order.
    # You can do it multiple ways, but make sure to follow the order in the return.
    # You access the elements of the input list 'items' and store them in 'result' list.

    result = [items[0], items[-1], items[2]]
    
    return result


# ==========================================
# EXERCISE 3: List Length and Membership (5 points)
# ==========================================
def exercise3(items, search_item):
    """
    Return the count of items in the list and whether search_item exists in it.
    
    Args:
        items (list): A list of items
        search_item: Item to search for
    
    Returns:
        dict: {'count': int, 'found': bool}
    
    Example:
        exercise3(['apple', 'banana', 'cherry'], 'banana') 
        returns {'count': 3, 'found': True}
    """
    # TODO: Use len() and 'in' operator
    # HINT: You use dictionary if you want to return multiple values.
    # Don't change the return statement structure.

    count = 0
    found = False

    count = len(items)
    found = search_item in items
    
    return {'count': count, 'found': found}


# ==========================================
# EXERCISE 4: Append Items (6 points)
# ==========================================
def exercise4(items, item1, item2):
    """
    Append two items to the end of the list and return the modified list.
    
    Args:
        items (list): Original list
        item1: First item to append
        item2: Second item to append
    
    Returns:
        list: Modified list with both items appended
    
    Example:
        exercise4(['a', 'b'], 'c', 'd') returns ['a', 'b', 'c', 'd']
    """
    # TODO: Use .append() to add both items
    items.append(item1)
    items.append(item2)
    return items


# ==========================================
# EXERCISE 5: Insert at Position (6 points)
# ==========================================
def exercise5(items, new_item, position):
    """
    Insert new_item at the specified position in the list.
    
    Args:
        items (list): Original list
        new_item: Item to insert
        position (int): Index where item should be inserted
    
    Returns:
        list: Modified list with item inserted
    
    Example:
        exercise5(['a', 'b', 'd', 'e'], 'c', 2) returns ['a', 'b', 'c', 'd', 'e']
    """
    # TODO: Use .insert() to add item at position
    items.insert(position, new_item)
    return items


# ==========================================
# SECTION B: LOOPS WITH LISTS (25 points)
# ==========================================

# ==========================================
# EXERCISE 6: Collect All Items (4 points)
# ==========================================
def exercise6(items):
    """
    Loop through the list and create a new list where each item 
    is formatted as "Item: {name}".
    
    Args:
        items (list): List of item names
    
    Returns:
        list: List of formatted strings
    
    Example:
        exercise6(['apple', 'banana', 'cherry']) 
        returns ['Item: apple', 'Item: banana', 'Item: cherry']
    """
    # TODO: Use a for loop to create formatted strings
    # HINT: How do you combine (concat) strings with variables?
    result = []
    for item in items:
        result.append(f"Item: {item}")
    
    return result


# ==========================================
# EXERCISE 7: Sum All Numbers (5 points)
# ==========================================
def exercise7(numbers):
    """
    Calculate the sum of all numbers in the list using a loop.
    Do NOT use the built-in sum() function.
    
    Args:
        numbers (list): List of numbers
    
    Returns:
        int or float: Sum of all numbers
    
    Example:
        exercise7([10, 20, 30, 40]) returns 100
    """
    # TODO: Use accumulator pattern with a loop
    total = 0
    for number in numbers :
        total += number
    
    return total


# ==========================================
# EXERCISE 8: Count Specific Value (5 points)
# ==========================================
def exercise8(items, target):
    """
    Count how many times target appears in the list using a loop.
    Do NOT use the built-in .count() method.
    
    Args:
        items (list): List of items
        target: Value to count
    
    Returns:
        int: Number of times target appears
    
    Example:
        exercise8([1, 2, 3, 2, 4, 2], 2) returns 3
    """
    # TODO: Use a loop with a counter
    count = 0
    for item in items :
        if item == target :
            count += 1
    
    return count


# ==========================================
# EXERCISE 9: Filter by Threshold (6 points)
# ==========================================
def exercise9(numbers, threshold):
    """
    Create a new list containing only numbers greater than threshold.
    
    Args:
        numbers (list): List of numbers
        threshold (int or float): Threshold value
    
    Returns:
        list: Numbers greater than threshold
    
    Example:
        exercise9([10, 55, 30, 75, 20], 40) returns [55, 75]
    """
    # TODO: Use loop with conditional to build new list
    result = []
    for number in numbers:
        if number > threshold:
            result.append(number)

    return result


# ==========================================
# EXERCISE 10: Generate Number List (5 points)
# ==========================================
def exercise10(start, end):
    """
    Create a list of numbers from start to end (inclusive) using range().
    
    Args:
        start (int): Starting number
        end (int): Ending number (inclusive)
    
    Returns:
        list: List of numbers from start to end
    
    Example:
        exercise10(5, 10) returns [5, 6, 7, 8, 9, 10]
    """
    # TODO: Use range() and convert to list
    # HINT: you convert a range to a list using list(range(...))

    result = []
    for number in range(start, end + 1) :
        result.append(number)

    return result


# ==========================================
# SECTION C: FILE OPERATIONS (20 points)
# ==========================================

# ==========================================
# EXERCISE 11: Read Entire File (4 points)
# ==========================================
def exercise11(filename):
    """
    Read the entire contents of a text file and return as a string.
    
    Args:
        filename (str): Name of file to read
    
    Returns:
        str: Contents of the file
    
    Example:
        If file contains "Hello\nWorld", returns "Hello\nWorld"
    """
    # TODO: Use 'with open()' to read file
    content = ""
    with open(filename, 'r') as file:
        content = file.read()
    
    return content


# ==========================================
# EXERCISE 12: Count Lines (5 points)
# ==========================================
def exercise12(filename):
    """
    Read a file and count the total number of lines.
    
    Args:
        filename (str): Name of file to read
    
    Returns:
        int: Number of lines in the file
    
    Example:
        If file has 5 lines, returns 5
    """
    # TODO: Read file line by line and count
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            count += 1
    
    return count


# ==========================================
# EXERCISE 13: Parse Numbers from File (5 points)
# ==========================================
def exercise13(filename):
    """
    Read a file containing numbers (one per line) and return list of integers.
    
    Args:
        filename (str): Name of file with numbers
    
    Returns:
        list: List of integers from the file
    
    Example:
        If file contains "42\n17\n93", returns [42, 17, 93]
    """
    # TODO: Read file, convert each line to int, and collect in list
    numbers = []
    with open(filename, 'r') as file :
        for line in file :
            line = line.strip()
            if line :
                numbers.append(int(line))
    return numbers

# ==========================================
# EXERCISE 14: Write List to File (6 points)
# ==========================================
def exercise14(filename, items):
    """
    Write a list of strings to a file, one item per line.
    
    Args:
        filename (str): Name of file to write
        items (list): List of strings to write
    
    Returns:
        str: "Success" if file written successfully
    
    Example:
        exercise14('output.txt', ['apple', 'banana']) creates file with:
        apple
        banana
    """
    # TODO: Use 'with open()' in write mode to write each item
    # HINT: how do you combine a string and a newline character?
    with open(filename, 'w') as file :
        for item in items :
            file.write(item + "\n")
    return "Success"


# ==========================================
# SECTION D: INTEGRATION (10 points)
# ==========================================

# ==========================================
# EXERCISE 15: Filter File Numbers (5 points)
# ==========================================
def exercise15(filename, threshold):
    """
    Read numbers from a file and return only those greater than threshold.
    
    Args:
        filename (str): Name of file with numbers (one per line)
        threshold (int): Threshold value
    
    Returns:
        list: Numbers from file that are greater than threshold
    
    Example:
        If file contains [42, 17, 93, 28] and threshold is 50,
        returns [93]
    """
    # TODO: Read file, parse numbers, filter, and return result
    result = []
    with open(filename, "r") as file:
        for line in file :
            line = line.strip()
            if line :
                 number = int(line)
                 if number > threshold :
                    result.append(number)
    return result


# ==========================================
# EXERCISE 16: Count Words Starting With Letter (5 points)
# ==========================================
def exercise16(filename, letter):
    """
    Read words from a file (one per line) and count how many start 
    with the given letter (case-insensitive).
    
    Args:
        filename (str): Name of file with words
        letter (str): Letter to search for (single character)
    
    Returns:
        int: Count of words starting with letter
    
    Example:
        If file contains ['apple', 'Apricot', 'banana', 'Avocado']
        and letter is 'a', returns 3
    """
    # TODO: Read file, check first letter of each word (case-insensitive)
    # HINT: To lowercase a string, use str.lower() for example: letter.lower()
    # HINT: To check if a string starts with a letter, use str.startswith(),
    # for example: word.startswith(letter)
    count = 0
    letter = letter.lower()
    with open (filename, "r") as file :
        for line in file :
            word = line.strip()
            if word.lower().startswith(letter) :
                count += 1
    return count


# ==========================================
# DO NOT MODIFY BELOW THIS LINE
# ==========================================
if __name__ == "__main__":
    print("Run 'python test_lab2.py' to test your solutions!")
