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
  # Google 一共有三層class (LC20lb MBeuO DKV0Md)，一層一層找
  layer1 = driver.find_elements(By.CLASS_NAME,"main")
  layer2 = layer1.find_elements(By.CLASS_NAME,"LC20lb")

  for fragment in layer2:
    print(fragment.text)


  input("如果看到此訊息，表示一切執行正常，請按任意鍵終止程式。")
