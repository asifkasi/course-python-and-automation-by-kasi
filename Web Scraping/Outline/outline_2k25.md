# Web Scraping & Automation — Course Outline (Hands-on)

## 0) Onboarding & Setup (Day 1)

* Install: Python 3.11+, VS Code, Git, Chrome/Chromium
* Quick intro to HTTP, HTML/DOM, CSS selectors, JSON
* Mini-lab: parse a simple HTML page and save data to CSV

## Week 1) Core Scraping with `requests` + `BeautifulSoup`

* Requests basics: methods, headers, cookies, sessions
* Parsing with Soup: find/select, CSS selectors vs. tag traversal
* Pagination patterns & URL discovery
* Project 1: scrape book titles/prices from *books.toscrape.com* and export CSV/JSON

## Week 2) Selectors, XPath & Regex Precision

* CSS specificity, nth-child, attribute selectors
* XPath fundamentals (when & why)
* Light use of regex for cleanup (not for full parsing)
* Lab: build robust selectors; write selector tests

## Week 3) Working with Statics and Dynamic Sites (JS-rendered)

* When static fails: detecting JS rendering
* Headless browsers: Playwright (preferred) vs Selenium
* Waiting strategies: locators, network idle, timeouts
* Project 2: scrape infinite scroll results (e.g., a demo shop like *scrapeme.live/shop*)

## Week 4) Sessions, Logins, and State

* Cookies, auth flows, CSRF tokens, maintaining sessions
* Handling redirects; form submissions
* Project 3: log in to a practice site and scrape your dashboard data (use a demo site you control)

## Week 5) Anti-bot Hygiene, Ethics & Compliance (must-have)

* `robots.txt`, Terms of Service, fair use, rate limits
* Polite scraping: concurrency caps, jitter, exponential backoff, retries
* IP rotation & proxies (concepts, when appropriate & lawful)
* CAPTCHAs: detect & avoid (do not bypass); prefer APIs/allowlisted sources
* Lab: add retry/backoff & caching to an existing scraper

## Week 7) Data Storage & Pipelines

* Writing to CSV/JSON/Parquet
* SQLite/PostgreSQL basics; SQLAlchemy
* File storage & structure for large runs
* Project 5: store scraped jobs/news into a Postgres DB and build a simple query script

## Week 8) Automation & RPA with Playwright

* Filling forms, clicking, file uploads, keyboard/clipboard
* Scheduling tasks (cron/Task Scheduler) & notifications (email/webhook)
* Project 6: daily automation bot—login → download a report → clean → email summary

## Week 9) Async & High-Throughput Scraping

* Concurrency primitives: `asyncio`, `aiohttp`, semaphores
* Rate limiting per host; connection pools
* Batching URLs & graceful error handling
* Project 7: async price monitor for 200+ product URLs with delta alerts

## Week 10) APIs First (When Available)

* Finding & using public APIs; reading API docs
* Auth: API keys, OAuth basics; pagination & filtering
* Project 8: compare API vs. scrape for the same data; measure speed/accuracy

## Week 11) Cleaning, Validation, and QA

* Normalizing text, dates, currency; duplicate detection
* Pydantic for data models & validation
* Snapshot tests, golden files, and pytest for scrapers
* Lab: write tests that fail when site layout changes

## Week 12) Files, Media & Edge Cases

* Downloading files (PDF/images) with streaming & checksum
* Extracting text from PDFs (pdfminer/pymupdf) and basic OCR (Tesseract) when permitted
* Project 9: PDF report collector → extract tables → append to DB

## Week 13) Monitoring, Logging & Observability

* Structured logs; rotating log files
* Job run summaries & alerts (Slack/email)
* Run IDs, checkpoints, idempotency
* Lab: add metrics & alerts to a long-running crawler

## Week 14) Packaging & Deployment

* Dockerizing scrapers; environment variables & secrets
* Cloud runs: GitHub Actions, serverless (AWS Lambda/Cloud Run) basics
* Cost control & reliability tips
* Capstone: productionized pipeline—crawl → validate → store → notify, running on a schedule

---

## Suggested Hands-on Projects (mix & match)

1. Bookstore tracker: price & availability monitor with weekly diff email.
2. Job aggregator (allowlisted sites): titles, companies, locations, skills → searchable DB.
3. Real-time news headlines: scrape a permissible feed + sentiment tag + daily digest.
4. E-commerce catalog builder: categories, variants, images, pagination & incremental updates.
5. Event calendar builder: city events into Google Sheet with de-dupe & date normalization.
6. Report fetcher bot: logs in, downloads CSV, cleans it, emails dashboard snapshot.

*(Use training-friendly/demo sites like* `books.toscrape.com`, `quotes.toscrape.com`, `scrapeme.live/shop` *and official APIs where possible.)*

---

## Tooling Stack (recommended)

* Python: requests, httpx/aiohttp, BeautifulSoup4, lxml, Playwright, Scrapy, Pydantic, SQLAlchemy, pytest
* Infra: Docker, GitHub Actions, Postgres/SQLite, Redis (optional caching), cron
* Utilities: tenacity (retries), backoff, loguru/structlog, python-dotenv

---

## Deliverables per Module

* Slides/notes (short)
* Starter & solution notebooks/scripts
* A repeatable project template repo
* Checklists: ethics & rate limiting, deployment, QA

---
# Course Benefits

* Job-ready skills, fast: Go from zero to production—HTTP, parsing, dynamic sites, and automation workflows you can ship.
* Portfolio projects: 6–9 real scrapers/automation bots (login flows, infinite scroll, PDF/table extractors) you can showcase.
* Automation superpowers: Build bots that log in, download reports, clean data, and alert you—hands-free.
* Data you can trust: Learn validation (Pydantic), tests (pytest), and QA checks so pipelines don’t silently break.
* Scalable tooling: Scrapy for crawling at scale; Playwright/Selenium for tough, JS-heavy sites.
* Faster workflows: Async patterns and smart rate-limiting to handle hundreds of pages efficiently and politely.
* Deployment ready: Docker + schedulers/CI so your jobs run reliably on a timer (cloud or on-prem).
* Ethical & compliant: Best practices for robots.txt, ToS, rate limits, and when to prefer official APIs.
* Clean outputs, any stack: Export to CSV/JSON/Parquet, load into SQLite/Postgres, and hook into dashboards.
* Debug like a pro: Structured logs, retries/backoff, and monitoring to spot failures early.
* Career leverage: Roles in data engineering, growth, research, or RPA—plus talking points for interviews.
* Reusable templates: Starter repos, checklists, and patterns you’ll reuse on future projects.
* Community & feedback: Code reviews on projects and guidance on improving scraper resilience.
* Certificate of completion: Document your skills and project outcomes.

## You’ll be able to

* Identify when to scrape vs. when to use an API, and implement both.
* Handle auth, sessions, pagination, and dynamic rendering confidently.
* Build end-to-end pipelines: crawl → clean → validate → store → notify.

## Tools you’ll master

`requests`, `BeautifulSoup`, Playwright/Selenium, Scrapy, `aiohttp/httpx`, Pydantic, pytest, SQLAlchemy, Docker, GitHub Actions/cron.
