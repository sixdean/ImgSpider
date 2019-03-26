import scrapy
from Imagespider.items import ImagespiderItem

class ImgspiderSpider(scrapy.Spider):
    name = 'ImgSpider'
    allowed_domains = ['lab.scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn/archives/55.html']

    def parse(self, response):
        item = ImagespiderItem()  # 实例化item1
        imgurls = response.css(".post img::attr(src)").extract() # 注意这里是一个集合也就是多张图片
        item['imgurl'] = imgurls
        self.logger.info(imgurls)
        yield item
        pass