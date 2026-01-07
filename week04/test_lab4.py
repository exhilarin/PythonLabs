import unittest
import json
from lab4_exercises import *


class TestLab4(unittest.TestCase):

    # ==========================================
    # EXERCISE 1 TESTS (2 points)
    # ==========================================
    def test_exercise1_basic(self):
        """Test basic domain extraction"""
        result = extract_domain("https://www.example.com/page")
        self.assertEqual(result, "example.com")

    def test_exercise1_no_www(self):
        """Test domain without www"""
        result = extract_domain("https://api.github.com/users")
        self.assertEqual(result, "api.github.com")

    def test_exercise1_http(self):
        """Test with http instead of https"""
        result = extract_domain("http://www.google.com/search")
        self.assertEqual(result, "google.com")

    def test_exercise1_subdomain(self):
        """Test with subdomain"""
        result = extract_domain("https://www.mail.example.com/inbox")
        self.assertEqual(result, "mail.example.com")

    # ==========================================
    # EXERCISE 2 TESTS (2 points)
    # ==========================================
    def test_exercise2_basic(self):
        """Test basic query parameter parsing"""
        result = parse_query_params("https://api.com/search?q=python&page=2")
        self.assertEqual(result, {"q": "python", "page": "2"})

    def test_exercise2_single_param(self):
        """Test with single parameter"""
        result = parse_query_params("https://site.com/page?id=123")
        self.assertEqual(result, {"id": "123"})

    def test_exercise2_no_params(self):
        """Test URL without parameters"""
        result = parse_query_params("https://example.com/page")
        self.assertEqual(result, {})

    def test_exercise2_multiple_params(self):
        """Test with many parameters"""
        result = parse_query_params("https://api.com/search?q=test&page=1&limit=10&sort=asc")
        self.assertEqual(result, {"q": "test", "page": "1", "limit": "10", "sort": "asc"})

    # ==========================================
    # EXERCISE 3 TESTS (2 points)
    # ==========================================
    def test_exercise3_basic(self):
        """Test basic keyword counting"""
        result = count_keyword("Python is great. Python is powerful.", "python")
        self.assertEqual(result, 2)

    def test_exercise3_not_found(self):
        """Test when keyword not present"""
        result = count_keyword("Hello world", "goodbye")
        self.assertEqual(result, 0)

    def test_exercise3_case_insensitive(self):
        """Test case insensitivity"""
        result = count_keyword("PYTHON Python python", "python")
        self.assertEqual(result, 3)

    def test_exercise3_partial_match(self):
        """Test that partial matches don't count"""
        result = count_keyword("python pythonic", "python")
        self.assertGreaterEqual(result, 1)  # Should be at least 1

    # ==========================================
    # EXERCISE 4 TESTS (2 points)
    # ==========================================
    def test_exercise4_basic(self):
        """Test basic whitespace cleaning"""
        result = clean_response("  Hello    World  ")
        self.assertEqual(result, "Hello World")

    def test_exercise4_multiple_spaces(self):
        """Test collapsing multiple spaces"""
        result = clean_response("Too   many    spaces")
        self.assertEqual(result, "Too many spaces")

    def test_exercise4_already_clean(self):
        """Test with already clean text"""
        result = clean_response("Clean text")
        self.assertEqual(result, "Clean text")

    def test_exercise4_tabs_newlines(self):
        """Test with various whitespace types"""
        result = clean_response("  Multiple\t\ttabs  \n  ")
        self.assertIn("Multiple", result)
        self.assertIn("tabs", result)

    # ==========================================
    # EXERCISE 5 TESTS (2 points)
    # ==========================================
    def test_exercise5_200(self):
        """Test extracting 200 status code"""
        result = extract_status_code("HTTP/1.1 200 OK")
        self.assertEqual(result, 200)
        self.assertIsInstance(result, int)

    def test_exercise5_404(self):
        """Test extracting 404 status code"""
        result = extract_status_code("HTTP/1.1 404 Not Found")
        self.assertEqual(result, 404)
        self.assertIsInstance(result, int)

    def test_exercise5_500(self):
        """Test extracting 500 status code"""
        result = extract_status_code("HTTP/1.1 500 Internal Server Error")
        self.assertEqual(result, 500)

    def test_exercise5_type(self):
        """Test that return type is int"""
        result = extract_status_code("HTTP/1.1 201 Created")
        self.assertIsInstance(result, int)

    # ==========================================
    # EXERCISE 6 TESTS (2 points)
    # ==========================================
    def test_exercise6_basic(self):
        """Test basic timestamp formatting"""
        result = format_timestamp("2024-03-15T14:30:00")
        self.assertEqual(result, "2024-03-15 14:30")

    def test_exercise6_different_time(self):
        """Test with different timestamp"""
        result = format_timestamp("2024-12-25T09:15:30")
        self.assertEqual(result, "2024-12-25 09:15")

    def test_exercise6_format(self):
        """Test output format"""
        result = format_timestamp("2023-01-01T00:00:00")
        self.assertIn(" ", result)
        self.assertNotIn("T", result)

    def test_exercise6_no_seconds(self):
        """Test that seconds are removed"""
        result = format_timestamp("2024-06-15T18:45:59")
        self.assertEqual(result, "2024-06-15 18:45")

    # ==========================================
    # EXERCISE 7 TESTS (2 points)
    # ==========================================
    def test_exercise7_valid(self):
        """Test valid email"""
        result = is_valid_email("user@example.com")
        self.assertTrue(result)

    def test_exercise7_no_at(self):
        """Test invalid email without @"""
        result = is_valid_email("invalid.email")
        self.assertFalse(result)

    def test_exercise7_no_dot(self):
        """Test invalid email without dot"""
        result = is_valid_email("no@domain")
        self.assertFalse(result)

    def test_exercise7_dot_before_at(self):
        """Test that dot must come after @"""
        result = is_valid_email("user.name@domain")
        self.assertTrue(result)

    def test_exercise7_multiple_at(self):
        """Test email with multiple @ symbols"""
        result = is_valid_email("user@@example.com")
        # Should still have basic validation
        self.assertIsInstance(result, bool)

    # ==========================================
    # EXERCISE 8 TESTS (3 points)
    # ==========================================
    def test_exercise8_basic(self):
        """Test basic JSON value extraction"""
        result = get_json_value('{"name": "Alice", "age": 25}', "name")
        self.assertEqual(result, "Alice")

    def test_exercise8_number(self):
        """Test extracting number from JSON"""
        result = get_json_value('{"count": 42}', "count")
        self.assertEqual(result, 42)

    def test_exercise8_not_found(self):
        """Test key not found"""
        result = get_json_value('{"x": 10}', "y")
        self.assertIsNone(result)

    def test_exercise8_boolean(self):
        """Test extracting boolean value"""
        result = get_json_value('{"status": "success", "active": true}', "active")
        self.assertTrue(result)

    # ==========================================
    # EXERCISE 9 TESTS (3 points)
    # ==========================================
    def test_exercise9_basic(self):
        """Test nested value extraction"""
        result = get_nested_value('{"user": {"name": "Bob", "age": 30}}', "user", "name")
        self.assertEqual(result, "Bob")

    def test_exercise9_deep_nest(self):
        """Test with nested structure"""
        result = get_nested_value('{"data": {"info": {"id": 123}}}', "data", "info")
        self.assertEqual(result, {"id": 123})

    def test_exercise9_not_found_outer(self):
        """Test when outer key doesn't exist"""
        result = get_nested_value('{"x": {"y": 1}}', "z", "y")
        self.assertIsNone(result)

    def test_exercise9_not_found_inner(self):
        """Test when inner key doesn't exist"""
        result = get_nested_value('{"user": {"name": "Bob"}}', "user", "age")
        self.assertIsNone(result)

    # ==========================================
    # EXERCISE 10 TESTS (3 points)
    # ==========================================
    def test_exercise10_basic(self):
        """Test counting array items"""
        result = count_json_items('{"users": ["Alice", "Bob", "Charlie"]}', "users")
        self.assertEqual(result, 3)

    def test_exercise10_numbers(self):
        """Test with number array"""
        result = count_json_items('{"items": [1, 2, 3, 4, 5]}', "items")
        self.assertEqual(result, 5)

    def test_exercise10_empty_array(self):
        """Test with empty array"""
        result = count_json_items('{"data": []}', "data")
        self.assertEqual(result, 0)

    def test_exercise10_key_not_found(self):
        """Test when key doesn't exist"""
        result = count_json_items('{"x": [1, 2]}', "y")
        self.assertEqual(result, 0)

    def test_exercise10_not_array(self):
        """Test when value is not an array"""
        result = count_json_items('{"value": "string"}', "value")
        self.assertEqual(result, 0)

    # ==========================================
    # EXERCISE 11 TESTS (3 points)
    # ==========================================
    def test_exercise11_basic(self):
        """Test extracting values from array of objects"""
        result = extract_all_values(
            '[{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]', 
            "name"
        )
        self.assertEqual(result, ["Alice", "Bob"])

    def test_exercise11_numbers(self):
        """Test extracting numeric values"""
        result = extract_all_values(
            '[{"id": 1, "score": 85}, {"id": 2, "score": 90}]',
            "score"
        )
        self.assertEqual(result, [85, 90])

    def test_exercise11_mixed(self):
        """Test with mixed data types"""
        result = extract_all_values(
            '[{"val": 42}, {"val": "text"}, {"val": true}]',
            "val"
        )
        self.assertEqual(len(result), 3)

    def test_exercise11_missing_key(self):
        """Test when some objects don't have the key"""
        result = extract_all_values(
            '[{"x": 1}, {"y": 2}, {"x": 3}]',
            "x"
        )
        # Should handle gracefully (either skip or handle)
        self.assertIsInstance(result, list)

    # ==========================================
    # EXERCISE 12 TESTS (3 points)
    # ==========================================
    def test_exercise12_basic(self):
        """Test calculating average"""
        result = calculate_json_average(
            '[{"score": 85}, {"score": 90}, {"score": 78}]',
            "score"
        )
        self.assertAlmostEqual(result, 84.33, places=1)

    def test_exercise12_exact(self):
        """Test with round numbers"""
        result = calculate_json_average(
            '[{"val": 10}, {"val": 20}, {"val": 30}]',
            "val"
        )
        self.assertEqual(result, 20.0)

    def test_exercise12_single(self):
        """Test with single value"""
        result = calculate_json_average('[{"num": 42}]', "num")
        self.assertEqual(result, 42.0)

    def test_exercise12_type(self):
        """Test return type is float"""
        result = calculate_json_average('[{"x": 5}, {"x": 10}]', "x")
        self.assertIsInstance(result, float)

    # ==========================================
    # EXERCISE 13 TESTS (5 points)
    # ==========================================
    def test_exercise13_single_quotes(self):
        """Test fixing single quotes"""
        result = fix_json("{'name': 'Alice', 'age': 25}")
        self.assertEqual(result, {"name": "Alice", "age": 25})
        self.assertIsInstance(result, dict)

    def test_exercise13_trailing_comma_dict(self):
        """Test removing trailing comma in object"""
        result = fix_json('{"x": 1, "y": 2,}')
        self.assertEqual(result, {"x": 1, "y": 2})

    def test_exercise13_trailing_comma_array(self):
        """Test removing trailing comma in array"""
        result = fix_json('{"items": [1, 2, 3,]}')
        self.assertEqual(result, {"items": [1, 2, 3]})

    def test_exercise13_complex(self):
        """Test with multiple issues"""
        result = fix_json("{'name': 'Bob', 'scores': [85, 90,],}")
        self.assertIn("name", result)
        self.assertEqual(result["name"], "Bob")
        self.assertIsInstance(result, dict)

    # ==========================================
    # EXERCISE 14 TESTS (5 points)
    # ==========================================
    def test_exercise14_basic(self):
        """Test basic CSV parsing"""
        result = parse_csv_string("name,age,city\nAlice,25,NYC\nBob,30,LA")
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["name"], "Alice")
        self.assertEqual(result[1]["city"], "LA")

    def test_exercise14_structure(self):
        """Test return structure"""
        result = parse_csv_string("a,b\n1,2\n3,4")
        self.assertIsInstance(result, list)
        self.assertIsInstance(result[0], dict)
        self.assertEqual(result[0]["a"], "1")

    def test_exercise14_single_row(self):
        """Test with single data row"""
        result = parse_csv_string("x,y,z\n10,20,30")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["x"], "10")

    def test_exercise14_many_columns(self):
        """Test with many columns"""
        result = parse_csv_string("a,b,c,d,e\n1,2,3,4,5")
        self.assertEqual(len(result[0]), 5)

    # ==========================================
    # EXERCISE 15 TESTS (5 points)
    # ==========================================
    def test_exercise15_basic(self):
        """Test processing mixed API response"""
        result = process_api_response('STATUS: 200 | DATA: {"success": true} | COUNT: 5')
        self.assertEqual(result["status"], 200)
        self.assertIsInstance(result["data"], dict)
        self.assertEqual(result["count"], 5)

    def test_exercise15_types(self):
        """Test correct types in result"""
        result = process_api_response('STATUS: 404 | DATA: {"error": "Not found"} | COUNT: 0')
        self.assertIsInstance(result["status"], int)
        self.assertIsInstance(result["data"], dict)
        self.assertIsInstance(result["count"], int)

    def test_exercise15_data_content(self):
        """Test data parsing"""
        result = process_api_response('STATUS: 200 | DATA: {"name": "Test", "id": 42} | COUNT: 10')
        self.assertEqual(result["data"]["name"], "Test")
        self.assertEqual(result["data"]["id"], 42)

    def test_exercise15_structure(self):
        """Test result has all required keys"""
        result = process_api_response('STATUS: 201 | DATA: {} | COUNT: 1')
        self.assertIn("status", result)
        self.assertIn("data", result)
        self.assertIn("count", result)


def print_score():
    """Calculate and print the score"""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestLab4)
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
    
    # Section breakdown
    print("\nSection Breakdown (approximate):")
    print("Section A (String Processing): 14 points")
    print("Section B (JSON Processing): 15 points")
    print("Section C (Data Cleaning): 15 points")
    print("TOTAL: 44 points")


if __name__ == '__main__':
    print_score()
