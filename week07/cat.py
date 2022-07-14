#! /usr/bin/env python3

import sys


number = False
verbose = False


# deals with several command line arguments
while len(sys.argv) > 1 and sys.argv[1].startswith('-'):
    arg = sys.argv.pop(1)
    arg = arg[1:]
    if arg == 'n':
        number = True
    elif arg == 'v':
        verbose = True


# add "-" as a filename to represent reading from stdin
if len(sys.argv) == 1:
    sys.argv.append("-")

counter = 1
for filename in sys.argv[1:]:
    try:
        # read from stdin if filename is "-"
        if filename == "-":
            stream = sys.stdin

        # otherwise, open file for reading
        else:
            stream = open(filename)

        for line in stream:
            if verbose:
                # build up new line character by character
                new_line = ""
                for char in line:
                    if char == '\n':
                        new_line += '$\n'

                    # ord: character -> ascii code
                    # chr: ascii code -> character
                    elif ord(char) < 32:
                        new_line += '^' + chr(ord(char) + ord('A') - 1)
                    else:
                        new_line += char

                line = new_line

            if number:
                # {var:num} lets variable 'var' take up 'num' fields
                print(f'{counter:6}  {line}', end='')
            else:
                sys.stdout.write(line)

            counter += 1

        # make sure we don't close stdin
        if stream != sys.stdin:
            stream.close()

    except IOError as e:
        print(f"{sys.argv[0]}: can not open: {e.filename}: {e.strerror}")
