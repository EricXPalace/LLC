from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# Replit 用的環境設定，本地環境上可以全部砍掉
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

with webdriver.Chrome(options=chrome_options) as driver:  
  driver.get("https://www.google.com")
  
  widget = driver.find_element(By.ID,"APjFqb")
  widget.send_keys("Honda\n")


  input("如果看到此訊息，表示一切執行正常，請按任意鍵終止程式。")
