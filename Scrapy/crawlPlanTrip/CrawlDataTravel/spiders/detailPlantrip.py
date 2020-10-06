import scrapy
from scrapy_splash import SplashRequest
from ..items import CrawldatatravelItem

class CrawlData(scrapy.Spider):
	name = "detailplantrip"
	allowed_domains = ["google.com.vn"]
	
	start_urls = [
		'https://www.google.com.vn/destination/map/itineraries/contained?sa=X&gl=us&hl=vi&tcfs=EhcKCS9tLzAxY3JkNRIKVmnhu4d0IE5hbQ&output=search&dest_mid=/m/06fbpd&itin_id=f39122b7_b5a1fea0_e77b0f68_f7236a3d_72c4f398&ictx=1&ved=0ahUKEwiQsLCo-pjmAhX26nMBHd5IBkoQzYoBCDMoAA#dest_mid=/m/06fbpd&tcfs=EiIKCS9tLzA2ZmJwZBIVVGjDoG5oIHBo4buRIEjhu5lpIEFu'
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
		all_div = response.css('div.L8zLFc')
		filename = 'quotes.html'
		with open(filename, 'wb') as f:
			f.write(response.body)
		self.log('Saved file %s' % filename)

			

