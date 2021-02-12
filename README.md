
## Introduction

The goal of this script is to gather all the informations of the books in the following site : [BookstoScrape](http://books.toscrape.com/index.html)

It generates CSV files fullfilled with the universal product code, the price, the number available, the url, the image url and path, the rating and the description of the books, one for each book category.
It also download every book imagesin the same location of the CSV files.

## Prerequisites

You must have Python 3.8 or higher installed in order to execute this code.

## Installation

1 - Clone the github Repository.

```bash
git clone https://github.com/HaroldHaldemann/Openclassrooms
```

2 - Create your virtual environment.

```bash
python -m venv name-virtual-env
```

3 - Activate your virtual environment.

On Windows
```windows
name-virtaul-env\Scripts\activate.bat #In cmd
name-virtaul-env\Scripts\Activate.ps1 #In Powershell
```

NB: If you activate your environment with Powershell, don't forget to enable running script :
```windows
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser
```

On Unix/MacOs
```bash
source tutorial-env/bin/activate
```

4 - Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required modules.

```bash
pip install -r requirements.txt
```

## Usage

To execute this script, you have to enter the following code line:

```python
python main.py
```

You can enter the options --category or --path

--path permit you to chose the location where your CSV files and Images will be stored. 
If entered, path is a string type must end with /
If not enterd, the CSV files and images will be stored in your current working directory.

Example:
```python
python main.py --path "C:/path/to/files/"
```

--category permit you to scrape a single category of book and so to create a single CSV file and all the book images of this caetgory.
If entered, category is a string type and must be the url of the category page you want to scrape.
If not entered, the script will scrape every categories.

Example:
```python
python main.py --category "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"
```

You can execute the script with both options

Example:
```python
python main.py --category "http://books.toscrape.com/catalogue/category/books/travel_2/index.html" --path "C:/path/to/files/"
```

## Troubleshooting