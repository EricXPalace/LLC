import urllib.request as req
from bs4 import BeautifulSoup as bs

def mobile01_login(url):
    return req.urlopen(req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82",
}))

main_url="https://www.mobile01.com"    
        
soup = bs(mobile01_login(main_url).read().decode("utf-8"), "html.parser")
next_page = soup.find('a',string="討論區").get("href")
url = f"{main_url}{next_page}"

soup = bs(mobile01_login(url).read().decode("utf-8"), "html.parser")

# 查找所有 `ul` 標籤
ul_tags = soup.find_all("ul")

# 查找每個 `ul` 標籤中的所有 `li` 標籤
li_tags = [li for ul in ul_tags for li in ul.find_all("li")]

# 獲取每個 `li` 標籤中的文字
li_texts = [li.text for li in li_tags]

# 打印每個 `li` 標籤中的文字
for li_text in li_texts:
    print(li_text)

print(url)


    




        
    
