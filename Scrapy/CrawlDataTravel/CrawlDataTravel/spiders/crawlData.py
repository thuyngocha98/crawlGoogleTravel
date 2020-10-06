import scrapy
from ..items import CrawldatatravelItem



class CrawlData(scrapy.Spider):
	name = "crawlData"
	
	start_urls = ['https://www.google.com.vn/travel/guide?dest_mid=%2Fm%2F06cl9r&dest_src=yts&ved=0CAsQm_ECahcKEwig_NHMzuzlAhUAAAAAHQAAAAAQAw&hl=vi&gl=us#dest_mid=/m/06cl9r&dest_src=yts&tcfs=EiQKCS9tLzA2Y2w5chIXVGjDoG5oIHBo4buRIMSQw6AgTOG6oXQ']

	def parse(self, response):

		items = CrawldatatravelItem()

		all_div = response.css('destination-card-large.pOVhe')
		for data in all_div:
			title = data.css('div.KMnnid::text').extract()
			image = data.css('img.rISBZc::attr(src)').extract()
			desc = data.css('div.hO00Vc::text').extract()

			items['title'] = title
			items['image'] = image
			items['desc'] = desc
			yield items

