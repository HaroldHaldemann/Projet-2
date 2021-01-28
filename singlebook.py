from bs4 import BeautifulSoup
import requests
import re

def acquire_html(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.content, 'html.parser')
	return soup

def acquire_title(soup):
	title =f"{soup.h1.string}"
	return title

def acquire_code_tax_number(soup):
	table = soup.table.find_all('td')
	code_tax_number = {
		'universal_product_code': table[0].string,
		'price_including_tax': table[3].string,
		'price_excluding_tax': table[2].string,
		'number_available': table[5].string,
	}
	return code_tax_number

def acquire_category(soup):
	table = soup.ul.find_all('a')
	category = table[2].string
	return category