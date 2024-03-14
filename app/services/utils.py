import asyncio

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


async def get_page_content(path) -> str:
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    service = Service(executable_path="/usr/local/bin/chromedriver")
    driver = webdriver.Chrome(
        options=chrome_options,
        service=service
    )

    try:
        driver.get(f"https://blackrussia.online/{path}/")
        await asyncio.sleep(5)
        content = driver.page_source
        return content
    finally:
        driver.close()
