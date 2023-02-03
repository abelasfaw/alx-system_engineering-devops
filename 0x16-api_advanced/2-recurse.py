#!/usr/bin/python3
"""returns a list containing the titles of all hot articles for
a given subreddit recursively"""
import requests
after = None


def recurse(subreddit, hot_list=[]):
    global after
    headers = {'User-Agent': '0x16. API advanced'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=parameters)
    if response.status_code == 200:
        next_article = response.json().get('data').get('after')
        if next_article is not None:
            after = next_article
            recurse(subreddit, hot_list)
        list_titles = response.json().get('data').get('children')
        for title_ in list_titles:
            hot_list.append(title_.get('data').get('title'))
        return hot_list
    else:
        return (None)
