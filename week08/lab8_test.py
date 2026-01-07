# test_lab8.py (tolerant version)
import unittest
import os
import tempfile

# Headless backend (autograder safe)
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

try:
    import lab8_exercises as lab
except Exception as e:
    lab = None
    IMPORT_ERROR = e
else:
    IMPORT_ERROR = None

if lab is not None:
    print("LAB PATH:", lab.__file__)
else:
    print("LAB IMPORT ERROR:", IMPORT_ERROR)

class TestLab8Tolerant(unittest.TestCase):

    # -------------------------
    # Helpers (NO SKIP -> FAIL)
    # -------------------------
    def require_symbol(self, name: str):
        if lab is None:
            self.fail(f"Could not import lab8_exercises.py: {IMPORT_ERROR}")
        if not hasattr(lab, name):
            self.fail(f"Missing required function: '{name}' (name must match exactly).")

    def assert_fig_ax(self, out):
        self.assertIsInstance(out, tuple, "Return must be a tuple.")
        self.assertEqual(len(out), 2, "Return must be (fig, ax).")
        fig, ax = out
        # tolerate Figure subclasses
        self.assertTrue(hasattr(fig, "savefig"), "First item must be a matplotlib Figure-like object.")
        self.assertTrue(hasattr(ax, "plot"), "Second item must be a matplotlib Axes-like object.")
        return fig, ax

    def assert_title_exact(self, ax, expected_title: str):
        self.assertEqual(ax.get_title(), expected_title, f"Title must be exactly: '{expected_title}'")

    def axes_len(self, axes):
        # tolerate: list/tuple/np.ndarray/Axes
        if axes is None:
            return 0
        if hasattr(axes, "__len__") and not isinstance(axes, plt.Axes):
            try:
                return len(axes)
            except Exception:
                return 0
        # single axes
        return 1

 # =========================================================
    # SECTION A: EASY (2 Points Each) — 5 Exercises
    # =========================================================

    def test_ex1_parse_and_enrich_dates(self):
        self.require_symbol("parse_and_enrich_dates")
        import pandas as pd

        inp = ["2024-02-02 12:38", "2023-12-03"]
        df = lab.parse_and_enrich_dates(inp)

        # 1. Tip Kontrolü
        self.assertIsInstance(df, pd.DataFrame, "Dönen değer bir DataFrame olmalı.")
        
        # 2. Sütun İsimleri ve Sırası
        expected_cols = ["datetime", "year", "month", "day", "day_name", "is_leap_year"]
        self.assertEqual(list(df.columns), expected_cols, "Sütun isimleri veya sırası hatalı.")

        # 3. Uzunluk
        self.assertEqual(len(df), len(inp), "Satır sayısı girdiyle aynı olmalı.")

        # 4. Veri Tipleri (En çok hata alınan yer)
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(df["datetime"]), "datetime sütunu datetime tipinde olmalı.")
        
        # Değer Kontrolleri (Toleranslı karşılaştırma)
        # .iloc[0] kullanarak indekse değil sıraya bakıyoruz
        self.assertEqual(int(df["year"].iloc[0]), 2024)
        self.assertEqual(int(df["month"].iloc[0]), 2)
        self.assertEqual(int(df["day"].iloc[0]), 2)
        self.assertEqual(str(df["day_name"].iloc[0]), "Friday")
        self.assertEqual(bool(df["is_leap_year"].iloc[0]), True)

    def test_ex2_make_line_plot(self):
        self.require_symbol("make_line_plot")
        fig, ax = self.assert_fig_ax(lab.make_line_plot([1, 2, 3], [2, 4, 6], "My Title"))
        self.assertEqual(ax.get_xlabel(), "x", 'xlabel must be "x"')
        self.assertEqual(ax.get_ylabel(), "y", 'ylabel must be "y"')
        self.assertEqual(ax.get_title(), "My Title", "Title must be set to the given title.")

    def test_ex3_make_histogram(self):
        self.require_symbol("make_histogram")
        fig, ax = self.assert_fig_ax(lab.make_histogram([1, 1, 2, 3, 5, 8, 13]))
        self.assert_title_exact(ax, "Value Distribution")

    def test_ex4_plot_category_counts(self):
        self.require_symbol("plot_category_counts")
        import pandas as pd

        df = pd.DataFrame({"category": ["A", "B", "A", "C", "A"]})
        fig, ax = self.assert_fig_ax(lab.plot_category_counts(df))
        self.assert_title_exact(ax, "Category Counts")

    def test_ex5_pandas_line_plot(self):
        self.require_symbol("pandas_line_plot")
        import pandas as pd

        df = pd.DataFrame({"x": [1, 2, 3], "y": [10, 20, 30]})
        ax = lab.pandas_line_plot(df)
        self.assertTrue(hasattr(ax, "plot"), "Must return a matplotlib Axes-like object.")

    # =========================================================
    # SECTION B: MEDIUM (3 Points Each) — 5 Exercises
    # =========================================================

    def test_ex6_daily_totals(self):
        self.require_symbol("daily_totals")
        import pandas as pd

        df = pd.DataFrame({
            "timestamp": ["2024-01-01 10:00", "2024-01-01 12:00", "2024-01-02 09:00"],
            "value": [10, 5, 7]
        })
        out = lab.daily_totals(df)

        self.assertIsInstance(out, pd.DataFrame)
        self.assertEqual(list(out.columns), ["date", "total"], "Output columns must match exactly.")
        self.assertEqual(len(out), 2, "Should aggregate into 2 dates.")

        # tolerate date column type (string/date/datetime)
        first_date = out.loc[0, "date"]
        self.assertTrue(str(first_date).startswith("2024-01-01"), "Must be sorted by date ascending.")
        self.assertAlmostEqual(float(out.loc[0, "total"]), 15.0, places=6)

    def test_ex7_plot_and_save_line(self):
        self.require_symbol("plot_and_save_line")
        with tempfile.TemporaryDirectory() as td:
            out_file = os.path.join(td, "line.png")
            fig, ax = self.assert_fig_ax(lab.plot_and_save_line([1, 2, 3], [3, 2, 1], out_file))
            self.assertTrue(os.path.exists(out_file), "Figure must be saved to out_file.")
            self.assertGreater(os.path.getsize(out_file), 0, "Saved file must not be empty.")

    def test_ex8_plot_on_existing_ax(self):
        self.require_symbol("plot_on_existing_ax")
        import pandas as pd

        df = pd.DataFrame({
            "Sale Date": ["2024-01-01", "2024-01-02"],
            "Total Sales": [100, 200]
        })

        fig, ax = plt.subplots()
        returned_ax = lab.plot_on_existing_ax(df, ax)

        self.assertIs(returned_ax, ax, "Must plot on the provided ax and return the same ax.")
        self.assert_title_exact(ax, "Total Sales Over Time")

    def test_ex9_histogram_with_bins(self):
        self.require_symbol("histogram_with_bins")
        import pandas as pd

        df = pd.DataFrame({"value": [1, 2, 2, 3, 5, 8, 13]})
        fig, ax = self.assert_fig_ax(lab.histogram_with_bins(df, bins=5))
        self.assert_title_exact(ax, "Histogram")

    def test_ex10_simple_subplots(self):
        self.require_symbol("simple_subplots")
        out = lab.simple_subplots([1, 2, 3], [10, 20, 30])

        self.assertIsInstance(out, tuple)
        self.assertEqual(len(out), 2)
        fig, axes = out

        self.assertTrue(hasattr(fig, "savefig"), "First return must be a Figure-like object.")
        self.assertEqual(self.axes_len(axes), 2, "Must create 2 subplots (2 axes).")

    # =========================================================
    # SECTION C: HARD (5 Points Each) — 5 Exercises
    # =========================================================

    def test_ex11_plot_sales_dashboard(self):
        self.require_symbol("plot_sales_dashboard")
        import pandas as pd

        df = pd.DataFrame({
            "date": ["2024-01-01", "2024-01-02", "2024-01-03"],
            "sales": [10, 20, 15]
        })

        with tempfile.TemporaryDirectory() as td:
            out_file = os.path.join(td, "dash.png")
            out = lab.plot_sales_dashboard(df, out_file)

            self.assertIsInstance(out, tuple)
            self.assertEqual(len(out), 2)
            fig, axes = out

            self.assertTrue(hasattr(fig, "savefig"))
            self.assertEqual(self.axes_len(axes), 2, "Must create 2-row dashboard (2 axes).")

            self.assertTrue(os.path.exists(out_file), "Must save the dashboard figure.")
            self.assertGreater(os.path.getsize(out_file), 0, "Saved dashboard file must not be empty.")

    def test_ex12_weekly_mean(self):
        self.require_symbol("weekly_mean")
        import pandas as pd

        df = pd.DataFrame({
            "timestamp": ["2024-01-01", "2024-01-02", "2024-01-08"],
            "value": [10, 20, 30]
        })
        out = lab.weekly_mean(df)

        self.assertIsInstance(out, pd.DataFrame)
        self.assertEqual(list(out.columns), ["week", "mean_value"], "Output columns must match exactly.")
        self.assertGreaterEqual(len(out), 1, "Should produce at least 1 row.")
        self.assertTrue(pd.api.types.is_numeric_dtype(out["mean_value"]), "mean_value must be numeric.")

    def test_ex13_top_n_days_by_total(self):
        self.require_symbol("top_n_days_by_total")
        import pandas as pd

        df = pd.DataFrame({
            "timestamp": ["2024-01-01 10:00", "2024-01-01 11:00", "2024-01-02 09:00"],
            "value": [5, 10, 7]
        })
        out = lab.top_n_days_by_total(df, n=1)

        self.assertIsInstance(out, pd.DataFrame)
        self.assertEqual(list(out.columns), ["date", "total"], "Output columns must match exactly.")
        self.assertEqual(len(out), 1, "Must return top N rows only.")
        self.assertTrue(str(out.iloc[0]["date"]).startswith("2024-01-01"))
        self.assertAlmostEqual(float(out.iloc[0]["total"]), 15.0, places=6)

    def test_ex14_compare_two_metrics(self):
        self.require_symbol("compare_two_metrics")
        import pandas as pd

        df = pd.DataFrame({"a": [1, 2, 3], "b": [10, 20, 30]})
        out = lab.compare_two_metrics(df)

        self.assertIsInstance(out, tuple)
        self.assertEqual(len(out), 2)
        fig, axes = out
        self.assertTrue(hasattr(fig, "savefig"))
        self.assertEqual(self.axes_len(axes), 2, "Must return 2 axes (2 subplots).")

    def test_ex15_plot_date_range(self):
        self.require_symbol("plot_date_range")
        import pandas as pd

        df = pd.DataFrame({
            "timestamp": ["2024-01-01", "2024-01-05", "2024-01-10"],
            "value": [10, 50, 100]
        })
        fig, ax = self.assert_fig_ax(lab.plot_date_range(df, "2024-01-02", "2024-01-10"))
        # No strict line-data checks (tolerant); just ensure no crash.


