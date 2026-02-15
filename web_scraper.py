import requests
from bs4 import BeautifulSoup
import csv
url="https://books.toscrape.com/"
headers={"User-Agent":"Mozilla/5.0"}
try:
    response=requests.get(url,headers=headers,timeout=10)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Request failed:",e)
    exit()
soup=BeautifulSoup(response.text,"html.parser")
books=soup.find_all("article",class_="product_pod")
with open("books.csv","w",newline="",encoding="utf-8") as file:
    writer=csv.writer(file)
    writer.writerow(["Title","Price","Availability","Link"])
    for book in books:
        title=book.h3.a["title"] if book.h3 and book.h3.a else "N/A"
        price=book.find("p",class_="price_color").text if book.find("p",class_="price_color") else "N/A"
        availability=book.find("p",class_="instock availability").text.strip() if book.find("p",class_="instock availability") else "N/A"
        link="https://books.toscrape.com/"+book.h3.a["href"] if book.h3 and book.h3.a else "N/A"
        writer.writerow([title,price,availability,link])
print("Data scraped and saved to books.csv successfully.")