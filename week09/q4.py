#!/usr/bin/env python3

from collections import Counter
import argparse
import requests
from bs4 import BeautifulSoup


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--frequency', action='store_true', help='print tags by frequency')
    parser.add_argument('url', help='url to fetch')
    args = parser.parse_args()

    url = args.url
    response = requests.get(url)
    webpage = response.text.lower()

    # need to install html5 lib using:
    # pip install html5lib
    soup = BeautifulSoup(webpage, 'html5lib')

    tags = soup.find_all()
    tag_names = [tag.name for tag in tags]

    tags_dict = Counter()
    for tag in tag_names:
        tags_dict[tag] += 1

    if args.frequency:
        for tag, counter in reversed(tags_dict.most_common()):
            print(f"{tag} {counter}")
    else:
        for tag, counter in sorted(tags_dict.items()):
            print(f"{tag} {counter}")



if __name__ == "__main__":
    main()
