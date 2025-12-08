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
soup = BeautifulSoup(driver.page_source,'html')
frm = soup.find('div',class_='col-md-4 turtle-family-card')
frm

list = []
base_url = 'https://www.scrapethissite.com/'
dict = {
    'name':'',
    'url':'',
    'img_url':'',
   "detail":'',
}
dict ['img_url']=frm.find('img')['src']
dict ['url']=base_url + frm.find('a')['href']
dict ['name']=frm.find('h3').text
dict
        

act_url = urljoin(base_url,dict["url"])
resp = requests.get(act_url)
soup_nw = BeautifulSoup(resp.text, "html.parser")
soup_nw

dict["detail"]=soup_nw.find('p').text.strip()
list.append(dict)
dict
df = pd.DataFrame(list)

# method 1: Save CSV in specific location
#%%

folder_path = r"C:\Users\T460\web scraping\course-python-and-automation-by-kasi\Student's Folders\abdur rehman\from_dynamic_wibsite"
file_name = "\q3_1_by_py.csv"
path = folder_path + file_name
path
#%%


df.to_csv(path,index=False)# to save into csv file 

# method 2: Save CSV in specific location
# df.to_csv("C:\Users\T460\web scraping\course-python-and-automation-by-kasi\Student's Folders\abdur rehman\from_dynamic_wibsite\q3_1.csv",index=False)# to save into csv file 


print("code finished with zero error")
