
import pandas as pd
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver



# get the of files in folder
path = "files"

import os
import random

df_pg_2_scrape = pd.read_excel("pg_to_scrape.xlsx")

for pg_no in range(1,11):

    files = os.listdir(path)
    all_files = [int(f.replace(".csv","")) for f in files if f.endswith('.csv')]

    df_pg_2_scrape_list = df_pg_2_scrape['pg_no'].tolist()
    remaing_pgs = list(set(df_pg_2_scrape_list) - set(all_files))

    # selecting random number from remaing_pgs list
    random_pg = random.choice(remaing_pgs)

    driver  = webdriver.Chrome()

    url   = f"https://getlatka.com/saas-companies?page={random_pg}"
    driver.get(url)
    time.sleep(5)
    try:
        driver.find_element("xpath","//button[@class='newsletter-popup__close']").click()
    except:
        pass
    soup = BeautifulSoup(driver.page_source,"html")
    trs = soup.find_all("tr",class_ = "data-table_row__aX_dq")
    len(trs)
    lst = []
    for i in range(len(trs)):
        tds_of_each_row = trs[i].find_all("td") # trs[0] matlb 1st row of data, next row k leye trs[1]

        dic = {
            "name": ""
        }

        second_colum_of_row = tds_of_each_row[1] # q k second col me company data han

        all_a_of_2nd_td = second_colum_of_row.find_all("a") # find all a tags

        dic["name"] = all_a_of_2nd_td[0].text # fisrt a k tag k andar company name

        for a in all_a_of_2nd_td[1:]: #baki sary links `a tag`` k andar han os k leye loop lagyga. k automatically key/column name with value pick kary 
            key  = a["aria-label"] # `a` tag k attribute `aria-label` mein key/column  name houwta
            value = a["href"] # `a` tag k attribute `href` mein url/link houwta
            # print(f"{key} = {value}")
            dic[key] = value # har row me jis social media links huengy wo automatically save hun jaengy. jaisy k 1st row me 2 links and last row me 5 links. toh humra code chal jayga dono situation py without any error

        dic["company location"]  = tds_of_each_row[-2].text # company location sary tds me sy second last `td tag`` me han. jis k leye -2 lagaya
        dic["company founder"]  =tds_of_each_row[-6].text.strip() # company founder sary tds me sy last 6th `td tag`` me han. jis k leye -6 lagaya
        lst.append(dic.copy())
    df = pd.DataFrame(lst)
    df.to_csv(f"files\\{random_pg}.csv")
    # df
    driver.quit()

