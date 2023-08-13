import urllib.request as req
import bs4 as bs
import html5lib

url = req.Request(url="https://docs.python.org/zh-tw/3/howto/urllib2.html",\
                  headers={\
    "User-Agent": \
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.79"\
    })

with req.urlopen(url=url) as webPage:

    data = webPage.read().decode("UTF-8")
    analyzer = bs.BeautifulSoup(data, "html5lib")
    items = analyzer.find("section", id="introduction")

    print(analyzer.title.string)
    print(items)
    '''
    counter = 0
    for item in items:
        counter += 1
        print(f"{counter}:\t{item}")
    '''