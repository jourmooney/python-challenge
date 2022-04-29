import os
import csv
import requests
from bs4 import BeautifulSoup

def get_jobs(keyword):
    url = f"https://remoteok.com/remote-{keyword}-jobs"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    results = soup.select("td.company.position.company_and_position")
    jobs = extract_jobs(results[1:])
    return jobs

def extract_job(html):
    company = html.select_one("h3").get_text(strip=True)
    title = html.select_one("h2").get_text(strip=True)
    link = f"https://remoteOK.com{html.select_one('a')['href']}"
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
