#include:utf-8

import os
import sys
import acquireurls as au
import writeincsv as wic
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
	"--category",
	type=str,
	help="Enter the category url you want to scrap",
)
parser.add_argument(
	"--path",
	type=str,
	help="Enter the path where the Csv Files and Images will be saved." \
	"Must end with /",
	default="",
)
args = parser.parse_args()

def main(url):
	"""
	Take the url of the site.
	Write the informations of the books in CSV files.
	One CSV for a single category.
	"""
	for url_category in au.acquire_urls_categories(url):
		wic.write_info_books(url_category)

path = args.path
if __name__ == '__main__':
	if args.category:
		wic.write_info_books(args.category)
		sys.exit()
	url = "http://books.toscrape.com/catalogue/" \
		"category/books_1/index.html"
	main(url)