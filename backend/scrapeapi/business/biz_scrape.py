
from selectorlib import Extractor
import os
import requests
import json 
import csv
from time import sleep
from datetime import date, datetime, timezone
from scrapeapi.definitions import ROOT_DIR

from sqlalchemy.orm import Session

from sqlalchemy.orm import Session

from scrapeapi.api import apimodels
from scrapeapi.persistence import dbmodels
from scrapeapi.persistence import database
# from scrapeapi.api.apimodels import Article

# Create an Extractor by reading from the YAML file

extractor = Extractor.from_yaml_file(f'{ROOT_DIR}/business/selectors.yml')

def biz_amazon_scrape(url):  
    headers = {
        'authority': 'www.amazon.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    # Download the page using requests
    print("Downloading %s"%url)
    r = requests.get(url, headers=headers)
    # Simple check to check if page was blocked (Usually 503)
    if r.status_code > 500:
        
        if "To discuss automated access to Amazon data please contact" in r.text:
            print("Page %s was blocked by Amazon. Please try using better proxies\n"%url)
        else:
            print("Page %s must have been blocked by Amazon as the status code was %d"%(url,r.status_code))
        return None
    if str(r.status_code)[0] != "2":
        print(f'Page {url} could not be retrieved successfully: {r.text[:500]}')
    # Pass the HTML of the page and create
    data = extractor.extract(r.text)
    if data:
        data["id"] = -1
        data["scraped_at"] = datetime.utcnow().isoformat()
        data["scrape_url"] = url
    return data


def create_article(db: Session, article: apimodels.AmazonArticle):
    article = dbmodels.AmazonArticle(
        name = article.name,
        price = article.price,
        short_description = article.short_description
    )
    db.add(article)
    db.commit()
    db.refresh(article)
    return article


#   id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     price = Column(Numeric)
#     short_description=Column(String)
#     images=Column(String)
#     rating=Column(String)
#     number_of_reviews=Column(Integer)
#     variants=Column(String)
#     product_description=Column(String)
#     sales_rank=Column(Integer)
#     link_to_all_reviews=Column(String)
#     scrape_timestamp=Column(DateTime)
#     url=Column(String)

# def write_csv(file, data_list):

#     exists = False
#     if os.path.exists(file) and os.path.getsize(file) > 0:
#         exists = True

#     with open(file, 'a', newline='', encoding='utf-8') as csvfile:
#         fieldnames = ['name', 'price', 'short_description', 'images', 'rating', 'number_of_reviews', 'variants', 'product_description', 'sales_rank', 'link_to_all_reviews', 'scrape_timestamp', 'url']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect=csv.excel_tab)

#         if not exists:
#             writer.writeheader()
#         for data in data_list:
#             writer.writerow(data)


# if __name__ == "__main__":
#     print("scraping...")
#     date = date.today().strftime('%Y%m%d')
    
#     data_list = []
#     with open("urls.txt",'r') as urllist:
#         for url in urllist.read().splitlines():
#             data = scrape(url)
#             if data:
#                 data["scrape_timestamp"] = datetime.utcnow().isoformat()
#                 data["url"] = url
#                 data_list.append(data)

#     write_csv(f'output_{date}.csv', data_list)
#     with open(f'output_{date}.json','a') as outfile:
#         json.dump(data_list, outfile, indent=2)
#         outfile.write("\n")