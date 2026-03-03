"""
Workshop Demo — Script 2: Fetch weather data

Pull a 7-day temperature forecast for Fort Worth, TX from Open-Meteo
(free, no API key needed) and save it to a CSV file.

Vibe coding prompt that produced this:
"Write Python that fetches the 7-day weather forecast for Fort Worth, TX
from the Open-Meteo API. Get the date, high temp, and low temp for each
day. Save the results to a CSV file called forecast.csv."
"""

import csv
import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 32.75,
    "longitude": -97.33,
    "daily": "temperature_2m_max,temperature_2m_min",
    "temperature_unit": "fahrenheit",
    "timezone": "America/Chicago",
}

response = requests.get(url, params=params, timeout=10)
data = response.json()

daily = data["daily"]
rows = []
for i in range(len(daily["time"])):
    rows.append({
        "date": daily["time"][i],
        "high_f": daily["temperature_2m_max"][i],
        "low_f": daily["temperature_2m_min"][i],
    })

# Print to screen
print("7-Day Forecast for Fort Worth, TX")
print("-" * 36)
for row in rows:
    print(f"  {row['date']}  High: {row['high_f']}°F  Low: {row['low_f']}°F")
print()

# Save to CSV
output_file = "forecast.csv"
with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["date", "high_f", "low_f"])
    writer.writeheader()
    writer.writerows(rows)

print(f"Saved to {output_file}")
