import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.ca/Sony-Full-Frame-Mirrorless-Interchangeable-Lens-ILCE7M3K/dp/B07B45D8WV/ref=sr_1_1?dchild=1&keywords=sony+a7&qid=1620780952&sr=8-1'

headers = {"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15', 'Cache-Control':'no-cache', "Pragma":"no-cache"}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = price
    converted_price = converted_price.replace(',',"")
    converted_price = float(converted_price[1:])

    if(converted_price < 3000):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('angelding27@gmail.com', 'tgsnwhwlapbqggez')

    subject = 'Price fell down!'
    body = 'Check the amazon link: https://www.amazon.ca/Sony-Full-Frame-Mirrorless-Interchangeable-Lens-ILCE7M3K/dp/B07B45D8WV/ref=sr_1_1?dchild=1&keywords=sony+a7&qid=1620780952&sr=8-1'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'angelding27@gmail.com',
        'angelding27@gmail.com',
        msg=msg
    )

    print("Email has been sent!")

    server.quit()

while(True):
    check_price()
    time.sleep(3600*24)