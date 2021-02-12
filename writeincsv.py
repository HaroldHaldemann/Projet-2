#include:utf-8

import acquireurls as au
import acquireinfobook as aib
import csv
import os
import sys
import main

def write_info_books(url):
	"""
	Take the url of a category page.
	Write in a CSV file the informations of the books.
	"""
	try:
		os.mkdir(f"{main.path}CSVFiles")
	except FileExistsError:
		pass
	except PermissionError:
		print("Permission denied, " \
			"please report to README.md for further informations."
		)
		sys.exit()
	if not os.path.exists(f"{main.path}BookImages"):
		os.mkdir(f"{main.path}BookImages")
	soup = aib.acquire_html(url)
	category = soup.h1.string
	try:
		file = csv.writer(open(
			f"{main.path}CSVFiles/{category}.csv".replace(" ", ""),
			'w',
			encoding='utf8',
			newline='',
		))
	except PermissionError:
		print("Permission denied, " \
			"please report to README.md for further informations."
		)
		sys.exit()
	file.writerow([
		'product_page_url',
		'universal_product_code',
		'title',
		'price_including_tax',
		'price_excluding_tax',
		'number_available',
		'category',
		'review_rating',
		'url_image',
		'path_image',
		'product_description'
	])
	books = map(
		lambda x: aib.info_book(x),
		au.acquire_list_urls_books(url),
	)
	file.writerows(books)
