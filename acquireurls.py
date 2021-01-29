from bs4 import BeautifulSoup
from acquireinfobook import acquire_html
import requests

def acquire_page_list_urls_books(soup):
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
	response = requests.get(url)
	soup = acquire_html(url)
	list_urls_books = []
	base_url = url[:-11]
	index = 2
	while response.ok:
		list_urls_books += acquire_page_list_urls_books(soup)
		next_url = f"{base_url}/page-{index}.html"
		response = requests.get(next_url)
		soup = acquire_html(next_url)
		index += 1
	return list_urls_books

def acquire_urls_categories(url):
	soup = acquire_html(url)
	list_partial_urls_categories = soup.find('ul', {'class': None}).find_all('a')
	list_urls_categories = map(
		lambda x: f"{url[:43]}{x['href'][2:]}",
		list_partial_urls_categories,
	)
	return list_urls_categories