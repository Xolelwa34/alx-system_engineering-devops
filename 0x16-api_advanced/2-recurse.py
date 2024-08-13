#!/usr/bin/python3
""" Exporting csv files"""
import json
import requests
import sys


def recurse(subreddit, the_list=[], after="null"):
    """Read reddit API and return top 10 hotspots """
    username = 'X-User-Agent'
    password = 'RedditL'
    user_pass_dict = {'user': username, 'passwd': password, 'api_type': 'json'}
    headers = {'user-agent': 'X-User-Agent'}
    payload = {"limit": "100", "after": after}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    client = requests.session()
    client.headers = headers
    r = client.get(url, allow_redirects=False, params=payload)
    if r.status_code == 200:
        list_titles = r.json()['data']['children']
        after = r.json()['data']['after']
        if after is not None:
            the_list.append(list_titles[len(the_list)]['data']['title'])
            recurse(subreddit, the_list, after)
        else:
            return(the_list)
    else:
        return(None)
