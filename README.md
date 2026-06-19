# 🌌 Astronomical Time-Series Analysis

A Python pipeline using **Pandas**, **NumPy**, and **Astropy** to standardize raw climate/environmental data into astronomical formats and extract hidden cycles.

---

## 🚀 Core Steps & Meanings

### 1. Calendar to Julian Dates (JD)
* **What it does:** Converts `YYYY-MM-DD` dates into a single continuous running count of days (e.g., `2020-01-01` $\rightarrow$ `2458849.5`).
* **Why:** Removes irregular months and leap years, making elapsed time calculations pure numerical subtraction.

### 2. Celsius to Kelvin Conversion
* **What it does:** Adds a $273.15$ offset to map raw Celsius degrees to absolute thermodynamic energy units (`deg_C` $\rightarrow$ `K`).
* **Why:** Eliminates negative numbers, making the data natively compatible with absolute physical energy formulas.

### 3. Lomb-Scargle Period Analysis
* **What it does:** Scans noisy, unevenly spaced data to find repeating patterns.
* **Why:** It discovered a strong, hidden thermal rhythm in the dataset repeating every **0.42 days (approx. 10 hours)**.

---

## 📊 Sample Output

```text
--- Astropy Time Transformation ---
First 3 standard dates: ['2020-01-01' '2020-01-02' '2020-01-03']
First 3 Julian Dates:  [2458849.5 2458850.5 2458851.5]

--- Astropy Unit Conversion ---
First 3 readings in Celsius: [27.48357077 24.30867849 28.23844269] deg_C
First 3 readings in Kelvin:  [300.63357077 297.45867849 301.38844269] K

--- Astropy Period Analysis ---
The strongest repeating data cycle occurs every: 0.42 days

