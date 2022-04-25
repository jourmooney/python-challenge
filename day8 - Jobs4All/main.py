import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")
alba_url = "http://www.alba.co.kr"

def get_company_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    result = soup.select("div#MainSuperBrand > ul.goodsBox > li > a.goodsBox-info")
    return result

def get_last_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    result = soup.select("div#NormalInfo > p.jobCount > strong")[0].get_text(strip=True)
    last_page = int(result) // 50 + 1
    return int(last_page)

def extract_job(html):
    place = html.select_one("td.local.first")
    title = html.select_one("span.company")
    time = html.select_one("td.data")
    pay = html.select_one("td.pay")
    date = html.select_one("td.regDate.last")
    return {
        'place': place,
        'title': title,
        'time': time,
        'pay': pay,
        'date': date,
    }

def extract_jobs(last_page, url):
    jobs=[]
    for page in range(last_page):
        print(f"Scrapping SO: Page: {page+1}")
        response = requests.get(f"{url}/job/brand/?page={page+1}")
        soup = BeautifulSoup(response.text, "html.parser")
        results = soup.select("div#SubContents > div#NormalInfo > table > tbody > tr:not(.summaryView)")[0]
        for result in results:
            print(result)
            job = extract_job(result)
            jobs.append(job)
    return jobs
    
company_urls = get_company_links(alba_url)
for url in company_urls[:2]:
    print(f"Scraping {url.select('img')[0]['alt']}")
    # print(f"Scraping {url.select('span.company')[0].get_text()}")
    url = url['href']
    last_page = get_last_page(url)
    jobs = extract_jobs(last_page, url)

print(jobs)

