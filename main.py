#include:utf-8

from bs4 import BeautifulSoup
import acquireurls as au
import writeincsv as wic
import tqdm

def main(url):
	"""
	Take the url of the site.
	Write the informations of the books in CSV files.
	One CSV for a single category.
	"""
	for url_category in tqdm.tqdm(au.acquire_urls_categories(url)):
		wic.write_info_books(url_category)


if __name__ == '__main__':
	url = 'http://books.toscrape.com/catalogue/category/books_1/index.html'
	main(url)
