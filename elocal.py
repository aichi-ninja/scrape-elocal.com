import urllib2
from bs4 import BeautifulSoup

def getHtml(url):
    sock = urllib2.urlopen(url)
    data = sock.read()
    sock.close()
    return data

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
