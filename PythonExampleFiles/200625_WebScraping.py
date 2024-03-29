from bs4 import BeautifulSoup
import requests
import re

session = requests.Session()
sp500 = 'https://www.reuters.com/finance/markets/index/.SPX'
page = 1
regex = re.compile(r'\/finance\/stocks\/overview\/.*')
symbols = []
while True:
    print('Scraping page:', page)
    params = params={'sortBy': '', 'sortDir' :'', 'pn': page}
    html = session.get(sp500, params=params).text
    soup = BeautifulSoup(html, "html.parser")
    pagenav = soup.find(class_='pageNavigation')
    if not pagenav:
        break
    companies = pagenav.find_next('table', class_='dataTable')
    for link in companies.find_all('a', href=regex):
        symbols.append(link.get('href').split('/')[-1])
    page += 1
print(symbols)
