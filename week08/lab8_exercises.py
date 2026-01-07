# ==========================================
# 🐍 LAB 8: Visualization & Pandas DateTime
# ==========================================
# NOTE:
# - Each exercise is independent.
# - Student implementations MUST be written where "pass" is placed.
# - No extra solution hints exist in this file (by design).

import pandas as pd
import matplotlib.pyplot as plt


# ==========================================
# SECTION A: EASY (2 Points Each) — 5 Exercises
# ==========================================

# ==========================================
# EXERCISE 1: Week 6 Reminder - DateTime Parsing (2 points)
# ==========================================
# TODO:
#   Function Name: parse_and_enrich_dates
#   Parameters:
#       date_strings (list): List of date strings
#   Returns:
#       pandas.DataFrame with EXACT columns (in this order):
#           ["datetime", "year", "month", "day", "day_name", "is_leap_year"]
#   Description:
#       Convert each string to datetime and add datetime-based features.
def parse_and_enrich_dates(date_strings):
	"""Convert date strings to a DataFrame with datetime features.

	Returns DataFrame with columns in this order:
	["datetime", "year", "month", "day", "day_name", "is_leap_year"]
	"""
	dt = pd.to_datetime(date_strings, errors="coerce")
	df = pd.DataFrame({"datetime": dt})
	df["year"] = df["datetime"].dt.year
	df["month"] = df["datetime"].dt.month
	df["day"] = df["datetime"].dt.day
	df["day_name"] = df["datetime"].dt.day_name()
	# pandas 1.3+ has is_leap_year
	try:
		df["is_leap_year"] = df["datetime"].dt.is_leap_year
	except Exception:
		# fallback: compute via year
		df["is_leap_year"] = df["year"].apply(lambda y: (y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)))

	return df[["datetime", "year", "month", "day", "day_name", "is_leap_year"]]
#       Preserve input order.
#   Note:
def make_line_plot(x, y, title):
	fig, ax = plt.subplots()
	ax.plot(x, y)
	ax.set_xlabel("x")
	ax.set_ylabel("y")
	ax.set_title(title)
	return fig, ax
#       date_strings may include both "YYYY-MM-DD" and "YYYY-MM-DD HH:MM" formats.
#   IMPORTANT:
def make_histogram(values):
	fig, ax = plt.subplots()
	ax.hist(values, bins=10)
	ax.set_title("Value Distribution")
	return fig, ax
#       Function name MUST be exactly "parse_and_enrich_dates".

def plot_category_counts(df):
	counts = df["category"].value_counts()
	fig, ax = plt.subplots()
	counts.plot(kind="bar", ax=ax)
	ax.set_title("Category Counts")
	return fig, ax

# ==========================================
def pandas_line_plot(df):
	# pandas returns an Axes object
	ax = df.plot(x="x", y="y")
	return ax
# EXERCISE 2: Week 7 Reminder - OO Line Plot (2 points)
# ==========================================
# TODO:
#   Function Name: make_line_plot
#   Parameters:
#       x (list): x-values
def daily_totals(df):
	df2 = df.copy()
	df2["timestamp"] = pd.to_datetime(df2["timestamp"])
	df2["date"] = df2["timestamp"].dt.date
	grouped = df2.groupby("date", sort=True, as_index=False)["value"].sum()
	grouped = grouped.rename(columns={"value": "total"})
	# Ensure sorted by date ascending
	grouped = grouped.sort_values(by="date").reset_index(drop=True)
	return grouped[["date", "total"]]
#       y (list): y-values
#       title (str): plot title
#   Returns:
def plot_and_save_line(x, y, out_file):
	fig, ax = plt.subplots()
	ax.plot(x, y)
	fig.savefig(out_file)
	return fig, ax
#       tuple: (fig, ax) from matplotlib
#   Description:
#       Create a line plot using Matplotlib object-oriented API (plt.subplots()).
#       Set xlabel="x", ylabel="y" and set the given title.
def plot_on_existing_ax(df, ax):
	df2 = df.copy()
	df2["Sale Date"] = pd.to_datetime(df2["Sale Date"])
	# Use pandas plotting on provided ax
	returned_ax = df2.plot(x="Sale Date", y="Total Sales", ax=ax)
	returned_ax.set_title("Total Sales Over Time")
	return returned_ax
#       Do NOT call plt.show().
#   IMPORTANT:
#       Function name MUST be exactly "make_line_plot".
def histogram_with_bins(df, bins):
	fig, ax = plt.subplots()
	ax.hist(df["value"], bins=bins)
	ax.set_title("Histogram")
	return fig, ax


def simple_subplots(x, y):
	fig, axes = plt.subplots(nrows=2, ncols=1, sharex=True)
	# Top: line
	axes[0].plot(x, y)
	# Bottom: histogram
	axes[1].hist(y, bins=10)
	return fig, axes
