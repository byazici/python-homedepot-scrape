from homedepot import scrape_html
from homedepot import scrape_url

# mongo_db connection string
mongo_url = "mongodb://localhost:27017"

try:
    # scrapes downloaded homedepot product page for testing purposes
    file = "test.html"
    id = scrape_html(file, mongo_url)
    print ("new recod id: " + str(id))

    #scrapes directly from homedepot product page
    url = "https://www.homedepot.com/p/Godinger-77-Piece-Stainless-Steel-Flatware-Set-43009/307532424"
    id = scrape_url(url, mongo_url)
    print ("new recod id: " + str(id))

except Exception as ex:
    print(getattr(ex, 'message', str(ex)))



