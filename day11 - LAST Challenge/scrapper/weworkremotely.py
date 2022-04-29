import os
import csv
import requests
from bs4 import BeautifulSoup

def get_jobs(keyword):
    url = f"https://weworkremotely.com/remote-jobs/search?term={keyword}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    results = soup.select(".jobs > article > ul > li.feature > a")
    jobs = extract_jobs(results)
    return jobs

def extract_job(html):
    company = html.select_one("span.company").get_text()
    title = html.select_one("span.title").get_text()
    link = f"https://weworkremotely.com{html['href']}"
    return {
        "title": title,
        "company": company,
        "link": link
    }

def extract_jobs(htmls):
    jobs = []
    for html in htmls:
        jobs.append(extract_job(html))
    return jobs
