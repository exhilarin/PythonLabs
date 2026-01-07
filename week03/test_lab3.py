import unittest
import os
import tempfile
from lab3_exercises import *


class TestLab3(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Create test data files before running tests"""
        # Create numbers.txt for file reading exercises
        with open('numbers.txt', 'w') as f:
            f.write('10\n20\n30\n40\n50\n')

        # Create log.txt for log analysis exercise
        with open('log.txt', 'w') as f:
            f.write('ERROR: Connection failed\n')
            f.write('INFO: Server started\n')
            f.write('ERROR: Timeout occurred\n')
            f.write('WARNING: Low memory\n')
            f.write('INFO: Request processed\n')
            f.write('ERROR: Database error\n')

    @classmethod
    def tearDownClass(cls):
        """Clean up test files after all tests"""
        for file in ['numbers.txt', 'log.txt']:
            if os.path.exists(file):
                os.remove(file)

    # ==========================================
    # EXERCISE 1 TESTS (2 points)
    # ==========================================
    def test_exercise1_freezing(self):
        """Test converting 0°C (freezing point)"""
        result = celsius_to_fahrenheit(0)
        self.assertAlmostEqual(result, 32.0, places=1)

    def test_exercise1_boiling(self):
        """Test converting 100°C (boiling point)"""
        result = celsius_to_fahrenheit(100)
        self.assertAlmostEqual(result, 212.0, places=1)

    def test_exercise1_negative(self):
        """Test converting negative temperature"""
        result = celsius_to_fahrenheit(-40)
        self.assertAlmostEqual(result, -40.0, places=1)

    def test_exercise1_room_temp(self):
        """Test converting room temperature"""
        result = celsius_to_fahrenheit(25)
        self.assertAlmostEqual(result, 77.0, places=1)

    # ==========================================
    # EXERCISE 2 TESTS (2 points)
    # ==========================================
    def test_exercise2_student_exists(self):
        """Test getting grade for existing student"""
        grades = {"Alice": 85, "Bob": 92, "Charlie": 78}
        result = get_student_grade(grades, "Alice")
        self.assertEqual(result, 85)

    def test_exercise2_student_not_found(self):
        """Test getting grade for non-existent student"""
        grades = {"Alice": 85, "Bob": 92}
        result = get_student_grade(grades, "David")
        self.assertEqual(result, 0)

    def test_exercise2_empty_dict(self):
        """Test with empty grades dictionary"""
        grades = {}
        result = get_student_grade(grades, "Alice")
        self.assertEqual(result, 0)

    def test_exercise2_different_student(self):
        """Test getting different student's grade"""
        grades = {"Alice": 85, "Bob": 92, "Charlie": 78}
        result = get_student_grade(grades, "Bob")
        self.assertEqual(result, 92)

    # ==========================================
    # EXERCISE 3 TESTS (2 points)
    # ==========================================
    def test_exercise3_basic(self):
        """Test basic person formatting"""
        result = format_person("Alice", 25, "Boston")
        self.assertEqual(result, "Name: Alice, Age: 25, City: Boston")

    def test_exercise3_different_values(self):
        """Test with different values"""
        result = format_person("Bob", 30, "New York")
        self.assertEqual(result, "Name: Bob, Age: 30, City: New York")

    def test_exercise3_young_person(self):
        """Test with younger age"""
        result = format_person("Charlie", 18, "Chicago")
        self.assertEqual(result, "Name: Charlie, Age: 18, City: Chicago")

    def test_exercise3_format_exact(self):
        """Test that format is exactly correct"""
        result = format_person("Test", 99, "City")
        self.assertIn("Name: Test", result)
        self.assertIn("Age: 99", result)
        self.assertIn("City: City", result)

    # ==========================================
    # EXERCISE 4 TESTS (2 points)
    # ==========================================
    def test_exercise4_basic(self):
        """Test calculating average of simple list"""
        result = calculate_average([10, 20, 30])
        self.assertAlmostEqual(result, 20.0, places=1)

    def test_exercise4_four_numbers(self):
        """Test with four numbers"""
        result = calculate_average([5, 10, 15, 20])
        self.assertAlmostEqual(result, 12.5, places=1)

    def test_exercise4_single_number(self):
        """Test with single number"""
        result = calculate_average([42])
        self.assertAlmostEqual(result, 42.0, places=1)

    def test_exercise4_floats(self):
        """Test with floating point numbers"""
        result = calculate_average([1.5, 2.5, 3.5, 4.5])
        self.assertAlmostEqual(result, 3.0, places=1)

    # ==========================================
    # EXERCISE 5 TESTS (2 points)
    # ==========================================
    def test_exercise5_with_spaces(self):
        """Test cleaning filename with spaces"""
        result = clean_filename("  MyFile.TXT  ")
        self.assertEqual(result, "myfile.txt")

    def test_exercise5_uppercase(self):
        """Test converting uppercase to lowercase"""
        result = clean_filename("REPORT.PDF")
        self.assertEqual(result, "report.pdf")

    def test_exercise5_mixed_case(self):
        """Test with mixed case"""
        result = clean_filename("MyDocument.Docx")
        self.assertEqual(result, "mydocument.docx")

    def test_exercise5_already_clean(self):
        """Test with already clean filename"""
        result = clean_filename("file.txt")
        self.assertEqual(result, "file.txt")

    # ==========================================
    # EXERCISE 6 TESTS (3 points)
    # ==========================================
    def test_exercise6_basic(self):
        """Test counting basic extensions"""
        result = count_extensions(["a.txt", "b.txt", "c.jpg"])
        self.assertEqual(result, {"txt": 2, "jpg": 1})

    def test_exercise6_all_same(self):
        """Test when all files have same extension"""
        result = count_extensions(["file1.pdf", "file2.pdf", "file3.pdf"])
        self.assertEqual(result, {"pdf": 3})

    def test_exercise6_many_types(self):
        """Test with many different types"""
        result = count_extensions(["a.txt", "b.jpg", "c.png", "d.txt", "e.gif"])
        self.assertEqual(result["txt"], 2)
        self.assertEqual(result["jpg"], 1)
        self.assertEqual(result["png"], 1)
        self.assertEqual(result["gif"], 1)

    def test_exercise6_single_file(self):
        """Test with single file"""
        result = count_extensions(["document.docx"])
        self.assertEqual(result, {"docx": 1})

    def test_exercise6_case_sensitive(self):
        """Test that extensions are counted as-is"""
        result = count_extensions(["file.txt", "file.TXT"])
        # Should be separate unless normalized (implementation dependent)
        total = sum(result.values())
        self.assertEqual(total, 2)

    # ==========================================
    # EXERCISE 7 TESTS (3 points)
    # ==========================================
    def test_exercise7_basic(self):
        """Test filtering passing students"""
        grades = {"Alice": 85, "Bob": 45, "Charlie": 70}
        result = filter_passing_students(grades)
        self.assertEqual(result, {"Alice": 85, "Charlie": 70})

    def test_exercise7_all_pass(self):
        """Test when all students pass"""
        grades = {"Alice": 85, "Bob": 75, "Charlie": 90}
        result = filter_passing_students(grades)
        self.assertEqual(len(result), 3)

    def test_exercise7_none_pass(self):
        """Test when no students pass"""
        grades = {"Alice": 45, "Bob": 55, "Charlie": 50}
        result = filter_passing_students(grades)
        self.assertEqual(result, {})

    def test_exercise7_boundary(self):
        """Test boundary case (exactly 60)"""
        grades = {"Alice": 60, "Bob": 59}
        result = filter_passing_students(grades)
        self.assertIn("Alice", result)
        self.assertNotIn("Bob", result)

    def test_exercise7_high_scores(self):
        """Test with high scores"""
        grades = {"Alice": 95, "Bob": 88, "Charlie": 92}
        result = filter_passing_students(grades)
        self.assertEqual(len(result), 3)

    # ==========================================
    # EXERCISE 8 TESTS (3 points)
    # ==========================================
    def test_exercise8_basic(self):
        """Test basic number analysis"""
        result = analyze_numbers([10, 50, 30, 70])
        self.assertEqual(result[0], 10)  # min
        self.assertEqual(result[1], 70)  # max
        self.assertAlmostEqual(result[2], 40.0, places=1)  # average

    def test_exercise8_single_number(self):
        """Test with single number"""
        result = analyze_numbers([42])
        self.assertEqual(result, (42, 42, 42.0))

    def test_exercise8_negative_numbers(self):
        """Test with negative numbers"""
        result = analyze_numbers([-10, 5, 20, -5])
        self.assertEqual(result[0], -10)
        self.assertEqual(result[1], 20)
        self.assertAlmostEqual(result[2], 2.5, places=1)

    def test_exercise8_return_type(self):
        """Test that return type is tuple"""
        result = analyze_numbers([1, 2, 3])
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 3)

    def test_exercise8_floats(self):
        """Test with floating point numbers"""
        result = analyze_numbers([1.5, 2.5, 3.5])
        self.assertAlmostEqual(result[0], 1.5, places=1)
        self.assertAlmostEqual(result[1], 3.5, places=1)
        self.assertAlmostEqual(result[2], 2.5, places=1)

    # ==========================================
    # EXERCISE 9 TESTS (3 points)
    # ==========================================
    def test_exercise9_basic(self):
        """Test reading numbers from file"""
        result = read_numbers_from_file('numbers.txt')
        self.assertEqual(result, [10, 20, 30, 40, 50])

    def test_exercise9_correct_length(self):
        """Test correct number of items read"""
        result = read_numbers_from_file('numbers.txt')
        self.assertEqual(len(result), 5)

    def test_exercise9_first_number(self):
        """Test first number is correct"""
        result = read_numbers_from_file('numbers.txt')
        self.assertEqual(result[0], 10)

    def test_exercise9_all_integers(self):
        """Test all values are integers"""
        result = read_numbers_from_file('numbers.txt')
        for num in result:
            self.assertIsInstance(num, int)

    def test_exercise9_sum_check(self):
        """Test sum of numbers"""
        result = read_numbers_from_file('numbers.txt')
        self.assertEqual(sum(result), 150)

    # ==========================================
    # EXERCISE 10 TESTS (3 points)
    # ==========================================
    def test_exercise10_basic(self):
        """Test basic cart total calculation"""
        cart = {
            "apple": (1.5, 3),
            "banana": (0.8, 5)
        }
        result = calculate_cart_total(cart)
        self.assertAlmostEqual(result, 8.5, places=2)

    def test_exercise10_single_item(self):
        """Test with single item"""
        cart = {"orange": (2.0, 4)}
        result = calculate_cart_total(cart)
        self.assertAlmostEqual(result, 8.0, places=2)

    def test_exercise10_multiple_items(self):
        """Test with multiple items"""
        cart = {
            "apple": (1.0, 2),
            "banana": (0.5, 4),
            "orange": (1.5, 1)
        }
        result = calculate_cart_total(cart)
        self.assertAlmostEqual(result, 5.5, places=2)

    def test_exercise10_empty_cart(self):
        """Test with empty cart"""
        cart = {}
        result = calculate_cart_total(cart)
        self.assertAlmostEqual(result, 0.0, places=2)

    def test_exercise10_high_quantities(self):
        """Test with high quantities"""
        cart = {
            "item1": (10.0, 10),
            "item2": (5.0, 20)
        }
        result = calculate_cart_total(cart)
        self.assertAlmostEqual(result, 200.0, places=2)

    # ==========================================
    # EXERCISE 11 TESTS (5 points)
    # ==========================================
    def test_exercise11_basic_grades(self):
        """Test basic grade report generation"""
        scores = {"Alice": 92, "Bob": 78, "Charlie": 85}
        result = generate_grade_report(scores)
        self.assertIn("Alice", result)
        self.assertIn("92", result)
        self.assertIn("Grade: A", result)

    def test_exercise11_all_grade_levels(self):
        """Test all grade levels appear correctly"""
        scores = {"Student1": 95, "Student2": 85, "Student3": 75, "Student4": 65, "Student5": 55}
        result = generate_grade_report(scores)
        self.assertIn("Grade: A", result)
        self.assertIn("Grade: B", result)
        self.assertIn("Grade: C", result)
        self.assertIn("Grade: D", result)
        self.assertIn("Grade: F", result)

    def test_exercise11_format_check(self):
        """Test that format includes required elements"""
        scores = {"Alice": 92}
        result = generate_grade_report(scores)
        self.assertIn("Student:", result)
        self.assertIn("Score:", result)
        self.assertIn("Grade:", result)

    def test_exercise11_multiple_lines(self):
        """Test multiple students create multiple lines"""
        scores = {"Alice": 92, "Bob": 85}
        result = generate_grade_report(scores)
        lines = result.strip().split('\n')
        self.assertEqual(len(lines), 2)

    def test_exercise11_boundary_grades(self):
        """Test boundary scores"""
        scores = {"Student90": 90, "Student89": 89, "Student80": 80}
        result = generate_grade_report(scores)
        # 90 should be A, 89 should be B, 80 should be B
        result_lines = result.split('\n')
        a_count = sum(1 for line in result_lines if "Grade: A" in line)
        b_count = sum(1 for line in result_lines if "Grade: B" in line)
        self.assertEqual(a_count, 1)
        self.assertEqual(b_count, 2)

    def test_exercise11_failing_grade(self):
        """Test failing grades"""
        scores = {"Failing": 45}
        result = generate_grade_report(scores)
        self.assertIn("Grade: F", result)

    # ==========================================
    # EXERCISE 12 TESTS (5 points)
    # ==========================================
    def test_exercise12_total_lines(self):
        """Test counting total lines"""
        result = analyze_log_file('log.txt')
        self.assertEqual(result["total_lines"], 6)

    def test_exercise12_error_count(self):
        """Test counting ERROR level"""
        result = analyze_log_file('log.txt')
        self.assertEqual(result["levels"]["ERROR"], 3)

    def test_exercise12_info_count(self):
        """Test counting INFO level"""
        result = analyze_log_file('log.txt')
        self.assertEqual(result["levels"]["INFO"], 2)

    def test_exercise12_warning_count(self):
        """Test counting WARNING level"""
        result = analyze_log_file('log.txt')
        self.assertEqual(result["levels"]["WARNING"], 1)

    def test_exercise12_structure(self):
        """Test return structure is correct"""
        result = analyze_log_file('log.txt')
        self.assertIn("total_lines", result)
        self.assertIn("levels", result)
        self.assertIsInstance(result["levels"], dict)

    def test_exercise12_all_levels_present(self):
        """Test all level keys exist"""
        result = analyze_log_file('log.txt')
        self.assertIn("ERROR", result["levels"])
        self.assertIn("WARNING", result["levels"])
        self.assertIn("INFO", result["levels"])


def print_score():
    """Calculate and print the score"""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestLab3)
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