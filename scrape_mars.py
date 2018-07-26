# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 10:22:00 2018

@author: Michael Diaz
"""
import flask
import numpy as np
import os
import pandas as pd
import pymongo
import re
import requests
import splinter
import urllib
from bs4 import BeautifulSoup
from flask import Flask, render_template
from flask import Flask, Response
from flask import jsonify
from selenium import webdriver
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist

def scrape():
#    execution = {"execution": "chromedriver.exe"}
    browser = Browser("chrome", headless=False)
    mars = {}
    #Set browser as html object
    html = browser.html
    #Connect BeautifulSoup to browser html for parsing
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    
    #NASA Mars News article
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)
    #Latest News Titles and Paragraphs
    #Iterate through homepage and all articles to find title and paragraph object
    #Set browser as html object
    html = browser.html
    #Parse HTML using Beautiful Soup
    soup = BeautifulSoup(html, "html.parser")
    sidebar = soup.find("ul", class_="item_list")
    categories = sidebar.find_all("li")
    # print(categories)
    #Retrieve all elements
    for category in categories:
        titles = category.find(class_="content_title")
        paragraph = category.find(class_="article_teaser_body")
    #     news_paragraph_lists.append(paragraph)
        for title in titles:
            headings = title.text.strip()
            mars["news_title"] = headings
        for news in paragraph.stripped_strings:
            mars["news_paragraph"] = news
    
    #JPL Mars Space Images
    
    #Use Browser to visit Mars Images URL Page
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    #Use Browser to interact with button element using id "full_image"
    full_image = browser.find_by_id("full_image")
    full_image.click()
    #Use Browser to interact with "more info" button
    img_info = browser.find_link_by_partial_text("more info")
    img_info.click()
    #Parse with Beautiful soup
    feature = soup.find("figure", class_="lede")
    #Slice the img tag
    feature_image = feature.find("img")["src"]
    #Assign this as a complete url
    mars["featured_img"] = f"https://www.jpl.nasa.gov{feature_image}"
        
    
    #Mars Weather
    #Latest Mars Weather Tweet
    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)
    #Iterate through homepage and all articles to find title and paragraph objects

    #Append Lists through parsing
    
    #Set browser as html object
    html = browser.html
    #Parse HTML using Beautiful Soup
    soup = BeautifulSoup(html, "html.parser")
    latest_tweet = soup.find(class_="TweetTextSize")
    # print(categories)
    #Retrieve all elements
    for tweet in latest_tweet:
        mars["tweets"] = tweet

    #Mars Facts
    #Web Scrape Mars Fact Table using Pandas
    #Set Url Variable 
    url = "https://space-facts.com/mars/"
    mars_table = pd.read_html(url)[0]
    mars_table.columns=['description', 'value']
    mars_table.set_index('description', inplace=True)
    mars_table
    #Export to HTML
    mars_df = mars_table.to_html()
    mars_df = mars_df.replace("\n", "")
    #Cleanup HTML using BeautifulSoup.prettify()
    mars["facts"] = mars_table
    #Mars Pictures
    hemisphere_pictures = {}
    #Connect to USGS Astrogeology Sit with browser
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    
    #Build a Loop that appends a python dictionary of titles with image url's
    title_list = []
    image_list = []
    links = []
    data = browser.find_by_css("img.thumb")
    data.click()

    for img in range(len(data)):
        browser.find_by_css("img.thumb")[img].click()
        sample_link = browser.find_link_by_text("Sample").first
        hemisphere_pictures["title"] = browser.find_by_css("h2.title").text
        hemisphere_pictures["img_url"] = sample_link["href"]
        links.append(hemisphere_pictures)

    mars["hemispheres"] = links
    browser.quit()
    return mars
    return scrape
    
scrape()
    
    