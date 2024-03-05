#!/usr/bin/python3
"""
Function to query subscribers in a given reddit subreddit
"""
import requests


def top_ten(subreddit):
    """ Return total number of subs in a given subreddit """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux/api.advance.0-sub/v1.0.0 (by sundaymba)"}
    params = {"limit": 10}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=params)
    if response.status_code == 200:
        response = response.json()
        children = response.get("data").get("children")
        for child in children:
            title = child.get("data").get("title")
            print(title)
    else:
        print("None")
