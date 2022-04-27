import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")
alba_url = "http://www.alba.co.kr"

def get_company(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    result = soup.select("div#MainSuperBrand > ul.goodsBox > li > a.goodsBox-info")
    company = [(r.select_one('span.company').get_text(strip=True).replace("/", "-"), r['href']) for r in result]
    return company

def get_last_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    result = soup.select("div#NormalInfo > p > strong")[0].get_text(strip=True).replace(",", "")
    if int(result) % 50 == 0:
        last_page = int(result) // 50
    else:
        last_page = int(result) // 50 + 1
    return int(last_page)

def extract_job(html):
    place = html.select_one("td.local.first").get_text(strip=True)
    title = html.select_one("span.company").get_text(strip=True)
    time = html.select_one("td.data").get_text(strip=True)
    pay = html.select_one("td.pay").get_text(strip=True)
    date = html.select_one("td.regDate.last").get_text(strip=True)
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
        print(f"Scrapping: Page: {page+1}")
        response = requests.get(f"{url}/job/brand/?page={page+1}")
        soup = BeautifulSoup(response.text, "html.parser")
        results = soup.select("div#SubContents > div#NormalInfo > table > tbody > tr:not(.summaryView)")
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs

def save_to_file(jobs, name):
    file = open(f"{name}.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(["Title", "Company", "Location", "Link"])
    for job in jobs:
        writer.writerow(list(job.values()))
    print("Saved to file.")
    return

company = get_company(alba_url)
for name, url in company:
    print(f"Scraping {url}")
    last_page = get_last_page(url)
    jobs = extract_jobs(last_page, url)
    save_to_file(jobs, name)
print("Scraping completed.")

