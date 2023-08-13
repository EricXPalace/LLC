from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

option = Options()
# This line was abandon as Selenium is now pre-installed webdriver on it.
# option.chrome_executable_path = "C:\Users\USER\coding\Day05\chromedriver.exe"

with webdriver.Chrome(options=option) as driver:
    driver.maximize_window()
    driver.get("https://www.google.com")
    driver.save_screenshot("Day08/googleToday.png")