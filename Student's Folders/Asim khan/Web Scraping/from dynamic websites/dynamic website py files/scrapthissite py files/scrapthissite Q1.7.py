# 1.7 Extract Tables from year 2015 to 2010 & save into single csv file.

#---- ye sab libraries he---
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

#---har kisam ke browser hote he ye chrome se chalega---
driver = webdriver.Chrome()
url = "https://www.scrapethissite.com/pages/ajax-javascript/"
driver.get(url)

#---csv me lane ke lia ham list banainge---
all_list = []

#--- loof chale ga one by bone 2015 se 2010 tak chale ga---
for year in range(2015, 2009, -1):
    
    #---is se har element ko jake hit karega
    driver.find_element('xpath',f"//a[@id='{year}']").click()

    #---time is lia use howa he ke jab loading hota he tho us time quch nahi hota empty print hota he thora sa wait karne ke lia ye use karte hen
    time.sleep(3)

    #---sourse code lane ke lia---
    soup = BeautifulSoup(driver.page_source, "html.parser")

    #---saray tr mind karenge is se---
    table = soup.find_all("tr", class_="film")

    #---saray trs ke andar jo data he matlab tds wo saray one by one ainge---
    for row in table:

        #---har ak ko dictionary me ad karne ke lia---
        dic = {
            'Title': row.find('td', class_='film-title').text.strip(),
            'Nominations': row.find('td', class_='film-nominations').text.strip(),
            'Awards': row.find('td', class_='film-awards').text.strip(),
        }

        #---dictionary ko list me append karne ke lia---
        all_list.append(dic)

#---jab driver ka kaam khatam hojai tho wo khudhi band hojata he---
driver.quit()

#---poray list ko dataframe me lane ke lia---
df = pd.DataFrame(all_list)

#---csv file create karne ke lia---
df.to_csv("scrap_2015_to_2010.csv", index=False)
df
