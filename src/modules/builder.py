"""
Name: 
Author: Dakota Carter (dakota.carter@perficient.com)
Owner: Perficient Inc.
License: N/A (if you ask me its MIT)
Description: 
"""

"""
Name: Omnivision
Author: Dakota Carter
License: MIT
Description: Scrapes webpage for objects on the page, that are specified in common
"""

from bs4 import BeautifulSoup
import urllib3
import os

from common.objects import bs4Rep, CategorizedList
from core.core import Core
import multiprocessing
from common.my_house import MyPool
from common.enums import ScrapeType
from common.annotations import timeit

class BuildUrl(Core):
    def __init__(self, base_url: str):
        super().__init__()
        if base_url.endswith("/"):
            base_url = base_url[:-1]
        self.base_url = base_url
        self.results = list()

    @timeit
    def main(self, pages: list):
        # TODO: multiprocess by urls too lmao
        # You can do it you had the idea on Friday October 4, 2019 7:42 PM
        pool = MyPool(3)
        for result in pool.map(self._combine_url, pages, 1000):
            self.results.append(result)
        return self.results

    def _combine_url(self, page: str):
        if page.startswith("/"):
            page = page[1:]
        return f"{self.base_url}/{page}"