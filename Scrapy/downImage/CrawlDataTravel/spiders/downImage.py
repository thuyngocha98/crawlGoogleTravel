import scrapy
from scrapy_splash import SplashRequest
from ..items import CrawldatatravelItem

class CrawlData(scrapy.Spider):
	name = "downImage"
	allowed_domains = ["google.com.vn"]
	
	start_urls = [
		'https://www.google.com.vn/travel/guide/map/itineraries/contained?dest_mid=%2Fm%2F06cl9r&itin_id=5e50baa2_89575a57_7a610d1d_bdbe5aac_832f469a&ved=0CGgQzYoBKABqFwoTCJi8v42di-wCFQAAAAAdAAAAABAB&ictx=1&hl=vi&gl=VN'
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
		all_div = response.css('div.eie4Pc')
		for data in all_div:
			image = data.css('img.vu5p2b::attr(src)').extract_first()
			title = data.css('p.KGzLrd::text').extract()
			#img_urls.append(image[0])
			print(title)
			#items['image_urls'] = img_urls
			#yield items
			

