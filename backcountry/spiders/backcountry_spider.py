import scrapy

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from backcountry.items import BackcountryItem
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

class BackcountrySpider(CrawlSpider):
  name = 'back'
  allowed_domains = ['http://www.backcountry.com/', 'www.backcountry.com']

  #Start URL categories.
  #1 mens-jackets
  #2 mens-pants
  #3 mens-shirts
  #4 mens-underwear-baselayers
  #5 mens-shorts
  #6 mens-shoes-footwear
  #7 mens-accessories
  #8 sunglasses
  #9 watches
  #10 mens-bike-clothing
  #11 mens-running-clothing
  #12 fly-fishing-apparel
  start_urls = ['http://www.backcountry.com/Store/catalog/categoryLanding.jsp?categoryId=bcsCat110004&page=0',
                'http://www.backcountry.com/Store/catalog/categoryLanding.jsp?categoryId=bcsCat1100026&page=0',
                'http://www.backcountry.com/Store/catalog/categoryLanding.jsp?categoryId=bcsCat1100075&page=0',
                'http://www.backcountry.com/Store/catalog/categoryLanding.jsp?categoryId=bcsCat11000115&page=0',
                'http://www.backcountry.com/Store/catalog/categoryLanding.jsp?categoryId=bcsCat11000142&page=0',
                'http://www.backcountry.com/Store/catalog/categoryLanding.jsp?categoryId=bcsCat11000219&page=0',
                'http://www.backcountry.com/Store/catalog/categoryLanding.jsp?categoryId=bcsCat11000148&page=0',
                'http://www.backcountry.com/Store/catalog/categoryLanding.jsp?categoryId=bcsCat131000072&page=0',
                'http://www.backcountry.com/Store/catalog/categoryLanding.jsp?categoryId=bcsCat1310000126&page=0',
                'http://www.backcountry.com/Store/catalog/categoryLanding.jsp?categoryId=bcsCat141000004&page=0',
                'http://www.backcountry.com/Store/catalog/categoryLanding.jsp?categoryId=bcsCat15000010&page=0',
                'http://www.backcountry.com/Store/catalog/categoryLanding.jsp?categoryId=cat100201200&page=0'
                ]

  rules = (Rule (SgmlLinkExtractor(restrict_xpaths=('//li[@class="pag-next"]'))
    , callback="parse_items", follow= True),
    )

  def parse_start_url(self, response):
    return self.parse_items(response)
  
  def parse_items(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//div[contains(@class, "item-listing")]')
        items = []
        for site in sites:
            item = BackcountryItem()
            item['brand'] = site.select('a/h4/span/strong[@class="brand-name"]/text()').extract()
            item['product_name'] = site.select('a/h4/span[@class="product-name"]/text()').extract()
            item['price'] = str(site.select('a/p[@class="item-listing-offers"]/strong[@class="qa-price price"]/text()').extract()).replace("u'\\n","").replace(" ","").replace("'","")
            item['low_price'] = str(site.select('a/p[@class="item-listing-offers"]/span[@class="from-price-wrap"]/strong/text()').extract()).replace("u'\\n","").replace(" ","").replace("'","")
            item['high_price'] = str(site.select('a/p[@class="item-listing-offers"]/small/span[@class="qa-high-price high-price"]/text()').extract()).replace("u'\\n","").replace(" ","").replace("'","")
            item['href'] = site.select('a[contains(@class, "qa-product-link")]/@href').extract()
            items.append(item)
        return items
