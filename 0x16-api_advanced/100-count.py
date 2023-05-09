#!/usr/bin/python3

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursive function that queries the Reddit API, parses the title of all hot
    articles, and prints a sorted count of given keywords (case-insensitive).

    subreddit: string representing the name of the subreddit to query.
    word_list: list of strings representing the keywords to count.
    after: string representing the Reddit "after" parameter for pagination.
    counts: dictionary that stores the counts of each keyword.

    Returns: None.
    """
    if counts is None:
        counts = {}
    if after is None:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    else:
        url = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit, after)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return
    data = response.json().get("data")
    if data is None:
        return
    children = data.get("children")
    if children is None or len(children) == 0:
        return
    for child in children:
        title = child.get("data", {}).get("title", "")
        title_words = [word.lower().rstrip("!.") for word in title.split()]
        for word in word_list:
            if word.lower() in title_words:
                if word.lower() not in counts:
                    counts[word.lower()] = 1
                else:
                    counts[word.lower()] += 1
    count_words(subreddit, word_list, data.get("after"), counts)
    if after is None:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for count in sorted_counts:
            print("{}: {}".format(count[0], count[1]))
