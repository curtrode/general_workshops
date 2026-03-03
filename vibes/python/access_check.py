"""
Workshop Demo — Script 1: Who lets you in?

Hit two URLs with a simple GET request and compare the status codes.
Open-Meteo is a free public API — it welcomes requests.
LinkedIn is a commercial site — it blocks automated access.

Vibe coding prompt that produced this:
"Write Python that uses the requests library to check if two URLs are
accessible. Print the status code for each. Use Open-Meteo's API and
a LinkedIn profile page."
"""

import requests

urls = {
    "Open-Meteo (public API)": "https://api.open-meteo.com/v1/forecast?latitude=32.75&longitude=-97.33&daily=temperature_2m_max&timezone=America/Chicago",
    "LinkedIn (commercial site)": "https://www.linkedin.com/in/williamshakespeare/",
}

for label, url in urls.items():
    try:
        response = requests.get(url, timeout=10)
        print(f"{label}")
        print(f"  URL:    {url}")
        print(f"  Status: {response.status_code}")
        print()
    except requests.RequestException as e:
        print(f"{label}")
        print(f"  URL:    {url}")
        print(f"  Error:  {e}")
        print()
