from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

option = Options()
# This line was abandon as Selenium is now pre-installed webdriver on it.
# option.chrome_executable_path = "C:\Users\USER\coding\Day05\chromedriver.exe"

with webdriver.Chrome(options=option) as driver:
    driver.get("https://www.selenium.dev/documentation/")

    tag = driver.find_elements(By.CLASS_NAME, "td-content")
    print(tag)

    link = driver.find_elements(By.LINK_TEXT, "")

