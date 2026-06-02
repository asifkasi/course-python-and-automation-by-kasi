# 4. Write a Python program to count number of tweets by a given Twitter account.
from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver=webdriver.Chrome()
driver.get('https://x.com/asifokasi')
time.sleep(5)

soup=BeautifulSoup(driver.page_source,'html')
post=soup.find('div',class_='css-146c3p1 r-dnmrzs r-1udh08x r-1udbk01 r-3s2u2q r-bcqeeo r-1ttztb7 r-qvutc0 r-37j5jr r-n6v787 r-1cwl3u0 r-16dba41').text
print(post)