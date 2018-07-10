import scrapy

class jobCrawler(scrapy.Spider):
    name="jobSpider"
    start_urls = ['https://search.51job.com/list/330000%252C010000,000000,0000,00,9,99,%25E5%2589%258D%25E7%25AB%25AF,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=']

    def parse(self, response):
        # print(response.url)
        titles = response.xpath('//*[@id="resultList"]/div[@class="el"]/span[@class="t3"]/text()').extract()
        for title in titles:
            print(title.strip())
