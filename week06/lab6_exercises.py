# ==========================================
# LAB 6: OBJECT-ORIENTED PROGRAMMING (OOP)
# Advanced Python Course - Week 6
# ==========================================
# 
# INSTRUCTIONS:
# - Use only basic Python and OOP concepts
# - NO external libraries (only built-in)
# - NO advanced Python features unless specified
# - Complete each exercise below
# - Test with: python test_lab6.py
# 
# TOTAL POINTS: 44
# ==========================================

# ==========================================
# SECTION A: EASY - BASIC CONCEPTS (12 points)
# 3 reminders + 3 OOP fundamentals (2 points each)
# ==========================================

# ==========================================
# EXERCISE 1: Week 4 Reminder - String Processing (2 points)
# ==========================================
def clean_filename(filename):
    """
    Given a filename string, clean it by removing any leading/trailing whitespace
    and converting all alphabetical characters to lowercase.
    The function should handle edge cases such as strings that are empty or consist only of spaces.

    Args:
        filename (str): The raw filename provided by the user.

    Returns:
        str: The cleaned filename.
    """
    # TODO: Implement the cleaning logic using basic string methods.
    #Important: Function name MUST be 'clean_filename'.
    return(filename.strip().lower())


# ==========================================
# EXERCISE 2: Week 5 Reminder - Dictionary Operations (2 points)
# ==========================================
def merge_dicts(dict1, dict2):
    """
    Merge two dictionaries into a new dictionary.
    If a key exists in both dictionaries, the value from dict2 should be used.
    The original dictionaries must not be modified.

    Args:
        dict1 (dict): The first dictionary.
        dict2 (dict): The second dictionary.

    Returns:
        dict: A new dictionary containing the merged key-value pairs.
    """
    # TODO: Implement the merge without modifying the original dictionaries.
    # IMPORTANT: Function name MUST be exactly "merge_dicts"
    # Hint: Consider how to create a new dictionary and combine key-value pairs.
    dicts = dict1.copy()
    dicts.update(dict2)
    return dicts


# ==========================================
# EXERCISE 3: Week 5 Reminder - Filter List (2 points)
# ==========================================
def filter_by_length(strings, min_len):
    """
    Return a new list containing only the strings whose length is  
    greater than OR EQUAL TO the specified minimum length.

    The original list must not be modified, and the order of elements
    must be preserved.

    Args:
        strings (list): A list of strings.
        min_len (int): The minimum acceptable length for a string.

    Returns:
        list: A new list containing the filtered strings.
    """
    # TODO: Implement the filter. Ensure the original list remains unchanged.
    # IMPORTANT: Function name MUST be exactly "filter_by_length"
    ret = []
    for item in strings:
        if len(item) >= min_len:
            ret.append(item)
    return ret


# ==========================================
# EXERCISE 4: Week 6 - Simple Class (2 points)
# ==========================================
# TODO: Create a Person class from scratch.
# IMPORTANT: You MUST use EXACTLY these names:
# - Class name: Person
# - Method names: __init__, get_info
# - Attribute names: name, age
#
# Requirements:
#   1. An __init__(self, name, age) method that stores the provided name and age
#      in instance attributes named exactly 'name' and 'age'.
#   2. A method named get_info(self) that returns a string in the exact format:
#      "Name: {name}, Age: {age}"
# 
# Student writes the class here
class Person:
    def __init__(self, name, age):
       self.name = name
       self.age = age

    def get_info(self):
       return (f"Name: {self.name}, Age: {self.age}")



# ==========================================
# EXERCISE 5: Week 6 - Basic Inheritance (2 points)
# ==========================================
# TODO: In this exercise, create TWO classes from scratch:
# IMPORTANT: You MUST use EXACTLY these names:
# - Class names: Shape, Circle
# - Method names: __init__, get_info
# - Attribute names for Shape: color
# - Attribute names for Circle: color, radius

# Requirements:
# 1. Shape class with:
#    - __init__(self, color) method that stores color as instance attribute
#    - get_info(self) method that returns a string: "Shape color: {color}"
#
# 2. Circle class that INHERITS from Shape:
#    - __init__(self, color, radius) method
#    - Must use super() to initialize the color attribute from parent class
#    - Add radius instance attribute
#    - Override get_info() method to return:
#      "Circle color: {color}, Radius: {radius}"
#
# Important: Do not copy-paste code from Shape to Circle. Use proper inheritance.
# NOTE: This exercise is independent.
# If a Shape class was created in Exercise 4, DO NOT reuse it. You must rewrite a fresh Shape class here.
# Student writes both classes here

class Shape:
    def __init__(self, color):
        self.color = color
    def get_info(self):
        return (f"Shape color: {self.color}")

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    def get_info(self):
        return (f"Circle color: {self.color}, Radius: {self.radius}")


