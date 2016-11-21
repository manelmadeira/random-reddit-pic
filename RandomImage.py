import re
from random import randint
import requests
from Storage import Storage
import json


MAX_PAGES = 10
MAIN_URL = 'https://www.reddit.com/r/'
CATEGORIES = []


def get_random_category():
    rand = randint(0, len(CATEGORIES) - 1)
    return CATEGORIES[rand]


def get_json(category, next_page=None):
    params = ''
    if next_page is not None:
        params = '?after=' + next_page

    url = MAIN_URL + category + '/.json' + params
    print 'Getting info from: ' + url

    req = requests.get(url, headers={'User-agent': 'Random Pic Bot 0.1'})
    return req


def get_image(configs):
    storage = Storage(configs)

    category = None
    data = None

    for i in range(0, MAX_PAGES):
        # get initial request
        status_code = 0
        while status_code != 200:
            if category is None or status_code != 0:
                # select category
                category = get_random_category()

            next_page = None
            if data is not None:
                next_page = data['after']

            # do the request
            resp = get_json(category, next_page)

            # update status code
            status_code = resp.status_code

        data = resp.json()['data']
        for post in data['children']:
            info = post['data']

            if 'selftext' in info and len(info['selftext']) == 0:
                url = info['url']

                # check if url already used
                if not storage.url_already_exists(url, category):
                    # if not, add to DB
                    storage.save_new_url(url, category)
                    return url

    return ''


def parse_url(url):
    # if image from imgur, add .jpeg to url for image only
    is_imgur = re.findall(r'imgur\.com', url)
    needs_suffix = re.findall(r'\.jpg|\.gifv', url)

    if len(is_imgur) > 0 and len(needs_suffix) == 0:
        return url + '.jpeg'

    return url


def get_random_image(configs):
    global CATEGORIES
    CATEGORIES = configs.get_categories()

    url = get_image(configs)

    # replace amp by '&'
    url = url.split('amp;')
    url = '&'.join(url)

    # parse url
    url = parse_url(url)

    print url
    return url
