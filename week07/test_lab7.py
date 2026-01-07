import unittest
import sqlite3
import os
import tempfile

# ==========================================
# SECURE IMPORT
# ==========================================
try:
    import lab7_exercises as lab
except Exception as e:
    print(f"WARNING: Could not import lab7_exercises.py: {e}")
    lab = None


class TestLab7Friendly(unittest.TestCase):

    # Strict helper: missing item should FAIL (not SKIP)
    def require_symbol(self, name):
        if lab is None:
            self.fail("Could not import lab7_exercises.py (syntax/import error).")
        if not hasattr(lab, name):
            self.fail(f"Missing or misspelled required item: '{name}'")

    # ==========================================
    # SECTION A: EASY (2 Points Each)
    # ==========================================

    def test_ex1_sql_reminder(self):
        """Test Ex 1: SQL Reminder - High Balance"""
        self.require_symbol('get_high_balance_users')

        # Use a safe temporary DB file (Windows-friendly)
        tmp_path = None
        try:
            with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as tmp:
                tmp_path = tmp.name

            conn = sqlite3.connect(tmp_path)
            conn.execute("CREATE TABLE accounts (owner TEXT, balance REAL)")
            conn.execute("INSERT INTO accounts VALUES ('UserA', 1000)")
            conn.execute("INSERT INTO accounts VALUES ('UserB', 200)")
            conn.commit()
            conn.close()

            res = lab.get_high_balance_users(tmp_path, 500)
            self.assertEqual(list(res), ["UserA"], "SQL filtering logic is incorrect.")
        finally:
            if tmp_path and os.path.exists(tmp_path):
                try:
                    os.remove(tmp_path)
                except PermissionError:
                    # Very rare on Windows if a connection is still open somewhere
                    pass

    def test_ex2_oop_reminder(self):
        """Test Ex 2: OOP Reminder - DataPoint Class"""
        self.require_symbol('DataPoint')
        try:
            dp = lab.DataPoint("Test", 10)
            self.assertEqual(dp.as_tuple(), ("Test", 10), "as_tuple() should return (label, value).")
        except Exception as e:
            self.fail(f"DataPoint class failed to execute: {e}")

    def test_ex3_convert_usd(self):
        """Test Ex 3: Map - TRY to USD (Robust Float Comparison)"""
        self.require_symbol('convert_to_usd')

        # Define inputs and expected outputs
        prices = [100, 200]
        rate = 0.03  # Assuming rate is a multiplier here based on your expected output
        expected_values = [3.0, 6.0]

        # Run function
        result = lab.convert_to_usd(prices, rate)

        # 1. Check if result is a list
        self.assertIsInstance(result, list, "Function must return a list.")

        # 2. Check length matches
        self.assertEqual(len(result), len(expected_values), "List length mismatch.")

        # 3. Check element-wise almost equality
        for computed, correct in zip(result, expected_values):
            self.assertAlmostEqual(
                computed,
                correct,
                places=2,  # Checks up to 2 decimal places
                msg=f"Float mismatch: got {computed}, expected {correct}"
            )

    def test_ex4_high_ratings(self):
        """Test Ex 4: Filter - Product Ratings"""
        self.require_symbol('filter_high_ratings')
        data = [{"name": "A", "rating": 4.8}, {"name": "B", "rating": 4.0}]
        res = lab.filter_high_ratings(data, 4.5)
        self.assertEqual(len(list(res)), 1, "Should filter products below threshold.")

    def test_ex5_normalize_names(self):
        """Test Ex 5: Map - Name Cleaning"""
        self.require_symbol('normalize_names')
        res = lab.normalize_names(["  john  ", " DOE "])
        self.assertEqual(list(res), ["John", "Doe"], "Should trim spaces and use Title Case.")

    def test_ex6_square_numbers(self):
        """Test Ex 6: Map - Squares"""
        self.require_symbol('square_numbers')
        res = lab.square_numbers([2, 5])
        self.assertEqual(list(res), [4, 25])

    # ==========================================
    # SECTION B: MEDIUM (3 Points Each)
    # ==========================================

    def test_ex7_bonus_calc(self):
        """Test Ex 7: Bonus Calculation Pipeline"""
        self.require_symbol('calculate_bonuses')
        emps = [{'name': 'Ali', 'salary': 1000, 'performance_score': 80}]
        res = lab.calculate_bonuses(emps)
        self.assertIn("Ali bonus: 100.0", list(res)[0], "Format must be 'Name bonus: amount'.")

    def test_ex8_total_order(self):
        """Test Ex 8: Reduce - Total Value"""
        self.require_symbol('total_order_value')
        cart = [{'price': 10, 'quantity': 2}, {'price': 5, 'quantity': 1}]
        self.assertEqual(lab.total_order_value(cart), 25)

    def test_ex9_sensor_data(self):
        """Test Ex 9: CSV string to Dict"""
        self.require_symbol('format_sensor_data')
        res = lab.format_sensor_data(["1,temp,20.0"])
        self.assertEqual(res[0]['type'], 'temp')
        self.assertIsInstance(res[0]['id'], int, "ID must be integer.")

    def test_ex10_extract_emails(self):
        """Test Ex 10: Email Extraction"""
        self.require_symbol('extract_emails')
        res = lab.extract_emails([{"email": "TEST@mail.com"}])
        self.assertEqual(list(res)[0], "test@mail.com", "Emails should be lowercase.")

    # ==========================================
    # SECTION C: HARD (5 Points Each)
    # ==========================================

    def test_ex11_it_projects(self):
        """Test Ex 11: IT Projects (Flattening)"""
        self.require_symbol('get_department_projects')
        data = [{"dept": "IT", "projects": ["A"]}, {"dept": "IT", "projects": ["A", "B"]}]
        res = lab.get_department_projects(data, "IT")
        self.assertEqual(res, ["A", "B"], "Result should be sorted and unique.")

    def test_ex12_log_parsing(self):
        """Test Ex 12: Log Pipeline"""
        self.require_symbol('clean_and_query_logs')
        logs = ["ERROR CODE:404", "INFO CODE:200", "ERROR CODE:404"]
        res = lab.clean_and_query_logs(logs)
        self.assertEqual(res, [404], "Only ERRORs, unique, and integers.")

    def test_ex13_revenue_cat(self):
        """Test Ex 13: Revenue by Category"""
        self.require_symbol('total_revenue_by_category')
        sales = [{"cat": "X", "p": 10, "q": 2}, {"cat": "Y", "p": 50, "q": 1}]
        self.assertEqual(lab.total_revenue_by_category(sales, "X"), 20)

    def test_ex14_inventory_summary(self):
        """Test Ex 14: Inventory Summary Strings"""
        self.require_symbol('summarize_inventory')
        data = [{"id": "W1", "stock": [10, 5]}]
        res = lab.summarize_inventory(data)
        self.assertIn("Warehouse W1: Total Items = 15", list(res)[0])


