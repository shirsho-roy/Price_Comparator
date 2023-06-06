from bs4 import BeautifulSoup
import requests
from flipkart import *
from amazon import *


def convert(a):
    b=a.replace(" ",'')
    c=b.replace("INR",'')
    d=c.replace(",",'')
    f=d.replace("₹",'')
    g=int(float(f))
    return g

name=input("Product Name:\n")
flipkart_price=flipkart(name)
amazon_price=amazon(name)


if flipkart_price=='0':
    print("Flipkart: No product found!")
    flipkart_price = int(flipkart_price)
else:
    print("\nFlipkart Price:",flipkart_price)
    flipkart_price=convert(flipkart_price)
if amazon_price=='0':
    print("Amazon: No product found!")
    amazon_price = int(amazon_price)
else:
    print("\nAmazon price: ₹",amazon_price)
    amazon_price=convert(amazon_price)