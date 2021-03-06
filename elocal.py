#!/usr/bin/python
#aichi-ninja 2013
import urllib2
from bs4 import BeautifulSoup

#get html from a link
def getHtml(url):
    sock = urllib2.urlopen(url)
    data = sock.read()
    sock.close()
    return data

#get state links from the main page
def getStateLinks():
    state_links = []
    url = "http://www.elocalplumbers.com/"
    html = getHtml(url)
    soup = BeautifulSoup(html)
    for ulink in soup.find_all('ul','groups-4'):
        links = ulink.find_all('li')
        for link in links:
            state_links.append("http://www.elocalplumbers.com" + link.find('a').get('href'))
    return state_links

#get city links by state
#ex; http://www.elocalplumbers.com/ak
def getCitiesByStateLink(url):
    city_links = []
    html = BeautifulSoup(getHtml(url))
    cities = html.find_all('div','blue-fill')
    for city in cities:
        ul = city.find_all('ul')
        for u in ul:
            li = u.find_all('li')
            for li_a in li:
                city_links.append(li_a.find('a').get('href'))
    return city_links

#x. check if we have a next link
def getNextLink(url):
    html = BeautifulSoup(getHtml(url))
    return html.find('ul','page-list').find('a','arrow-right').get('href')

#x. get all the links to the business profiles
url = "http://www.elocalplumbers.com/city/Anchorage_AK/#!/page=2"
#html = BeautifulSoup(getHtml(url))
#listings = html.find_all('article','listing')
#for listing in listings:
#    bus_phone = listing.find('li','view-phone').get_text()
#    name = listing.find('h2')
#    bus_name = name.find('a').get_text()
    
print str(getNextLink(url))
    
#x. scrape business information
