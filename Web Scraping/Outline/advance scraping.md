
### **Week 1: Advanced Web Scraping Concepts**


#### **Day 1: Introduction to Web Scraping and HTTP Protocols (Advanced)**

- **What is Web Scraping?**
  - Web scraping refers to extracting data from websites by sending HTTP requests and parsing the HTML of web pages.
  
- **HTTP Protocol and Requests (In-depth)**
  - **HTTP Methods**: The most common HTTP methods are:
    - **GET**: Used to request data from a server.
    - **POST**: Sends data to the server (used for form submissions).
    - **PUT**: Used to update resources on the server.
    - **DELETE**: Deletes resources on the server.
  
  - **Headers**: HTTP headers allow the client and the server to send additional information along with a request or response. Important headers include:
    - **User-Agent**: Identifies the browser or application making the request.
    - **Authorization**: Used for authentication tokens (e.g., OAuth tokens for APIs).
    - **Accept-Language**: Specifies the language preference.
  
- **Advanced Request Example**:
  ```python
  import requests

  headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
      'Accept-Language': 'en-US,en;q=0.9',
      'Authorization': 'Bearer <your_token>'  # for APIs that require authentication
  }

  response = requests.get('https://api.example.com/data', headers=headers)
  if response.status_code == 200:
      print(response.json())  # Parse JSON response
  else:
      print(f"Error: {response.status_code}")
  ```

---

#### **Day 2: Parsing Complex HTML Structures with BeautifulSoup**

- **CSS Selectors and Advanced Parsing**:
  - **CSS Selectors** can be used to pinpoint more specific elements in complex HTML structures, which might not be easy to target with basic methods like `find()` or `find_all()`.
  - You can use methods like `soup.select()` to target elements with complex CSS paths.
  
- **Advanced BeautifulSoup Techniques**:
  - **Finding by Class and ID**: Use CSS classes and IDs to target specific elements.
  - **Navigating the DOM Tree**: Use `.parent`, `.children`, `.next_sibling`, `.previous_sibling` to navigate HTML elements.
  - **Dealing with Inconsistent HTML**: Use `try/except` blocks to handle cases where elements may not exist on every page.

- **Example: Using `select()` for complex structures**:
  ```python
  from bs4 import BeautifulSoup
  import requests

  url = 'https://example.com/articles'
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')

  # Using CSS selectors to find specific elements
  articles = soup.select('div.article > h2.title')  # Finds all <h2> inside a div with class 'article'
  for article in articles:
      print(article.get_text())
  ```

---

#### **Day 3: Scraping Dynamic Web Pages with `Selenium`**

- **Why use `Selenium`?**
  - Many modern websites use JavaScript to load content dynamically (e.g., Infinite scroll, AJAX calls). `Selenium` can interact with these elements because it controls a real web browser.

- **`Selenium` Basics**:
  - **Setting up Selenium with Chrome/Firefox WebDriver**:
    - Install WebDriver for your browser.
    - Install `selenium` with `pip install selenium`.

- **Example: Automating a login process and scraping dynamic content**:
  ```python
  from selenium import webdriver
  from selenium.webdriver.common.by import By
  from selenium.webdriver.common.keys import Keys
  import time

  # Set up WebDriver (Chrome)
  driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

  # Open a website
  driver.get('https://www.example.com/login')

  # Interact with the login form
  username = driver.find_element(By.NAME, 'username')
  password = driver.find_element(By.NAME, 'password')

  username.send_keys('your_username')
  password.send_keys('your_password')
  password.send_keys(Keys.RETURN)  # Hit Enter

  time.sleep(3)  # Wait for the page to load

  # Scrape dynamic content after login
  content = driver.find_element(By.CLASS_NAME, 'content-class').text
  print(content)

  driver.quit()  # Close the browser
  ```

---

#### **Day 4: Handling Anti-Scraping Techniques (Advanced)**

