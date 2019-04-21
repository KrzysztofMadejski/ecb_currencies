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

## TODOs

- Store crawled currencies in the database
- Create setup.py: specify Python version (Python 3.6.7) + document the app
- Create proper error handling in REST responses `{errors: {msg: code:}`
- Add Swagger documentation: https://github.com/axnsan12/drf-yasg/#installation
- Prepare for production deployment (Docker, etc)
- Write simple scraper test than crawls the ECB website and makes sure something is retrieved. As it requires internet connection make sure it is not run by default