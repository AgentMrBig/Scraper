# Scrape Any Website with Playwright (Beginner Tutorial)

This quick Python script shows you how to scrape headlines from any website using Playwright.

---

## Requirements

- Python 3.7+
- Playwright

---

## Setup Instructions

1. **Install Playwright and dependencies:**

```bash
pip install playwright
playwright install
```

2. **Save the following code into a file called `scrape_headlines.py`:**

```python
import asyncio
from playwright.async_api import async_playwright

async def scrape():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto('https://www.cnn.com')

        headlines = await page.query_selector_all('h1, h2')

        for h in headlines:
            text = await h.inner_text()
            print(text.strip())

        await browser.close()

asyncio.run(scrape())
```

3. **Run the scraper:**

```bash
python scrape_headlines.py
```

---

## What This Script Does

- Launches a Chromium browser.
- Navigates to a website (CNN.com by default).
- Scrapes all `<h1>` and `<h2>` headline elements.
- Prints the headlines neatly in your terminal.

---

## Notes

- You can replace `'https://www.cnn.com'` with any website URL you want to scrape.
- Playwright can be configured for stealth scraping if needed (not covered in this basic example).

---

🔔 For more quick automation tutorials, [subscribe to the YouTube channel](#)!
