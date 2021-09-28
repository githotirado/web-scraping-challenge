# Scrape various Mars data web sites, return a dictionary of information

# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time, pprint

def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=True)

def nasa_mars_news():
    browser = init_browser()
    print("\n\n*** Scraping the mars nasa news site ***")
    mnns_url = "https://mars.nasa.gov/news/"
    browser.visit(mnns_url)
    time.sleep(5)
    html = browser.html

    # Convert browser html to soup object
    soup = bs(html, 'html.parser')
    browser.quit()

    # Find first content title and the paragraph text
    first_article = soup.find('div', { 'class' : 'list_text'})
    news_title = first_article.a.text
    news_p = first_article.find('div', { 'class' : 'article_teaser_body'}).text
    mars_news = {
        'news_title'        : news_title,
        'news_paragraph'    : news_p
    }

    return mars_news


def jpl_featured_image():
    browser = init_browser()
    print("\n\n*** Scraping JPL Space Images ***")
    jpl_url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"
    browser.visit(jpl_url)
    time.sleep(5)

    # Find and click the full image button
    browser.links.find_by_partial_text('FULL IMAGE').click()

    # Parse the resulting html with soup
    html = browser.html
    soup = bs(html, 'html.parser')
    browser.quit()

    # find the relative image url
    relative_image_url = soup.find('img', class_="fancybox-image")["src"]

    # Use the base url to create an absolute url
    base_url = jpl_url.split('index.html')[0]
    featured_image_url = base_url + relative_image_url

    return featured_image_url

def mars_weather():
    browser = init_browser()
    # Mars weather site
    weather_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(weather_url)
    html = browser.html
    weather_soup = bs(html, 'html.parser')
    # Retrieve latest tweet with Mars weather info
    mars_weather = weather_soup.find_all('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')[0].text
    browser.quit()

    return mars_weather

def mars_facts():
    # Create a dataframe from the space-facts.com mars page
    print("\n\n*** Scraping space-facts ***")
    url = "https://space-facts.com/mars/"
    tables = pd.read_html(url, header=None)
    mars_df = tables[0]

    # clean the dataframe and export to HTML
    mars_df.columns = ['description', 'value']
    mars_df.set_index('description', inplace=True)
    # mars_df.to_html('visualizations/table.html')
    html_table = mars_df.to_html()
    html_table = html_table.replace('\n', '')

    return html_table


def hemispheres():
    # visit the USGS astrogeology page for hemisphere data from Mars
    browser = init_browser()
    print("\n\n*** Scraping USGS Astrogeology ***")
    usgs_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(usgs_url)
    time.sleep(5)
    html = browser.html
    soup =  bs(html, 'html.parser')

    # List of hemispheres
    hemispheres_h3 = soup.div.find_all('h3')
    hemispheres = [x.text.replace(' Enhanced', '') for x in hemispheres_h3]

    # For each hemisphere, click the link, find the sample anchor, return the href
    hemisphere_image_urls = []
    for hemisphere in hemispheres:
        # Click into hemisphere page
        browser.links.find_by_partial_text(hemisphere).click()

        # Find the elements on each loop to avoid a stale element exception
        html = browser.html
        soup =  bs(html, 'html.parser')
        sample = soup.find('div', { "class" : "downloads"})

        # Find the Sample image anchor tag and extract the href
        sample_image_url = sample.a['href']
        
        # Get Hemisphere title
        hemisphere_title = hemisphere

        # Append hemisphere object to list
        hemisphere_object = {
            "img_url" : sample_image_url,
            "title"   : hemisphere_title
        }
        hemisphere_image_urls.append(hemisphere_object)
        
        browser.back()
        
    # Quit the browser
    browser.quit()

    return hemisphere_image_urls


def scrape():
    mars_dict = {
        'mars_news': nasa_mars_news(),
        'mars_featured_image': jpl_featured_image(),
        'mars_weather': mars_weather(),
        'mars_facts': mars_facts(),
        'mars_hemispheres': hemispheres()
    }

    return mars_dict

if __name__ == '__main__':
    pprint.pprint(scrape())