#!/usr/bin/env python3

import sys

def main():
    for line in sys.stdin:
        words = line.split()
        # option 1: the reverse method sorts in place
        words.reverse()

        # option 2: the reversed function makes a new copy of the array which has the value reversed
        # words = reversed(words)
        
        # option 3: list splicing also works
        # words = words[::-1]

        print(" ".join(words))



if __name__ == "__main__":
    main()
