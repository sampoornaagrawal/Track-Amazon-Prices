import requests
from bs4 import BeautifulSoup
import smtplib
import time

URl = "https://www.amazon.in/Pigeon-Stovekraft-Plastic-Chopper-Blades/dp/B01LWYDEQ7/ref=sr_1_5?dchild=1&keywords=chopper&qid=1602706714&sr=8-5"
headers = {
    "user-agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()  # establish connection
    server.starttls()  # encrypt connection
    server.ehlo()

    server.login('babarandom5@gmail.com', 'babarandom123')
    subject = "PRICE FELL DOWN !!!"
    body = 'check the amazon link : https://www.amazon.in/Pigeon-Stovekraft-Plastic-Chopper-Blades/dp/B01LWYDEQ7/ref=sr_1_5?dchild=1&keywords=chopper&qid=1602706714&sr=8-5'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'babarandom5@gmail.com',
        'sampoorna.agrawal01_2017@galgotiasuniversity.edu.in',
        msg
    )

    print("Hey! E-mail has been sent")
    server.quit()


def check_price():
    page = requests.get(URl, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup.prettify())

    product_title = soup.find(id="productTitle").get_text()
    product_price = soup.find(id="priceblock_ourprice").get_text()

    converted_price = int(product_price[1:5])

    # print(product_price)
    # print(converted_price)

    if(converted_price < 250):
        send_mail()


check_price()

# choose the time gap when you want to run it.
"""
while(True):
    check_price()
    time.sleep(60*60)
"""
