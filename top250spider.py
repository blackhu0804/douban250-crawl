import scrapy
from scrapy.spiders import Spider
from scrapy_test.items import DoubanMovieItem

class MovieTop250Spider(Spider):
    name = 'movie_top250'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    start_urls = [
        'https://movie.douban.com/top250'
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse, headers=self.headers)

    def parse(self, response):
        item = DoubanMovieItem()
        for quote in response.css('div.item'):
            item['ranking'] = quote.css('div.pic em::text').extract()
            item['name'] = quote.css('div.info div.hd a span.title::text').extract_first()
            item['score'] = quote.css('div.info div.bd div.star span.rating_num::text').extract()
            yield item

        next_url = response.css('div.paginator span.next a::attr(href)').extract()
        if next_url:
            next_url = "https://movie.douban.com/top250" + next_url[0]
            print(next_url)
            yield scrapy.Request(next_url, headers=self.headers)