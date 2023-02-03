"""
Name: Omnivision
Author: Dakota Carter
License: MIT
Description: Link-checker designed by Dakota Carter to check images and links on entire site.
TODO: Read file
TODO: Write Excel
TODO: TRy G
"""

from modules.validator import Validate
from modules.scraper import Scrape
from modules.verifier import Verify
from modules.exxel import write_excel
from modules.builder import BuildUrl
from common.arguments import get_arguments

class Omnivision:
    def __init__(self):
        args = get_arguments()
        if args.base_url:
            urlBuilder = BuildUrl(args.base_url)
            args.urls = urlBuilder.main(args.urls)

        scraper = Scrape(args.scrape)
        links, forms, images = scraper.main(args.urls)

        verifier = Verify(args.scrape)
        normalized_links, normalized_forms, normalized_images = verifier.main(links, forms, images)

        validator = Validate()
        validated_links, validated_forms, validated_images = validator.main(links, forms, images)

        write_excel(images, links, forms)


if __name__ == '__main__':
    Omnivision()