# Lab 6 Quick Reference: OOP Cheat Sheet

## Object-Oriented Programming - Helpful Tips (NOT SOLUTIONS!)

⚠️ **IMPORTANT**: This is a reference guide, NOT the solutions!
Use these tips to understand concepts, not copy-paste code.

---

## 🏗️ Class Structure Template

```python
# Basic class template
class ClassName:
    """Docstring explaining the class purpose"""

    # Class variable (shared by all instances)
    class_variable = "value"

    def __init__(self, param1, param2):
        """Constructor - initialize instance attributes"""
        self.instance_var1 = param1  # Instance attribute
        self.instance_var2 = param2

    def instance_method(self):
        """Instance method - operates on instance data"""
        return f"Value: {self.instance_var1}"

    @classmethod
    def class_method(cls):
        """Class method - operates on class-level data"""
        return f"Class var: {cls.class_variable}"

    @staticmethod
    def static_method(param):
        """Static method - doesn't need self or cls"""
        return param * 2

    def __str__(self):
        """String representation for users"""
        return f"ClassName({self.instance_var1})"

    def __repr__(self):
        """Code representation for developers"""
        return f"ClassName({self.instance_var1!r}, {self.instance_var2!r})"
```

## 🔄 Inheritance Patterns

### Basic Inheritance

```python
class Parent:
    def __init__(self, value):
        self.value = value

    def display(self):
        return f"Value: {self.value}"

class Child(Parent):
    def __init__(self, value, extra):
        super().__init__(value)  # Call parent constructor
        self.extra = extra

    # Override parent method
    def display(self):
        parent_result = super().display()  # Call parent method
        return f"{parent_result}, Extra: {self.extra}"
```

### Multiple Inheritance

```python
class A:
    def method(self):
        return "From A"

class B:
    def method(self):
        return "From B"

class C(A, B):  # Method Resolution Order: C -> A -> B
    def call_both(self):
        return f"{A.method(self)} and {B.method(self)}"
```

## 🔐 Encapsulation Guidelines

### Access Modifiers

```python
class SecureClass:
    def __init__(self):
        self.public = "Anyone can access"      # Public
        self._protected = "Shouldn't access"   # Protected (convention)
        self.__private = "Can't access directly"  # Private (name mangling)

    # Getter for private attribute
    def get_private(self):
        return self.__private

    # Setter for private attribute
    def set_private(self, value):
        if self._is_valid(value):  # Validation
            self.__private = value

    def _is_valid(self, value):  # Protected helper method
        return value is not None
```

### Property Decorators

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius  # Internal storage

    @property
    def celsius(self):
        """Get celsius (read-only property)"""
        return self._celsius

    @property
    def fahrenheit(self):
        """Computed property (no setter = read-only)"""
        return self._celsius * 9/5 + 32

    @celsius.setter
    def celsius(self, value):
        """Setter with validation"""
        if -273.15 <= value <= 1000:  # Absolute zero to reasonable max
            self._celsius = value
```

## 🎭 Polymorphism Examples

### Method Overriding

```python
class PaymentMethod:
    def process(self, amount):
        raise NotImplementedError("Subclasses must implement")

class CreditCard(PaymentMethod):
    def process(self, amount):
        return f"Processing ${amount} via Credit Card"

class PayPal(PaymentMethod):
    def process(self, amount):
        return f"Processing ${amount} via PayPal"
```

### Polymorphic Behavior

```python
payments = [CreditCard(), PayPal()]
for payment in payments:
    print(payment.process(100))  # Same method, different behavior
```

### Duck Typing

```python
def make_sound(animal):
    """Works with ANY object that has a speak() method"""
    return animal.speak()

class Dog:
    def speak(self):
        return "Woof!"

class Car:  # Not an animal, but has speak()
    def speak(self):
        return "Vroom!"

# Both work because they implement speak()
print(make_sound(Dog()))  # "Woof!"
print(make_sound(Car()))  # "Vroom!"
```

## 🔄 Iterator Protocol

### Custom Iterator Class

```python
class Countdown:
    def __init__(self, start):
        self.current = start
        self.end = 1

    def __iter__(self):
        return self  # Returns itself as iterator

    def __next__(self):
        if self.current < self.end:
            raise StopIteration
        else:
            value = self.current
            self.current -= 1
            return value

# Usage
for number in Countdown(5):
    print(number)  # 5, 4, 3, 2, 1
```

### Generator Function (Alternative)

```python
def countdown_gen(start):
    """Generator version - simpler!"""
    current = start
    while current >= 1:
        yield current
        current -= 1

# Same usage
for number in countdown_gen(5):
    print(number)  # 5, 4, 3, 2, 1
```

## 🏗️ Composition vs Inheritance

### Composition (HAS-A Relationship)

```python
class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()  # Car HAS an Engine

    def start(self):
        return self.engine.start()  # Delegate to engine

car = Car()
print(car.start())  # "Engine started"
```

### Inheritance (IS-A Relationship)

```python
class Animal:
    def move(self):
        return "Moving"

class Bird(Animal):  # Bird IS an Animal
    def fly(self):
        return "Flying"

