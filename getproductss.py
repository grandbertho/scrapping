import requests
from bs4 import BeautifulSoup
import random

url = "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt"

headers = {
  "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
  "Accept-Encoding" : "gzip, deflate, br",
  "Accept-Language" : "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
  "Cache-Control" : "max-age=0",
  "Connection" : "keep-alive",
  "Host" : "shield.pythonanywhere.com",
  "sec-ch-ua" : "\"Google Chrome\";v=\"111\", \"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"111\"",
  "sec-ch-ua-mobile" : "?1",
  "sec-ch-ua-platform" : "\"Android\"",
  "Sec-Fetch-Dest" : "document",
  "Sec-Fetch-Mode" : "navigate",
  "Sec-Fetch-Site" : "none",
  "Sec-Fetch-User" : "?1",
  "Upgrade-Insecure-Requests" : "1",
  "User-Agent" : "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36",
}

website = requests.get(url)

proxybs = BeautifulSoup(website.content,"html.parser")

proxylist = proxybs.get_text().strip().split("\n")

productlistmap = []

i = 1

while True:
    proxy = random.choice(proxylist)
    try:
        res = requests.get(f"https://shield.pythonanywhere.com/?page={i}",headers=headers,proxies={"http":proxy},timeout=5)
        print(res)
        if res.status_code == 200:
            websitebs = BeautifulSoup(res.content,"html.parser")

            productlistcard = websitebs.find_all("div",{"class":"card-body"})

            for product in productlistcard:
                productlistmap.append({"name":product.find("h5",{"class":"card-title"}).get_text(),
                                    "prix":product.find("p",{"class":"card-price"}).get_text(),
                                    "description":product.find("p",{"class":"card-text"}).get_text()})
            i=i+1
        if i == 10:
            break
    except :
        pass

print(f"Longueur de la liste : {len(productlistmap)}")

for product in productlistmap:
    print(product)