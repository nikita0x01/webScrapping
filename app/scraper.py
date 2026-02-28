import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

URL = "https://realpython.github.io/fake-jobs/"

def scrape_jobs():
    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []
    cards = soup.find_all("div", class_="card-content")

    for card in cards:
        title = card.find("h2", class_="title").text.strip()
        company = card.find("h3", class_="company").text.strip()
        location = card.find("p", class_="location").text.strip()
        link = card.find("a", text="Apply")["href"]

        jobs.append({
            "title": title,
            "company": company,
            "location": location,
            "link": link
        })

    return jobs
