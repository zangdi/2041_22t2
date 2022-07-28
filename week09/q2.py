#!/usr/bin/env python3

import re, subprocess, sys
from collections import Counter


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <url>")
        sys.exit(1)

    url = sys.argv[1]
    process = subprocess.run(["wget", "-qO-", url], capture_output=True, text=True)
    webpage = process.stdout.lower()

    # <!--.*?-->
    webpage = re.sub(r"<!--.*?-->", "", webpage, flags=re.DOTALL)

    tags = re.findall(r"<\s*(\w+)", webpage)

    tags_dict = Counter()
    for tag in tags:
        tags_dict[tag] += 1

    for tag, counter in sorted(tags_dict.items()):
        print(f"{tag} {counter}")



if __name__ == "__main__":
    main()
