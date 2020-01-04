import scrapy


class JavbooksMovieItem(scrapy.Item):
    # outside info
    movie_name = scrapy.Field()
    thumbnail = scrapy.Field()
    serial_url = scrapy.Field()

    # detail info
    cover_image = scrapy.Field()

    serial_number = scrapy.Field()
    serial_group_url = scrapy.Field()

    issue_date = scrapy.Field()
    movie_duration = scrapy.Field()

    director_name = scrapy.Field()
    director_url = scrapy.Field()

    manufacturer = scrapy.Field()
    manufacturer_url = scrapy.Field()

    publisher = scrapy.Field()
    publisher_url = scrapy.Field()

    series = scrapy.Field()
    series_url = scrapy.Field()

    movie_category = scrapy.Field()
    actress = scrapy.Field()

    gallery = scrapy.Field()
    download_info = scrapy.Field()
