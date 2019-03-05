import requests
from bs4 import BeautifulSoup
import csv
import datetime
# lxml has to be installed

def get_html(url):
    r = requests.get(url)
    return r.text

def refined(s):
    r = s.split(' ')[0]
    result = r.replace(',', '')
    return result

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    popular = soup.find_all('section')[1]
    plugins = popular.find_all('article')
    for plugin in plugins:
        # [plugin1, plugin2, plugin3, plugin4]
        name = plugin.find('h2').text
        url = plugin.find('h2').find('a').get('href')
        rating = plugin.find('span', class_='rating-count').find('a').text
        rating = refined(rating)
        data = {'name': name,
                'url': url,
                'reviews': rating}
        write_csv(data)

def write_csv(data):
    with open('plugins.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'],
                         data['url'],
                         data['reviews'],
                         f"{datetime.datetime.now():%Y-%m-%d}"))

def main():
    url = 'https://wordpress.org/plugins/'
    print(get_data(get_html(url)))

if __name__ == "__main__":
    main()