- **Common Anti-Scraping Techniques**:
  - **CAPTCHAs**: Used to prevent bots from accessing a website.
  - **IP Blocking**: Websites might block your IP if they detect repeated requests.
  - **Rate Limiting**: Sites might limit how often you can request data within a certain time frame.

- **Solutions**:
  - **CAPTCHAs**: Use services like **2Captcha** or **Anti-Captcha** to solve CAPTCHAs.
  - **Rotating Proxies**: Use proxy services to rotate IP addresses, making your requests appear as if they are coming from different locations.
  - **Randomized User-Agents**: Use libraries like `fake_useragent` to randomly rotate User-Agent strings.
  - **Adding Delays**: Use `time.sleep()` to add delays between requests to avoid rate-limiting.

- **Example: Using Proxies and User-Agent Rotation**:
  ```python
  import requests
  from fake_useragent import UserAgent
  import random

  ua = UserAgent()

  proxies = {
      'http': 'http://10.10.10.10:8000',  # Example proxy
      'https': 'http://10.10.10.10:8000',
  }

  headers = {
      'User-Agent': ua.random  # Randomly selected User-Agent
  }

  response = requests.get('https://www.example.com', headers=headers, proxies=proxies)
  print(response.status_code)
  ```

---

#### **Day 5: Data Storage and Scraping Large Datasets**

- **Storing Data in Databases**:
  - Instead of storing data in CSV files, large-scale scraping projects benefit from using databases. You can use SQLite for simple setups or more advanced databases like MySQL or MongoDB for large-scale projects.
  
- **Example: Storing Data in SQLite**:
  ```python
  import sqlite3

  # Create a SQLite database connection
  conn = sqlite3.connect('scraped_data.db')
  cursor = conn.cursor()

  # Create a table
  cursor.execute('''CREATE TABLE IF NOT EXISTS articles (title TEXT, link TEXT)''')

  # Insert data
  articles = [('Article 1', 'https://example.com/1'), ('Article 2', 'https://example.com/2')]
  cursor.executemany('INSERT INTO articles (title, link) VALUES (?, ?)', articles)

  conn.commit()
  conn.close()
  ```

---

### **Week 2: Web Crawling and Advanced Data Handling**

---

#### **Day 6: Building Web Crawlers with `Scrapy`**

- **What is `Scrapy`?**
  - `Scrapy` is a powerful framework for building web crawlers. It allows for efficient data extraction by automatically handling tasks like request management, parsing, and error handling.

- **`Scrapy` Structure**:
  - **Spiders**: The core component in `Scrapy`. It defines how to follow links, parse data, and store the results.
  - **Pipelines**: These are used to process scraped data (e.g., cleaning and saving to a database).

- **Example: Simple `Scrapy` Spider**:
  ```python
  import scrapy

  class QuotesSpider(scrapy.Spider):
      name = 'quotes'
      start_urls = ['http://quotes.toscrape.com']

      def parse(self, response):
          for quote in response.css('div.quote'):
              yield {
                  'text': quote.css('span.text::text').get(),
                  'author': quote.css('span small::text').get(),
              }

          next_page = response.css('li.next a::attr(href)').get()
          if next_page is not None:
              yield response.follow(next_page, self.parse)
  ```

---

#### **Day 7: Handling JavaScript-based Content with APIs**

- **Why use APIs instead of scraping HTML?**
  - Many modern websites provide APIs to access their data directly, which is often cleaner and more efficient than scraping HTML.

- **Example: Accessing a REST API**:
  ```python
  import requests

  url = 'https://api.example.com/data'
  headers = {
      'Authorization': 'Bearer your_token'
  }

  response = requests.get(url, headers=headers)
  data = response.json()
  print(data)
  ```

---

#### **Day 8: Polite Scraping: Following Robots.txt and Ethical Guidelines**

- **What is `robots.txt`?**
  - `robots.txt` is a file hosted by websites to tell crawlers which parts of the site they can or cannot access. It's important to respect this when scraping.

- **How to check `robots.txt`**:
  - Go to `https://www.example.com/robots.txt