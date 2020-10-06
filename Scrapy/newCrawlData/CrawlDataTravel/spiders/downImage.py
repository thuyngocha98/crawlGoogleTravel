import scrapy
from scrapy_splash import SplashRequest
from ..items import CrawldatatravelItem
import urllib.request
import uuid
from PIL import Image
import asyncio
import pickle
class CrawlData(scrapy.Spider):
	name = "downImage"
	allowed_domains = ["google.com.vn"]
	
	start_urls = [
		'https://www.google.com.vn/travel/things-to-do/see-all?dest_mid=%2Fm%2F02z4p59&dest_state_type=sattd&dest_src=yts&hl=vi&gl=VN&tcfs=EikKCi9tLzAyejRwNTkSG1bGsOG7nW4gUXXhu5FjIEdpYSBDw6F0IELDoA#ttdm=20.770016_107.027666_13&ttdmf=%252Fm%252F08dx1l'
]
	def start_requests(self):
		for url in self.start_urls:
			yield SplashRequest(
				url,
				self.parse,
				endpoint='render.html',
				args={'wait': 10}
			)

	async def downImage(self,pathDown, image):
		await urllib.request.urlretrieve(image, pathDown)
	def parse(self, response):
		items = CrawldatatravelItem()
		all_div = response.css('div.f4hh3d')
		for data in all_div:
			image = data.css('img.R1Ybne::attr(data-src)').extract_first()
			title = data.css('div.skFvHc::text').extract_first()
			desc = data.css('div.nFoFM::text').extract_first()
			if len(image) > 0:
				try:
					#down image
					pathDown = 'images/download/'+str(uuid.uuid4())+'.jpg'
					yield urllib.request.urlretrieve(image, pathDown)
					#resize image
					basewidth = 200
					img = Image.open(pathDown)
					filename = str(uuid.uuid4())+'.jpg'
					wpercent = (basewidth/float(img.size[0]))
					hsize = int((float(img.size[1])*float(wpercent)))
					img = img.resize((basewidth,hsize), Image.ANTIALIAS)
					yield img.save('images/resize/' + filename)
					obj = {'url': filename, 'title': title, 'desc': desc}
					items['url'] = filename
					items['title'] = title
					items['desc'] = desc
					yield items
				except:
					print('error')
