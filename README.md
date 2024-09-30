# Homework 2 - Bus Schedule Scraping

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
- You will have to install Selenium with the following command in your CodeSpace terminal
```
pip install selenium
```

### The Problem
UNO students can ride the Ometro busses for free with their MavCard. The problem is that, when you are at a bus stop, there is no indication of how near the bus is.

This information can be found on the metro website [ometro.com](https://ometro.com) but this is not always accessible to people at the stop.

Our plan is to add a [Raspberry Pi Zero](https://www.adafruit.com/product/2885) along with an [e-ink display](https://www.adafruit.com/product/3743) to each bus stop sign. For around $50 a sign, we are going to be able to add a useful feature that improves the experience of people using the bus.

Ometro does not have an API that we can directly access to get the up-to-date bus arrival time. As a result, we need to load their website and scrape the data ourselves.

### BusSchedule.py
For the purpose of this assignment, we will be reading the contents of a website, and extracting the time table.
The website [ometro.com](https://myride.ometro.com/) displays real-time estimate of when the bus will arrive.

## Program Requirements
- Unique variables for:
  - Stop Number
  - Route Number
  - Direction
- Use current time to find the next stop time.
  - Remember since DateTime uses GMT, you will need to adjust the time from GMT to Central Time Zone.
  - [Lab 2](https://github.com/UNO-Babb/Lab2) used the datetime function to get the current hours and minutes.

The example we are using is the Bus 11 stop at 67th and Pacific - Eastbound. You can select any stop in the Metro system but it should be different than the one in our example.

These can be "hard coded" into your program (you don't need to prompt the user) but the URL that you are fetching from Craigslist should be dynamic in that we could change the information in a clear way and not within the complicated URL.

- Helper Functions
  - loadURL(url) - This function loads a given URL and displays the contents of the site.
  - loadTestPage() - This function returns the contents of a test page we have previously copied. The goal is to avoid unnecessary calls to the Metro web site during our testing phase.

You should create additional helper functions to deconstruct the problem. There is no requirement on exactly how these functions work but here are some ideas.
- isLater(time1, time2) - Provide True or False if time 1 is later than time 2
- getHours(time) - Given a string in the form "HH:MM AM/PM" this will extract just the hour portion and return. Converts from AM/PM to a 24 hour clock.
- getMinutes(time) - Given a string in the form "HH:MM AM/PM" will return just the minutes portion.

As always, please make sure you are commenting your code to make it clear what you are intending to do. Also, choose variables that make it clear what they are doing to help support others who are reading your code.

### Sample Output
```
Current Time 10:41 AM
The next bus will arrive in 9 minutes.
The following bus will arrive in 39 minutes.
```
