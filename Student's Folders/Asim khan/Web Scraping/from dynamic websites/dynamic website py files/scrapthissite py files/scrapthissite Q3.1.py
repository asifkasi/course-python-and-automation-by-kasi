# 3.1 Extract first Testudines details save into csv file. e.g# Carettochelyidae

from  selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
import requests
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
    'detail':'',
}
base_url='https://www.scrapethissite.com/'
dic['turtle_name']=div.find('h3').text.strip()
dic['url']=base_url+div.find('a')['href']
dic['img_url']=div.find('img')['src']
## method 1 for inner static websites
actural_url=dic['url']
r=requests.get(actural_url)
soup=BeautifulSoup(r.text,'html.parser')
dic['detail']=soup.find('p',class_='lead').text.strip()
## method 2 for inner dynamic websites
# actural_url=dic['url']
# driver.get(actural_url)
# time.sleep(3)
# dic['detail']=driver.find_element('xpath',"//p[@class='lead']").text.strip()
list.append(dic)
driver.quit()
df1=pd.DataFrame(list)
df1.to_csv('scrapthissite q3.1.csv',index=False)
df1