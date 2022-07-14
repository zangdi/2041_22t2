#!/usr/bin/env python3


import sys


def read_from_file(stream, max_lines):
    n = 1
    for line in stream:
        if n > max_lines:
            break

        # print -> adds a newline character at the end of your line

        # option 1: treating stdout as a file
        # sys.stdout.write(line)

        # option 2: print without adding newline character at the end
        print(line, end='')

        n += 1



n_lines = 10

# check if there is a command line argument
if len(sys.argv) > 1 and sys.argv[1].startswith('-'):
    # remove and return index 1 of the sys.argv list
    arg = sys.argv.pop(1)
    # remove the '-' in the command line argument
    arg = arg[1:]
    # convert the command line argument from a string to an int
    n_lines = int(arg)


if len(sys.argv) == 1:
    read_from_file(sys.stdin, n_lines)
else:
    for filename in sys.argv[1:]:
        # open file can fail with an exception, so try and except can catch the error
        try:
            print(f"==> {filename} <==")

            stream = open(filename)
            read_from_file(stream, n_lines)
            stream.close()

        # if there is an exception from trying to open the file, it will execute the code below
        except IOError as e:
            print(f"{sys.argv[0]}: can not open: {e.filename}: {e.strerror}")
