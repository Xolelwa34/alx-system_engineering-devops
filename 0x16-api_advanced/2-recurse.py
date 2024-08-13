#!/usr/bin/python3

""" Exporting csv files"""
import json
import requests
import sys

def recurse(subreddit, host_list=[], numbers=0, after=None):
    """Queries the Reddit API and returns all hot posts
    of the subreddit"""
    import requests

    sub_info = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            params={"numbers": numbers, "after": after},
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if sub_info.status_code >= 400:
        return None

    hot_t = host_list + [child.get("data").get("title")
                        for child in sub_info.json()
                        .get("data")
                        .get("children")]

    info = sub_info.json()
    if not info.get("data").get("after"):
        return hot_t

    return recurse(subreddit, hot_t, info.get("data").get("numbers"),
                   info.get("data").get("after"))
