#include:utf-8

from bs4 import BeautifulSoup
import acquireurls as au
import acquireinfobook as aib
import csv
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
	"--category",
	type=str,
	help="Enter the category url you want to scrap",
)
args = parser.parse_args()

# path for the location of the CSV files
path = "" # must finish by / if unempty

def write_info_books(url):
	"""
	Take the url of a category page.
	Write in a CSV file the informations of the books.
	"""
	if not os.path.exists(f"{path}Fichiers CSV"):
		os.mkdir(f"{path}Fichiers CSV")
	soup = aib.acquire_html(url)
	category = soup.h1.string
	with open(f"{path}Fichiers CSV/{category} Books.csv", 'w') as file:
		file.write('product_page_url,universal_product_code,title,price_including_tax,price_excluding_tax,number_available,category,review_rating,image_url,product_description\n')
		books = map(
			lambda x: aib.info_book(x),
			 au.acquire_list_urls_books(url),
		)
		for book in list(books):
			for info in book:
				try:
					file.write(f"{info},")
				except UnicodeEncodeError:
					file.write(f"'{info.encode(encoding='ascii',errors='replace')}',")
			file.write('\n')

if __name__ == '__main__':
	if args.category:
		write_info_books(args.category)
