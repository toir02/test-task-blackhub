import asyncio

from selenium import webdriver

from selenium.webdriver.chrome.options import Options


async def get_page_content(path) -> str:
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(f"https://blackrussia.online/{path}/")
        await asyncio.sleep(5)
        content = driver.page_source
        return content
    finally:
        driver.close()
