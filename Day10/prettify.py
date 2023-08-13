import urllib.request as req
from bs4 import BeautifulSoup as bs

def chinese_login(url):
    return bs(req.urlopen(req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82",
})).read().decode("utf-8"), "html.parser")

main_url="https://www.google.com"    
        
soup = chinese_login(main_url)

print(soup.prettify())