#include:utf-8

from bs4 import BeautifulSoup
from acquireurls import acquire_list_urls_books
from acquireinfobook import acquire_html, info_book
import os

# chemin pour la création du dossier où se situera les fichiers CSV
path = "" # doit terminer par / si non vide

def write_info_books(url):
	if not os.path.exists(f"{path}Fichiers CSV"):
		os.mkdir(f"{path}Fichiers CSV")
	soup = acquire_html(url)
	category = soup.h1.string
	with open(f"{path}Fichiers CSV/{category} Books.csv", 'w') as file:
		file.write('product_page_url,universal_product_code,title,price_including_tax,price_excluding_tax,number_available,category,review_rating,image_url,product_description\n')
		books = map(
			lambda x: info_book(x),
			 acquire_list_urls_books(url),
		)
		for book in list(books):
			for info in book:
				file.write(f"{info},")
			file.write('\n')