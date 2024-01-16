import pandas as pd
import cloudscraper
from bs4 import BeautifulSoup

class AmazonASINScraper:
    def __init__(self):
        # Initialize the scraper
        self.scraper = cloudscraper.create_scraper()

    def asin_lookup2(self, product_name):
        query_product_name = product_name.replace(' ', '+')
        asin_query_url = "http://www.amazon.com/s/?url=search-alias%3Daps&field-keywords=" + query_product_name + "&rh=i%3Aaps%2Ck%3A" + query_product_name
        try:
            response = self.scraper.get(asin_query_url)
            soup = BeautifulSoup(response.text, 'lxml')
            products = soup.find_all('div', {'data-asin': True})
            data_asin = [{'ASIN': product['data-asin'], 'Product Name': product.find('h2').get_text().strip() if product.find('h2') else 'Name not found'} for product in products if product['data-asin']]
            return pd.DataFrame(data_asin)
        except Exception as e:
            print(f"Error occurred: {e}")
            return pd.DataFrame()

    def get_first_three_asins(self, product_name):
        result_df = self.asin_lookup2(product_name)
        if not result_df.empty:
            valid_asins = result_df['ASIN'].dropna().unique()[:3]
            return valid_asins.tolist()
        else:
            return []

