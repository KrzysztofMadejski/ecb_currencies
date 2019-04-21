# ECB currencies exchange rates

This app scrapes European Central Bank currencies exchange rates from https://www.ecb.europa.eu/home/html/rss.en.html.

## Architecture

This project consists of three parts:
- default simple Django project
- an app `currencies` implementing v1 of the API
- a scrapy project crawling ECB's websites (I haven't managed in 3 hours to connect it with Django in order to store results in the DB)

## Install

Python version: 3.6.7+

```bash
pip install -r requirements.txt
```

## Test

```bash
python manage.py test
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

## TODOs

- Store crawled currencies in the database (via ItemPipelines calling API, or Django executing scrapy programatically)
- Create setup.py: specify Python version (Python 3.6.7) + document the app
- Create proper error handling in REST responses `{errors: {msg: code:}`
- Add Swagger documentation: https://github.com/axnsan12/drf-yasg/#installation
- Prepare for production deployment (Docker, etc)
- Write simple scraper test than crawls the ECB website and makes sure something is retrieved. As it requires internet connection make sure it is not run by default