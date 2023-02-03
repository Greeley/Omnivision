"""
Name: 
Author: Dakota Carter (dakota.carter@perficient.com)
Owner: Perficient Inc.
License: N/A (if you ask me its MIT)
Description: 
"""

from bs4 import BeautifulSoup

from common.objects import bs4Rep, CategorizedList
from core.core import Core
import multiprocessing
from common.my_house import MyPool
from common.enums import ScrapeType
from common.annotations import timeit


class Scrape(Core):

    def __init__(self, scrape_types: list):
        super().__init__()
        self.scrape_types = list()
        self.scrape_types.extend([scrape.upper() for scrape in scrape_types])
        self.successfully_scraped = set()


    def main(self, urls: list):
        #todo: remove urls from urls list if url is in self.successfully_scraped

        images_list = CategorizedList(ScrapeType.IMAGES.name)
        links_list = CategorizedList(ScrapeType.LINKS.name)
        forms_list = CategorizedList(ScrapeType.FORMS.name)

        bs4Reps = list()

        pool = MyPool()
        for result in pool.map(self._scrape, urls, 1000):
            [locals()['{}_list'.format(element.category.lower())].append(element) for element in result]

        return images_list, links_list, forms_list

    def _scrape(self, url) -> list:
        to_scrape = list()
        soup = BeautifulSoup(self.get_source(url), 'lxml')
        to_scrape.extend([ScrapeType[st].value for st in self.scrape_types])
        return [bs4Rep(element, url) for element in soup.find_all(to_scrape)]

