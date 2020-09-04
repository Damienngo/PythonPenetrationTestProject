import scrapy
import requests
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


# Get Status_Code and Change Header.
x = requests.get('http://172.18.58.238/spicyx/')
xheaders = {'Title': 'Mobile'}
xcookies = {'visit-month': 'February'}
xy = requests.get(headers=xheaders, url='http://172.18.58.238/spicyx/')

# True or False Status 200.
p = x.status_code == requests.codes.ok
if p == True:
    print("Status_Ok")
    print(x.status_code)
else:
    print("Failed")


# Crawl Entire HTML
class MyEntireHTTPSpider(scrapy.Spider):
    name = 'http'
    start_urls = ["http://172.18.58.238/spicyx/"]

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),)

    def parse(self, response):
            filename = response.url.split("/")[-2] + '.html'
            with open(filename, 'wb') as f:
                f.write(response.body)
            # scrapy crawl http -o http.json

# Crawl Text
class MyTextSpider(scrapy.Spider):

    name = 'scrapycrawling'
    start_urls = [
        'http://172.18.58.238/spicyx/',
        ]

    def parse(self, response):

        for text in response.xpath('.//div[@class="tab-content"]'):

            relative_image = htmltext.xpath('//a/img/@src').getall()
            p1 = htmltext.xpath('.//p/text()').getall()
            h4 = htmltext.xpath('.//h4/text()').getall()


            yield {
                'Image': relative_image,
                'h4': h4,
                'p': p1,

            }

class MyEntireSpider(scrapy.Spider):
    name = 'http2'
    start_urls = ["http://172.18.58.238/spicyx/"]

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),)

    def parse(self, response):
            filename = response.url.split("/")[-2] + '.json'
            with open(filename, 'wb') as f:
                f.write(response.body)
            # scrapy crawl http -o http.json

class testspider(unittest.TestCase):

    def test_1(self):
        pass


if __name__ == '__main__':
    unittest.main()
