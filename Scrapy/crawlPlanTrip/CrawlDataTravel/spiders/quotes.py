import scrapy
from scrapy_splash import SplashRequest
from ..items import CrawldatatravelItem

class CrawlData(scrapy.Spider):
	name = "quotesss"
	allowed_domains = ["google.com.vn"]
	
	start_urls = [
		'https://www.google.com.vn/travel/things-to-do/see-all?g2lb=2502405%2C2502548%2C4208993%2C4254308%2C4258168%2C4260007%2C4270442%2C4274032%2C4285990%2C4289525%2C4291318%2C4301054%2C4305595%2C4308216%2C4313006%2C4315873%2C4317816%2C4317915%2C4322164%2C4324289%2C4326763%2C4329288%2C4270859%2C4284970%2C4291517%2C4292955%2C4316256%2C4333107&hl=vi&gl=us&un=1&otf=1&dest_mid=%2Fm%2F06cl9r&dest_state_type=sattd#ttdm=11.915031_108.436638_12'
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

		all_div = response.css('div.NnEw9')
		for data in range(21):
			title = all_div[data].css('div.skFvHc::text').extract()
			image = all_div[data].css('img.R1Ybne::attr(src)').extract()
			desc = all_div[data].css('div.nFoFM::text').extract()
			if desc:
				items['title'] = title[0]
				items['image'] = image[0]
				items['desc'] = desc[0]
				yield items
			

