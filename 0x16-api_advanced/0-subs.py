#!/usr/bin/python3
"""
queries the Reddit API and returns the number
of subscribers (not active users.
"""
import requests


def number_of_subscribers(subreddit):
    """returns number of total subscribers"""
    url = ("https://api.reddit.com/r/{}/about".format(subreddit))
    headers = {'User-Agent': 'X-User-Agent'}
    host = requests.get(url, headers=headers, allow_redirects=False)

    if host.status_code != 200:
        return (0)
    host = host.json()
    if 'data' in host:
        return (host.get('data').get('subscribers'))

    else:
        return (0)
