# ASIN codes scraping
This repository provides an updated function to scrape and collect up ASIN codes of Amazon together with the product names related to the provided keyword.

### Usage

Download the file asin_check2.py.
If you work on Jupyter put it in the repository where you have your main .ipynb file.
Then type:

`from asin_check2 import asin_lookup2`

The usage is simple. Just type `asin_lookup2("product_name")`.

### Example usage:

asin_lookup2("airpods"):

<img width="286" alt="Screenshot 2024-01-16 at 3 23 26 PM" src="https://github.com/federiconuta/asin_python/assets/51603270/82e7b22a-0aaf-48a1-83c3-5c0e921e8326">


Clean the dataset whereby necessary.

## Class version

The file called amazonscraperclass.py provides a more compact way to perform the task. Specifically it defines a class `AmazonASINScraper` with an attribute called `get_first_three_asins` which returns the name of the product and the first 3 non missing ASIN for the product search input.

# Usage
```
scraper = AmazonASINScraper()
df = pd.DataFrame({'Name': ['Airpods', 'Echo', 'Kindle']})  # Example DataFrame

df['ASINs'] = df['Name'].apply(scraper.get_first_three_asins)
print(df)
```

