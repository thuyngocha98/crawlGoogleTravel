# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
from PIL import Image
from cStringIO import StringIO
import re

class CrawldatatravelPipeline(ImagesPipeline):

    CONVERTED_ORIGINAL = re.compile('^full/[0-9,a-f]+.jpg$')

    # name information coming from the spider, in each item
    # add this information to Requests() for individual images downloads
    # through "meta" dictionary
    def get_media_requests(self, item, info):
        return [Request(x, meta={'image_name': item["image_name"]})
                for x in item.get('image_urls', [])]

    # this is where the image is extracted from the HTTP response
    def get_images(self, response, request, info):

        for key, image, buf, in super(jellyImagesPipeline, self).get_images(response, request, info):
            if self.CONVERTED_ORIGINAL.match(key):
                key = self.change_filename(key, response)
            yield key, image, buf

    def change_filename(self, key, response):
        return "full/%s.jpg" % response.meta['image_name'][0]
