#!/usr/bin/env python3


import sys

VOWELS = "aeiou"

def main():
    # make a translation table
    table = str.maketrans(VOWELS.upper() + VOWELS.lower(), VOWELS.lower() + VOWELS.upper())
    for line in sys.stdin:
        print(line.translate(table), end="")


if __name__ == "__main__":
    main()
