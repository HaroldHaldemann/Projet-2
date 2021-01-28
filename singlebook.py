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

def acquire_star_rating(soup):
	review_rating = soup.find(class_=re.compile("^star"))['class'][1]
	return review_rating

def acquire_image_url(soup):
	partial_url = soup.img['src'][5:]
	image_url = f"http://books.toscrape.com{partial_url}"
	return image_url

def acquire_product_description(soup):
	is_description =  soup.find('p', {'class': None})
	if is_description:
		product_description = is_description.string
	else:
		product_description = ""
	return product_description