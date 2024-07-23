import urllib.parse

def strip_file_protocol(url):
    parsed_url = urllib.parse.urlparse(url)
    if parsed_url.scheme == 'file':
        return parsed_url.path
    return url
