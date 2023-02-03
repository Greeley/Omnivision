"""
Name: Omnivision
Author: Dakota Carter
License: MIT
Description: Link-checker designed by Dakota Carter to check images and links on entire site.
TODO: Read file
TODO: Write Excel
TODO: TRy G
"""

import unittest
from modules.builder import BuildUrl

class BuilderTestCase(unittest.TestCase):


    def test_url_builder_expected(self):
        URL_TEST_KEY = ["https://example.com/page1", "https://example.com/page2", "https://example.com/page3"]

        base_url = "https://example.com"
        url_pages = ["/page1", "/page2", "/page3"]
        urlBuilder = BuildUrl(base_url)
        full_urls = urlBuilder.main(url_pages)
        self.assertEqual(URL_TEST_KEY, full_urls)

    def test_url_builder_unexpected(self):
        URL_TEST_KEY = ["http://example.com/page1", "http://example.com/page2", "http://example.com/page3"]

        base_url = "http://example.com/" #note the delimiter "/" here and at beginning of pages
        url_pages = ["/page1", "/page2", "/page3"]
        urlBuilder = BuildUrl(base_url)
        full_urls = urlBuilder.main(url_pages)
        self.assertEqual(URL_TEST_KEY, full_urls)


if __name__ == '__main__':
    unittest.main()
