import unittest
import os
import tempfile
from lab2_exercises import *


class TestLab2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Create test data files before running tests"""
        # Create numbers.txt
        with open('numbers.txt', 'w') as f:
            f.write('42\n17\n93\n28\n55\n8\n76\n61\n34\n89\n')

        # Create words.txt
        with open('words.txt', 'w') as f:
            f.write('apple\nApricot\nbanana\ncherry\nAvocado\ndate\n')

        # Create shopping.txt
        with open('shopping.txt', 'w') as f:
            f.write('milk\neggs\nbread\ncheese\napples\n')

    @classmethod
    def tearDownClass(cls):
        """Clean up test files after all tests"""
        for file in ['numbers.txt', 'words.txt', 'shopping.txt']:
            if os.path.exists(file):
                os.remove(file)

    # ==========================================
    # EXERCISE 1 TESTS (4 points)
    # ==========================================
    def test_exercise1_type(self):
        """Test that exercise1 returns a list"""
        result = exercise1()
        self.assertIsInstance(result, list, "Should return a list")

    def test_exercise1_length(self):
        """Test that exercise1 returns exactly 5 items"""
        result = exercise1()
        self.assertEqual(len(result), 5, "List should contain exactly 5 items")

    def test_exercise1_content_type(self):
        """Test that all items are strings"""
        result = exercise1()
        for item in result:
            self.assertIsInstance(item, str, "All items should be strings")

    def test_exercise1_not_empty(self):
        """Test that items are not empty strings"""
        result = exercise1()
        for item in result:
            self.assertNotEqual(item, "", "Items should not be empty strings")

    # ==========================================
    # EXERCISE 2 TESTS (4 points)
    # ==========================================
    def test_exercise2_basic(self):
        """Test basic element access"""
        result = exercise2(['a', 'b', 'c', 'd', 'e'])
        self.assertEqual(result, ['a', 'e', 'c'])

    def test_exercise2_different_list(self):
        """Test with different list"""
        result = exercise2([10, 20, 30, 40, 50, 60])
        self.assertEqual(result, [10, 60, 30])

    def test_exercise2_strings(self):
        """Test with string list"""
        result = exercise2(['first', 'second', 'third', 'fourth'])
        self.assertEqual(result, ['first', 'fourth', 'third'])

    # ==========================================
    # EXERCISE 3 TESTS (5 points)
    # ==========================================
    def test_exercise3_found(self):
        """Test when item is found"""
        result = exercise3(['apple', 'banana', 'cherry'], 'banana')
        self.assertEqual(result['count'], 3)
        self.assertTrue(result['found'])

    def test_exercise3_not_found(self):
        """Test when item is not found"""
        result = exercise3(['apple', 'banana', 'cherry'], 'grape')
        self.assertEqual(result['count'], 3)
        self.assertFalse(result['found'])

    def test_exercise3_empty_list(self):
        """Test with empty list"""
        result = exercise3([], 'anything')
        self.assertEqual(result['count'], 0)
        self.assertFalse(result['found'])

    def test_exercise3_numbers(self):
        """Test with numbers"""
        result = exercise3([1, 2, 3, 4, 5], 3)
        self.assertEqual(result['count'], 5)
        self.assertTrue(result['found'])

    # ==========================================
    # EXERCISE 4 TESTS (6 points)
    # ==========================================
    def test_exercise4_basic(self):
        """Test appending two items"""
        result = exercise4(['a', 'b'], 'c', 'd')
        self.assertEqual(result, ['a', 'b', 'c', 'd'])

    def test_exercise4_numbers(self):
        """Test with numbers"""
        result = exercise4([1, 2, 3], 4, 5)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_exercise4_empty_list(self):
        """Test starting with empty list"""
        result = exercise4([], 'first', 'second')
        self.assertEqual(result, ['first', 'second'])

    def test_exercise4_order(self):
        """Test that order is preserved"""
        result = exercise4(['x'], 'y', 'z')
        self.assertEqual(result[-2], 'y')
        self.assertEqual(result[-1], 'z')

    # ==========================================
    # EXERCISE 5 TESTS (6 points)
    # ==========================================
    def test_exercise5_middle(self):
        """Test inserting in middle"""
        result = exercise5(['a', 'b', 'd', 'e'], 'c', 2)
        self.assertEqual(result, ['a', 'b', 'c', 'd', 'e'])

    def test_exercise5_beginning(self):
        """Test inserting at beginning"""
        result = exercise5(['b', 'c', 'd'], 'a', 0)
        self.assertEqual(result, ['a', 'b', 'c', 'd'])

    def test_exercise5_end(self):
        """Test inserting at end"""
        result = exercise5([1, 2, 3], 4, 3)
        self.assertEqual(result, [1, 2, 3, 4])

    def test_exercise5_numbers(self):
        """Test with numbers"""
        result = exercise5([10, 20, 40], 30, 2)
        self.assertEqual(result, [10, 20, 30, 40])

    # ==========================================
    # EXERCISE 6 TESTS (4 points)
    # ==========================================
    def test_exercise6_basic(self):
        """Test formatting items"""
        result = exercise6(['apple', 'banana', 'cherry'])
        self.assertEqual(result, ['Item: apple', 'Item: banana', 'Item: cherry'])

    def test_exercise6_single(self):
        """Test with single item"""
        result = exercise6(['solo'])
        self.assertEqual(result, ['Item: solo'])

    def test_exercise6_numbers(self):
        """Test with numbers converted to strings"""
        result = exercise6(['1', '2', '3'])
        self.assertEqual(result, ['Item: 1', 'Item: 2', 'Item: 3'])

    # ==========================================
    # EXERCISE 7 TESTS (5 points)
    # ==========================================
    def test_exercise7_basic(self):
        """Test summing numbers"""
        result = exercise7([10, 20, 30, 40])
        self.assertEqual(result, 100)

    def test_exercise7_single(self):
        """Test with single number"""
        result = exercise7([42])
        self.assertEqual(result, 42)

    def test_exercise7_negative(self):
        """Test with negative numbers"""
        result = exercise7([10, -5, 20, -15])
        self.assertEqual(result, 10)

    def test_exercise7_floats(self):
        """Test with floats"""
        result = exercise7([1.5, 2.5, 3.0])
        self.assertAlmostEqual(result, 7.0, places=2)

    # ==========================================
    # EXERCISE 8 TESTS (5 points)
    # ==========================================
    def test_exercise8_basic(self):
        """Test counting occurrences"""
        result = exercise8([1, 2, 3, 2, 4, 2], 2)
        self.assertEqual(result, 3)

    def test_exercise8_not_found(self):
        """Test when target not in list"""
        result = exercise8([1, 2, 3, 4], 5)
        self.assertEqual(result, 0)

    def test_exercise8_all_same(self):
        """Test when all items match"""
        result = exercise8([7, 7, 7, 7], 7)
        self.assertEqual(result, 4)

    def test_exercise8_strings(self):
        """Test with strings"""
        result = exercise8(['a', 'b', 'a', 'c', 'a'], 'a')
        self.assertEqual(result, 3)

    # ==========================================
    # EXERCISE 9 TESTS (6 points)
    # ==========================================
    def test_exercise9_basic(self):
        """Test filtering by threshold"""
        result = exercise9([10, 55, 30, 75, 20], 40)
        self.assertEqual(result, [55, 75])

    def test_exercise9_none_pass(self):
        """Test when no numbers pass threshold"""
        result = exercise9([10, 20, 30], 50)
        self.assertEqual(result, [])

    def test_exercise9_all_pass(self):
        """Test when all numbers pass threshold"""
        result = exercise9([60, 70, 80], 50)
        self.assertEqual(result, [60, 70, 80])

    def test_exercise9_exact_threshold(self):
        """Test that threshold is not included (greater than, not equal)"""
        result = exercise9([40, 50, 60], 50)
        self.assertEqual(result, [60])

    # ==========================================
    # EXERCISE 10 TESTS (5 points)
    # ==========================================
    def test_exercise10_basic(self):
        """Test range creation"""
        result = exercise10(5, 10)
        self.assertEqual(result, [5, 6, 7, 8, 9, 10])

    def test_exercise10_single(self):
        """Test range with same start and end"""
        result = exercise10(7, 7)
        self.assertEqual(result, [7])

    def test_exercise10_large_range(self):
        """Test larger range"""
        result = exercise10(1, 5)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_exercise10_negative(self):
        """Test with negative numbers"""
        result = exercise10(-3, 2)
        self.assertEqual(result, [-3, -2, -1, 0, 1, 2])

    # ==========================================
    # EXERCISE 11 TESTS (4 points)
    # ==========================================
    def test_exercise11_shopping(self):
        """Test reading shopping.txt"""
        result = exercise11('shopping.txt')
        self.assertIn('milk', result)
        self.assertIn('eggs', result)
        self.assertIn('bread', result)

    def test_exercise11_is_string(self):
        """Test that result is a string"""
        result = exercise11('shopping.txt')
        self.assertIsInstance(result, str)

    def test_exercise11_not_empty(self):
        """Test that file content is not empty"""
        result = exercise11('shopping.txt')
        self.assertGreater(len(result), 0)

    # ==========================================
    # EXERCISE 12 TESTS (5 points)
    # ==========================================
    def test_exercise12_shopping(self):
        """Test counting lines in shopping.txt"""
        result = exercise12('shopping.txt')
        self.assertEqual(result, 5)

    def test_exercise12_words(self):
        """Test counting lines in words.txt"""
        result = exercise12('words.txt')
        self.assertEqual(result, 6)

    def test_exercise12_numbers(self):
        """Test counting lines in numbers.txt"""
        result = exercise12('numbers.txt')
        self.assertEqual(result, 10)

    # ==========================================
    # EXERCISE 13 TESTS (5 points)
    # ==========================================
    def test_exercise13_basic(self):
        """Test parsing numbers from file"""
        result = exercise13('numbers.txt')
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 10)

    def test_exercise13_first_number(self):
        """Test first number is correct"""
        result = exercise13('numbers.txt')
        self.assertEqual(result[0], 42)

    def test_exercise13_all_numbers(self):
        """Test all numbers are integers"""
        result = exercise13('numbers.txt')
        for num in result:
            self.assertIsInstance(num, int)

    def test_exercise13_contains_expected(self):
        """Test specific numbers are in result"""
        result = exercise13('numbers.txt')
        self.assertIn(93, result)
        self.assertIn(17, result)
        self.assertIn(55, result)

    # ==========================================
    # EXERCISE 14 TESTS (6 points)
    # ==========================================
    def test_exercise14_creates_file(self):
        """Test that file is created"""
        temp_file = 'test_output.txt'
        try:
            result = exercise14(temp_file, ['apple', 'banana', 'cherry'])
            self.assertTrue(os.path.exists(temp_file))
        finally:
            if os.path.exists(temp_file):
                os.remove(temp_file)

    def test_exercise14_content(self):
        """Test file content is correct"""
        temp_file = 'test_output.txt'
        try:
            items = ['line1', 'line2', 'line3']
            exercise14(temp_file, items)
            with open(temp_file, 'r') as f:
                lines = f.read().strip().split('\n')
            self.assertEqual(lines, items)
        finally:
            if os.path.exists(temp_file):
                os.remove(temp_file)

    def test_exercise14_returns_success(self):
        """Test that function returns 'Success'"""
        temp_file = 'test_output.txt'
        try:
            result = exercise14(temp_file, ['test'])
            self.assertEqual(result, "Success")
        finally:
            if os.path.exists(temp_file):
                os.remove(temp_file)

    def test_exercise14_line_count(self):
        """Test correct number of lines written"""
        temp_file = 'test_output.txt'
        try:
            items = ['a', 'b', 'c', 'd', 'e']
            exercise14(temp_file, items)
            with open(temp_file, 'r') as f:
                lines = f.readlines()
            self.assertEqual(len(lines), 5)
        finally:
            if os.path.exists(temp_file):
                os.remove(temp_file)

    # ==========================================
    # EXERCISE 15 TESTS (5 points)
    # ==========================================
    def test_exercise15_basic(self):
        """Test filtering numbers from file"""
        result = exercise15('numbers.txt', 50)
        # Numbers > 50: 93, 55, 76, 61, 89
        self.assertEqual(len(result), 5)

    def test_exercise15_high_threshold(self):
        """Test with high threshold"""
        result = exercise15('numbers.txt', 80)
        # Numbers > 80: 93, 89
        self.assertIn(93, result)
        self.assertIn(89, result)
        self.assertEqual(len(result), 2)

    def test_exercise15_all_pass(self):
        """Test when all numbers pass"""
        result = exercise15('numbers.txt', 0)
        self.assertEqual(len(result), 10)

    def test_exercise15_none_pass(self):
        """Test when no numbers pass"""
        result = exercise15('numbers.txt', 100)
        self.assertEqual(result, [])

    # ==========================================
    # EXERCISE 16 TESTS (5 points)
    # ==========================================
    def test_exercise16_letter_a(self):
        """Test counting words starting with 'a'"""
        # words.txt contains: apple, Apricot, banana, cherry, Avocado, date
        # Words starting with 'a' (case-insensitive): apple, Apricot, Avocado = 3
        result = exercise16('words.txt', 'a')
        self.assertEqual(result, 3)

    def test_exercise16_letter_b(self):
        """Test counting words starting with 'b'"""
        result = exercise16('words.txt', 'b')
        self.assertEqual(result, 1)

    def test_exercise16_letter_c(self):
        """Test counting words starting with 'c'"""
        result = exercise16('words.txt', 'c')
        self.assertEqual(result, 1)

    def test_exercise16_uppercase(self):
        """Test with uppercase letter"""
        result = exercise16('words.txt', 'A')
        self.assertEqual(result, 3)

    def test_exercise16_no_match(self):
        """Test letter with no matches"""
        result = exercise16('words.txt', 'z')
        self.assertEqual(result, 0)


def print_score():
    """Calculate and print the score"""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestLab2)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    total_tests = result.testsRun
    failures = len(result.failures)
    errors = len(result.errors)
    passed = total_tests - failures - errors

    print("\n" + "=" * 50)
    print(f"RESULTS: {passed}/{total_tests} tests passed")
    print(f"Estimated Score: {(passed / total_tests) * 100:.1f}%")
    print("=" * 50)


if __name__ == '__main__':
    print_score()