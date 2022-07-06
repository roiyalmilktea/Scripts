from ssl import SSL_ERROR_WANT_X509_LOOKUP
from bs4 import BeautifulSoup

# Read HTML file
filepath=""
with open('file',encoding='utf-8') as fp:
	html_str = fp.read()

# make object of Beautiful Soup
soup = BeautifulSoup(html_str,'html5lib')

# search title element and indecate
title = soup.find('title')
print(title)