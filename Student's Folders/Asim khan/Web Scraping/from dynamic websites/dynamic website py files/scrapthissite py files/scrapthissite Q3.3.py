# 3.3 Extract all Testudines family details save into csv file.
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
import requests

driver=webdriver.Chrome()
driver.get('https://www.scrapethissite.com/pages/frames/')
time.sleep(5)
driver.switch_to.frame(0)
soup=BeautifulSoup(driver.page_source,'html')
firs_row=soup.find_all('div',class_='col-md-4 turtle-family-card')
list1=[]
for i in firs_row:
    dictionary={
        'turtle_name':'',
        'url':'',
        'img_url':'',
        'detail':'',  
    }
    base_url='https://www.scrapethissite.com/'
    dictionary['turtle_name']=i.find('h3').text.strip()
    dictionary['url']=base_url+i.find('a')['href']
    dictionary['img_url']=i.find('img')['src']
    ## method 1 for inner static websites scraping
    main_url=dictionary['url']
    r=requests.get(main_url)
    soup=BeautifulSoup(r.text,'html.parser')
    dictionary['detail']=soup.find('p',class_='lead').text.strip()
    ## method 2 for inner dynamic websites scraping
    # main_url=dictionary['url']
    # driver.get(main_url)
    # dictionary['detail']=driver.find_element('xpath',"//p[@class='lead']").text.strip()
    list1.append(dictionary)
driver.quit()
df=pd.DataFrame(list1)
df.to_csv('scrapthissite_q_3.3.csv',index=False)
df