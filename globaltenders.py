import scrapy


class GlobalTendersSpider(scrapy.Spider):
    name = "globaltenders"

    def start_requests(self):
        urls = [
            'https://www.globaltenders.com/free-global-tenders/index.php',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'globaltenders-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
            
        self.log(f'Saved file {filename}')