import requests
from BeautifulSoup import BeautifulSoup

word = input("Choose a word for a simple define\n Please put double quotation marks around the word. \n")
url = 'http://www.thesaurus.com/browse/'+word+'?s=t'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('strong', attrs={'class': 'ttl'})

print table.text.replace('&nbsp;','')
