# Week 9 Tute


### 2. Write a Python program, `tags.py` which given the URL of a web page fetches it by running [__wget__](https://manpages.debian.org/jump?q=wget.1) and prints the HTML tags it uses.
### The tag should be converted to lower case and printed in alphabetical order with a count of how often each is used.
### Don't count closing tags.
### Make sure you don't print tags within HTML comments.
```
$ ./tags.py https://www.cse.unsw.edu.au
a 141
body 1
br 14
div 161
em 3
footer 1
form 1
h2 2
h4 3
h5 3
head 1
header 1
hr 3
html 1
img 12
input 5
li 99
link 3
meta 4
noscript 1
p 18
script 14
small 3
span 3
strong 4
title 1
ul 25
```
### Note the counts in the above example will not be current - the CSE pages change almost daily.

```py
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
```


___
### 3, Add an `-f` option to `tags.py` which indicates the tags are to be printed in order of frequency.
```
$ ./tags.py -f https://www.cse.unsw.edu.au
head 1
noscript 1
html 1
form 1
title 1
footer 1
header 1
body 1
h2 2
hr 3
h4 3
span 3
link 3
small 3
h5 3
em 3
meta 4
strong 4
input 5
img 12
br 14
script 14
p 18
ul 25
li 99
a 141
div 161
```

```py
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
```


___
### 4. Modify tags.py to use the `requests` and `beautifulsoup4` modules.
```py
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
```
