from selenium import webdriver
from bs4 import BeautifulSoup
import time
driver=webdriver.Chrome()
driver.get('https://x.com/asifokasi')
time.sleep(5)
soup=BeautifulSoup(driver.page_source,'html')
divs=soup.find_all('a',class_='css-146c3p1 r-bcqeeo r-1ttztb7 r-qvutc0 r-37j5jr r-a023e6 r-rjixqe r-16dba41 r-1loqt21')[1].text
print(divs)