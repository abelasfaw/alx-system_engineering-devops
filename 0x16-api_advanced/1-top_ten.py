#!/usr/bin/python3
"""prints the titles of the first 10 hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):
    api = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': '0x16-api_advanced'}
    params = {'limit': 10}
    res = requests.get(api, headers=headers, allow_redirects=False,
                            params=params)
    if res.status_code == 200:
        res_data = res.json().get('data')
        for child in res_data.get('children'):
            print("{}".format(child.get('data').get('title')))
    else:
        print('None')
