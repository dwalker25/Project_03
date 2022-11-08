import argparse
import requests
from bs4 import BeautifulSoup
import json

def parse_itemssold(text):
    numbers = ''
    for char in text:
        if char in '1234567890':
            numbers += char
    if 'sold' in text:
        return int(numbers)
    else:
        return 0

def parse_prices(s):
    s = s.replace('$', '')
    s = s.replace('.', '')
    s = s.replace(',', '')
    s = s.split()
    try:
        s = int(s[0])
        return s
    except:
        return s

def parse_shipping(s):
    if 'free' in s.lower():
        return 0
    else:
        s = s.replace('$', '')
        s = s.replace('.', '')
        s = s.replace('+', '')
        s = s.split()
        return int(s[0])
        
        
# Get command line aruments
parser = argparse.ArgumentParser(
                    description = 'Download info from Ebay and convet to JSON')
parser.add_argument('search_term') 
parser.add_argument('--num_pages', default=10)
args = parser.parse_args()
print('search_term = ', args.search_term)

#list of all items found in ebay webpages
items = []

# loop over the ebay webpages
for page_number in range(1, int(args.num_pages)+1):

    # build the url
    url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=' + args.search_term + '&_sacat=0&_pgn=' + str(page_number)
    print('url =', url)

    # download the html
    r = requests.get(url)
    status = r.status_code
    print('status =', status)

    html = r.text
    # print('html =', html[:50])

    # proccess the html
    soup = BeautifulSoup(html, 'html.parser')

    # loop over the items in the page
    tags_items = soup.select('.s-item')
    for tag_item in tags_items:

        name = None
        tags_name = tag_item.select('.s-item__title')
        for tag in tags_name:
            name = tag.text

        freereturns = None
        tags_freereturns = tag_item.select('.s-item__free-returns')
        for tag in tags_freereturns:
            freereturns = True

        items_sold = None
        tags_itemssold = tag_item.select('.s-item__hotness')
        for tag in tags_itemssold:
            items_sold = parse_itemssold(tag.text)

        status = None
        tags_status = tag_item.select('.SECONDARY_INFO')
        for tag in tags_status:
            status = tag.text

        price = None
        tags_price = tag_item.select('.s-item__price')
        for tag in tags_price:
            price = parse_prices(tag.text)

        shipping = None
        tags_shipping = tag_item.select('.s-item__shipping, .s-item__logisticsCost, .s-item__freeXDays')
        for tag in tags_shipping:
            shipping = parse_shipping(tag.text)

        item = {
            'name': name,
            'freereturns': freereturns,
            'items_sold': items_sold,
            'status': status,
            'price': price,
            'shipping': shipping,
        }
        items.append(item)

# write the json to a file
filename = args.search_term+'.json'
with open(filename, 'w', encoding='ascii') as f:
    f.write(json.dumps(items))
