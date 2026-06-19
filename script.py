import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import the specific tools we need from Astropy
from astropy.time import Time
from astropy.timeseries import LombScargle
import astropy.units as u

# PART 1: CONVERTING TO ASTRONOMICAL TIME

# Load the clean data
df = pd.read_csv('/home/astrotuk/D/data_02/cleaned_time_series_data.csv')

# Drop any rows where the date or temperature is missing
df = df.dropna(subset=['date', 'temp_celsius'])

# Convert the column into standard Pandas Datetime objects
df['date'] = pd.to_datetime(df['date'])

# Extract them using a safe numpy conversion to avoid deprecation warnings
pure_datetime_list = np.array(df['date'].dt.to_pydatetime()).tolist()

# Pass the clean list directly to Astropy
astro_times = Time(pure_datetime_list)

# Extract Julian Dates as a pure NumPy array for calculations
julian_days = astro_times.jd


# PART 2: ATTACHING PHYSICAL UNITS


# Attach the Celsius unit to our raw temperature numbers
raw_temps = df['temp_celsius'].to_numpy()
temperatures_with_units = raw_temps * u.deg_C

# FIX: Added equivalencies=u.temperature() to handle the Celsius to Kelvin offset math
temperatures_in_kelvin = temperatures_with_units.to(u.K, equivalencies=u.temperature())


# PART 3: FINDING HIDDEN CYCLES (LOMBSCARGLE PERIODOGRAM)

# Calculate the repeating frequencies hidden in the temperature data
frequency, power = LombScargle(julian_days, raw_temps).autopower()

# Find the single strongest repeating cycle (the peak frequency)
best_frequency = frequency[np.argmax(power)]
repeating_period_days = 1 / best_frequency

# PART 4: PRINTING THE RESULTS

print("--- Astropy Time Transformation ---")
print("First 3 standard dates:", df['date'].dt.strftime('%Y-%m-%d').iloc[:3].values)
print("First 3 Julian Dates: ", julian_days[:3])

print("\n--- Astropy Unit Conversion ---")
print("First 3 readings in Celsius:", temperatures_with_units[:3])
print("First 3 readings in Kelvin: ", temperatures_in_kelvin[:3])

print("\n--- Astropy Period Analysis ---")
print(f"The strongest repeating data cycle occurs every: {repeating_period_days:.2f} days")
