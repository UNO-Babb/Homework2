# Homework 2 - Email Extractor

### Web Scraping
In our last assignment, we used an API to get information from a source. Not all data sources have a nice means for programmers to access. There are times that we need to read data from a web page.
Example applications:
- Weather data
- Price comparisons
- Stock information
- Web indexing

### Beautiful Soup
Beautiful Soup is a python library designed to make web scraping easy. There are a lot of built-in functionality. I encourage you to research and use this library but for this assignment, we are only going to look at the contents of a web site.
- [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

### Installing on a home computer
To install Beautiful soup, go to a command line and run the following:
```
python -m pip install --upgrade pip
pip install beautifulsoup4
```
We will not need to do this in repl.it

### Email_Extractor.py
For the purpose of this assignment, we will be reading the contents of a website, and extracting the email addresses and storing the results to a list. The list should be printed in the end. If this were part of a larger e-mail harvesting operation, we would want to be able to crawl from one website to another, with the final list saved to a file for future use.

## Program Requirements
- Accept a URL from the user
- Identify all e-mail addresses on that page.
  - An e-mail address contains the '@' symbol
  - The addresses will be bound by HTML tags
- Prints a list of all e-mail addresses on the web site.
  - Duplicate e-mail addresses should not be in the list.
- There should be text on both sides of the @ symbol in an e-mail address.
- Beyond that, addresses do not need to be validated.

### Sample Output
```
Enter url: https://www.example.comm
Email addresses found:
webmaster@example.com
bob@example.com
```
