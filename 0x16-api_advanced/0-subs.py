#!/usr/bin/python3
"""Number of subscribers for a subreddit"""
import requests


def number_of_subscribers(subreddit):
    api = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': '0x16-api_advanced'}
    res = requests.get(api, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        res_data = res.json().get('data')
        return res_data.get('subscribers')
    return 0
