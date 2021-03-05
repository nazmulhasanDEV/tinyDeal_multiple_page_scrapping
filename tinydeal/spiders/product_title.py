import scrapy


class ProductTitleSpider(scrapy.Spider):
    name = 'product_title'
    allowed_domains = ['www.tinydeals.co/product-category/smart-phones-tablets/']
    start_urls = ['https://www.tinydeals.co/product-category/smart-phones-tablets/%s' % x for x in range(13)]

    def parse(self, response):
        title = response.xpath("//div[@class='product-loop-header product-item__header']/a[@class='woocommerce-LoopProduct-link woocommerce-loop-product__link']/h2[@class='woocommerce-loop-product__title']")

        for x in title:
            yield {
                "Product Title" : x.xpath(".//text()").get()
            }