# ==========================================
# EXERCISE 3: Lab 8 - Histogram Basics (2 points)
# ==========================================
# TODO:
#   Function Name: make_histogram
#   Parameters:
def plot_sales_dashboard(df, out_file):
	df2 = df.copy()
	df2["date"] = pd.to_datetime(df2["date"])
	fig, axes = plt.subplots(nrows=2, ncols=1, sharex=True)
	axes[0].plot(df2["date"], df2["sales"])
	axes[1].hist(df2["sales"], bins=10)
	fig.savefig(out_file)
	return fig, axes
#       values (list): list of numeric values
#   Returns:
#       tuple: (fig, ax)
def weekly_mean(df):
	df2 = df.copy()
	df2["timestamp"] = pd.to_datetime(df2["timestamp"])
	df2 = df2.set_index("timestamp")
	weekly = df2.resample("W")["value"].mean().reset_index()
	weekly = weekly.rename(columns={"timestamp": "week", "value": "mean_value"})
	return weekly[["week", "mean_value"]]
#   Description:
#       Create a histogram using Matplotlib OO API with bins=10.
#       Set title EXACTLY: "Value Distribution".
def top_n_days_by_total(df, n):
	df2 = df.copy()
	df2["timestamp"] = pd.to_datetime(df2["timestamp"])
	df2["date"] = df2["timestamp"].dt.date
	grouped = df2.groupby("date", as_index=False)["value"].sum()
	grouped = grouped.rename(columns={"value": "total"})
	grouped = grouped.sort_values(by="total", ascending=False).reset_index(drop=True)
	return grouped[["date", "total"]].head(n)
#       Do NOT call plt.show().
#   IMPORTANT:
def compare_two_metrics(df):
	fig, axes = plt.subplots(nrows=2, ncols=1, sharex=True)
	axes[0].plot(df["a"])
	axes[1].plot(df["b"])
	return fig, axes
#       Function name MUST be exactly "make_histogram".
#       Title must match exactly.
def plot_date_range(df, start_date, end_date):
	df2 = df.copy()
	df2["timestamp"] = pd.to_datetime(df2["timestamp"])
	start = pd.to_datetime(start_date)
	end = pd.to_datetime(end_date)
	mask = (df2["timestamp"] >= start) & (df2["timestamp"] <= end)
	filtered = df2.loc[mask]
	fig, ax = plt.subplots()
	ax.plot(filtered["timestamp"], filtered["value"]) 
	return fig, ax


# ==========================================
# EXERCISE 4: Lab 8 - Bar Plot (Category Counts) (2 points)
# ==========================================
# TODO:
#   Function Name: plot_category_counts
#   Parameters:
#       df (pandas.DataFrame): must contain column "category"
#   Returns:
#       tuple: (fig, ax)
#   Description:
#       Count occurrences of each category and create a bar plot (OO API).
#       Set title EXACTLY: "Category Counts".
#       Do NOT call plt.show().
#   IMPORTANT:
#       Function name MUST be exactly "plot_category_counts".
#       Title must match exactly.


# ==========================================
# EXERCISE 5: Lab 8 - Pandas Line Plot (2 points)
# ==========================================
# TODO:
#   Function Name: pandas_line_plot
#   Parameters:
#       df (pandas.DataFrame): must contain columns "x" and "y"
#   Returns:
#       matplotlib.axes.Axes: the axes returned by pandas plotting
#   Description:
#       Create a line plot using pandas plotting (df.plot(...)).
#       Return the Axes object.
#       Do NOT call plt.show().
#   IMPORTANT:
#       Function name MUST be exactly "pandas_line_plot".


# ==========================================
# SECTION B: MEDIUM (3 Points Each) — 5 Exercises
# ==========================================

# ==========================================
# EXERCISE 6: Daily Aggregation (3 points)
# ==========================================
# TODO:
#   Function Name: daily_totals
#   Parameters:
#       df (pandas.DataFrame): must contain columns "timestamp" and "value"
#   Returns:
#       pandas.DataFrame: DataFrame with EXACT columns ["date", "total"]
#   Description:
#       Convert "timestamp" to datetime.
#       Aggregate values by DATE only (not full timestamp).
#       Sort result by date ascending.
#   IMPORTANT:
#       Function name MUST be exactly "daily_totals".
#       Output columns must match exactly.


# ==========================================
# EXERCISE 7: Line Plot + Save to File (3 points)
# ==========================================
# TODO:
#   Function Name: plot_and_save_line
#   Parameters:
#       x (list): x-values
#       y (list): y-values
#       out_file (str): output file path to save the figure
#   Returns:
#       tuple: (fig, ax)
#   Description:
#       Create a line plot (OO API) and save it to out_file.
#       Do NOT call plt.show().
#   IMPORTANT:
#       Function name MUST be exactly "plot_and_save_line".
#       Must save the figure to the given path.