# ==========================================
# REPORTING & SCORING (UPDATED)
# ==========================================
def run_reports():
    POINTS_MAP = {
        'test_ex1': 2, 'test_ex2': 2, 'test_ex3': 2, 'test_ex4': 2, 'test_ex5': 2, 'test_ex6': 2,
        'test_ex7': 3, 'test_ex8': 3, 'test_ex9': 3, 'test_ex10': 3,
        'test_ex11': 5, 'test_ex12': 5, 'test_ex13': 5, 'test_ex14': 5
    }

    suite = unittest.TestLoader().loadTestsFromTestCase(TestLab7Friendly)
    result = unittest.TestResult()
    suite.run(result)

    # Helper to get short name from test object
    def get_name(t):
        return t.id().split('.')[-1]

    # Collect IDs for scoring
    failure_ids = [get_name(t) for t, _ in result.failures]
    error_ids = [get_name(t) for t, _ in result.errors]
    skipped_ids = [get_name(t) for t, _ in result.skipped]

    all_tests = unittest.TestLoader().getTestCaseNames(TestLab7Friendly)

    score = 0
    successful_count = 0

    # Calculate Score
    for t_name in all_tests:
        if t_name not in failure_ids and t_name not in error_ids and t_name not in skipped_ids:
            key = "_".join(t_name.split('_')[:2])  # e.g., "test_ex11"
            score += POINTS_MAP.get(key, 0)
            successful_count += 1

    # --- PRINT SUMMARY ---
    print("\n" + "=" * 40)
    print(f"SUCCESSFUL: {successful_count} | FAILED: {len(failure_ids) + len(error_ids)} | SKIPPED: {len(skipped_ids)}")
    print(f"ESTIMATED SCORE: {score} / 44")
    print("=" * 40)

    # --- PRINT DETAILED ERRORS (This is the new part) ---
    if len(result.failures) > 0:
        print("\n" + "!" * 10 + " FAILURES (Assertion Errors) " + "!" * 10)
        for t, trace in result.failures:
            print("-" * 60)
            print(f"❌ TEST: {get_name(t)}")
            print(f"REASON:\n{trace}")

    if len(result.errors) > 0:
        print("\n" + "!" * 10 + " ERRORS (Code Crashes) " + "!" * 10)
        for t, trace in result.errors:
            print("-" * 60)
            print(f"💥 TEST: {get_name(t)}")
            print(f"TRACEBACK:\n{trace}")

    if len(result.skipped) > 0:
        print("\n>>> SKIPPED ITEMS:")
        for t, reason in result.skipped:
            print(f"⚠️ {get_name(t)}: {reason}")


if __name__ == "__main__":
    run_reports()