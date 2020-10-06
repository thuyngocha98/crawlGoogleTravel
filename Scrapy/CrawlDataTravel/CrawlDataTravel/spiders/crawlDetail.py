import scrapy
from ..items import CrawldatatravelItem
from scrapy_splash import SplashRequest



class CrawlData(scrapy.Spider):
	name = "crawlDetail"
	allowed_domains = ["google.com.vn"]
	start_urls = (
		'https://www.google.com.vn/travel/things-to-do/see-all?g2lb=2502405%2C2502548%2C4208993%2C4254308%2C4258168%2C4260007%2C4270442%2C4274032%2C4285990%2C4288513%2C4289525%2C4291318%2C4296668%2C4301054%2C4302819%2C4305595%2C4308216%2C4313006%2C4315873%2C4317816%2C4317909%2C4322164%2C4324289%2C4329288%2C4270859%2C4284970%2C4291517%2C4292955%2C4316256&hl=vi&gl=us&un=1&otf=1&dest_mid=%2Fm%2F0hn4h&dest_state_type=sattd#ttdm=10.814388_106.627157_9&ttdmf=%25252Fg%25252F120tb76z',
	)

	def start_requests(self):
		for url in self.start_urls:
			yield scrapy.Request(url, self.parse, meta={
				'splash': {
					'endpoint': 'render.html',
					'args': {'wait': 5}
				}
			})

	def parse(self, response):
		all_div = response.css("div.kXlUEb")
		for data in all_div:
			image = data.css('img.R1Ybne::attr(src)').extract()
			yield {
				'image': image
			}
