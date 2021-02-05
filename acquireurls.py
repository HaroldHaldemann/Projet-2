#include:utf-8

from bs4 import BeautifulSoup
import acquireinfobook as aib
import requests

def acquire_page_list_urls_books(soup):
	"""
	Take a BeautifulSoup content of a category page.
	Return a list of the urls of the books in the first page for a unique category.
	"""
	page_list_partial_urls_books = map(
		lambda x: x.a['href'][8:],
		soup.find_all('h3'),
	)
	page_list_urls_books = map(
		lambda x: f"http://books.toscrape.com/catalogue{x}",
		page_list_partial_urls_books,
	)
	return list(page_list_urls_books)

def acquire_list_urls_books(url):
	"""
	Take a url of a category page.
	Return a list of the urls of the books for a single category page.
	"""
	response = requests.get(url)
	soup = aib.acquire_html(url)
	list_urls_books = []
	base_url = url[:-11]
	index = 2
	while response.ok:
		list_urls_books += acquire_page_list_urls_books(soup)
		next_url = f"{base_url}/page-{index}.html"
		response = requests.get(next_url)
		soup = acquire_html(next_url)
		index += 1
	return list(list_urls_books)

def acquire_urls_categories(url):
	"""
	Take the url of the site.
	Return a list of the urls of the category pages.
	"""
	soup = aib.acquire_html(url)
	list_partial_urls_categories = soup.find('ul', {'class': None}).find_all('a')
	list_urls_categories = map(
		lambda x: f"{url[:44]}{x['href'][2:]}",
		list_partial_urls_categories,
	)
	return list_urls_categories