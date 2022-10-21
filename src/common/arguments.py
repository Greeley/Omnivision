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
                        help='.txt file to import a list of urls from. One URL per line. Include http:// or https://\n'
                             'file path can be an SVN url location')
    parser.add_argument('-s', "--scrape", action='store', dest='scrape',
                        help='Options: ' + str(scrapable) + " separate scrape types with commas")
    parser.add_argument('-su', "--svn-user", action='store', dest='svnuser',
                        help='The username for the svn repository given as --file')
    parser.add_argument('-sp', "--svn-user", action='store', dest='svnpass',
                        help='The password for the svn repository given as --file')
    arguments = parser.parse_args()

    arguments.urls = arguments.urls.split(',')
    arguments.scrape = arguments.scrape.split(',')
    if arguments.file:
        if schema_pattern.match(arguments.file):
            if not arguments.svnuser and not arguments.svnpass:
                parser.error("if --file is an svn url --svn-user and --svn-password are required")
            arguments.urls = download_by_svn(arguments.file, arguments.svnuser, arguments.svnpass)
        else:
            arguments.urls = open(arguments.file, 'r').read().splitlines(keepends=False)
    return arguments


def download_by_svn(address: str, username: str, password: str):
    response = requests.get(address, auth=(username, password), verify=False)
    try:
        lines = response.text.split('\n')
        for index, line in enumerate(lines):
            lines[index] = line
    except:
        raise Exception("SVN url might have failed on us, we'll be adding svn auth to the configuration file")
    return lines