# ==========================================
# EXERCISE 6: Week 6 - Method Overriding (2 points)
# ==========================================
# TODO: Create two classes from scratch:
# IMPORTANT: You MUST use EXACTLY these names:
# - Class names: Device, Smartphone
# - Method names: get_sound
#
# Requirements:
# 1. Device class:
#    - Has a method called get_sound(self)
#    - The get_sound() method should not return any meaningful value.
#      (Use pass or return None)
#
# 2. Smartphone class:
#    - MUST inherit from Device
#    - MUST override the get_sound() method
#    - The overridden get_sound() method MUST return the exact string: "Ring!"
#
# Write both classes below. Do not include any test code.
class Device:
    def get_sound(self):
        return None
    
class Smartphone(Device):
    def get_sound(self):
        return "Ring!"


# ==========================================
# SECTION B: MEDIUM - BASIC OOP CONCEPTS (18 points)
# Core OOP principles (3 points each)
# ==========================================

# ==========================================
# EXERCISE 7: Create Simple Class (3 points)
# ==========================================
# TODO: Create a Product class from scratch for an e-commerce system.
# IMPORTANT: You MUST use EXACTLY these names:
# - Class name: Product
# - Method names: __init__, get_total_value, apply_discount
# - Attribute names: name, price, quantity
#
# Requirements:
#   1. __init__(self, name, price, quantity) method
#      - Stores name, price, and quantity as instance attributes.
#   
#   2. get_total_value(self) method
#      - Returns the total monetary value of the product.
#      - Total value = price × quantity
#   
#   3. apply_discount(self, percent) method
#      - Applies a percentage discount to the product's price.
#      - The discount should permanently reduce the price attribute.
#      - The percent parameter is an integer (e.g., 20 means 20%).
#
# Important: The class should handle its own state; methods should not
# require external calculations. All calculations must be done within
# the class methods.
# Write your Product class below:
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_value(self):
        return(self.price * self.quantity)

    def apply_discount(self, percent):
        self.price = self.price - (self.price * (percent / 100))



# ==========================================
# EXERCISE 8: Inheritance (3 points)
# ==========================================
# TODO: Create a clothing tracking system using inheritance.
# IMPORTANT: You MUST use EXACTLY these names:
# - Class names: ClothingItem, Shoe
# - Method names: __init__, calculate_price
# - Attribute names for ClothingItem: name, price, quantity
# - Attribute names for Shoe: name, price, quantity, brand, size
#
# IMPORTANT: This exercise is COMPLETELY INDEPENDENT from Exercise 7.
# You must create all classes from scratch here.
#
# Requirements:
# 1. ClothingItem class:
#    - __init__(self, name, price, quantity) method
#    - Stores name, price, and quantity as instance attributes
#    - calculate_price(self) method that returns price multiplied by quantity
#
# 2. Shoe class (inherits from ClothingItem):
#    - __init__(self, name, price, quantity, brand, size) method
#    - Must use super() to initialize name, price, and quantity from ClothingItem
#    - Adds two new instance attributes: brand and size
#    - Overrides the calculate_price() method
#    - Must return a value noticeably different from (price × quantity)
#    - (Example: adding a size-based surcharge such as +5 per size above 40, 
#      OR adding a brand premium)
#
# Note: Do not copy any code from Exercise 7. Write everything fresh.
# Write both classes below:
class ClothingItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def calculate_price(self):
        return(self.price * self.quantity)

class Shoe(ClothingItem):
    def __init__(self, name, price, quantity, brand, size):
        super().__init__(name, price, quantity)
        self.brand = brand
        self.size = size

    def calculate_price(self):
        total = self.price * self.quantity
        if self.size > 40:
            total += (self.size - 40) * 5 * self.quantity
        premium_brands = ["Nike", "Adidas", "Puma"]
        if self.brand in premium_brands:
            total += 10 * self.quantity
        return total


# ==========================================
# EXERCISE 9: Encapsulation (3 points)
# ==========================================
# TODO: Create a BankAccount class that demonstrates proper encapsulation.
# IMPORTANT: You MUST use EXACTLY these names:
# - Class name: BankAccount
# - Method names: __init__, deposit, withdraw, get_balance
# - Private attribute MUST be named __balance (double underscore, name-mangled)
#
# Requirements:
# 1. The balance should be stored as a private attribute named _balance
# 2. The class should have an __init__(self, initial_balance) method
# 3. It should have methods:
#    - deposit(self, amount): adds amount to balance
#    - withdraw(self, amount): subtracts amount from balance if sufficient funds
#    - get_balance(self): returns current balance
# 4. Withdrawals should only succeed if sufficient funds are available
# 5. The _balance attribute should not be directly accessible from outside
#
# Write your BankAccount class below:
class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance
    
    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def get_balance(self):
        return (self.__balance)


