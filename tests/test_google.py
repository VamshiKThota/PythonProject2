from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_beghou_title():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=option3s)
    driver.get("https://www.beghou.com")

    assert "Beghou" in driver.title


    driver.quit()
