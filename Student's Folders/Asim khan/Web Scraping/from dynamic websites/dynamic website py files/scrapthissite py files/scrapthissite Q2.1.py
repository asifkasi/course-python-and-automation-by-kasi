# 2.1 Extract first Testudines details save into csv file. e.g# Carettochelyidae
from  selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
driver=webdriver.Chrome()
driver.get('https://www.scrapethissite.com/pages/frames/')
time.sleep(5)
driver.switch_to.frame(0)
soup=BeautifulSoup(driver.page_source,'html')
div=soup.find('div',class_='col-md-4 turtle-family-card')
list=[]
dic={
    'turtle_name':'',
    'url':'',
    'img_url':'',
}
base_url='https://www.scrapethissite.com/'
dic['turtle_name']=div.find('h3').text.strip()
dic['url']=base_url+div.find('a')['href']
dic['img_url']=div.find('img')['src']
list.append(dic)
driver.quit()
df1=pd.DataFrame(list)
df1.to_csv('scrapthissite q2.1.csv',index=False)
df1
