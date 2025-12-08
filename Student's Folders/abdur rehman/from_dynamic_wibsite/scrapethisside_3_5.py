from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
from urllib.parse import urljoin
import requests 

driver = webdriver.Edge() # to get webdriver to edge
url= ("https://www.scrapethissite.com/pages/frames/") # to get the url 
driver.get(url)
driver.switch_to.frame(0)
driver.find_element("xpath",'//h3').text
soup = BeautifulSoup(driver.page_source,('html'))
frm = soup.find_all('div',class_='col-md-4 turtle-family-card')
frm
list =[]



for i in frm[1:14:3]:
    base_url = 'https://www.scrapethissite.com/'
    dict = {
        'name':'',
        'url':'',
        'img_url':'',
        "detail":'',
    }
    dict ['img_url']=i.find('img')['src']
    dict ['url']=base_url + i.find('a')['href']
    dict ['name']=i.find('h3').text
    
    inner_url = dict["url"] # inner url
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(inner_url, headers=headers)
    soup_nw = BeautifulSoup(resp.text, "html.parser")
    # soup_nw
    dict["detail"]=soup_nw.find('p').text.strip()# all url details
    
    list.append(dict)
df = pd.DataFrame(list)
folder_path = r"C:\Users\T460\web scraping\course-python-and-automation-by-kasi\Student's Folders\abdur rehman\from_dynamic_wibsite"
file_name = "\q3_5_by_py.csv"
path = folder_path + file_name
path
#%%


df.to_csv(path,index=False)# to save into csv file
