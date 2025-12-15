from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Edge()
driver.get("https://webscraper.io/test-sites/e-commerce/ajax/computers/laptops")



soup = BeautifulSoup(driver.page_source, 'html.parser')
soup
all_products = soup.find_all("div",class_="col-md-4 col-xl-4 col-lg-4")
all_products
len(all_products)
list = []
for i in all_products[0:6]:
    prod_dictionary = {
        'product_name': '',
        'product_link': '',
        'product_img': '',
        'product_price': '',
        'product_details': '',
        'product_reviews_number': '',
        'product_reviews_star_number': '',
    }
    prod_dictionary['product_name']= i.find('a').text.strip()
    prod_dictionary['product_details']=i.find('p').text
    prod_dictionary['product_img']=i.find('img')['src']
    prod_dictionary['product_link']=i.find('a')['href']
    prod_dictionary['product_reviews_number']=i.find('div',class_='ratings').text.strip()
    prod_dictionary['product_reviews_star_number']
    prod_dictionary['product_price']=i.find('h4').text.strip()
    list.append(prod_dictionary)
list
import pandas as pd 
df = pd.DataFrame(list)
folder_path = r"C:\Users\T460\web scraping\course-python-and-automation-by-kasi\Student's Folders\abdur rehman\from_dynamic_wibsite"
file_name = "\q4_3_by_py.csv"
path = folder_path + file_name
path
#%%


df.to_csv(path,index=False)# to save into csv file