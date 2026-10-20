#!/usr/bin/python3
"""Fetch posts from JSONPlaceholder, print their titles or save them to CSV."""
import csv

import requests

POSTS_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """Print the status code of the request, then the title of every post."""
    response = requests.get(POSTS_URL)
    print("Status Code: {}".format(response.status_code))
    if response.status_code == 200:
        for post in response.json():
            print(post["title"])


def fetch_and_save_posts():
    """Save the id, title and body of every post into posts.csv."""
    response = requests.get(POSTS_URL)
    if response.status_code != 200:
        return
    posts = [{"id": post["id"], "title": post["title"], "body": post["body"]}
             for post in response.json()]
    with open("posts.csv", "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["id", "title", "body"])
        writer.writeheader()
        writer.writerows(posts)
