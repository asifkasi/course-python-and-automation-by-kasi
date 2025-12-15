from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Edge()

driver.get("https://webscraper.io/test-sites/e-commerce/more/computers/laptops")



soup = BeautifulSoup(driver.page_source, 'html.parser')
soup
product = soup.find('div',class_='product-wrapper card-body')
product
list = []
prod_dictionary = {
    'product_name': '',
    'product_link': '',
    'product_img': '',
    'product_price': '',
    'product_details': '',
    'product_reviews_number': '',
    'product_reviews_star_number': '',
}
prod_dictionary['product_name']= product.find('a').text.strip()
prod_dictionary['product_details']=product.find('p').text
prod_dictionary['product_img']=product.find('img')['src']
prod_dictionary['product_link']=product.find('a')['href']
prod_dictionary['product_reviews_number']=product.find('div',class_='ratings').text.strip()
prod_dictionary['product_reviews_star_number']
prod_dictionary['product_price']=product.find('h4').text.strip()
list.append(prod_dictionary)
list
import pandas as pd
df = pd.DataFrame(list)
folder_path = r"C:\Users\T460\web scraping\course-python-and-automation-by-kasi\Student's Folders\abdur rehman\from_dynamic_wibsite"
file_name = "\q5_1_by_py.csv"
path = folder_path + file_name
path
#%%


df.to_csv(path,index=False)# to save into csv file