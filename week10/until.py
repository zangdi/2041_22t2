#!/usr/bin/env python3

from argparse import ArgumentParser
import re
import sys

def main():
    parser = ArgumentParser()
    parser.add_argument('address')
    args = parser.parse_args()

    # option 1: try to convert address to int, if it doesn't work, is string
    try:
        address = int(args.address)
    except ValueError:
        if args.address[0] == "/" and args.address[-1] == "/":
            address = args.address[1:-1]
        else:
            print("invalid address")
            sys.exit(1)

    # option 2: manually check if address is int before converting
    # if args.address.isdigit():
    #     address = int(args.address)
    # elif args.address[0] == "/" and args.address[-1] == "/":
    #     address = args.address[1:-1]
    # else:
    #     print("invalid address")
    #     sys.exit(1)

    for line_number, line_content in enumerate(sys.stdin, start=1):
        if line_content[-1] == "\n":
            line_content = line_content[:-1]

        if isinstance(address, int):
            if address == line_number:
                break
        else:
            if re.search(address, line_content):
                break

        print(line_content)

    print(line_content)


if __name__ == "__main__":
    main()
