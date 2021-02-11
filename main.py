#include:utf-8

import sys
import acquireurls as au
import writeincsv as wic

def main(url):
	"""
	Take the url of the site.
	Write the informations of the books in CSV files.
	One CSV for a single category.
	"""
	for url_category in au.acquire_urls_categories(url):
		wic.write_info_books(url_category)


if __name__ == '__main__':
	url = 'http://books.toscrape.com/catalogue/category/books_1/index.html'
	main(url)
