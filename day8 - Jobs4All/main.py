import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")
alba_url = "http://www.alba.co.kr"

# def get_company_links(url):
#     response = requests.get(alba_url)
#     soup = BeautifulSoup(response.text, "html.parser")
#     result = soup.select("div#MainSuperBrand ul.goodsBox li a[href]")
#     return result

# url = get_company_links(alba_url)[0].get('href')
url = "http://mcdonalds.alba.co.kr/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
result = soup.select("div#SubContents > div#NormalInfo > table > tbody")
print(result[0])
# title = html.select("")

# place = html.select_one("span.local").get_text()
# title = html.select_one("span.company").get_text()
# time
# pay
# date
