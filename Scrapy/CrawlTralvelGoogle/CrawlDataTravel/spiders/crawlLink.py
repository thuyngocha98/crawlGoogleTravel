import scrapy
from scrapy_splash import SplashRequest
from ..items import CrawldatatravelItem

class CrawlData(scrapy.Spider):
	name = "crawlLink"
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
		array = []
		all_div = response.css('a.sjglme')
		for data in all_div:
			href = data.css('a.sjglme::attr(href)').extract()
			
			if href:
				url = 'https://www.google.com.vn' + href[0]
				yield SplashRequest(
					url,
					self.parse_first_dropdown,
					endpoint='render.html',
					args={
						'wait': 5
					}
				)

	def parse_first_dropdown(self, response):

		all_div = response.css('a.vwv1Oe')
		for data in all_div:
			href = data.css('a.vwv1Oe::attr(href)').extract()
			if href:
				url = 'https://www.google.com.vn' + href[0]
				yield SplashRequest(
					url,
					self.parse_second_dropdown,
					endpoint='render.html',
					args={
						'wait': 5
					}
				)

	def parse_second_dropdown(self, response):
		items = CrawldatatravelItem()
		all_div = response.css('div.rbj0Ud')
		for data in all_div:
			href = data.css('div.skFvHc::text').extract()
			if href:
				items['title'] = href[0]
				yield items


			

