"""
Name: 
Author: Dakota Carter

License: MIT
Description: Common Enumerations that are required through the
"""

from enum import Enum

class ScrapeType(Enum):
    """
    Every enum in here adds that same optio nto the --scrape command line argument
    """
    IMAGES = ['img', 'source']
    LINKS = ['a', 'link']
    FORMS = ['input', 'textarea', 'select', 'button']