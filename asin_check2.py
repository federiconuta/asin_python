#!/usr/bin/env python\

"""
ASIN checking on Amazon.com
"""

import sys
import urllib.request as urllib2
import copy
from bs4 import BeautifulSoup
import pandas as pd
import cloudscraper


# Query ASIN on Amazon\


def asin_lookup2(product_name):


    # Convert spaces to pluses\
    query_product_name = product_name.replace(' ', '+')

    # Query the movie title on Amazon.com
    asin_query_url = "http://www.amazon.com/s/?url=search-alias%3Daps&field-keywords=" + query_product_name + "&rh=i%3Aaps%2Ck%3A" + query_product_name

    try:
        scraper = cloudscraper.create_scraper()
        q1 = scraper.get(asin_query_url)
        soup = BeautifulSoup(q1.text, 'lxml')
    except:
        print("URL could not be opened")
        return None
    else:
        # Find all divs with a 'data-asin' attribute (assuming each one represents a product)
        products = soup.find_all('div', {'data-asin': True})

        data_asin = []

        for product in products:
            asin = product['data-asin']
            product_name_tag = product.find('h2')
            product_name = product_name_tag.get_text().strip() if product_name_tag else 'Name not found'
    #print(f'ASIN: {asin}, Product Name: {product_name}')
    
            data_asin.append({'ASIN': asin, 'Product Name': product_name})
    
        df = pd.DataFrame(data_asin)


    return df



def main(argv=None):
    if argv is None:
        argv = sys.argv

    # Parse options and user input
    if len(argv) < 2:
        print("Please enter product name to lookup")
        exit()

    product_name = argv[1]

    # Query for keywords and capture the returned DataFrame
    df = asin_lookup2(product_name)

    # Check if the DataFrame is not empty and print it
    if df is not None:
        print(df)
    else:
        print("No data found.")

if __name__ == "__main__":
    sys.exit(main())

#def main(argv=None):
#    if argv is None:
#        argv = sys.argv

#    #0 Parse options and user input
#    if len(argv) < 2:
#        print("Please enter product name to lookup")
#        exit()

#    product_name = argv[1]

#    #1 Query for keywords
#    asin_lookup2(product_name)

#if __name__ == "__main__":
#    sys.exit(main())