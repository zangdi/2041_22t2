# Week 8 Tute

### 1. What types are avalible as inbuilt types in Python?

- `int()` -> integers
- `float()` -> floating point number (decimals)
- `str()` -> string
- `list()` -> an array of things
  - `[]` -> empty list
  - `[1, 2, 3]` -> list containing elements 1, 2 and 3
- `dict()` -> key value pairs
  - `{}` -> empty dict
  - `{'key1': 'value1', 'key2': 'value2'}` -> dict containing the pairs (key1 -> key2) and (key2 -> value2)
- `tuple()` -> immutable list, i.e. you can't change it
  - `tuple()` -> empty tuple, but `()` does not
  - `('hello', 'world')` -> tuple containing 'hello' and 'world
  - `(1,)` -> add a comma after for just a single element
- `set()` -> unordered collection of unique elements
  - `set()` -> empty set, but `{}` does not work (will be empty dict)
  - `{'hello', 'world'}` -> set continaing 'hello' and 'world'
  - `{1,}` -> add a comma after for just a single element
- `frozenset` -> immutable set


____
### 2. What other useful types are available with Python's standard library?

Look at the [collections module](https://docs.python.org/3.9/library/collections.html#module-collections) for other interesting data types

___
### 3. Write a Python function `print_dict()` that displays the contents of a dict in the format below:
```
[key] => value
[Andrew] => green
[Anne] => red
[John] => blue
```

```py
def print_dict(d):
    # iterating over d only gives us keys
    for key, value in d.items():
        print(f"[{key}] => {value}")
```

___
### 4. Write a Python program, `times.py` which prints a table of multiplications.
### Your program will be given the dimension of the table and the width of the columns to be printed. For example:
```sh
$ ./times.py 5 5 5
    1     2     3     4     5
    2     4     6     8    10
    3     6     9    12    15
    4     8    12    16    20
    5    10    15    20    25
```

```sh
$ ./times.py 10 10 3
  1   2   3   4   5   6   7   8   9  10
  2   4   6   8  10  12  14  16  18  20
  3   6   9  12  15  18  21  24  27  30
  4   8  12  16  20  24  28  32  36  40
  5  10  15  20  25  30  35  40  45  50
  6  12  18  24  30  36  42  48  54  60
  7  14  21  28  35  42  49  56  63  70
  8  16  24  32  40  48  56  64  72  80
  9  18  27  36  45  54  63  72  81  90
 10  20  30  40  50  60  70  80  90 100
```

```py
#!/usr/bin/env python3
import sys


def main():
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <n> <m> <column-width>")
        sys.exit(1)

    n = int(sys.argv[1])
    m = int(sys.argv[2])
    width = int(sys.argv[3])

# range(n) gives us [0, 1, ..., n - 1]
# range(1, n) gives us [1, 2, ..., n - 1]
# range(1, n + 1) gives us [1, 2, ..., n]
    for x in range(1, n + 1):
        for y in range(1, m + 1):
            print(f" {x * y: >{width}}", end="")
        print()


if __name__ == "__main__":
    main()
```


___
### 5. Write a Python program `missing_words.py` which given two files as arguments prints, in sorted order, all the words found in file1 but not file2.

### You can assume words occur one per line in each file.

```py
#!/usr/bin/env python3
import sys


def create_words_set(filename):
    # use set rather than dict because we don't have a value to store, just a key
    words = set()

    with open(filename) as file1:
        for word in file1:
            word = word.strip()
            words.add(word)
    
    return words


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <file1> <file2>")
        sys.exit(1)

    words1 = create_words_set(sys.argv[1])
    words2 = create_words_set(sys.argv[2])

    # option 1: checks if word that is in words1 is not in words2
    words_list = []
    for word in words1:
        if word not in words2:
            words_list.append(word)

    # option2: this is same as option1, but using list comprehension
    words_list = [word for word in words1 if word not in words2]

    # option3: using set subtraction
    words_list = []
    for word in words1 - words2:
        words_list.append(word)

    # option4: this is same as option3, but using list comprehension
    words_list = [word for word in words1 - words2]

    # sorted: returns a sorted version of a list
    # .sort: sorts a list in place
    for word in sorted(words_list):
        print(word)


if __name__ == "__main__":
    main()
```


____
### 6. Write a Python program `source_count.py` which prints the number of lines of C source code in the current directory. In other words, this Python program should behave similarly to `wc -l *.[ch]`. (Note: you are not allowed to use `wc` or other Unix programs from within the Python script). For example:
```sh
$ ./source_count.py
    383 cyclorana.c
    280 cyclorana.h
     15 enum.c
    194 frequency.c
    624 model.c
    293 parse.c
    115 random.c
     51 smooth.c
    132 util.c
     16 util.h
    410 waveform.c
   2513 total
```

```py
#!/usr/bin/env python3
from glob import glob


def main():
    total = 0
    for filename in glob("*.[ch]"):
        with open(filename) as file:
            lines = file.readlines()
            lines_count = len(lines)
            print(f"{lines_count: >7} {filename}")
            total += lines_count
    
    print(f"{total: 7} total")


if __name__ == "__main__":
    main()
```


___
### 7. Write a Python program, `phone_numbers.py` which given the URL of a web page fetches it by running `wget` and prints any strings that might be phone numbers in the web page.
### Assume the digits of phone numbers may be separated by zero or more spaces or hyphens ('-') and can contain between 8 and 15 digits inclusive.
### You should print the phone numbers one per line with spaces & hyphens removed.
```sh
$ ./phone_numbers.py https://www.unsw.edu.au
20151028
11187777
841430912571345
413200225
61293851000
57195873179
```

```py
#!/usr/bin/env python3
import subprocess
import sys
import re


def main():
    # shell -> runs the process in shell
    # capture_output -> lets us use stdout and stderr
    # text -> puts output in text format (default is binary)
    process = subprocess.run(f"wget -qO- {sys.argv[1]}", shell=True, capture_output=True, text=True)
    webpage = process.stdout

    for number in re.findall(r'[\d \-]+', webpage):
        number = re.sub(r'\D', '', number)
        if len(number) >= 8 and len(number) <= 15:
            print(number)


if __name__ == "__main__":
    main()
```
