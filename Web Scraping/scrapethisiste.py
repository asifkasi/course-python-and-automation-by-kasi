import requests
from bs4 import BeautifulSoup
import pandas as pd

url ="https://www.scrapethissite.com/pages/"

r = requests.get(url)

print(r.status_code)

soup = BeautifulSoup(r.text,"html")
# print(soup)

# divs = soup.find("div",class_="page") #it will give the first one
divs = soup.find_all("div",class_="page") #it will give all divs in list

for div in divs:
    print("(***********)")
    
    print("h3 value: ",div.find("h3").text)
    print("p value: ",div.find("p").text)





