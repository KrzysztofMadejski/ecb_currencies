import scrapy
import re
import dateutil.parser
from decimal import Decimal


class CurrenciesSpider(scrapy.Spider):
    name = "currencies"
    start_urls = ['https://www.ecb.europa.eu/home/html/rss.en.html']
    allowed_domains = ['www.ecb.europa.eu', 'ecb.europa.eu']

    def parse(self, response):
        for link in response.css('a.rss::attr(href)').getall():
            # TODO we might want to scrape ::text as well to get and store the names of the currencies
            m = re.match(r'/rss/fxref\-(\w{3})\.html', link)
            if m:
                # To save a list of currencies
                # yield {
                #     'currency': m[1]
                # }
                yield response.follow(link, callback=self.parse_rss)

    def parse_rss(self, response):
        """Parses RSS feed of a given currency"""
        response.selector.remove_namespaces()  # TODO properly would be to register all needed namespaces
        for item in response.xpath('/RDF/item'):
            data = {
                'date': item.xpath('date/text()').get(),
                'rate': Decimal(item.xpath('statistics/exchangeRate/value/text()').get()),
                'currency': item.xpath('statistics/exchangeRate/targetCurrency/text()').get(),
                'base': item.xpath('statistics/exchangeRate/baseCurrency/text()').get()
            }
            data['date_parsed'] = dateutil.parser.parse(data['date'])
            # TODO use datetime.fromisoformat(date_string) in python 3.7+

            yield data
