import scrapy
from scrapy_splash import SplashRequest
from ..items import CrawldatatravelItem

class CrawlData(scrapy.Spider):
	name = "crawlMainData"
	allowed_domains = ["google.com.vn"]
	
	start_urls = [
		'https://www.google.com.vn/destination/compare?hl=vi&gl=us&output=search&dest_mid=/m/01crd5#dest_mid=/m/01crd5&tcfs=EhcKCS9tLzAxY3JkNRIKVmnhu4d0IE5hbQ'
	]
	def start_requests(self):
		for url in self.start_urls:
			yield SplashRequest(
				url,
				self.parse,
				endpoint='render.html',
				args={
					'wait': 5
				}
			)


	def parse(self, response):
		items = CrawldatatravelItem()
		img_urls = []
		all_div = response.css('div.gws-trips-desktop__city-card')
		for data in all_div:
			image = data.css('img.bh9Cef::attr(src)').extract()
			if image:
				img_urls.append(image[0])
				items['image_urls'] = img_urls

				yield items
			

