"""
Scrape user reviews for 'Sinners' from IMDB.
Uses Selenium to handle JavaScript rendering and Beautiful Soup to parse HTML.

Workshop demo: this is what an AI coding tool would generate from the prompt:
"Using Beautiful Soup, Selenium, and/or other relevant packages, write the PY
that scrapes as many user reviews with their dates of posting as we can for
the film Sinners."
"""

import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

URL = "https://www.imdb.com/title/tt31193180/reviews/"

# Set up headless Chrome
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                     "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=options)
driver.get(URL)

# Wait for reviews to load
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "article.user-review-item"))
    )
except Exception:
    print("Could not find review cards on the page.")
    print("Page title:", driver.title)
    driver.quit()
    exit(1)

# Click "25 more" button until all reviews are loaded
load_more_clicks = 0
while True:
    try:
        load_more = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".ipc-see-more__button"))
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", load_more)
        time.sleep(1)
        load_more.click()
        load_more_clicks += 1
        print(f"Loaded page {load_more_clicks + 1}...")
        time.sleep(3)
    except Exception:
        break

print(f"Clicked 'Load More' {load_more_clicks} time(s).")

# Parse the fully loaded page
soup = BeautifulSoup(driver.page_source, "html.parser")
driver.quit()

# Extract reviews
reviews = []
cards = soup.select("article.user-review-item")

for card in cards:
    # Review title
    title_el = card.select_one("[data-testid='review-summary'] h3")
    title = title_el.get_text(strip=True) if title_el else "N/A"

    # Review text
    text_el = card.select_one("[data-testid='review-overflow'] .ipc-html-content-inner-div")
    text = text_el.get_text(strip=True) if text_el else "N/A"

    # Date
    date_el = card.select_one("li.review-date")
    date = date_el.get_text(strip=True) if date_el else "N/A"

    # Rating (if present)
    rating_el = card.select_one(".ipc-rating-star--rating")
    rating = rating_el.get_text(strip=True) if rating_el else "N/A"

    reviews.append({"date": date, "rating": rating, "title": title, "text": text})

print(f"Scraped {len(reviews)} reviews.\n")

# Print first 5 as preview
for i, r in enumerate(reviews[:5], 1):
    print(f"--- Review {i} ---")
    print(f"Date:   {r['date']}")
    print(f"Rating: {r['rating']}")
    print(f"Title:  {r['title']}")
    print(f"Text:   {r['text'][:200]}...")
    print()

# Save all to CSV
output_file = "sinners_reviews.csv"
with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["date", "rating", "title", "text"])
    writer.writeheader()
    writer.writerows(reviews)

print(f"Saved all reviews to {output_file}")
