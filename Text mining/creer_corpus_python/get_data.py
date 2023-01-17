import requests
import bs4 as BeautifulSoup	
import re
from urllib import urlopen
import urllib2
import io
import sys
import urllib


encoding = 'utf-8'

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]


argv = sys.argv
argv.pop(0)
argv = "".join(argv)
argv = urllib.quote_plus(argv)

url = "https://www.google.fr/search?site=&source=hp&q=" + argv + "&num=10"
page = opener.open(url)
soup = BeautifulSoup.BeautifulSoup(page)

res = ""
print("SITES SOURCES:\n")
for cite in soup.findAll('cite'):
	temp = cite.text;
	if not cite.text.startswith("https://") and not cite.text.startswith("http://"):
		temp =  "http://" + temp
	print(temp)	
	try:	
		html = urlopen(temp).read()
		soup2 = BeautifulSoup.BeautifulSoup(html)
		[s.extract() for s in soup2(['style', 'script', '[document]', 'head', 'title'])]
		text = soup2.get_text()
		res+=text

	except EnvironmentError:
		print


with io.open('texte.txt','w',encoding=encoding) as f:
	f.write(res)










	