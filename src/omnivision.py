"""
Name: Omnivision
Author: Dakota Carter
License: MIT
Description: Link-checker designed by Dakota Carter to check images and links on entire site.
TODO: Read file
TODO: Write Excel
TODO: TRy G
"""

from modules.scraper import Scrape
from modules.validator import Verify
from modules.exxel import write_excel
from common.arguments import get_arguments

class Omnivision:
    def __init__(self):
        args = get_arguments()
        scraper = Scrape(args.scrape)
        links, forms, images = scraper.main(args.urls)
        verifier = Verify()
        links, forms, images = verifier.main(links, forms, images)
        write_excel(images, links, forms)


if __name__ == '__main__':
    Omnivision()