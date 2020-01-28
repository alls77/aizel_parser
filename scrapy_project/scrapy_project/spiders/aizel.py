import scrapy

from scrapy_redis.spiders import RedisSpider

from scrapy_project.items import ScrapyProjectItem


class AizelSpider(RedisSpider):
    name = 'aizel'
    allowed_domains = ['aizel.ru']

    def parse(self, response):
        pages_count = int(response.xpath("//li[contains(@class, 'm-pagination__item')]/a/text()").extract()[-1])
        urls = [f'https://aizel.ru/ua-ru/zhenskoe/obuv/?page={page}' for page in range(1, pages_count + 1)]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.get_items)

    def get_items(self, response):
        links = response.xpath(
            "//a[contains(@class, 'a-urlOverlay js-loadRevealImage ddl_product_link')]/@href").extract()

        for link in links:
            yield scrapy.Request(url=f'https://aizel.ru{link}', callback=self.get_item_details)

    def get_item_details(self, response):
        category = response.xpath("//li[contains(@class, 'a-breadcrumbs__item')]/a/text()").extract()[-1]
        price = response.xpath("//div[contains(@class, 'js-productPrice')]/div[contains(@class, 'a-amount -big')]"
                               "/div[contains(@class, 'a-amount__amount')]/text()").get()
        title = response.xpath("//h1[contains(@class, 'a-heading -h1 -h1Seo')]/span/text()").get()
        brand = response.xpath("//h1[contains(@class, 'a-heading -h1 -h1Seo')]/a/span/text()").get()
        sizes = response.xpath(
            "//select[contains(@class, 'a-select js-productSizeSelect js-stockId js-productSelectChange js-sizeView')]"
            "/option/text()").extract()
        images = response.xpath('//img[contains(@class, "js-productPicture js-lazyLoad")]/@data-src').extract()
        description = response.xpath("//div[contains(@class, 'm-accordion__contentInner')]//text()").extract()

        items = ScrapyProjectItem()
        items['category'] = category
        items['price'] = ''.join(price.split("\xa0")) + " RUB" if price is not None else None
        items['title'] = title
        items['brand'] = brand
        items['sizes'] = sizes
        items['images'] = images
        items['description'] = ''.join(description[-1])

        yield items
