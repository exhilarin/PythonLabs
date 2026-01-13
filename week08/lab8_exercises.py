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
#       Preserve input order.
#   Note:
#       date_strings may include both "YYYY-MM-DD" and "YYYY-MM-DD HH:MM" formats.
#   IMPORTANT:
#       Function name MUST be exactly "parse_and_enrich_dates".


def parse_and_enrich_dates(date_strings):
    """Convert date strings to datetime and extract features."""
    dates = pd.to_datetime(date_strings, format='mixed')
    df = pd.DataFrame({
        "datetime": dates,
        "year": dates.year,
        "month": dates.month,
        "day": dates.day,
        "day_name": dates.day_name(),
        "is_leap_year": dates.is_leap_year
    })
    return df


# ==========================================
# EXERCISE 2: Week 7 Reminder - OO Line Plot (2 points)
# ==========================================
# TODO:
#   Function Name: make_line_plot
#   Parameters:
#       x (list): x-values
#       y (list): y-values
#       title (str): plot title
#   Returns:
#       tuple: (fig, ax) from matplotlib
#   Description:
#       Create a line plot using Matplotlib object-oriented API (plt.subplots()).
#       Set xlabel="x", ylabel="y" and set the given title.
#       Do NOT call plt.show().
#   IMPORTANT:
#       Function name MUST be exactly "make_line_plot".


def make_line_plot(x, y, title):
    """Create a line plot with matplotlib OO API."""
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title(title)
    return fig, ax


# ==========================================
# EXERCISE 3: Lab 8 - Histogram Basics (2 points)
# ==========================================
# TODO:
#   Function Name: make_histogram
#   Parameters:
#       values (list): list of numeric values
#   Returns:
#       tuple: (fig, ax)
#   Description:
#       Create a histogram using Matplotlib OO API with bins=10.
#       Set title EXACTLY: "Value Distribution".
#       Do NOT call plt.show().
#   IMPORTANT:
#       Function name MUST be exactly "make_histogram".
#       Title must match exactly.


def make_histogram(values):
    """Create a histogram with matplotlib OO API."""
    fig, ax = plt.subplots()
    ax.hist(values, bins=10)
    ax.set_title("Value Distribution")
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


def plot_category_counts(df):
    """Plot category counts as a bar chart."""
    counts = df["category"].value_counts()
    fig, ax = plt.subplots()
    ax.bar(counts.index, counts.values)
    ax.set_title("Category Counts")
    return fig, ax


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


def pandas_line_plot(df):
    """Create a line plot using pandas plotting."""
    ax = df.plot(x="x", y="y", kind="line")
    return ax


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


def daily_totals(df):
    """Aggregate values by date (daily totals)."""
    df_copy = df.copy()
    df_copy["timestamp"] = pd.to_datetime(df_copy["timestamp"])
    df_copy["date"] = df_copy["timestamp"].dt.date
    result = df_copy.groupby("date")["value"].sum().reset_index()
    result.columns = ["date", "total"]
    result = result.sort_values("date")
    return result


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


def plot_and_save_line(x, y, out_file):
    """Create a line plot and save it to a file."""
    fig, ax = plt.subplots()
    ax.plot(x, y)
    fig.savefig(out_file)
    return fig, ax


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


def plot_on_existing_ax(df, ax):
    """Plot on an existing matplotlib axes."""
    df_copy = df.copy()
    df_copy["Sale Date"] = pd.to_datetime(df_copy["Sale Date"])
    df_copy.plot(x="Sale Date", y="Total Sales", ax=ax, legend=False)
    ax.set_title("Total Sales Over Time")
    return ax


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


def histogram_with_bins(df, bins):
    """Create a histogram with custom bins."""
    fig, ax = plt.subplots()
    ax.hist(df["value"], bins=bins)
    ax.set_title("Histogram")
    return fig, ax


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


def simple_subplots(x, y):
    """Create 2 subplots: line plot and histogram."""
    fig, axes = plt.subplots(nrows=2, ncols=1, sharex=True)
    
    # Top subplot: line plot
    axes[0].plot(x, y)
    
    # Bottom subplot: histogram
    axes[1].hist(y, bins=10)
    
    return fig, axes


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


def plot_sales_dashboard(df, out_file):
    """Create a sales dashboard with line plot and histogram."""
    fig, axes = plt.subplots(nrows=2, ncols=1)
    
    # Convert date to datetime
    df_copy = df.copy()
    df_copy["date"] = pd.to_datetime(df_copy["date"])
    
    # Row 1: line plot of sales over date
    axes[0].plot(df_copy["date"], df_copy["sales"])
    axes[0].set_title("Sales Over Time")
    
    # Row 2: histogram of sales
    axes[1].hist(df_copy["sales"], bins=10)
    axes[1].set_title("Sales Distribution")
    
    # Save the figure
    fig.savefig(out_file)
    
    return fig, axes


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


def weekly_mean(df):
    """Compute weekly mean values using resampling."""
    df_copy = df.copy()
    df_copy["timestamp"] = pd.to_datetime(df_copy["timestamp"])
    df_copy = df_copy.set_index("timestamp")
    
    # Resample by week and compute mean
    weekly = df_copy["value"].resample("W").mean()
    
    # Convert back to DataFrame with required columns
    result = pd.DataFrame({
        "week": weekly.index,
        "mean_value": weekly.values
    })
    
    return result


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


def top_n_days_by_total(df, n):
    """Get top N days by total value."""
    df_copy = df.copy()
    df_copy["timestamp"] = pd.to_datetime(df_copy["timestamp"])
    df_copy["date"] = df_copy["timestamp"].dt.date
    
    # Group by date and sum
    daily = df_copy.groupby("date")["value"].sum().reset_index()
    daily.columns = ["date", "total"]
    
    # Sort descending and get top N
    daily = daily.sort_values("total", ascending=False).head(n)
    
    return daily


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


def compare_two_metrics(df):
    """Compare two metrics in separate subplots."""
    fig, axes = plt.subplots(nrows=2, ncols=1, sharex=True)
    
    # Plot metric a
    axes[0].plot(df["a"])
    axes[0].set_title("Metric A")
    
    # Plot metric b
    axes[1].plot(df["b"])
    axes[1].set_title("Metric B")
    
    return fig, axes


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


def plot_date_range(df, start_date, end_date):
    """Plot values within a date range."""
    df_copy = df.copy()
    df_copy["timestamp"] = pd.to_datetime(df_copy["timestamp"])
    
    # Filter by date range (inclusive)
    start = pd.to_datetime(start_date)
    end = pd.to_datetime(end_date)
    filtered = df_copy[(df_copy["timestamp"] >= start) & (df_copy["timestamp"] <= end)]
    
    # Create line plot
    fig, ax = plt.subplots()
    ax.plot(filtered["timestamp"], filtered["value"])
    ax.set_xlabel("Date")
    ax.set_ylabel("Value")
    
    return fig, ax
