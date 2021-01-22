import requests, time
from bs4 import BeautifulSoup

	
with open('books.csv', 'w', encoding="utf-8") as file:
	file.write('product_page_url,universal_product_code,title,price_including_tax,price_excluding_tax,number_available,category,review_rating,image_url,product_description\n')

	url = 'http://books.toscrape.com/catalogue/category/books_1/index.html'
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')
	urls = []
	soup_links = []

	soup_categories = soup.find('ul', {'class': 'nav nav-list'}).find('ul').findAll('li')
	for soup_category in soup_categories:
		link_category = soup_category.find('a')['href'][2:]
		category = link_category[7:-11]

		index = 2
		url = 'http://books.toscrape.com/catalogue/category' + link_category
		response = requests.get(url)
		soup = BeautifulSoup(response.text, 'html.parser')

		while response.ok:
			soup_links += soup.find('section').findAll('h3')
			url = 'http://books.toscrape.com/catalogue/category/books/{0}/page-{1}.html'.format(category, index)
			response = requests.get(url)
			soup = BeautifulSoup(response.text, 'html.parser')
			index += 1

	for soup_link in soup_links:
		link = soup_link.find('a')['href'][8:]
		urls += ['http://books.toscrape.com/catalogue' + link]

	for url in urls:
		response = requests.get(url)
		soup = BeautifulSoup(response.text, 'html.parser')

		product_page_url = url
		universal_product_code = soup.find('table').findAll('td')[0].text
		title = '"' + soup.find('h1').text + '"'
		price_including_tax = soup.find('table').findAll('td')[3].text
		price_excluding_tax = soup.find('table').findAll('td')[2].text
		number_available = '"' + soup.find('table').findAll('td')[5].text + '"'
		category = soup.find('ul', {'class': 'breadcrumb'}).find('a', text = lambda l: "Books" not in l and "Home" not in l).text
		review_rating = soup.find('div', {'class': 'col-sm-6 product_main'}).find('p', {'class': lambda l: "star-rating" in l})['class'][1]
		image_url = 'http://books.toscrape.com' + soup.find('div', {'class': 'item active'}).find('img')['src'][5:]
		try:
			product_description = '"' + soup.find('p', {'class': None}).text + '"'
		except:
			product_description = ""
		else:
			product_description = '"' + soup.find('p', {'class': None}).text + '"'

		info_book = [
			product_page_url,
			universal_product_code,
			title,
			price_including_tax,
			price_excluding_tax,
			number_available,
			category,
			review_rating,
			image_url,
			product_description,
		]

		for info in info_book:
			file.write(info + ',')
		file.write('\n')
