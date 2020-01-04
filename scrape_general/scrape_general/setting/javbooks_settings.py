# -*- coding: utf-8 -*-

CUSTOM_SETTINGS = {
    'ITEM_PIPELINES': {
        'scrape_general.pipeline.javbooks_pipeline.ScrapeGeneralPipeline': 1,
    },
}

mongo_db_name = 'javbooks'
mongo_db_collection = 'mosaic_movies'
