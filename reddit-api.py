#!/usr/bin/env python3
import sys
import praw
import json
from praw.exceptions import ClientException
from dataclasses import dataclass, asdict


@dataclass
class Post:
    title: str
    author: str
    score: int


def get_posts(subreddit, count):
    """Extract $count latest posts and collect them in the list"""
    result = []
    try:
        for submission in subreddit.top(limit=count):
            post = Post(title=submission.title, author=submission.author.name, score=submission.score)
            result.append(asdict(post))
    except Exception as e:
        print(f"Unexpected error: {e}.", file=sys.stderr)

    return result


def main():
    """Connect with Reddit and print posts in JSON format"""
    try:
        reddit = praw.Reddit("default")
    except ClientException as e:
        print(f"Client error: {e}. Please check credentials or config", file=sys.stderr)
        return

    try:
        subreddit = reddit.subreddit("cosmos")
    except Exception as e:
        print(f"Wrong subreddit field: {e}", file=sys.stderr)
        return

    posts = get_posts(subreddit, 5)
    print(json.dumps(posts, indent=4, ensure_ascii=False))


if __name__ == "__main__":
   main()

