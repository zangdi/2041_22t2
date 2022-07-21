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
