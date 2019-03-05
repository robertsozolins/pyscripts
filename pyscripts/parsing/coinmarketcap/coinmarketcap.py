import requests
from bs4 import BeautifulSoup
import csv
import datetime

def get_html(url):
    r = requests.get(url)
    return r.text

def get_page_data(html):
    # https://coinmarketcap.com
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find('table', id='currencies').find('tbody').find_all('tr')
    for tr in trs:
        tds = tr.find_all('td')
        name = tds[1].find('a', class_='currency-name-container').text
        symbol = tds[1].find('a').text
        url = 'https://coinmarketcap.com' + tds[1].find('a').get('href')
        price = tds[3].find('a').get('data-usd')
        today = f"{datetime.datetime.now():%Y-%m-%d}"
        data = {'name': name,
                'symbol': symbol,
                'url': url,
                'price': price,
                'date': today}
        write_csv(data)

def write_csv(data):
    with open('coinmarket.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([data['name'],
                         data['symbol'],
                         data['url'],
                         data['price'],
                         data['date']
                         ])

def main():
    url = 'http://coinmarketcap.com/'
    get_page_data(get_html(url))

if __name__ == "__main__":
    main()
