import requests
from bs4 import BeautifulSoup
URl = "https://www.amazon.in/Pigeon-Stovekraft-Plastic-Chopper-Blades/dp/B01LWYDEQ7/ref=sr_1_5?dchild=1&keywords=chopper&qid=1602706714&sr=8-5"
headers = {
    "user-agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

page = requests.get(URl, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

# print(soup.prettify())

product_title = soup.find(id="productTitle").get_text()
print(product_title.strip())

product_price = soup.find(id="priceblock_ourprice").get_text()
converted_price = int(product_price[1:5])
print(converted_price)
