# Job Scraper API

A RESTful API built with **FastAPI** to scrape and serve public job listings. This project demonstrates web scraping, database integration, and API development in Python, with an interactive interface provided via Swagger UI.

---

## **Features**

- Scrape job listings from a demo website using `requests` and `BeautifulSoup`.
- Store job data in a **SQLite database** using `SQLAlchemy`.
- Expose REST API endpoints for:
  - Viewing all jobs
  - Searching jobs by location
  - Triggering scraping
- Interactive API documentation with **Swagger UI** (no frontend code needed).

---

## **Tech Stack**

- **Python 3.13**
- **FastAPI** – Web framework for building APIs
- **Uvicorn** – ASGI server to run FastAPI
- **Requests** – For making HTTP requests
- **BeautifulSoup4** – For parsing HTML and scraping job data
- **SQLAlchemy** – ORM for database interactions
- **SQLite** – Lightweight database
- **Pydantic** – Data validation and serialization

---

## **Installation**

```bash
git clone https://github.com/YourUsername/job-scraper-api.git
cd job-scraper-api
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
