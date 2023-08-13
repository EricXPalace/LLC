import urllib.request as req
from bs4 import BeautifulSoup as bs

def ptt_login(url):
    return req.urlopen(req.Request(url, headers={
    "Cookie":"over18=1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82",
}))

url="https://www.ptt.cc/bbs/Gossiping/index1.html"
    
titlenum = 0
for count in range(5):
        
    soup = bs(ptt_login(url).read().decode("utf-8"), "html.parser")

    titles = soup.find_all('div', class_="title")
    for title in titles:
        titlenum += 1
        if title.a is not None:
            print(f"{titlenum}:\t{title.a.string}")
        
    print("============================================")

    next_page_button = soup.find('a',string="下頁 ›").get("href")
    # last_page_button = soup.find('a',string="‹ 上頁").get("href")
    url = f"https://www.ptt.cc{next_page_button}"


    




        
    
