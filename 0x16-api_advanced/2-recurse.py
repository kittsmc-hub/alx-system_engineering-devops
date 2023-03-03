#!/usr/bin/python3
"""Recursively get the titles of all hot articles for a given subreddit"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return a list of all hot articles for a given subreddit"""


url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

header = {'User-Agent': 'Mozilla/5.0'}
param = {'after': after} if after else {}
response = requests.get(url, header=header, param=param, allow_redirects=False)
if response.status_code == 200:
    data = response.json().get('data', {})
posts = data.get('children', {})
after = data.get('after', None)
for post in posts:
    hot_list.append(post.get('data', {}).get('title', ''))
if after:
    return recurse(subreddit, hot_list, after)
else:
    return hot_list
else:
    return None
