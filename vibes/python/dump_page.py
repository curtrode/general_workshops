"""Dump the rendered IMDB reviews page HTML so we can inspect the actual selectors."""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

URL = "https://www.imdb.com/title/tt31193180/reviews/"

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                     "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=options)
driver.get(URL)
time.sleep(5)

with open("page_dump.html", "w", encoding="utf-8") as f:
    f.write(driver.page_source)

print(f"Page title: {driver.title}")
print(f"Page length: {len(driver.page_source)} chars")
print("Saved to page_dump.html")
driver.quit()
