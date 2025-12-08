from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd 
import time
driver = webdriver.Chrome()
driver.get("https://www.scrapethissite.com/pages/ajax-javascript/#2015")
time.sleep(2)


soup = BeautifulSoup(driver.page_source, 'html.parser')
soup
dict_data = {
    'Title':'',
    'Nominations':'',
    'Best Picture':'',
    'Awards':'',

}
# soup.find_all('div',class_="col-md-12")[0].find_all('table")[0]
table= soup.find_all('div',class_="col-md-12")[4]
time.sleep(2)
# table

rows= table.find_all('tr')[1]
rows
rows= table.find_all('tr',class_='film')
rows
list = []
for i in rows:
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



df = pd.DataFrame(list)
folder_path = r"C:\Users\T460\web scraping\course-python-and-automation-by-kasi\Student's Folders\abdur rehman\from_dynamic_wibsite"
file_name = "\q1_1_by_py.csv"
path = folder_path + file_name
path
df.to_csv(path,index=False)# to save into csv file 
print('code finished with zero error')