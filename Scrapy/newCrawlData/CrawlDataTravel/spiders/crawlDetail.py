import scrapy
from ..items import CrawldatatravelItem
from scrapy_splash import SplashRequest



class CrawlData(scrapy.Spider):
	name = "crawlDetail"
	allowed_domains = ["google.com.vn"]
	start_urls = [
		'https://www.google.com.vn/travel/things-to-do/see-all?dest_mid=%2Fm%2F06cl9r&dest_state_type=sattd&dest_src=yts&g2lb=2502548%2C4258168%2C4270442%2C4306835%2C4308227%2C4317915%2C4322823%2C4328159%2C4371334%2C4401769%2C4419364%2C4424916%2C4433754&hl=vi&gl=VN#ttdm=11.915821_108.435778_12&ttdmf=%252Fm%252F0bbvkrv'
]

	def start_requests(self):
		for url in self.start_urls:
			yield scrapy.Request(url, self.parse, meta={
				'splash': {
					'endpoint': 'render.html',
					'args': {'wait': 15}
				}
			})

	def parse(self, response):
		all_div = response.css("div.kXlUEb")
		for data in all_div:
			image = data.css('img.R1Ybne::attr(src)').extract()
			yield {
				'image': image
			}
