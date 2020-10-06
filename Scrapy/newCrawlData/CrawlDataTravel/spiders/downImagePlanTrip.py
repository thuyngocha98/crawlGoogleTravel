import scrapy
from scrapy_splash import SplashRequest
from ..items import CrawldatatravelItem

class CrawlData(scrapy.Spider):
	name = "plantrip"
	allowed_domains = ["google.com.vn"]
	
	start_urls = [
		'https://www.google.com.vn/travel/things-to-do?dest_mid=%2Fm%2F06cl9r&dest_state_type=main&dest_src=yts&g2lb=2502548%2C4258168%2C4270442%2C4306835%2C4308227%2C4317915%2C4322823%2C4328159%2C4371334%2C4401769%2C4419364%2C4424916%2C4433754&hl=vi&gl=VN#ttdm=11.894518_108.464426_10&ttdmf=%25252Fm%25252F0bbvkrv'
]
	def start_requests(self):
		for url in self.start_urls:
			yield SplashRequest(
				url,
				self.parse,
				endpoint='render.html',
				args={
					'wait': 10
				}
			)


	def parse(self, response):
		items = CrawldatatravelItem()
		img_urls = []
		all_div = response.css('div.f4hh3d')
		for data in all_div:
			temp = data.css('easy-img.dBuxib')
			image = temp.css('img.R1Ybne::attr(data-src)').extract()
			print(image)
			#img_urls.append(image[0])
			#items['image_urls'] = img_urls
			#yield items
			

