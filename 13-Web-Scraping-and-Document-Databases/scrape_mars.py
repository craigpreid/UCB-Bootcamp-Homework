# Import Dependencies
import time
from splinter import Browser
from bs4 import BeautifulSoup
from selenium import webdriver

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path":"chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=True)

# scrape the headlines and store in a dictionary
def scrape():
    browser = init_browser()
    
    #########################
    # scrape the nasa.gov sitem
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    time.sleep(3)

    html = browser.html  

    soup = BeautifulSoup(html, "html.parser")
    time.sleep(3)
    # Empty dictionary to store the results
    mars={}

    nasa = soup.find_all("div", class_="content_title")

    article = soup.find("div",class_="list_text")

    # Extract the date for which the news was posted
    mars["news_date"] = article.find("div",class_="list_date").text
 
    # Extract the title for which the news posted
    mars["news_title"] = article.find("div",class_="content_title").text

    # Extract the partial link for which the news posted
    link = article.find("div",class_="content_title").find("a").get("href")

    # Form the complete link by appending the strings with the partial link
    mars["news_link"] = "https://mars.nasa.gov" + link

    # Extract the article for which the news posted
    mars["news_p"] = article.find("div",class_="article_teaser_body").text
    
    #####################
    # scrape the image
    jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars/"
    browser.visit(jpl_url)
    time.sleep(3)

    html = browser.html
    jpl_soup = BeautifulSoup(html, "html.parser")
    time.sleep(3)


    # Pull out the portion of the url for the image
    img_link = jpl_soup.find("div",class_="carousel_container").\
        find("div",class_="carousel_items").\
        find("article",class_="carousel_item").\
        get("style").\
        split("('",1)[1].split("')")[0]

    # Reconsturct the first portion of the URL so we don't need to hard code
    front_url = (jpl_url.split("/")[0]) + "//" + (jpl_url.split("/")[2])

    # Combine link to image with the first part of url
    featured_image_url = front_url + img_link
    
    # store values in mars dictionary
    mars["featured_image_url"] = featured_image_url
    img_title = jpl_soup.find("div",class_="carousel_container").find("div",class_="carousel_items").\
        find("article",class_="carousel_item").find("h1",class_="media_feature_title").text.strip()
    mars["featured_image_title"] = img_title
    
    ########################
    # Mars Weather from Twitter
    
    tweet_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(tweet_url)
    time.sleep(3)
   
    html = browser.html
    tweet_soup = BeautifulSoup(html, "html.parser")
    time.sleep(3)

    mars_weather = tweet_soup.find("li", class_= "js-stream-item").\
        find("div", class_ = "content").find("p", class_="tweet-text").text
    
    # store variable in dictionary
    mars["mars_weather"] = mars_weather

    ###########################
    # Mars Facts 
    # HTML to Pandas to HTML Table String
    
    import pandas as pd

    facts_url = "https://space-facts.com/mars/"

    table = pd.read_html(facts_url)
    time.sleep(3)

    mars_data = table[0]
    mars_data = mars_data.to_html(header = False, index = False)
    
    # story variable in dictionary
    mars["mars_data"] = mars_data
   
    #########################
    # Mars Hemispheres
    # scrape large images from website
    hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemispheres_url)
    time.sleep(3)

    html = browser.html
    hemispheres_soup = BeautifulSoup(html, "html.parser")
    time.sleep(3)

    # find the div with the target data and soup it
    hemispheres_links = hemispheres_soup.find_all("div",class_="item")

    # create blank dictionary for the the loop
    hemisphere_image_urls = []

    for item in hemispheres_links: 
        # loop through and extract the title
        title = item.find("h3").text

        # loop through and extract the partial url with large image
        link = item.find("a").get("href")

        # rebuild the front of the url
        front_hemis_url = hemispheres_url.split("/")
        front_hemis_url = (front_hemis_url[0]) + "//" + (front_hemis_url[2])

        # combine front and partial to get the url we want to use
        hemisphere_url = front_hemis_url + link

        # now we have to do another soup to get the actual image
        browser.visit(hemisphere_url)
        time.sleep(3)

        # Create a soup object to find the content from the URL with full size image
        html = browser.html
        img_soup = BeautifulSoup(html,"html.parser")

        # Extracting the parital link for the full sized image
        link = img_soup.find("div",class_="wide-image-wrapper").find("img",class_="wide-image").get("src")

        # Forming the entire link by appending the partial link
        img_url = "https://astrogeology.usgs.gov"+link

        hemisphere_image_urls.append({
            "title":title,
            "img_url":img_url,
            "hemisphere_url":hemisphere_url
        })

        # store variable in dictionary
        mars["hemisphere_image_urls"]=hemisphere_image_urls


    return mars

