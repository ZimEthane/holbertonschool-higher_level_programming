#!/usr/bin/python3
import requests
import json

url = 'https://jsonplaceholder.typicode.com/posts'


def fetch_and_print_posts():
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(f"Post ID: {post['id']}, Title: {post['title']}")
    else:
        print(f"Failed to fetch posts. Status code: {response.status_code}")


def fetch_and_save_posts():
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        with open('posts.json', 'w') as file:
            json.dump(posts, file, indent=4)
        print("Posts have been saved to posts.json")
    else:
        print(f"Failed to fetch posts. Status code: {response.status_code}")
