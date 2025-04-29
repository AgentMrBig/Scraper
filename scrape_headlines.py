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
