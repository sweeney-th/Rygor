from CitationParser import CitationParser

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import requests

# simple class to store results in a tidy way
class Results(object):
    def __init__(self, paperInput, queryString, url,  soup):
        self.paperInput = paperInput   # what we submit to the constructor
        self.queryString = queryString # what we search the database for
        self.url = url                 # the actualy url used to make the query
        self.soup = soup               # the BeautifulSoup Object



# get the tables from the BeautifulSoup object
def getResultsTable(soup):
    # get all the tables from th page
    tables = soup.find_all("tbody")
    # get the table with the results
    resultsTable = [t for t in tables if len(t.find_all("span", attrs = {"class" : "totalItems"})) > 0]
    if len(resultsTable) == 0:
        # there was no "totalItems" of retractions, we're taking this to mean no retraction for this string
        return None
    else:
        return resultsTable[0]



# parses out the parts of the tables that are of interest in a retraction
def getResultsTableData(resultsTable):
    spans = resultsTable.find_all("span")
    divs = resultsTable.find_all("div")
    return spans + divs



# clean the input and makes the actual query
def queryRWDB(paper, clean = False):

    # TODO: robustify this by looking up more characters and noting behaviors
    def formatForRWDB(s):
        rwBaseURL = 'http://retractiondatabase.org/RetractionSearch.aspx#?ttl%3d'
        # will need to research and expand on this
        s = s.replace(' ', '%2b')
        s = s.replace(':', '%253a')
        return rwBaseURL + s
    
    # set options for selenium
    opts = Options()
    opts.headless = True
    driver = webdriver.Firefox(options = opts)

    # clean the input string if we're using scraped data
    if clean == True:
        cleanString = CitationParser.clean(paper)
    else:
        cleanString = paper
    
    # make it into the url for RWDB
    url = formatForRWDB(cleanString)
    # get the result from RWDB
    driver.get(url)

    # get the source code
    htmlSrc = driver.page_source
    # make it into soup
    soup = BeautifulSoup(htmlSrc, features = "html.parser")
    driver.quit()

    return Results(
        paperInput = paper,
        queryString = cleanString,
        url = url,
        soup = soup
    )



def getCitationsFromMedrxivURL(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    meta = soup.find_all("meta", attrs = {"name" : "citation_reference"})
    return[m['content'] for m in meta]