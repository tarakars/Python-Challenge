# Dependencies
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
from selenium import webdriver
import pandas as pd
import tweepy
import time
# Twitter API Keys
from config import consumer_key,consumer_secret,access_token,access_token_secret




def init_browser():
    executable_path = {"executable_path": "/Users/David W. Jones/class/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()

    # Create a dictionary for all of the scraped data
    mars_data = {}

    # Visit the Mars news page. 
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
 

    # Search for news
    # Scrape page into soup
    html = browser.html
    soup = bs(html, 'html.parser')

    # Find the latest Mars news.
    article = soup.find("div", class_="list_text")
    news_p = article.find("div", class_="article_teaser_body").text
    news_title = article.find("div", class_="content_title").text
    news_date = article.find("div", class_="list_date").text
  
    # Add the news date, title and summary to the dictionary
    mars_data["news_date"] = news_date
    mars_data["news_title"] = news_title
    mars_data["summary"] = news_p


    # ## JPL Mars Space Images - Featured Image
    # ------
    # - Visit the url for JPL's Featured Space [Image](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).
    # - Use splinter to navigate the site and find the full size jpg image url for the current Featured Mars Image.
    # - Save a complete url string for this image


    # While chromedriver is open go to JPL's Featured Space Image page. 
    url2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url2)

    # Scrape the browser into soup and use soup to find the full resolution image of mars
    # Save the image url to a variable called `featured_image_url`
    html = browser.html
    soup = bs(html, 'html.parser')
    image = soup.find('img', class_="thumb")["src"]
    img_url = "https://jpl.nasa.gov"+image
    featured_image_url = img_url
    
    # Add the featured image url to the dictionary
    mars_data["featured_image_url"] = featured_image_url


    # ## Mars Weather 
    # ------
    # - From the [Mars Weather twitter](https://twitter.com/marswxreport?lang=en) account scrape the latest Mars weather tweet from the page.
    # - Save the tweet text for the weather report.
    # Setup Tweepy API Authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
    target_user = "marswxreport"
    full_tweet = api.user_timeline(target_user , count = 1)
    mars_weather=full_tweet[0]['text']
    
    # Add the weather to the dictionary
    mars_data["mars_weather"] = mars_weather

    # ## Mars Facts
    


    url3 = "https://space-facts.com/mars/"
    browser.visit(url3)

    grab=pd.read_html(url3)
    mars_info=pd.DataFrame(grab[0])
    mars_info.columns=['Mars','Data']
    mars_table=mars_info.set_index("Mars")
    marsinformation = mars_table.to_html(classes='marsinformation')
    marsinformation =marsinformation.replace('\n', ' ')

    # Add the Mars facts table to the dictionary
    mars_data["mars_table"] = marsinformation


    # Visit the USGS Astogeology site and scrape pictures of the hemispheres
    url4 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url4)
    html = browser.html
    soup = bs(html, 'html.parser')
    mars_hemis=[]

    for i in range (4):
        time.sleep(5)
        images = browser.find_by_tag('h3')
        images[i].click()
        html = browser.html
        soup = bs(html, 'html.parser')
        partial = soup.find("img", class_="wide-image")["src"]
        img_title = soup.find("h2",class_="title").text
        img_url = 'https://astrogeology.usgs.gov'+ partial
        dictionary={"title":img_title,"img_url":img_url}
        mars_hemis.append(dictionary)
        browser.back()

    #mars_data['mars_hemis'] = mars_hemis
    # Return the dictionary
    return mars_data
