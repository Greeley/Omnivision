import argparse
import re, requests


def get_arguments():
    schema_pattern = re.compile(r'([\w]+:/{2})')
    schema_pattern.match('string',)
    parser = argparse.ArgumentParser()
    scrapable = ['images', 'links', 'forms']

    parser.add_argument('-u', "--url", action='store', dest='urls',
                        help='http://<url> or https://<URL> for multiple urls separate with comma. e.g. example.com,example.com')
    parser.add_argument('-f', "--file", action='store', dest='file',
                        help='.txt file to import a list of urls from. One URL per line. Include http:// or https://')
    parser.add_argument('-s', "--scrape", action='store', dest='scrape',
                        help='Options: ' + str(scrapable) + " separate scrape types with commas")
    arguments = parser.parse_args()

    arguments.urls = arguments.urls.split(',')
    arguments.scrape = arguments.scrape.split(',')
    if arguments.file:
        if schema_pattern.match(arguments.file):
            arguments.urls = download_by_svn(arguments.file)
        else:
            arguments.urls = open(arguments.file, 'r').read().splitlines(keepends=False)
    return arguments


def download_by_svn(address):
    response = requests.get(address, auth=('detauto', 'Det@utos'), verify=False)
    try:
        lines = response.text.split('\n')
        for index, line in enumerate(lines):
            lines[index] = line
    except:
        raise Exception("SVN url might have failed on us, we'll be adding svn auth to the configuration file")
    return lines