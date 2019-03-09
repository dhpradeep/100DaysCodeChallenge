# Requirements: 
# *pip install beautifulsoup4
# *pip install requests
# *pip install lxml

from bs4 import BeautifulSoup
import requests
source = requests.get('http://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[1]=1&callback=').text
soup = BeautifulSoup(source, 'lxml')
quote = soup.find_all('p')[1].text
quotes = quote.split('\\')
print(quotes[0])
