import webbrowser
import sys

valid_websites = [
    'reddit.com',
    'stackoverflow.com',
    'stackexchange.com',
    'medium.com',
]

url = "https://www.google.com/search?q="

edge_path = 'open -a '
chrome_path = ''


def create_filter(): #Search query
    filter = '('
    for index, website in enumerate(valid_websites):
        filter += 'site: ' + website
        if index == len(valid_websites) - 1:
            filter += ')'
        else:
            filter += ' OR '
    return filter


def create_query(): #Reads the arguments that are being passed
    query = sys.argv[1:]
    return ' '.join(query)


def create_url():
    if len(sys.argv[1:]) == 0:
        print('Error: Please enter valid URL')
    else:
        final_url = url + create_query() + create_filter()
        webbrowser.get(edge_path).open(final_url)


create_url()
