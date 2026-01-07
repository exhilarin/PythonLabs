import unittest
from lab1_exercises import *

class TestLab1(unittest.TestCase):
    
    # ==========================================
    # EXERCISE 1 TESTS (5 points)
    # ==========================================
    def test_exercise1_structure(self):
        """Test that exercise1 returns a dictionary with correct keys"""
        result = exercise1()
        self.assertIsInstance(result, dict, "Should return a dictionary")
        self.assertIn('name', result, "Dictionary should have 'name' key")
        self.assertIn('age', result, "Dictionary should have 'age' key")
        self.assertIn('height', result, "Dictionary should have 'height' key")
        self.assertIn('loves_programming', result, "Dictionary should have 'loves_programming' key")
    
    def test_exercise1_types(self):
        """Test that exercise1 returns correct data types"""
        result = exercise1()
        self.assertIsInstance(result['name'], str, "Name should be a string")
        self.assertIsInstance(result['age'], int, "Age should be an integer")
        self.assertIsInstance(result['height'], float, "Height should be a float")
        self.assertIsInstance(result['loves_programming'], bool, "loves_programming should be a boolean")
    
    def test_exercise1_not_default(self):
        """Test that student filled in their own values"""
        result = exercise1()
        self.assertNotEqual(result['name'], "", "Name should not be empty string")
        self.assertNotEqual(result['age'], 0, "Age should not be 0")
        self.assertNotEqual(result['height'], 0.0, "Height should not be 0.0")
    
    # ==========================================
    # EXERCISE 2 TESTS (5 points)
    # ==========================================
    def test_exercise2_basic(self):
        """Test basic string concatenation"""
        self.assertEqual(exercise2("John", "Doe"), "John Doe")
    
    def test_exercise2_different_names(self):
        """Test with different names"""
        self.assertEqual(exercise2("Alice", "Smith"), "Alice Smith")
        self.assertEqual(exercise2("Bob", "Johnson"), "Bob Johnson")
    
    def test_exercise2_single_char(self):
        """Test with single character names"""
        self.assertEqual(exercise2("A", "B"), "A B")
    
    # ==========================================
    # EXERCISE 3 TESTS (5 points)
    # ==========================================
    def test_exercise3_basic(self):
        """Test average calculation"""
        self.assertAlmostEqual(exercise3(85, 92, 78), 85.0, places=2)
    
    def test_exercise3_all_same(self):
        """Test when all scores are the same"""
        self.assertAlmostEqual(exercise3(90, 90, 90), 90.0, places=2)
    
    def test_exercise3_different_values(self):
        """Test with different score combinations"""
        self.assertAlmostEqual(exercise3(100, 80, 70), 83.333, places=2)
        self.assertAlmostEqual(exercise3(95, 87, 91), 91.0, places=2)
    
    # ==========================================
    # EXERCISE 4 TESTS (7 points)
    # ==========================================
    def test_exercise4_basic(self):
        """Test Celsius to Fahrenheit conversion"""
        self.assertAlmostEqual(exercise4(25), 77.0, places=1)
    
    def test_exercise4_freezing(self):
        """Test freezing point"""
        self.assertAlmostEqual(exercise4(0), 32.0, places=1)
    
    def test_exercise4_boiling(self):
        """Test boiling point"""
        self.assertAlmostEqual(exercise4(100), 212.0, places=1)
    
    def test_exercise4_negative(self):
        """Test negative temperature"""
        self.assertAlmostEqual(exercise4(-40), -40.0, places=1)
    
    # ==========================================
    # EXERCISE 5 TESTS (7 points)
    # ==========================================
    def test_exercise5_basic(self):
        """Test rectangle calculations"""
        result = exercise5(12.5, 8.3)
        self.assertAlmostEqual(result['area'], 103.75, places=2)
        self.assertAlmostEqual(result['perimeter'], 41.6, places=2)
    
    def test_exercise5_square(self):
        """Test with a square"""
        result = exercise5(5, 5)
        self.assertAlmostEqual(result['area'], 25.0, places=2)
        self.assertAlmostEqual(result['perimeter'], 20.0, places=2)
    
    def test_exercise5_decimals(self):
        """Test with decimal values"""
        result = exercise5(7.5, 3.2)
        self.assertAlmostEqual(result['area'], 24.0, places=2)
        self.assertAlmostEqual(result['perimeter'], 21.4, places=2)
    
    # ==========================================
    # EXERCISE 6 TESTS (8 points)
    # ==========================================
    def test_exercise6_basic(self):
        """Test shopping cart calculation"""
        result = exercise6(29.99, 4, 0.07)
        self.assertAlmostEqual(result['subtotal'], 119.96, places=2)
        self.assertAlmostEqual(result['tax'], 8.3972, places=2)
        self.assertAlmostEqual(result['total'], 128.3572, places=2)
    
    def test_exercise6_no_tax(self):
        """Test with no tax"""
        result = exercise6(10.0, 2, 0.0)
        self.assertAlmostEqual(result['subtotal'], 20.0, places=2)
        self.assertAlmostEqual(result['tax'], 0.0, places=2)
        self.assertAlmostEqual(result['total'], 20.0, places=2)
    
    def test_exercise6_high_tax(self):
        """Test with higher tax rate"""
        result = exercise6(50.0, 3, 0.10)
        self.assertAlmostEqual(result['subtotal'], 150.0, places=2)
        self.assertAlmostEqual(result['tax'], 15.0, places=2)
        self.assertAlmostEqual(result['total'], 165.0, places=2)
    
    # ==========================================
    # EXERCISE 7 TESTS (8 points)
    # ==========================================
    def test_exercise7_cannot_vote(self):
        """Test ages below 18"""
        self.assertEqual(exercise7(16), "You cannot vote yet.")
        self.assertEqual(exercise7(10), "You cannot vote yet.")
        self.assertEqual(exercise7(17), "You cannot vote yet.")
    
    def test_exercise7_can_vote(self):
        """Test ages 18 and above"""
        self.assertEqual(exercise7(18), "You can vote!")
        self.assertEqual(exercise7(25), "You can vote!")
        self.assertEqual(exercise7(65), "You can vote!")
    
    # ==========================================
    # EXERCISE 8 TESTS (10 points)
    # ==========================================
    def test_exercise8_grade_a(self):
        """Test A grade range"""
        self.assertEqual(exercise8(90), "A")
        self.assertEqual(exercise8(95), "A")
        self.assertEqual(exercise8(100), "A")
    
    def test_exercise8_grade_b(self):
        """Test B grade range"""
        self.assertEqual(exercise8(80), "B")
        self.assertEqual(exercise8(85), "B")
        self.assertEqual(exercise8(89), "B")
    
    def test_exercise8_grade_c(self):
        """Test C grade range"""
        self.assertEqual(exercise8(70), "C")
        self.assertEqual(exercise8(75), "C")
        self.assertEqual(exercise8(79), "C")
    
    def test_exercise8_grade_d(self):
        """Test D grade range"""
        self.assertEqual(exercise8(60), "D")
        self.assertEqual(exercise8(65), "D")
        self.assertEqual(exercise8(69), "D")
    
    def test_exercise8_grade_f(self):
        """Test F grade range"""
        self.assertEqual(exercise8(59), "F")
        self.assertEqual(exercise8(50), "F")
        self.assertEqual(exercise8(0), "F")
    
    # ==========================================
    # EXERCISE 9 TESTS (10 points)
    # ==========================================
    def test_exercise9_twenty_percent(self):
        """Test 20% discount for $100+"""
        result = exercise9(150)
        self.assertAlmostEqual(result['discount_rate'], 0.20, places=2)
        self.assertAlmostEqual(result['discount_amount'], 30.0, places=2)
        self.assertAlmostEqual(result['final_price'], 120.0, places=2)
    
    def test_exercise9_ten_percent(self):
        """Test 10% discount for $50-99"""
        result = exercise9(75)
        self.assertAlmostEqual(result['discount_rate'], 0.10, places=2)
        self.assertAlmostEqual(result['discount_amount'], 7.5, places=2)
        self.assertAlmostEqual(result['final_price'], 67.5, places=2)
    
    def test_exercise9_no_discount(self):
        """Test no discount for under $50"""
        result = exercise9(40)
        self.assertAlmostEqual(result['discount_rate'], 0.0, places=2)
        self.assertAlmostEqual(result['discount_amount'], 0.0, places=2)
        self.assertAlmostEqual(result['final_price'], 40.0, places=2)
    
    def test_exercise9_boundary_100(self):
        """Test exactly $100"""
        result = exercise9(100)
        self.assertAlmostEqual(result['discount_rate'], 0.20, places=2)
    
    def test_exercise9_boundary_50(self):
        """Test exactly $50"""
        result = exercise9(50)
        self.assertAlmostEqual(result['discount_rate'], 0.10, places=2)
    
    # ==========================================
    # EXERCISE 10 TESTS (8 points)
    # ==========================================
    def test_exercise10_basic(self):
        """Test circle area calculation"""
        self.assertAlmostEqual(exercise10(5), 78.53975, places=3)
    
    def test_exercise10_different_radii(self):
        """Test with different radius values"""
        self.assertAlmostEqual(exercise10(1), 3.14159, places=3)
        self.assertAlmostEqual(exercise10(10), 314.159, places=3)
        self.assertAlmostEqual(exercise10(3), 28.27431, places=3)
    
    # ==========================================
    # EXERCISE 11 TESTS (7 points)
    # ==========================================
    def test_exercise11_positive(self):
        """Test positive numbers"""
        self.assertEqual(exercise11(5), "positive")
        self.assertEqual(exercise11(100), "positive")
        self.assertEqual(exercise11(1), "positive")
    
    def test_exercise11_negative(self):
        """Test negative numbers"""
        self.assertEqual(exercise11(-3), "negative")
        self.assertEqual(exercise11(-100), "negative")
        self.assertEqual(exercise11(-1), "negative")
    
    def test_exercise11_zero(self):
        """Test zero"""
        self.assertEqual(exercise11(0), "zero")


def print_score():
    """Calculate and print the score"""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestLab1)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    total_tests = result.testsRun
    failures = len(result.failures)
    errors = len(result.errors)
    passed = total_tests - failures - errors
    
    print("\n" + "="*50)
    print(f"RESULTS: {passed}/{total_tests} tests passed")
    print(f"Estimated Score: {(passed/total_tests)*100:.1f}%")
    print("="*50)


if __name__ == '__main__':
    print_score()
