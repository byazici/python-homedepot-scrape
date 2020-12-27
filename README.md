# python-homedepot-scrape

This code is scraping product information from https://www.homedepot.com/ and stores the data to mongodb database. 
You can find all products' url by fething https://www.homedepot.com/sitemap/d/pip_sitemap.xml. In this code I didn't implement batch scraping. I wrote this code for learning purposes only.

I used **MongoClient**, **BeautifulSoup** and  **requests** python packages.

<img src="https://corporate.homedepot.com/sites/default/files/image_gallery/THD_logo.jpg" width="250" alt="logo">

## Prerequisites
* Mongo DB 4.*
* Python 3.9.x

## Usage:
1. Clone the respository first:

`git clone https://github.com/byazici/python-homedepot-scrape.git`

2. You need **scrape.py** and **homedepot.py** files to scrape products. We have two methods in homedepot.py.
  - **scrape_html(html, mongo_url)** :  You can you this method for testing. I download a product html file and named "test.html". During the coding instead of fetching real url I used an html file.
  - **scrape_url(url, mongo_url)** : This method is the main function for scraping. You should pass homedepot url and mongo db connection url. 
3. I assumed that we have database named "devdb" and a table named "homedepot".

You should execute scrape.py:
`> python .\scrape.py`


### Success
If the execution finished successfully, you should see this:
```
> new recod id: 5fe87db3080ccedcb8e71e8f
> new recod id: 5fe87db4080ccedcb8e71e91
```

### Failure
I crated an index in mongodb to get an "duplicate" error for testing. When I execute second time;
```
> E11000 duplicate key error collection: devdb.homedepot index: ndx_url dup key: { url: "test.html" }, full error: {'index': 0, 'code': 11000, 'keyPattern': {'url': 1}, 'keyValue': {'url': 'test.html'}, 'errmsg': 'E11000 duplicate key error collection: devdb.homedepot index: ndx_url dup key: { url: "test.html" }'}
```

## Mongo Document Example
This is the scrape result fo **ttps://www.homedepot.com/p/Godinger-77-Piece-Stainless-Steel-Flatware-Set-43009/307532424** from mongo table.

```
{
    "_id" : ObjectId("5fe87db4080ccedcb8e71e91"),
    "url" : "https://www.homedepot.com/p/Godinger-77-Piece-Stainless-Steel-Flatware-Set-43009/307532424",
    "internet_no" : "307532424",
    "model_no" : "43009",
    "title" : "77-Piece Stainless Steel Flatware Set",
    "brand" : "Godinger",
    "currency" : "$",
    "price" : "82,00",
    "breadcrumbs" : [ 
        "Home", 
        "Kitchen", 
        "Tableware & Bar", 
        "Flatware", 
        "Flatware Sets"
    ],
    "media" : "https://images.homedepot-static.com/productImages/ec5f084c-8afc-4150-8aa7-4218ed21426c/svn/stainless-steel-godinger-flatware-sets-43009-64_600.jpg",
    "specs" : {
        "Cleaning Instructions" : "Hand Wash Only",
        "Color Family" : "Silver",
        "Color/Finish" : "STAINLESS STEEL",
        "Features" : "No Additional Features",
        "Handle Pattern" : "Solid",
        "Included" : "No Additional Items Included",
        "Intended Use" : "Residential,Restaurant",
        "Kitchen Product Type" : "Flatware Place Settings",
        "Material" : "Stainless Steel",
        "Number of Pieces" : "77",
        "Occasion" : "Year Round",
        "Package Type" : "Set",
        "Returnable" : "180-Day",
        "Service Set For" : "Set for 12",
        "Stainless Steel Grade" : "18/0",
        "Style" : "Classic",
        "Manufacturer Warranty" : "WILL REPLACE DAMAGED MERCHANDISE"
    },
    "overview" : "At Godinger Silver, we promise to give you flatware with unforgettable style and quality and, at the same time, an unbelievable value. Our standards of craftsmanship apply to every piece, every setting and accessory in our line. The result is that we provide the highest quality products to make your tabletop experience truly exceptional. 77- piece set includes 12 each: Salad forks, dinner forks, dinner knives, dinner spoons, teaspoons, and steak knives. And one of each, Serving Spoon, Serving Fork, Slotted Serving spoon, butter spreader, and sugar spoon. High-quality 18/0 stainless steel is dishwasher safe and never needs polishing, making it perfect for every day use and special occasions At Go dinger Silver, we expect the best.",
    "overviewBullets" : [ 
        "77-piece set includes 12-each dinner fork, dinner knife, dinner spoon, salad fork,teaspoon, steak knife, and one each serving spoon,serving fork,slotted serving spoon, butter spreader and sugar spoon", 
        "Made of stainless steel", 
        "Length for knife is 9 1/2 in. ,table spoon 8 in., large fork 8 in. ,salad fork 7 1/2 in. ,tea spoon 7 1/2 in.", 
        "Do not use in the oven", 
        "Return Policy"
    ]
}
```