bird = Bird()
print(bird.move())  # "Moving" (inherited)
print(bird.fly())   # "Flying" (specific)
```

### When to Use Which?

- **Inheritance**: When child IS-A special type of parent
- **Composition**: When object HAS-A component/part

## 💡 Common OOP Mistakes to Avoid

### 1. Forgetting self Parameter

```python
# ❌ WRONG
class MyClass:
    def method():  # Missing self!
        return "Hello"

# ✅ CORRECT
class MyClass:
    def method(self):  # Has self
        return "Hello"
```

### 2. Not Calling super().**init**()

```python
# ❌ WRONG - Parent attributes not initialized
class Child(Parent):
    def __init__(self, value, extra):
        self.extra = extra  # Forgot super().__init__(value)

# ✅ CORRECT
class Child(Parent):
    def __init__(self, value, extra):
        super().__init__(value)  # Initialize parent
        self.extra = extra
```

### 3. Misusing Class vs Instance Variables

```python
# ❌ WRONG - Shared mutable object
class Dog:
    tricks = []  # Class variable (shared by all dogs!)

    def add_trick(self, trick):
        self.tricks.append(trick)  # All dogs share same list!

# ✅ CORRECT - Instance variable
class Dog:
    def __init__(self):
        self.tricks = []  # Each dog has its own list

    def add_trick(self, trick):
        self.tricks.append(trick)
```

### 4. Overcomplicating with Inheritance

```python
# ❌ WRONG - Deep inheritance hierarchy
class Vehicle:
    pass

class MotorizedVehicle(Vehicle):
    pass

class FourWheelVehicle(MotorizedVehicle):
    pass

class Car(FourWheelVehicle):  # Too deep!
    pass

# ✅ BETTER - Flatter hierarchy with composition
class Vehicle:
    pass

class Engine:
    pass

class Wheel:
    pass

class Car(Vehicle):
    def __init__(self):
        self.engine = Engine()
        self.wheels = [Wheel() for _ in range(4)]
```

## 🧪 Testing Your OOP Code

### Manual Testing Pattern

```python
# After writing a class, test it immediately
class TestMyClass:
    def __init__(self):
        print("Testing MyClass...")

        # Create instance
        obj = MyClass("test", 123)

        # Test attributes
        print(f"Attribute1: {obj.attr1}")
        print(f"Attribute2: {obj.attr2}")

        # Test methods
        result = obj.method()
        print(f"Method result: {result}")

        # Test inheritance
        if hasattr(obj, '__class__'):
            print(f"Class: {obj.__class__.__name__}")

        print("Tests completed!\n")

# Quick test
if __name__ == "__main__":
    TestMyClass()
```

### Common Test Cases for OOP

- **Instance creation**: Can you create objects?
- **Attribute access**: Can you get/set attributes?
- **Method calls**: Do methods return expected values?
- **Inheritance**: Do child classes work correctly?
- **Polymorphism**: Do overridden methods work?
- **Encapsulation**: Are private attributes protected?

## 📚 OOP Design Principles (SOLID Reminder)

### S - Single Responsibility

```python
# ❌ One class doing too much
class Report:
    def fetch_data(self): ...
    def analyze_data(self): ...
    def format_report(self): ...
    def save_to_file(self): ...
    def send_email(self): ...

# ✅ Separate responsibilities
class DataFetcher: ...
class DataAnalyzer: ...
class ReportFormatter: ...
class FileSaver: ...
class EmailSender: ...
```

### O - Open/Closed Principle

```python
# Open for extension, closed for modification
class Shape:
    def area(self):
        raise NotImplementedError

class Circle(Shape):  # Can add new shapes without modifying Shape
    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):  # Another extension
    def area(self):
        return self.side ** 2
```

## ⚡ Quick Debugging Tips

### 1. Print Object State

```python
obj = MyClass("test", 123)
print(f"Object: {obj}")
print(f"Type: {type(obj)}")
print(f"Attributes: {obj.__dict__}")
```

### 2. Check Inheritance Chain

```python
print(f"Class: {obj.__class__.__name__}")
print(f"Bases: {obj.__class__.__bases__}")
print(f"MRO: {obj.__class__.__mro__}")
```

### 3. Test Method Overriding

```python
parent = Parent()
child = Child()
print(f"Parent method: {parent.method()}")
print(f"Child method: {child.method()}")
print(f"Are they different? {parent.method() != child.method()}")
```

## 🎯 Final Checklist Before Submission

- [ ] All classes have `__init__` methods
- [ ] Inheritance uses `super()` correctly
- [ ] Private attributes use `__` prefix
- [ ] Public methods are clearly named
- [ ] Property decorators used where appropriate
- [ ] `__str__` and `__repr__` implemented if needed
- [ ] No syntax errors
- [ ] Tests pass: `python test_lab6.py`
- [ ] Code follows OOP principles

## 🆘 When Stuck on OOP Concepts

1. **Draw diagrams** - Visualize class relationships
2. **Start simple** - Basic class first, then add features
3. **Test incrementally** - After each change, run tests
4. **Read error messages** - Python tells you what's wrong
5. **Check examples** - Refer to lecture materials
6. **Ask for help** - TAs can explain OOP concepts

**Remember**: OOP is about modeling REAL-WORLD relationships in code. Think about how objects interact in reality, then translate to classes and methods.

Good luck with Lab 6! 🚀
