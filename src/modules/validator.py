"""
Name: Omnivision
Author: Dakota Carter
License: MIT
Description: Validates what needs to be checked inside the bs4Rep class
"""

from common.objects import bs4Rep, CategorizedList
from core.core import Core
import multiprocessing
from common.my_house import MyPool
import base64
from common.annotations import timeit


class Validate(Core):

    def __init__(self):
        super().__init__()

    @timeit
    def main(self, links, forms, images):
        pool = MyPool()
        for result in pool.map(self._divvy_up, [links, images, forms]):
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
        proper_function = getattr(self, '_verify_{}'.format(categorized_list.category.lower()))
        new_list = list()
        for result in pool.map(proper_function, categorized_list, 1000):
            new_list.append(result)
        return CategorizedList(categorized_list.category, list_name, new_list)


    def _verify_forms(self, element):
        ...

    def _verify_images(self, element):
        response = self.get_response(element.check)
        print(response.status)
        element.status = response.status
        element.message = response.reason
        if element.validate:
            element.is_valid = base64.b64decode(element.validate, True)
        return element

    def _verify_links(self, element):
        response = self.get_response(element.check)
        element.status = response.status
        element.message = response.reason
        return element

