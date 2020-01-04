# -*- coding: utf-8 -*-


CUSTOM_SETTINGS = {
    'ITEM_PIPELINES': {
        'scrape_general.pipeline.douban_top250_pipeline.ScrapeGeneralPipeline': 1,
    },
}

mongo_db_name = 'douban'
mongo_db_collection = 'douban_top_movie'
