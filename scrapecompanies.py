import requests
from bs4 import BeautifulSoup
from scrapetools import ScrapeTools as st
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from classes import Company, Founder
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, \
    NoSuchAttributeException, \
    WebDriverException, MoveTargetOutOfBoundsException
import time


def get_company_hrefs(url):
    base_url = 'https://www.ycombinator.com'
    soup = st.get_new_soup(url)
    div = soup.find('div', class_='styles-module__section___2yul1 styles-module__results___2lP37')
    links = div.find_all('a')
    company_urls = []
    for link in links:
        rel_href = link.get('href')
        company_url = base_url + rel_href
        name = company_url.replace(base_url + '/companies/', '')
        company_urls.append((name, company_url))
    st.dump(company_urls, 'pkl/company_urls')
    return company_urls

def sel(url):
    base_url = 'https://www.ycombinator.com'
    company_urls = []
    d = wd.Chrome()
    d.get(url)
    time.sleep(3)
    # d.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    SCROLL_PAUSE_TIME = 0.5

    # Get scroll height
    last_height = d.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        d.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = d.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    el = d.find_element(By.XPATH, '/html/body/div/div[2]/section[2]/div/div[2]/div[4]')
    links = el.find_elements(By.XPATH, './/a[@class="styles-module__company___1UVnl no-hovercard"]')
    for link in links:
        company_url = link.get_attribute('href')
        name = company_url.replace(base_url + '/companies/', '')
        company_urls.append((name, company_url))
    d.close()
    st.dump(company_urls, 'pkl/company_urls')
    return company_urls


def init_companies():
    company_urls = st.load('pkl/company_urls')
    companies = []
    for tup in company_urls:
        companies.append(Company(name=tup[0]))
    st.dump(companies, 'pkl/companies')




if __name__ == '__main__':
    init_companies()



