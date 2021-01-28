from bs4 import BeautifulSoup
from singlebook import *
import requests

def acquire_list_urls_books(url):
	soup = acquire_html(url)
	list_partial_urls_books = map(lambda x: x.a['href'][8:], soup.find_all('h3'))
	list_urls_books = map(lambda x: f"http://books.toscrape.com/catalogue{x}", list_partial_urls_books)
	return list(list_urls_books)

url = 'http://books.toscrape.com/catalogue/category/books/fantasy_19/index.html'
print(acquire_list_urls_books(url))

"""
index = 2
url = 'http://books.toscrape.com/catalogue/category' + link_category
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

while response.ok:
	soup_links += soup.find('section').findAll('h3')
	url = 'http://books.toscrape.com/catalogue/category/books/{0}/page-{1}.html'.format(category, index)
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')
	index += 1
"""