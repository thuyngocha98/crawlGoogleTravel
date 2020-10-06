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
					'wait': 5
				}
			)


	def parse(self, response):
		items = CrawldatatravelItem()

		all_div = response.css('li.vb1Bh')
		for data in all_div:
			title = data.css('h3.NbdpWc::text').extract()
			image = data.css('img.vu5p2b::attr(src)').extract()
			desc = data.css('p.KGzLrd::text').extract()
			timemove = data.css('div::text').extract()
			if not desc:
				items['desc'] = "Not yet description"
			if desc:
				items['desc'] = desc[0]
			items['title'] = title[0]
			items['image'] = image[0]
			items['timemove'] = timemove[0]
			yield items
			
8
