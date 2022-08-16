from classes import Company, Founder
from scrapetools import ScrapeTools as st
import requests
from bs4 import BeautifulSoup as bs


def set_founders():
    companies = st.load('pkl/companies')
    for company in companies:
        soup = st.get_new_soup(company.url)
        divs1 = soup.find_all('div', class_='flex flex-row gap-3 items-start flex-col md:flex-row')
        if divs1:
            divs = divs1
        else:
            divs = soup.find_all('div', class_='ycdc-card shrink-0 space-y-1.5 sm:w-[300px]')
        for div in divs:
            name_el = div.find('div', class_='font-bold')
            name = name_el.get_text() if name_el else None
            twitter_el = div.find('a', title='Twitter account')
            twitter = twitter_el.get('href') if twitter_el else None
            linked_el = div.find('a', title='LinkedIn profile')
            linkedin = linked_el.get('href') if linked_el else None
            company.founders.append(Founder(name=name, twitter=twitter, linkedin=linkedin))
    st.dump(companies, 'pkl/companies_with_founders')



if __name__ == '__main__':
    set_founders()








