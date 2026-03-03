"""
Workshop Demo — Script 3: Analyze the forecast

Load forecast.csv (produced by fetch_weather.py) and answer a few
simple questions about the data using pandas.

Vibe coding prompt that produced this:
"Write Python that loads forecast.csv with pandas. It has columns: date,
high_f, low_f. Print the warmest day, the coolest night, and the average
high temperature for the week."
"""

import pandas as pd

df = pd.read_csv("forecast.csv")

# Warmest day
warmest = df.loc[df["high_f"].idxmax()]
print(f"Warmest day:     {warmest['date']} — High of {warmest['high_f']}°F")

# Coolest night
coolest = df.loc[df["low_f"].idxmin()]
print(f"Coolest night:   {coolest['date']} — Low of {coolest['low_f']}°F")

# Average high
avg_high = df["high_f"].mean()
print(f"Average high:    {avg_high:.1f}°F")

# Temperature spread each day
df["spread"] = df["high_f"] - df["low_f"]
biggest_swing = df.loc[df["spread"].idxmax()]
print(f"Biggest swing:   {biggest_swing['date']} — {biggest_swing['spread']:.1f}°F difference")

print()
print("Full forecast:")
print(df.to_string(index=False))
