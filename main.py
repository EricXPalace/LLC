from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# Replit 用的環境設定，本地環境上可以全部砍掉
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

with webdriver.Chrome(options=chrome_options) as driver:
  driver.maximize_window()
  
  driver.get("https://member.lccnet.com.tw/")
  print("[LOG] driver: get SUCCESS")
  search_frame = driver.find_element(By.ID ,'Account')
  print("[LOG] search_frame: find_element 'Account' SUCCESS")
  search_frame.send_keys("105684713")
  print("[LOG] search_frame: send_keys SUCCESS")
  search_frame = driver.find_element(By.ID ,'Password')
  print("[LOG] search_frame: find_element 'Password' SUCCESS")
  search_frame.send_keys("A128450607")
  print("[LOG] search_frame: send_keys SUCCESS")
  search_button = driver.find_element(By.CLASS_NAME ,'loginBtn')
  print("[LOG] search_button: find_element SUCCESS")
  search_button.click()
  print("[LOG] search_button: click SUCCESS")

input("如果看到此訊息，表示一切執行正常，請按任意鍵終止程式。")
