import unittest
import re
import sys
import importlib
from types import ModuleType

# Attempt to import student solution
try:
    from lab6_exercises import *
except ImportError:
    pass
except SyntaxError as e:
    print(f"CRITICAL: Syntax Error in lab6_exercises.py: {e}")
    sys.exit(1)


class TestLab6(unittest.TestCase):

    # ==========================================
    # SECTION A: EASY
    # ==========================================

    def test_exercise1_clean_filename(self):
        self.assertEqual(clean_filename("  MyFile.TXT  "), "myfile.txt")
        self.assertEqual(clean_filename("   "), "")

    def test_exercise2_merge_dicts(self):
        dict1 = {'a': 1}
        dict2 = {'a': 2}
        result = merge_dicts(dict1, dict2)
        self.assertIsNot(result, dict1)
        self.assertEqual(result, {'a': 2})

    def test_exercise3_filter_by_length(self):
        """Fixed: Correctly checks if original list is modified."""
        original_list = ['python', 'c', 'java', 'go', 'rust']
        original_copy = original_list.copy()

        # Run filter
        result = filter_by_length(original_list, 3)

        # Check result
        self.assertEqual(result, ['python', 'java', 'rust'])

        # CRITICAL FIX: Check that ORIGINAL list matches ORIGINAL copy
        # (Previous test incorrectly checked result vs copy)
        self.assertEqual(original_list, original_copy,
                         "Original list was modified. Function must be non-destructive.")

    def test_exercise4_person_class(self):
        p = Person("Alice", 25)
        self.assertEqual(p.get_info(), "Name: Alice, Age: 25")

    def test_exercise5_circle_inheritance(self):
        c = Circle("Blue", 10)
        self.assertEqual(c.get_info(), "Circle color: Blue, Radius: 10")
        self.assertTrue(issubclass(Circle, Shape))

    def test_exercise6_method_overriding(self):
        s = Smartphone()
        self.assertEqual(s.get_sound(), "Ring!")
        self.assertIsInstance(s, Device)

    # ==========================================
    # SECTION B: MEDIUM
    # ==========================================

    def test_exercise7_product_class(self):
        # Ensure clean import
        try:
            from lab6_exercises import Product
        except ImportError:
            self.fail("Product class missing")

        p = Product("Laptop", 1000, 2)
        self.assertEqual(p.get_total_value(), 2000)

        # Test Discount
        p.apply_discount(10)  # 1000 -> 900
        self.assertEqual(p.price, 900)
        self.assertEqual(p.get_total_value(), 1800)

        # Test Float Precision (Approximate)
        p2 = Product("Cheap", 100, 1)
        p2.apply_discount(33)  # 100 -> 67
        self.assertAlmostEqual(p2.price, 67.0)

    def test_exercise8_shoe_inheritance(self):
        s = Shoe("Nike", 100, 1, "Nike", 42)
        # Just ensure it runs and returns a number different from base
        self.assertNotEqual(s.calculate_price(), 100)

    def test_exercise9_bank_account_encapsulation(self):
        acc = BankAccount(100)
        acc.deposit(50)
        self.assertEqual(acc.get_balance(), 150)

        # Encapsulation Check
        # Check for name-mangled private variable OR protected variable
        has_private = hasattr(acc, '_BankAccount__balance') or hasattr(acc, '_balance')
        self.assertTrue(has_private, "Balance must be private")

        # Public 'balance' should NOT exist
        self.assertFalse(hasattr(acc, 'balance'), "Should not have public 'balance' attribute")

    def test_exercise10_polymorphism(self):
        dog = Dog()
        cat = Cat()
        self.assertNotEqual(dog.speak(), cat.speak())
        self.assertEqual(animal_concert([dog, cat]), [dog.speak(), cat.speak()])

    def test_exercise11_class_variables(self):
        try:
            from lab6_exercises import Employee
        except ImportError:
            self.fail("Employee class missing")

        Employee._total_employees = 0  # Reset
        e1 = Employee("A", 100)
        e2 = Employee("B", 100)

        self.assertEqual(Employee.get_total_employees(), 2)

        # CRITICAL FIX: Python resolves class variables on instances, so hasattr(e1, var) is True.
        # We must check e1.__dict__ to ensure it's not an INSTANCE variable.
        self.assertNotIn('_total_employees', e1.__dict__,
                         "_total_employees must be a CLASS variable, not instance variable")

    def test_exercise12_string_representation(self):
        try:
            from lab6_exercises import Point
        except ImportError:
            self.fail("Point class missing")

        p = Point(3, 4)
        s = str(p)
        r = repr(p)

        self.assertIn("3", s)
        self.assertIn("Point", r)
        self.assertNotEqual(s, r)

        # CRITICAL FIX: eval() needs the class in its scope
        try:
            p_new = eval(r, {'Point': Point})
            self.assertEqual(p_new.x, 3)
        except Exception as e:
            self.fail(f"repr() string could not be evaluated: {e}")

    # ==========================================
    # SECTION C: HARD
    # ==========================================

    def test_exercise13_rectangle_encapsulation(self):
        r = Rectangle(10, 20)
        self.assertEqual(r.get_area(), 200)
        r.set_dimensions(-5, 20)  # Should fail silently
        self.assertEqual(r.get_area(), 200)

    def test_exercise14_class_static_methods(self):
        # 1. Strict Import Check using the module object to avoid scope issues
        if 'lab6_exercises' not in sys.modules:
            self.fail("lab6_exercises module not loaded.")

        module = sys.modules['lab6_exercises']

        # Check if classes exist in the module
        if not hasattr(module, 'Counter'):
            self.fail("Class 'Count' is required for this exercise.")

        Counter = module.Counter
        Counter()

        self.assertGreaterEqual(Counter.get_instance_count(), 1)
        self.assertTrue(Counter.is_even(2))
        self.assertFalse(Counter.is_even(3))

    def test_exercise15_inheritance_method_chaining(self):
        """Fixed: Robust import handling without relying on global scope."""

        # 1. Robust Import
        try:
            # Import directly within test to ensure we get the class
            from lab6_exercises import Furniture, Chair
        except ImportError:
            self.fail("Classes 'Furniture' and 'Chair' are missing.")

        # 2. Test Instantiation
        try:
            furniture = Furniture("Modern", "Wood")
            chair = Chair("Victorian", "Velvet", 4)
        except Exception as e:
            self.fail(f"Instantiation failed: {e}")

        # 3. Test Inheritance
        self.assertTrue(issubclass(Chair, Furniture), "Chair must inherit from Furniture")
        self.assertIsInstance(chair, Furniture)

        # 4. Test Method Overriding and String Formatting
        f_desc = furniture.describe()
        c_desc = chair.describe()

        self.assertNotEqual(f_desc, c_desc, "Chair must override describe()")
        self.assertIn("4", c_desc, "Chair.describe() must include leg count")
        self.assertIn("Victorian", c_desc, "Chair.describe() must include style (from parent)")

    def test_exercise16_composition_over_inheritance(self):
        """Fixed: Explicitly asserts class existence and composition structure."""

        # 1. Strict Import Check using the module object to avoid scope issues
        if 'lab6_exercises' not in sys.modules:
            self.fail("lab6_exercises module not loaded.")

        module = sys.modules['lab6_exercises']

        # Check if classes exist in the module
        if not hasattr(module, 'Car') or not hasattr(module, 'Engine'):
            self.fail("Classes 'Car' and 'Engine' are required for this exercise.")

        Car = module.Car
        Engine = module.Engine

        # 2. Verify NO Inheritance (Car should NOT inherit from Engine)
        self.assertFalse(issubclass(Car, Engine),
                         "Car should not inherit from Engine. Use Composition (Car HAS AN Engine).")

        # 3. Verify Composition
        try:
            # Instantiate Car (Assumes constructor takes reasonable args like Make, HP)
            # We use generic args if specific ones aren't enforced,
            # but usually, these match the 'composition' lecture examples.
            c = Car("GenericMake", 100)
        except TypeError:
            # Fallback: try without args if student didn't implement __init__ params
            try:
                c = Car()
            except Exception as e:
                self.fail(f"Could not instantiate Car class: {e}")
        except Exception as e:
            self.fail(f"Car instantiation crashed: {e}")

        # Check for the presence of an Engine instance inside Car
        # We check both specific attribute names AND a general search
        has_engine_attr = hasattr(c, 'engine')

        self.assertTrue(has_engine_attr,
                        "Car instance must contain an Engine object named `engine` specifically as an attribute.")


def calculate_score():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLab6)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    # Simple score print
    total = result.testsRun
    passed = total - len(result.failures) - len(result.errors)
    print(f"\nSCORE: {passed}/{total}")


if __name__ == "__main__":
    calculate_score()