from pymongo import MongoClient
from bs4 import BeautifulSoup
import requests

def scrape_html(html, mongo_url):
    content = open(html)
    soup = BeautifulSoup(content.read(), "html.parser")
    doc = scraper(soup, html)
    return save_to_mongo(mongo_url, doc)

def scrape_url(url, mongo_url):
    req = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=20)
    soup = BeautifulSoup(req.text, "html.parser")
    doc = scraper(soup, url)
    return  save_to_mongo(mongo_url, doc)

def scraper(soup, src):
    title = soup.find("h1", "product-details__title").string
    brand = soup.find("h2", "product-details__brand-name").string
    media = soup.find("a", "mediagallery__anchor").div.img.get("src")
    overview = soup.find("div", "desktop-content-wrapper__main-description")
    int_no = soup.find("h2", "product-info-bar__detail")
    model_no = int_no.next_sibling

    price_ = soup.find("div", "price-format__main-price")
    currency = price_.contents[0].string
    price = price_.contents[1].string + "," +  price_.contents[2].string

    breadcrumb = soup.find("div", "breadcrumbs__nowrap--3qP_e")
    breadcrumbs = list()
    for child in breadcrumb.children:
        breadcrumbs.append (child.string)

    specs = {}
    for elem in soup.find_all("div", "specifications__row"):
        key = elem.div.next_element.string
        if key:
            key = key.replace(".", "")
            specs[key] = elem.div.next_element.next_element.string

    overviewBullets = list()
    for elem in overview.contents[1].find("ul"):
        overviewBullets.append(elem.string.replace("\n\r", ""))


    # build document
    doc = {}
    doc["url"] = src
    doc["internet_no"] = int_no.contents[2]
    doc["model_no"] = model_no.contents[2]
    doc["title"] = title
    doc["brand"] = brand
    doc["currency"] = currency
    doc["price"] = price
    doc["breadcrumbs"] = breadcrumbs
    doc["media"] = media
    doc["specs"] = specs
    doc["overview"] = overview.contents[0].replace('\n', '')
    doc["overviewBullets"] = overviewBullets

    return doc

# insert document to mongodb
def save_to_mongo(mongo_url, doc):
    client = MongoClient(mongo_url)
    db = client["devdb"]
    col = db["homedepot"]

    return col.insert_one(doc).inserted_id
