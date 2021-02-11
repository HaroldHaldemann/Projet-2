#include:utf-8

import acquireurls as au
import acquireinfobook as aib
import csv
import os
import argparse
import sys

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
	try:
		os.mkdir(f"{path}CSV Files")
	except FileExistsError:
		pass
	except PermissionError:
		print("Permission denied, " \
			"please report to README.md for further informations."
		)
		sys.exit()
	soup = aib.acquire_html(url)
	category = soup.h1.string
	try:
		file = csv.writer(open(
			f"{path}CSV Files/{category} Books.csv",
			'w',
			encoding='utf8',
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
		'image',
		'product_description'
	])
	books = map(
		lambda x: aib.info_book(x),
		au.acquire_list_urls_books(url),
	)
	file.writerows(books)

if __name__ == '__main__':
	if args.category:
		write_info_books(args.category)