# ==========================================
# EXERCISE 10: Polymorphism (3 points)
# ==========================================
# TODO: Create a demonstration of polymorphism with animals.
# IMPORTANT: You MUST use EXACTLY these names:
# - Class names: AnimalBase, Dog, Cat
# - Method names: speak
# - Function name: animal_concert
#
# Requirements:
# 1. An AnimalBase class:
#    - Must have a speak(self) method.
#    - The base implementation should return an empty string "".
#
# 2. Two subclasses that inherit from AnimalBase:
#    - Dog class: speak() method returns exactly "Woof!"
#    - Cat class: speak() method returns exactly "Meow!"
#
# 3. A function named animal_concert(animals):
#    - Takes a single parameter: a list of AnimalBase objects.
#    - Returns a list of strings.
#    - Should call the speak() method on each object in the list.
#    - Should preserve the order of the input list.
#
# Important: All classes and the function must be written from scratch.
# NOTE: This exercise is independent from Exercise 6.
# You must rewrite the Dog class here from scratch.

# Write all your code below (classes and function):
class AnimalBase:
    def speak(self):
        return ""

class Dog(AnimalBase):
    def speak(self):
        return ("Woof!")

class Cat(AnimalBase):
    def speak(self):
        return ("Meow!")

def animal_concert(animals):
    sounds = []
    for animal in animals:
        sounds.append(animal.speak())
    return sounds


# ==========================================
# EXERCISE 11: Class Variables (3 points)
# ==========================================
# TODO: Create an Employee class that demonstrates the use of class variables.
# IMPORTANT: You MUST use EXACTLY these names:
# - Class name: Employee
# The class variable must NOT appear on any instance. It must exist only on the class.
# - Method names: __init__, get_total_employees (class method)
# - Attribute names: name, salary
#
# Requirements:
# 1. The class must have a class-level variable named _total_employees 
#    that tracks how many Employee instances have been created.
# 2. Each instance should store its own name and salary.
# 3. When a new Employee instance is created, _total_employees should increment.
# 4. Add a class method named get_total_employees() that returns the current count.
# 5. The class variable should be accessible at the class level.
#
# Write your Employee class below:
class Employee:
    _total_employees = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee._total_employees += 1

    @classmethod
    def get_total_employees(cls):
        return (cls._total_employees)
    


# ==========================================
# EXERCISE 12: String Representation (3 points)
# ==========================================
# TODO: Create a Point class that represents a 2D point with special string methods.
# IMPORTANT: You MUST use EXACTLY these names:
# - Class name: Point
# - Method names: __init__, __str__, __repr__
# - Attribute names: x, y
#
# Requirements:
# 1. An __init__(self, x, y) method that stores x and y coordinates.
# 2. A __str__(self) method that returns format: "Point at ({x}, {y})"
# 3. A __repr__(self) method that returns format: "Point({x}, {y})"
#
# Important notes about the special methods:
# - __str__ is called by str(), print(), and format() functions.
# - __repr__ is called by repr() and should ideally allow object recreation.
# - Both methods must return strings.
#
# Write your Point class below:
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return (f"Point at {self.x}, {self.y}")

    def __repr__(self):
        return (f"Point({self.x}, {self.y})")


# ==========================================
# SECTION C: HARD - ADVANCED OOP CONCEPTS (20 points)
# Advanced OOP principles (5 points each)
# ==========================================
 #==========================================
# EXERCISE 13: Encapsulation and Computed Property (5 points)
# ==========================================
# TODO: Create a Rectangle class that demonstrates strong encapsulation
# and computed properties.
# IMPORTANT: You MUST use EXACTLY these names:
# - Class name: Rectangle
# - Method names: __init__, set_dimensions, get_area, get_perimeter
# - Private attribute names: __width, __height
#
# Requirements:
# 1. The rectangle's dimensions should be stored as private attributes:
#    - __width (float/int)
#    - __height (float/int)
#
# 2. The class should have an __init__(self, width, height) method 
#    to set initial dimensions with validation.
#
# 3. It should have a method set_dimensions(self, width, height):
#    - Updates both dimensions at once
#    - Validates that width and height are positive numbers (> 0)
#    - If validation fails, the dimensions must NOT change (no exception).
#
# 4. It should have methods:
#    - get_area(self): returns area (width × height)
#    - get_perimeter(self): returns perimeter (2 × (width + height))
#
# 5. Validation should ensure dimensions are valid geometric values.
#
# Important: Focus on proper encapsulation. The internal representation
# should be hidden, and all interactions should go through the class methods.
#
# Write your Rectangle class below:
class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def set_dimensions(self, width, height):
        if width > 0 and height > 0:
            self.__width = width
            self.__height = height

    def get_area(self):
        return (self.__width * self.__height)

    def get_perimeter(self):
        return (2 * (self.__width + self.__height))



