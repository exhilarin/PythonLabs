## 🧾 Cheatsheet — Lab 8 (DateTime & Visualization)

- Always be aware of whether your data is stored as **strings** or as **datetime objects**.
  Many date-related operations only work correctly after conversion.

- In Matplotlib, there is a difference between:

  - creating a new figure and axes
  - plotting on an existing axes object  
    Reading the function description carefully helps avoid mistakes.

- Date strings in real datasets are not always in a single, uniform format.
  Pandas can often infer formats automatically, but assumptions may lead to errors.

- **Mixed date formats edge case**: When your date strings have different formats
  (e.g., `"2024-02-02 12:38"` and `"2023-12-03"`), use `format='mixed'`:
  ```python
  pd.to_datetime(date_strings, format='mixed')
  ```
  This allows Pandas to infer the format for each element individually.

- When extracting parts of a date (year, month, day, etc.), Pandas typically provides
  specialized accessors designed for datetime data.

- Some plotting functions expect you to **return** the figure or axes,
  rather than displaying it on the screen.

- Aggregating data by time periods (daily, weekly, etc.) usually requires
  converting timestamps before grouping or resampling.

- Pandas plotting functions often return an object that can be further customized
  (titles, labels, limits) after the plot is created.

- Filtering data by date range is more reliable when comparisons are done
  using datetime objects instead of raw strings.

- Different plot types serve different purposes:
  line plots emphasize trends,
  histograms show distributions,
  bar plots compare categories.

- When working with multiple plots in the same figure,
  shared axes can improve readability.

- Index type matters: some time-based operations behave differently
  depending on whether the index is a DateTimeIndex or a regular index.

- Saving a figure to a file is not the same as displaying it.
  Automated testing environments often rely on saved figures.

- The return type of a function is just as important as the visual output it produces.

- Function names and column names are case-sensitive
  and must match the specification exactly.

- Writing clear, step-by-step code is often safer than compact one-liners,
  especially when working with dates and plots.

- Tests usually verify **structure and behavior**, not just the final visual result.
