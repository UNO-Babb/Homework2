#BusSchedule.py
#Name: Trevor Woosley
#Date: 03/10/2025
#Assignment: Homework 2

import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from datetime import datetime

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

def is_time(text):
    
    text = text.strip()

    
    time_formats = [
        "%H:%M",         
        "%H:%M:%S",      

    ]
    
    for fmt in time_formats:
        try:
            datetime.strptime(text, fmt)
            return True
        except ValueError:
            continue
    return False

current_time = datetime.now().strftime("%H:%M:%S")

print("Current Time:", current_time)

def get_next_bus(current_time=None):
    if current_time is None:
        current_time = datetime.now().time()

def bus_schedule(time):
    

    for bus_time in bus_schedule:
        if current_time < bus_time:
            return f"The next bus is at {bus_time.strftime('%H:%M')}."

   

def getHours(time):
  time_obj = datetime.strptime(time, "%I:%M %p")
  return time_obj.strftime("%H:%M")

def main():
  direction = "EAST"
  stopCode = "2269"
  routeNumber = "11"
  url = "https://myride.ometro.com/Schedule?stopCode=" + stopCode + "&routeNumber=" + routeNumber+ "&directionName="+ direction
  #c1 = loadURL(url) #loads the web page
  #c1 = loadTestPage() #loads the test page
  #print(c1)

  time = "9:49 PM"

main()



def main():
  url = "https://myride.ometro.com/Schedule?stopCode=2269&routeNumber=11&directionName=EAST"
  c1 = loadURL(url) #loads the web page
  #c1 = loadTestPage() #loads the test page
  print(c1)

main()