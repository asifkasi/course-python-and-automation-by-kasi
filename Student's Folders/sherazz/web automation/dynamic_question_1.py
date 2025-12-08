from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get("https://www.scrapethissite.com/pages/ajax-javascript/#2015")



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
table

rows= table.find_all('tr')[0]
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

list
import pandas as pd 
df = pd.DataFrame(list)
df
df.to_csv('scrapthisside_Q_1_1.csv',index=False)
df

