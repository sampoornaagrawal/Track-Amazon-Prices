import requests
from bs4 import BeautifulSoup
URl = "https://www.amazon.in/Apple-MacBook-16-inch-Storage-Intel-Core-i7/dp/B081JWZQJB/ref=sr_1_3?dchild=1&keywords=macbook+pro&qid=1602705225&sr=8-3"
headers = {
    "user-agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

page = requests.get(URl, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

# print(soup.prettify())

product_title = soup.find(id="productTitle").get_text()
print(product_title.strip())
