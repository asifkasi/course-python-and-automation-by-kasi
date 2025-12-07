from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd 

driver = webdriver.Edge() # to get webdriver to edge
url= ("https://www.scrapethissite.com/pages/ajax-javascript/") # to get the url 
driver.get(url)
list=[]
for j in range(2015,2009,-1): # for inner loop is 15 to 9 datas
    driver.find_element("xpath",f'//a[@id={j}]').click() # difrent file are element to chcek and click to  secand wibsite
    print(j) # print j this is all wibsite data
    time.sleep(3) # this a timer 
    soup = BeautifulSoup(driver.page_source, 'html.parser') # to website html code 
    tbs = soup.find_all('table',class_='table')[0] # to all table find 
    trs = tbs.find_all('tr') # to all find tr
    
    for i in trs[1:]: # for outer loop dict to control all data 
        dict_data = {
        'Title':'',
        'Nominations':'',
        'Best Picture':'',
        'Awards':'',

        }
        dict_data['Title']=i.find('td').text

        dict_data['Nominations']=i.find('td',class_='film-nominations').text
        dict_data['Awards']=i.find('td',class_='film-awards').text
        list.append(dict_data.copy()) # all data are append to list

df = pd.DataFrame(list) # to convert to data frame 
folder_path = r"C:\Users\T460\web scraping\course-python-and-automation-by-kasi\Student's Folders\abdur rehman\from_dynamic_wibsite"
file_name = "\q1_8_by_py.csv"
path = folder_path + file_name
path
df.to_csv(path,index=False)# to save into csv file 
print('code finished with zero error')


