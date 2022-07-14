# Week 7 Tute

### 1. In shell we have been using the following hashbang:
``` sh
#!/bin/dash
```
### How should we modify this hashbang to use it with python?

The hashband line for python is
``` py
#!/usr/bin/env python3
```

This uses the [`env`](https://manpages.debian.org/jump?q=env.1) utility to look for the PATH of the python3 interpreter

This means that we don't need to know where the python3 interpreter is

Some of the places it might be are
```sh
/bin/python3
/usr/bin/python3
```

Additionally, [`env`](https://manpages.debian.org/jump?q=env.1) is needed when using a virtual environment which we will look at in later weeks

___
### 2. What version of python should be used in this course?
### What are the differences between different versions of python?

We are using python3.9 in this course

If you are writing code, be sure to use features from python3.9 or lower; python3.10 features in your code will break autotesting and automarking


python2 and python3 are different languages

python2 has a lot of subtle differences to python3 and is also unsupported, so you should generally not use it


On CSE systems, `python` refers to `python2` so make sure you specify `python3` if you are trying to run python


___
### 3. Where can I find the [_python3_](https://manpages.debian.org/jump?q=python3.1) documentation?

```sh
man python3
```

Shows the command line arguments for python3

Python has inbuilt documentation which you can use via the `help` function when running python interactively

The fudocs.python.orgll documentation is available online at [docs.python.org](docs.python.org)

Make sure you select the correct version of python when using the online documentation (python3.9)


___
### 4. What is a REPL?
### How do you start the python REPL?

REPL stands for _read-eval-print-loop_

What that means is the terminal reads the command line, evaluates the command, prints out the stdout and stderr and then repeats the process

Shell and interactive python are examples of REPL

To run python REPL, run
```
$ python3
>>> 
```

This is useful for running code line by line, e.g. calculations or testing some code before you write your script


___
### 5. Write a simple version of the 'head' command in Python, that accepts an optional command line argument in the form '-n', where 'n' is a number, and displays the first 'n' lines from its standard input.
### If the '-n' option is not used, then the program simply displays the first ten lines from its standard input.
``` sh
# display first ten lines of file2
$ ./head.py < file2
# same as previous command
$ ./head.py -10 < file2
# display first five lines of file2
$ ./head.py -5 < file2
```

Look at [question 6](#6-modify-the-head-program-from-the-previous-question-so-that-as-well-as-handling-an-optional--n-argument-to-specify-how-many-lines-it-also-handles-multiple-files-on-the-command-line-and-displays-the-first-n-lines-from-each-file-separating-them-by-a-line-of-the-form--filename)

___
### 6. Modify the head program from the previous question so that, as well as handling an optional `-n` argument to specify how many lines, it also handles multiple files on the command line and displays the first `n` lines from each file, separating them by a line of the form `==> FileName <===`.
``` sh
# display first ten lines of file1, file2, and file3
$ ./head.py file1 file2 file3
# display first three lines of file1, and file2
$ ./head.py -3 file1 file2
```


```py
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
```


___
### 7.  The following is a Python version of the cat program.
``` py
#! /usr/bin/env python3

import sys

if len(sys.argv) == 1:
    sys.argv.append("-")

for filename in sys.argv[1:]:
    try:
        if filename == "-":
            stream = sys.stdin
        else:
            stream = open(filename)

        for line in stream:
            sys.stdout.write(line)

        if stream != sys.stdin:
            stream.close()

    except IOError as e:
        print(f"{sys.argv[0]}: can not open: {e.filename}: {e.strerror}")
```

### Write a new version of `cat` so that it accepts a `-n` command line argument and then prints a line number at the start of each line in a field of width 6, followed by two spaces, followed by the text of the line.
### The numbers should constantly increase over all of the input files (i.e. don't start renumbering at the start of each file).
``` sh
$ ./cat.py -n myFile
     1  This is the first line of my file
     2  This is the second line of my file
     3  This is the third line of my file
         ...
  1000  This is the thousandth line of my file
```

Look at [question 8](#8-modify-the-cat-program-from-the-previous-question-so-that-it-also-accepts-a--v-command-line-option-to-display-all-characters-in-the-file-in-printable-form)

___
### 8. Modify the `cat` program from the previous question so that it also accepts a `-v` command line option to display all characters in the file in printable form.
### In particular, end of lines should be shown by a `$` symbol (useful for finding trailing whitespace in lines) and all control characters (ascii code less than 32) should be shown as `^X` (where `X` is the printable character obtained by adding the code for `'A'` to the control character code). So, for example, tabs (ascii code 9) should display as `^I`.
``` sh
$ ./cat -v myFile
This file contains a tabbed list:$
^I- point 1$
^I- point 2$
^I- point 3$
And this line has trailing spaces   $
which would otherwise be invisible.$
```

```py
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
```

___
### 9. In Python, you can imitate a main function by using the `if __name__ == '__main__':` construct.
### How does this work?
### Why is this useful?

Python is a scripting language that executes top down

This means that when modules are imported, everything will be run, so using the `if __name__ == '__main__':` construct means that your code will only execute when your script is executed not when it is imported as a module


The variable `__name__` is set to the name of the current module and if we are not in a module, it is set to `__main__`


Typical usage looks like this:

```py
def main():
    ...


# other functions
...


if __name__ == '__main__':
    main()
```


___
### 10. How can we use regular expressions in python?

The `re` module lets us use regular expressions in python

You can import it as a library like this
``` py
import re

re.search(pattern, string, flags)
```

You can also import specific functions from it like this
```py
from re import search, match, fullmatch

search(pattern, string, falgs)
```


___
### 11. What is the difference between `search`, `match`, and `fullmatch`?

`search` is most similar to [_grep_](https://manpages.debian.org/jump?q=grep.1)

`search` finds a pattern anywhere in the string

`match` finds a pattern at the beginning of the string

So `re.match('hello')` is equivalent to `re.search('^hello')`

`fullmatch` finds the pattern in the entire string

So `re.fullmatch('hello')` is equivalent to `re.search('^hello$)`


___
### 12. How are Python's regular expressions different from [_grep_](https://manpages.debian.org/jump?q=grep.1)?

- grep: prints out entire line where match was found
- python: return match object

- grep: finds all non-overlapping matches
- python: only gives the first match

- grep: deals with files line by line
- python: deals with strings

___
### Note:
When using regex in python, it is often a good idea to use the raw string format
```py
r'...'
```

This is because in normal python strings, the backslash character `'\'` acts as an escape character (i.e. write `'\n'` for the newline character)

However, when you use a raw string, the backslash character does not escape any more so `'\n'` in a string will mean the two characters literally rather than the newline character
