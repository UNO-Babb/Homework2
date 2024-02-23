#CraigslistScraper.py
#Name:
#Date:
#Assignment:

import requests
from bs4 import BeautifulSoup


def loadURL(url):
  """Takes a URL and loads the content
  returns the text on the page."""
  page = requests.get(url)
  soup = BeautifulSoup(page.text, 'html.parser')
  text = soup.get_text()

  return text


def main():
  url = 'https://omaha.craigslist.org/search/sss?query=pinball'
  pageText = loadURL(url)
  print(pageText)



if __name__ == '__main__':
  main()
