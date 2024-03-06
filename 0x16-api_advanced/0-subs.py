#!/usr/bin/python3
"""
Function to query subscribers in a given reddit subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """ Return total number of subs in a given subreddit """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "linux/api.advance.0-sub/v1.0.0 (by sundaymba)"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404 or response.status_code == 302:
        return 0
    response = response.json()
    results = response.get("data")
    sub_count = results.get("subscribers")
    return sub_count
