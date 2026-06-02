# 2.2 Extract Testudines family from first row details save into csv file. e.g# Carettochelyidae, Cheloniidae, Chelydridae
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

driver=webdriver.Chrome()
driver.get('https://www.scrapethissite.com/pages/frames/')
time.sleep(5)
driver.switch_to.frame(0)
soup=BeautifulSoup(driver.page_source,'html')
firs_row=soup.find_all('div',class_='col-md-4 turtle-family-card')
list1=[]
for i in firs_row[:3]:
    dictionary={
        'turtle_name':'',
        'url':'',
        'img_url':'',  
    }
    base_url='https://www.scrapethissite.com/'
    dictionary['turtle_name']=i.find('h3').text.strip()
    dictionary['url']=base_url+i.find('a')['href']
    dictionary['img_url']=i.find('img')['src']
    list1.append(dictionary)
driver.quit()
df=pd.DataFrame(list1)
df.to_csv('scrapthissite q2.2.csv',index=False)
df