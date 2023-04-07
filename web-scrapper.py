from selenium import webdriver
from BeautifulSoup import BeautifulSoup
import pandas as pd

#configure webdriver to use Chrome browser, set the path to chromedriver
#Change this path to the specific location where chromedriver is stored. 
driver = webdriver.Chrome("/usr/local/bin/chromedriver")

#open the URL:
products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver.get("<a href="https://www.flipkart.com/laptops/">https://www.flipkart.com/laptops/</a>~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&amp;amp;amp;amp;amp;amp;amp;amp;amp;uniq")

# Extract the data from the website. The desired data to extract is nested in <div> tags.
# Find the div tags with those respective class-names, extract the data and store the data in a variable.

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
name=a.find('div', attrs={'class':'_3wU53n'})
price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
products.append(name.text)
prices.append(price.text)
ratings.append(rating.text) 

# After extracting the data, store it in a format. 
# This format varies depending on the requirements. 
# For this example, we will store the extracted data in a CSV (Comma Separated Value) format).

df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
df.to_csv('products.csv', index=False, encoding='utf-8')