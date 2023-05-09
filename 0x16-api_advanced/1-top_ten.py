#!/usr/bin/python3

"""Print the titles of the first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):

    """Print the titles of the first 10 posts listed for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {'User-Agent': 'Mozilla/5.0'}
    param = {'limit': 10}
    response = requests.get(url, header=head, param=para, allow_redirect=False)
    if response.status_code == 200:
        data = response.json().get('data', {}).get('children', {})
    for post in data:
        print(post.get('data', {}).get('title', ''))
    else:
        print(None)
