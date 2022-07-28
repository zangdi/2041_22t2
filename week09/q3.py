#!/usr/bin/env python3

import re, subprocess
from collections import Counter
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--frequency', action='store_true', help='print tags by frequency')
    parser.add_argument('url', help='url to fetch')
    args = parser.parse_args()

    url = args.url
    process = subprocess.run(["wget", "-qO-", url], capture_output=True, text=True)
    webpage = process.stdout.lower()

    # <!--.*?-->
    webpage = re.sub(r"<!--.*?-->", "", webpage, flags=re.DOTALL)

    tags = re.findall(r"<\s*(\w+)", webpage)

    tags_dict = Counter()
    for tag in tags:
        tags_dict[tag] += 1

    if args.frequency:
        for tag, counter in reversed(tags_dict.most_common()):
            print(f"{tag} {counter}")
    else:
        for tag, counter in sorted(tags_dict.items()):
            print(f"{tag} {counter}")



if __name__ == "__main__":
    main()