# ==========================================
# EXERCISE 8: Pandas Plot on Provided Axes (3 points)
# ==========================================
# TODO:
#   Function Name: plot_on_existing_ax
#   Parameters:
#       df (pandas.DataFrame): must contain columns "Sale Date" and "Total Sales"
#       ax (matplotlib.axes.Axes): target axes to plot on
#   Returns:
#       matplotlib.axes.Axes: the same ax after plotting
#   Description:
#       Convert "Sale Date" to datetime.
#       Plot "Total Sales" over "Sale Date" using pandas plotting on the given ax.
#       Set title EXACTLY: "Total Sales Over Time".
#       Do NOT call plt.show().
#   IMPORTANT:
#       Function name MUST be exactly "plot_on_existing_ax".
#       Must plot on the provided ax (not a new figure).
#       Title must match exactly.


# ==========================================
# EXERCISE 9: Histogram with Custom Bins (3 points)
# ==========================================
# TODO:
#   Function Name: histogram_with_bins
#   Parameters:
#       df (pandas.DataFrame): must contain column "value"
#       bins (int): number of bins for histogram
#   Returns:
#       tuple: (fig, ax)
#   Description:
#       Plot a histogram of df["value"] using OO API with the given bins.
#       Set title EXACTLY: "Histogram".
#       Do NOT call plt.show().
#   IMPORTANT:
#       Function name MUST be exactly "histogram_with_bins".
#       Title must match exactly.


# ==========================================
# EXERCISE 10: Simple Subplots (3 points)
# ==========================================
# TODO:
#   Function Name: simple_subplots
#   Parameters:
#       x (list): x-values
#       y (list): y-values
#   Returns:
#       tuple: (fig, axes)
#   Description:
#       Create a figure with 2 subplots (nrows=2, ncols=1, sharex=True).
#       Top subplot: line plot of x vs y.
#       Bottom subplot: histogram of y with bins=10.
#       Do NOT call plt.show().
#   IMPORTANT:
#       Function name MUST be exactly "simple_subplots".


# ==========================================
# SECTION C: HARD (5 Points Each) — 5 Exercises
# ==========================================

# ==========================================
# EXERCISE 11: Sales Dashboard (5 points)
# ==========================================
# TODO:
#   Function Name: plot_sales_dashboard
#   Parameters:
#       df (pandas.DataFrame): must contain columns "date" and "sales"
#       out_file (str): output file path to save the figure
#   Returns:
#       tuple: (fig, axes)
#   Description:
#       Create a 2-row dashboard (subplots).
#       Row 1: line plot of sales over date.
#       Row 2: histogram of sales with bins=10.
#       Save the figure to out_file.
#       Do NOT call plt.show().
#   IMPORTANT:
#       Function name MUST be exactly "plot_sales_dashboard".
#       Must save figure.


# ==========================================
# EXERCISE 12: Weekly Mean with DateTimeIndex (5 points)
# ==========================================
# TODO:
#   Function Name: weekly_mean
#   Parameters:
#       df (pandas.DataFrame): must contain columns "timestamp" and "value"
#   Returns:
#       pandas.DataFrame: DataFrame with EXACT columns ["week", "mean_value"]
#   Description:
#       Convert "timestamp" to datetime and set it as DateTimeIndex.
#       Compute weekly mean values using weekly resampling.
#   IMPORTANT:
#       Function name MUST be exactly "weekly_mean".
#       Output columns must match exactly.


# ==========================================
# EXERCISE 13: Top N Days by Total Value (5 points)
# ==========================================
# TODO:
#   Function Name: top_n_days_by_total
#   Parameters:
#       df (pandas.DataFrame): must contain columns "timestamp" and "value"
#       n (int): number of top days to return
#   Returns:
#       pandas.DataFrame: DataFrame with EXACT columns ["date", "total"]
#   Description:
#       Aggregate values by DATE and compute total per day.
#       Return only the top N days by total (descending).
#   IMPORTANT:
#       Function name MUST be exactly "top_n_days_by_total".
#       Output columns must match exactly.


# ==========================================
# EXERCISE 14: Compare Two Metrics (5 points)
# ==========================================
# TODO:
#   Function Name: compare_two_metrics
#   Parameters:
#       df (pandas.DataFrame): must contain numeric columns "a" and "b"
#   Returns:
#       tuple: (fig, axes)
#   Description:
#       Create 2 subplots (nrows=2, ncols=1, sharex=True).
#       Plot df["a"] as a line in the first axes.
#       Plot df["b"] as a line in the second axes.
#       Do NOT call plt.show().
#   IMPORTANT:
#       Function name MUST be exactly "compare_two_metrics".


# ==========================================
# EXERCISE 15: Date Range Filter + Plot (5 points)
# ==========================================
# TODO:
#   Function Name: plot_date_range
#   Parameters:
#       df (pandas.DataFrame): must contain columns "timestamp" and "value"
#       start_date (str): start date string
#       end_date (str): end date string
#   Returns:
#       tuple: (fig, ax)
#   Description:
#       Convert "timestamp" to datetime.
#       Filter rows between start_date and end_date (inclusive).
#       Create a line plot of filtered values over time.
#       Do NOT call plt.show().
#   IMPORTANT:
#       Function name MUST be exactly "plot_date_range".
