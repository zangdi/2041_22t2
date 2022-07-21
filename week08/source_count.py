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
