#!/usr/bin/python3
"""Recursively get the titles of all hot articles and prints a sorted count of given words"""


import requests


def count_words(subreddit, word_list, count_dict=None, after=None):
    if count_dict is None:
        count_dict = {}

    if subreddit is None:
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code != 200:
        return

    data = response.json().get("data")
    after = data.get("after")
    children = data.get("children")

    for child in children:
        title = child.get("data").get("title").lower()
        for word in word_list:
            if word.lower() in title:
                if word.lower() in count_dict:
                    count_dict[word.lower()] += 1
                else:
                    count_dict[word.lower()] = 1

    if after is not None:
        count_words(subreddit, word_list, count_dict, after)
    else:
        sorted_list = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_list:
            print(f"{word}: {count}")

