from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome()
driver.get("https://www.scrapethissite.com/pages/ajax-javascript/#2014")
time.sleep(2)


soup = BeautifulSoup(driver.page_source, 'html.parser')
soup
table= soup.find_all('tr',class_='film')
time.sleep(2)
list = []
for i in table:
    dict_data = {
    'Title':'',
    'Nominations':'',
    'Best Picture':'',
    'Awards':'',

    }
    dict_data['Title']=i.find('td').text

    dict_data['Nominations']=i.find('td',class_='film-nominations').text
    dict_data['Awards']=i.find('td',class_='film-awards').text
    list.append(dict_data)

list
import pandas as pd 
df = pd.DataFrame(list)
folder_path = r"C:\Users\T460\web scraping\course-python-and-automation-by-kasi\Student's Folders\abdur rehman\from_dynamic_wibsite"
file_name = "\q1_2_by_py.csv"
path = folder_path + file_name
path
df.to_csv(path,index=False)# to save into csv file 
print('code finished with zero error')