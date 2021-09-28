# Define a function called `scrape` that will execute all of your scraping code from the `mission_to_mars.ipynb` notebook and return one Python dictionary containing all of the scraped data. 

# It will be a good idea to create multiple smaller functions that are called by the `scrape()` function. 
# Remember, each function should have one 'job' (eg. you might have a `mars_news()` function that scrapes the NASA mars news site and returns the content as a list/tuple/dictionary/json)
# HINT: the headers in the notebook can serve as a useful guide to where one 'job' ends and another begins.

# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)

def nasa_mars_news():
    browser = init_browser()
    print("Scraping the mars nasa news site")
    mnns_url = "https://mars.nasa.gov/news/"
    browser.visit(mnns_url)
    time.sleep(5)
    html = browser.html

    # Convert browser html to soup object
    soup = bs(html, 'html.parser')
    print("Scraping complete.")
    browser.quit()

    # Find first content title and the paragraph text
    first_article = soup.find('div', { 'class' : 'list_text'})
    news_title = first_article.a.text
    news_p = first_article.find('div', { 'class' : 'article_teaser_body'}).text
    mars_news = {
        'news_title': news_title,
        'news_p'    : news_p
    }

    # Return findings
    return mars_news


def jpl_feagured_image():
    browser = init_browser()
    print("Scraping JPL Space Images")
    jpl_url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"
    browser.visit(jpl_url)
    time.sleep(5)
    



# def scrape():