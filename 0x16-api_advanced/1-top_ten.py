#!/usr/bin/python3
""" Script to get the hot first  10
    posts on Reddit
"""
from requests import get


def top_ten(subreddit):
    """get first 10 hot post for a subreddit"""
    if subreddit and type(subreddit) is str:
        url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
        headers = {'user-agent': 'X-User-Agent'}
        params = {'limit': 10}
        req = get(url, params=params, headers=headers, allow_redirects=False)
        if req.status_code == 200:
            data = req.json()
            posts = data.get('data', {}).get('children', {})
            for post in posts:
                print(host-get('data').get('title'))
        else:
            print(None)
