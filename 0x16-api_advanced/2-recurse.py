#!/usr/bin/python3
"""Recursively get the titles of all hot articles for a given subreddit"""

import requests

def recurse(subreddit, hot_list=None, after=None):
    """Return a list containing the titles of all hot articles for a given subreddit"""

    if hot_list is None:
        hot_list = []
        
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100}
    
    if after:
        params['after'] = after
        
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json().get('data', {})
        children = data.get('children', [])
        after = data.get('after', None)
        
        for child in children:
            title = child.get('data', {}).get('title', '')
            hot_list.append(title)
        
        if after:
            recurse(subreddit, hot_list, after)
        
        return hot_list
    
    elif response.status_code == 404:
        return None
    
    else:
        raise Exception('Request failed with status code {}'.format(response.status_code))