# ==========================================
# REPORTING & SCORING (44 points total)
# ==========================================
def run_reports():
    POINTS_MAP = {
        "test_ex1_parse_and_enrich_dates": 2,
        "test_ex2_make_line_plot": 2,
        "test_ex3_make_histogram": 2,
        "test_ex4_plot_category_counts": 2,
        "test_ex5_pandas_line_plot": 2,
        "test_ex6_daily_totals": 3,
        "test_ex7_plot_and_save_line": 3,
        "test_ex8_plot_on_existing_ax": 3,
        "test_ex9_histogram_with_bins": 3,
        "test_ex10_simple_subplots": 3,
        "test_ex11_plot_sales_dashboard": 5,
        "test_ex12_weekly_mean": 5,
        "test_ex13_top_n_days_by_total": 5,
        "test_ex14_compare_two_metrics": 5,
        "test_ex15_plot_date_range": 5,
    }

    suite = unittest.TestLoader().loadTestsFromTestCase(TestLab8Tolerant)
    result = unittest.TestResult()
    suite.run(result)

    all_tests = unittest.TestLoader().getTestCaseNames(TestLab8Tolerant)
    failures = [t.id().split(".")[-1] for t, _ in result.failures]
    errors = [t.id().split(".")[-1] for t, _ in result.errors]
    skipped = [t.id().split(".")[-1] for t, _ in result.skipped]

    score = 0
    successful_count = 0
    for t_name in all_tests:
        if t_name not in failures and t_name not in errors and t_name not in skipped:
            score += POINTS_MAP.get(t_name, 0)
            successful_count += 1

    total = sum(POINTS_MAP.values())

    print("\n" + "=" * 40)
    print(f"SUCCESSFUL: {successful_count} | FAILED: {len(failures) + len(errors)} | SKIPPED: {len(skipped)}")
    print(f"ESTIMATED SCORE: {score} / {total}")
    print("=" * 40)

    if failures or errors:
        print("\n>>> FAILED/ERROR TESTS:")
        for name in failures + errors:
            print(f"❌ {name}")


if __name__ == "__main__":
    run_reports()
