#Email_Extractor.py
#Name:
#Date:
#Assignment:

import urllib.request
from bs4 import BeautifulSoup

def main():
  #prompt the user for a webpage url
  url = 'https://www.unomaha.edu/college-of-information-science-and-technology/about/faculty-staff/index.php'
  url_html = urllib.request.urlopen(url)

  soup = BeautifulSoup(url_html, "html.parser")

  #Convert the soup to a string version
  soup = str(soup)

  #Split the text into a list, with the end of line \n as the delimiter
  for line in soup.split("\n"):
    print(line)

main()
