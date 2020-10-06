import scrapy
from scrapy_splash import SplashRequest
from ..items import CrawldatatravelItem

class CrawlData(scrapy.Spider):
	name = "plantrip"
	allowed_domains = ["google.com.vn"]
	
	start_urls = [
		'https://www.google.com.vn/destination/map/itineraries/contained?sa=X&gl=us&hl=vi&tcfs=EhcKCS9tLzAxY3JkNRIKVmnhu4d0IE5hbQ&output=search&dest_mid=/m/06cl9r&itin_id=5e50baa2_89575a57_7a610d1d_bdbe5aac_832f469a&ictx=1&ved=0ahUKEwjG6aPfk5nmAhVGb30KHWVeCjIQzYoBCDIoAA#dest_mid=/m/06cl9r&tcfs=EiQKCS9tLzA2Y2w5chIXVGjDoG5oIHBo4buRIMSQw6AgTOG6oXQ'
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
		all_div = response.css('div.Lp63bf')
		for data in all_div:
			image = data.css('img.vu5p2b::attr(src)').extract()
			img_urls.append(image[0])
			items['image_urls'] = img_urls
			yield items
			

