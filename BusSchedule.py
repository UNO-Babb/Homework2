#BusSchedule.py
#Name:
#Date:
#Assignment:

import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def loadURL(url):
  """
  This function loads a given URL and returns the text
  that is displayed on the site. It does not return the
  raw HTML code but only the code that is visible on the page.
  """
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  chrome_options.add_argument("--headless");
  driver = webdriver.Chrome(options=chrome_options)
  driver.get(url)
  content=driver.find_element(By.XPATH, "/html/body").text
  driver.quit()

  return content

def loadTestPage():
  """
  This function returns the contents of our test page.
  This is done to avoid unnecessary calls to the site
  for our testing.
  """
  page = open("testPage.txt", 'r')
  contents = page.read()
  page.close()

  return contents


def main():
  url = "https://myride.ometro.com/Schedule?stopCode=2269&routeNumber=11&directionName=EAST"
  #c1 = loadURL(url) #loads the web page
  Sc1 = loadTestPage() #loads the test page
  print(c1)

main()
