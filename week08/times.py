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
