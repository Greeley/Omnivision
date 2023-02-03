"""
Name: Omnivision
Author: Dakota Carter
License: MIT
Description: Scrapes webpage for objects on the page, that are specified in common
"""

from bs4 import BeautifulSoup

from common.objects import bs4Rep, CategorizedList
from core.core import Core
import multiprocessing
from common.my_house import MyPool
from common.enums import ScrapeType
from common.annotations import timeit

class Verify(Core):
    def __init__(self, scrape_types: list):
        super().__init__()
        self.scrape_types = list().extend([scrape.upper() for scrape in scrape_types])

    @timeit
    def main(self, images_list, links_list, forms_list):
        pool = MyPool(3)
        for result in pool.map(self._divvy_up, [images_list, links_list, forms_list]):
            if hasattr(self, result.name):
                attr = getattr(self, result.name)
                attr.extend(result)
                setattr(self, result.name, attr)
            else:
                setattr(self, result.name, CategorizedList(result.category, result.name, result))
        return self.checkable_links, self.checkable_forms, self.checkable_images


    def _divvy_up(self, categorized_list):
            pool = multiprocessing.Pool()
            list_name = "checkable_{}".format(categorized_list.category.lower())
            proper_function = getattr(self, '_scrape_{}'.format(categorized_list.category.lower()))
            new_list = list()
            for result in pool.map(proper_function, categorized_list, 1000):
                new_list.append(result)
            return CategorizedList(categorized_list.category, list_name, new_list)


    def _scrape_forms(self, element):
        """
        Nothing to do Here.
        :param element:
        :return:
        """
        return element

    def _scrape_images(self, element):
        image_attributes = ['src', 'srcset', 'data-srcset']
        for attribute in image_attributes:
            check = element.attrs.get(attribute)
            if check is None:
                pass
            elif check.startswith('http'):
                element.check = check
            elif check.startswith('/') and not check.startswith('//'):
                element.check = "{}{}".format(self.get_protocol(element.url), check)
            elif check.startswith('data'):
                element.validate = check
        return element

    def _scrape_links(self, element):
        try:
            try:
                check = element.attrs['href']
            except Exception as e:
                return element
            if check.startswith('http'):
                element.check = check
            elif check.startswith('//'):
                element.check = "{}{}".format(self.get_protocol(element.url), check)
            elif check.startswith('/') and not check.startswith('//'):
                element.check = "{}{}".format(self.get_site_root(element.url), check)
            elif check.startswith('#'):
                element.check = "{}{}".format(element.url, check)
            elif check.startswith('java'):
                element.check = "{}?{}".format(element.url, check)
        except Exception as e:
            raise(e)
        return element

if __name__ == '__main__':
    test = Verify(['links'])
    test.main(['https://www.lincoln.com', 'https://www.ford.com'])