# ==========================================
# EXERCISE 14: Class Method for Tracking (5 points)
# ==========================================
# TODO: Create a Counter class that demonstrates the use of both
# class methods and static methods.
# IMPORTANT: You MUST use EXACTLY these names:
# - Class name: Counter
# - Class variable name: _count
# - Method names: __init__, get_instance_count, is_even (static method)
#
# Requirements:
# 1. It should track how many instances of Counter have been created,
#    using a class-level variable named _count.
#
# 2. It should provide a class method named get_instance_count that retrieves 
#    the current count of instances.
#
# 3. It should also provide a static method named is_even(number) that:
#    - Takes a number as parameter
#    - Returns True if the number is even, False otherwise
#    - Does not need access to any instance or class data
#
# Important: Pay attention to which methods should operate on the class
# versus which should be standalone utilities. Use @classmethod and @staticmethod
# decorators appropriately.
# NOTE: get_instance_count MUST work when called from both:
# - the class: Counter.get_instance_count()
# - and an instance: obj.get_instance_count()
#
# Write your Counter class below:
class Counter:
    _count = 0
    def __init__(self):
        Counter._count += 1
    
    @classmethod
    def get_instance_count(cls):
        return (cls._count)
    
    @staticmethod
    def is_even(number):
        return(number % 2 == 0)


# ==========================================
# EXERCISE 15: Inheritance and Method Chaining (5 points)
# ==========================================
# TODO: Create a Furniture class hierarchy demonstrating inheritance
# and method overriding with proper use of super().
# IMPORTANT: You MUST use EXACTLY these names:
# - Class names: Furniture, Chair
# - Method names: __init__, describe
# - Attribute names for Furniture: style, material
# - Attribute names for Chair: style, material, num_legs
#
# Requirements:
# 1. A Furniture base class with:
#    - An __init__(self, style, material) method
#    - A describe(self) method that returns format:
#      "Furniture: style={style}, material={material}"
#
# 2. A Chair class that inherits from Furniture:
#    - __init__(self, style, material, num_legs) method
#    - Must use super() to initialize style and material
#    - Adds num_legs instance attribute
#    - Overrides the describe() method to return format:
#      "Chair: style={style}, material={material}, legs={num_legs}"
#
# The exact string formats must match exactly as shown above.
# Focus on creating a logical class hierarchy where the child class 
# extends the parent class functionality.
#
# Write both classes below:
class Furniture:
    def __init__(self, style, material):
        self.style = style
        self.material = material

    def describe(self):
        return f"Furniture: style={self.style}, material={self.material}"

class Chair(Furniture):
    def __init__(self, style, material, num_legs):
        super().__init__(style, material)
        self.num_legs = num_legs

    def describe(self):
        return f"Chair: style={self.style}, material={self.material}, legs={self.num_legs}"


# ==========================================
# EXERCISE 16: Composition over Inheritance (5 points)
# ==========================================
# TODO: Create a system demonstrating the "composition over inheritance" principle.
# IMPORTANT: You MUST use EXACTLY these names:
# - Class names: Engine, Car
# - Method names for Engine: __init__, activate
# - Method names for Car: __init__, start
# - Attribute names for Engine: horsepower
# - Attribute names for Car: brand, engine
#
# Requirements:
# 1. Create an Engine class that represents a mechanical part with:
#    - __init__(self, horsepower) method storing horsepower
#    - activate(self) method returning format: "Engine with {horsepower}HP started"
#
# 2. Create a Car class that represents a vehicle with:
#    - __init__(self, brand, engine_horsepower) method
#      * Stores brand as instance attribute
#      * Creates an Engine instance with `engine_horsepower` and stores it
#        as an instance attribute named `engine` (COMPOSITION)
#    - start(self) method that returns format:
#      "{brand} car: {engine_activation_string}"
#      where engine_activation_string is the result of calling engine.activate()
#
# The key concept is that the Car HAS-A Engine (composition),
# rather than IS-A Engine (inheritance).
#
# The start() method MUST include the exact result of engine.activate() 
# inside the returned string.

# The exact string formats must match exactly as shown above.
#
# Write both classes below:
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def activate(self):
        return f"Engine with {self.horsepower}HP started"


class Car:
    def __init__(self, brand, engine_horsepower):
        self.brand = brand
        self.engine = Engine(engine_horsepower)

    def start(self):
        engine_status = self.engine.activate()
        return f"{self.brand} car: {engine_status}"


# ==========================================
# DO NOT MODIFY BELOW THIS LINE
# ==========================================
if __name__ == "_main_":
    print("Run 'python lab6_exercises.py' to test your solutions!")
