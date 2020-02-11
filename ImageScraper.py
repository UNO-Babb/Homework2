#Need to install PIL
# python -m pip install Pillow
# python -m pip install --upgrade pip
#Need to install Beautiful Soup 4
# pip install beautifulsoup4

import urllib.request
from PIL import Image
from bs4 import BeautifulSoup

the_html = """<html>
  <head>
    <title>CYBR 2980 - HTML Page</title>
  </head>
  <body>
    <h1>Welcome to a great website</h1>
    <p>This is a testing page for your web scraping homework</p>
    <p>Use this site first before attempting to scrape the actual web</p>
    <img src = "image1.png">
    <h2>Contact</h2>
    <ul>
      <li>dvbabb@unomaha.edu</li>
      <li>a@b.c</li>
    </ul>

  </body>
</html>
  """
file_html = open("testPage.html")

#url = 'https://desmoines.craigslist.org/bik/d/des-moines-salsa-mukluk-fat-bike/7067648431.html'
url = 'https://www.unomaha.edu/college-of-information-science-and-technology/school-of-interdisciplinary-informatics/about/directory.php'
url_html = urllib.request.urlopen(url)

soup = BeautifulSoup(url_html, "html.parser")

#print(soup.body)
el = soup.findAll("img")
#print(el)

for img in el:
    print(img)

#image = Image.open(urllib.request.urlopen(url))
#width, height = image.size
#image.show()
#print (width,height)
