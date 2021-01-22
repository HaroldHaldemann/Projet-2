import requests
from bs4 import BeautifulSoup

	
with open('books.csv', 'w') as file:
	file.write('product_page_url,universal_product_code,title,price_including_tax,price_excluding_tax,number_available,category,review_rating,image_url,product_description\n')

	url = 'http://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html'
	response = requests.get(url)

	if response.ok:
		soup = BeautifulSoup(response.text, 'html.parser')

		product_page_url = url
		universal_product_code = soup.find('table').findAll('td')[0].text
		title = soup.find('h1').text
		price_including_tax = soup.find('table').findAll('td')[3].text
		price_excluding_tax = soup.find('table').findAll('td')[2].text
		number_available = soup.find('table').findAll('td')[5].text
		category = soup.find('ul', {'class': 'breadcrumb'}).find('a', text = lambda l: "Books" not in l and "Home" not in l).text
		review_rating = soup.find('div', {'class': 'col-sm-6 product_main'}).find('p', {'class': lambda l: "star-rating" in l})['class'][1]
		image_url = soup.find('div', {'class': 'item active'}).find('img')['src']
		product_description = soup.find('p', {'class': None}).text
		
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

