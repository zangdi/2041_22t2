#!/usr/bin/env python3

from collections import Counter
import sys

def main():
    frequencies = Counter()

    for line in sys.stdin:
        for char in line:
            if char.isalnum():
                frequencies[char] += 1

    for letter, frequency in sorted(frequencies.items()):
        print(f"'{letter}' occurred {frequency} times")


if __name__ == "__main__":
    main()
