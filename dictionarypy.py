import requests
from BeautifulSoup import BeautifulSoup

word = input("Choose words for a simple define. Please put double quotations around your words and leave a space between each. The definitions will be in opposite order when they appear\n")
word = word.split()
count = len(word)
count = count - 1
signal = -1
while (signal < count):
	url = 'http://www.thesaurus.com/browse/'+word[count]+'?s=t'
	response = requests.get(url)
	html = response.content
	soup = BeautifulSoup(html)
	table = soup.find('strong', attrs={'class': 'ttl'})
	print table.text.replace('&nbsp;','')
	count = count - 1





