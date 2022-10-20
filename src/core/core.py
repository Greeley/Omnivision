"""
Name: Omnivision - core.py
Author: Dakota Carter
License: MIT
Description: Core component of the link-checker known as Omnivision
TODO: Get arguments
TODO: Keep it multiprocessed
TODO: Read filed
TODO: Build Scraper
TODO: build validator
TODO: build verifier
"""

import platform, os, sys, urllib3, re, sqlite3, time, json
import multiprocessing
from urllib.parse import urlparse
from common.objects import FakeResposne

class Core:

    def __init__(self):
        self.name = "Omnivision"
        self.date = time.strftime("%Y-%m-%d")  # Date Format ISO 8601
        self.start = time.strftime("%I_%M")  # Time
        self.exec_time = str(time.strftime("%I_%M_%p"))  # Time
        self.timeout = 20

    def get_response(self, url) -> object:
        pool = urllib3.PoolManager()
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            return pool.urlopen('HEAD', url, timeout=self.timeout)
        except Exception as e:
            return FakeResposne()

    def get_source(self, url) -> str:
        pool = urllib3.PoolManager()
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            return pool.urlopen('GET', url, timeout=self.timeout).data
        except Exception as e:
            raise(e)

    def get_protocol(self, url) -> str:
        return "{}:".format(urlparse(url).scheme)

    def get_site_root(self, url) -> str:
        parsed_uri = urlparse(url)
        return "{}://{}".format(parsed_uri.scheme, parsed_uri.netloc)

    def get_resource(self, relative_path) -> str:
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            basePath = sys._MEIPASS
        # check if _meipass is equal to the documents path,
        # if it is equal use os.path.abspath('.')
        except Exception:
            basePath = os.path.abspath(".")

        return os.path.join(basePath, relative_path)

    def mkdir(self, dir):
        if not os.path.exists(dir):  # Check if logs directory does not exist
            os.makedirs(dir)  # Create logs directory
            print("Successfully created: {}".format(dir))
        else:
            print("Directory already exists.")