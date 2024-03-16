from bs4 import BeautifulSoup
import requests

url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1311&_nkw=gpu+graphics+card&_sacat=0"
response = requests.get(url)
print(response)