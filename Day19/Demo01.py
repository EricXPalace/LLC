from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# Replit 用的環境設定，本地環境上可以全部砍掉
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

with webdriver.Chrome(options=chrome_options) as driver:

  driver.maximize_window()
  
  driver.get("https://www.google.com")
  driver.save_screenshot("Google.png")

  driver.get("https://www.mobile01.com/")
  driver.save_screenshot("Mobile01.png")
