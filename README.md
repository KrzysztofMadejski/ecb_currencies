# ECB currencies exchange rates

This app scrapes European Central Bank currencies exchange rates from https://www.ecb.europa.eu/home/html/rss.en.html.

## Install

Python version: 3.6.7+

```bash
pip install -r requirements.txt
```

## Run

To download currencies run
```bash
scrapy crawl currencies
```

To expose an API run the server
```bash
python manage.py runserver
```