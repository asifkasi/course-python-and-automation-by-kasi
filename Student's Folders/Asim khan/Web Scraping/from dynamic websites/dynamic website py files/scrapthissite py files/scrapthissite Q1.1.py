from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

driver=webdriver.Chrome()
driver.get('https://www.scrapethissite.com/pages/ajax-javascript/#2015')
time.sleep(5)

soup=BeautifulSoup(driver.page_source,'html')
table=soup.find_all('tr',class_='film')
list=[]
for i in table:
    dic={
        'Tittle':'',
        'Nomination':'',
        'Awards':'',
        'Best_pictures':'',
    }
    dic['Tittle']=i.find('td',class_='film-title').text.strip()
    dic['Nomination']=i.find('td',class_='film-nominations').text.strip()
    dic['Awards']=i.find('td',class_='film-awards')
    #dic['Best_pictures']=i.find
    list.append(dic)
list
df=pd.DataFrame(list)
df
df.to_csv('scrapthissite q1.csv',index=False)