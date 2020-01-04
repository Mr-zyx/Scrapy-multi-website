import scrapy
from scrape_general.items.javbooks_items import JavbooksMovieItem
from scrape_general.setting import javbooks_settings


class JavbooksSpider(scrapy.Spider):
    name = "javbooks_spider"
    allowed_domains = ["ss9874.com"]
    custom_settings = javbooks_settings.CUSTOM_SETTINGS

    start_urls = [
        "https://ss9874.com/serchinfo_censored/topicsbt/topicsbt_1.htm"
    ]

    def parse(self, response):
        movie_list = response.xpath("//div[@id='PoShow_Box']/div[@class='Po_topic']")

        for i_item in movie_list:
            javbook_item = JavbooksMovieItem()
            javbook_item['movie_name'] = i_item.xpath("./div[@class='Po_topic_title']/a/b/text()").extract_first()
            javbook_item['thumbnail'] = i_item.xpath("./div[@class='Po_topicCG']/a/img/@src").extract_first()
            javbook_item['serial_url'] = i_item.xpath("./div[@class='Po_topicCG']/a/@href").extract_first()
            javbook_item = scrapy.Request(javbook_item['serial_url'], callback=self.get_detail_info,
                                          meta={'item': javbook_item})
            yield javbook_item

        next_page_url = response.xpath("//div[@class='PageBar']/span[@class='pageback']/a/@href").extract_first()
        if next_page_url:
            self.log('has next page, continue... %s' % next_page_url)
            yield scrapy.Request(next_page_url, callback=self.parse)

    def get_detail_info(self, response):
        javbook_item = response.meta['item']
        javbook_item['cover_image'] = response.xpath("//div[@id='info']/div[@class='info_cg']/img/@src").extract_first()
        javbook_item['serial_number'] = response.xpath("//div[@id='info']/div[@class='infobox']/font/a/font/font/text()").extract_first()
        javbook_item['serial_group_url'] = response.xpath(
            "//div[@id='info']/div[@class='infobox']/font/a/@href").extract_first()
        javbook_item['issue_date'] = response.xpath("//div[@id='info']/div[3][@class='infobox']/text()").extract_first()
        javbook_item['movie_duration'] = response.xpath(
            "//div[@id='info']/div[4][@class='infobox']/text()").extract_first()
        javbook_item['director_name'] = response.xpath(
            "//div[@id='info']/div[5][@class='infobox']/a/text()").extract_first()
        javbook_item['director_url'] = response.xpath(
            "//div[@id='info']/div[5][@class='infobox']/a/@href").extract_first()
        javbook_item['manufacturer'] = response.xpath(
            "//div[@id='info']/div[6][@class='infobox']/a/text()").extract_first()
        javbook_item['manufacturer_url'] = response.xpath(
            "//div[@id='info']/div[6][@class='infobox']/a/@href").extract_first()
        javbook_item['publisher'] = response.xpath(
            "//div[@id='info']/div[7][@class='infobox']/a/text()").extract_first()
        javbook_item['publisher_url'] = response.xpath(
            "//div[@id='info']/div[7][@class='infobox']/a/@href").extract_first()
        javbook_item['series'] = response.xpath(
            "//div[@id='info']/div[8][@class='infobox']/a/text()").extract_first()
        javbook_item['series_url'] = response.xpath(
            "//div[@id='info']/div[8][@class='infobox']/a/@href").extract_first()

        category_names = response.xpath("//div[@id='info']/div[9][@class='infobox']/a/text()").extract()
        category_urls = response.xpath("//div[@id='info']/div[9][@class='infobox']/a/@href").extract()
        javbook_item['movie_category'] = [{"name": name, "url": url} for name, url in
                                          zip(category_names, category_urls)]

        actress_names = response.xpath(
            "//div[@id='info']/div[10][@class='infobox']/div[@class='av_performer_cg_box']/div[@class='av_performer_name_box']/a/text()").extract()
        actress_urls = response.xpath(
            "//div[@id='info']/div[10][@class='infobox']/div[@class='av_performer_cg_box']/div[@class='av_performer_name_box']/a/@href").extract()
        actress_imgs = response.xpath(
            "//div[@id='info']/div[10][@class='infobox']/div[@class='av_performer_cg_box']/img/@src").extract()
        javbook_item['actress'] = []
        count = 0
        for actress_name in actress_names:
            javbook_item['actress'].append(
                {'name': actress_name, 'url': actress_urls[count], 'img': actress_imgs[count]})
            count += 1

        gallery_litimg_list = response.xpath("//div[@class='gallery']/div[@class='hvr-grow']/a/img/@src").extract()
        gallery_intact_list = response.xpath("//div[@class='gallery']/div[@class='hvr-grow']/a/@href").extract()
        count = 0
        javbook_item['gallery'] = []
        for gallery_litimg in gallery_litimg_list:
            javbook_item['gallery'].append(
                {'litimg_url': gallery_litimg, 'intact_url': gallery_intact_list[count]})
            count += 1

        download_info_names = response.xpath(
            "//div[@class='dht_dl_area']/div[@class='dht_dl_title_content']/span/a/font/font").extract()
        download_info_thunder_urls = response.xpath(
            "//div[@class='dht_dl_area']/div[@class='dht_dl_title_content']/span/a/@href").extract()
        download_info_size_list = response.xpath(
            "//div[@class='dht_dl_area']/div[@class='dht_dl_size_content']/font/font").extract()
        download_info_shared_date_list = response.xpath(
            "//div[@class='dht_dl_area']/div[@class='dht_dl_date_content']/font/font").extract()
        javbook_item['download_info'] = []
        count = 0
        for download_info_name in download_info_names:
            javbook_item['download_info'].append(
                {'name': download_info_name, 'thunder_url': download_info_thunder_urls[count],
                 'size': download_info_size_list[count], 'shared_date': download_info_shared_date_list[count]})
            count += 1

        yield javbook_item
