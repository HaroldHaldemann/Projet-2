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