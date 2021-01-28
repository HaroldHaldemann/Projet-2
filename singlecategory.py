from bs4 import BeautifulSoup
from singlebook import *
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

def write_info_books(url):
	soup = acquire_html(url)
	category = soup.h1.string
	with open(f"{category}_books.csv", 'w') as file:
		file.write('product_page_url,universal_product_code,title,price_including_tax,price_excluding_tax,number_available,category,review_rating,image_url,product_description\n')
		books = map(
			lambda x: info_book(x),
			 acquire_list_urls_books(url),
		)
		for book in list(books):
			for info in book:
				file.write(f"{info},")
			file.write('\n')

url = 'http://books.toscrape.com/catalogue/category/books/fantasy_19/index.html'
write_info_books(url)