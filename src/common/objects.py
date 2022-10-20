"""
Name: Omnivision
Author: Dakota Carter

License: MIT
Description: Common objects found throughout the code
"""
from .enums import ScrapeType

class bs4Rep:
    def __init__(self, ele, url):
        self.name = ele.name
        self.attrs = ele.attrs
        self.url = url
        self.check = str()
        self.status = int()
        self.message = str()
        self.validate = str()
        self.is_valid = str()
        self.category = self._check_category(ele.name)

    def _check_category(self, name):
        for scrape_type in ScrapeType:
            if name in scrape_type.value:
                return scrape_type.name

    def __repr__(self):
        return "\n\nFrom: {}\nFound <{}> with:\n{}\nCheck: {}\nstatus: {}".format(
            self.url, self.name, self.attrs, self.check, self.status
        )

class CategorizedList(list):
    def __init__(self, category, name=str(), iterable = list()):
        super(CategorizedList, self).__init__()
        self.name = name
        self.extend(iterable)
        self.category = category


class FakeResposne:
    def __init__(self):
        self.status = 408
        self.reason = "Connection timed out"