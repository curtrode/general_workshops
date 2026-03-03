import requests

url = "https://www.imdb.com/title/tt31193180/reviews/"

response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
print(f"Status: {response.status_code}")
