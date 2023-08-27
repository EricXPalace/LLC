from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# Replit 用的環境設定，本地環境上可以全部砍掉
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

with webdriver.Chrome(options=chrome_options) as driver:
  driver.maximize_window()
  # 取得聯成電腦官網的連結
  driver.get("https://member.lccnet.com.tw/")
  print("[LOG] driver: get succeed.")
  # 輸入我自己的帳戶密碼登入
  driver.find_element(By.ID ,'Account').send_keys("105684713")
  driver.find_element(By.ID ,'Password').send_keys("A128450607")
  driver.find_element(By.CLASS_NAME ,'loginBtn').click()
  print("[LOG] Login prograss succeed.")
  # 找到我要工作點擊
  driver.find_element(By.TAG_NAME, "我要就業").click()

  input("如果看到此訊息，表示一切執行正常，請按任意鍵終止程式。")
