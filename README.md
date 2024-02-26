# Homework 2 - Craigslist Scraping

### Web Scraping
In our last assignment, we used an API to get information from a source. Not all data sources have a nice means for programmers to access. There are times that we need to read data from a web page.
Example applications:
- Weather data
- Price comparisons
- Stock information
- Web indexing

### Beautiful Soup
Beautiful Soup is a python library designed to make web scraping easy. There are a lot of built-in functionality. I encourage you to research and use this library but for this assignment we are only going to look at the visible text from a website.
- [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

### Selenium
Beautiful Soup is a super useful tool but it does not "load" a website. It gets the contents of the HTML but sometimes a website needs to run to fully load. There might be Java Script or Python that run in your browser to get information and load dynamically.
- [Selenium Documentation](https://www.selenium.dev/)

### The Problem
We have been tracking several items on Craigslist. Noticing that we were looking every day to see if anything new had been posted, this seems like a great opportunity for automation.

We also have budget constraints and are only interested in items that fall within our parameters.

Craigslist does not have an API we can access directly, so we will have to load the page and look at the resulting data directly.

### CraigslistScraper.py
For the purpose of this assignment, we will be reading the contents of a website, and extracting the product title and the price.

The website [Craigslist](https://omaha.craigslist.org/) allows us to search for any keyword we are interested in.

## Program Requirements
- Unique variables for:
  - Searched Item
  - Minimum Price
  - Maximum Price

These can be "hard coded" into your program (you don't need to prompt the user) but the URL that you are fetching from Craigslist should be dynamic in that we could change the information in a clear way and not within the complicated URL.

- Helper Functions
  - loadURL(url) - This function loads a given URL and displays the contents of the site.

You should create additional helper functions to deconstruct the problem. There is no requirement on exactly how these functions work but here are some ideas.
- stringToMoney(money) - Take a string value like "$2,220" and convert to an integer value 2220.
- removeSpace(text) - Take a large text file and remove the unnecessary spaces and blank lines.
- addToList(list, description, price) - Adds a new entry to your running list of the new item.

As always, please make sure you are commenting your code to make it clear what you are intending to do. Also, choose variables that make it clear what they are doing to help support others who are reading your code.

### Sample Output
```
Search Item: Pinball
Minimum Price: $2000
Maximum Price: $7500

Price - Description
$2300 - Pinball machines Arcade
$2600 - Baby Pac-Man Arcade / Pinball Machine
$3300 - Atlantis pinball machine
$3700 - Torpedo Alley pinball machine
$5500 - Terminator 3 pinball machine

```
