from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

option = Options()
# This line was abandon as Selenium is now pre-installed webdriver on it.
# option.chrome_executable_path = "C:\Users\USER\coding\Day05\chromedriver.exe"

with webdriver.Chrome(options=option) as driver:
    driver.get("https://www.selenium.dev/documentation/")

    tags = driver.find_elements(By.CLASS_NAME, "td-content")
    for tag in tags:
        print(tag.text)

    print("=====================================================================")

    link = driver.find_element(By.LINK_TEXT, "Watch the Videos")
    link.click()

    print("=====================================================================")




