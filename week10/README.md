# Week 10

### 2. Write a Python program, `until.py` which takes as an argument either a line number (e.g. 3) or a regular expression (e.g. `/.[13579]/`) and prints all lines given to it by standard input until the given line number, or the first line matching the regular expression. For example:
``` sh
$ seq 1 5 | ./until.py 3
1
2
3
$ seq 1 20 | ./until.py /.3/
1
2
3
4
5
6
7
8
9
10
11
12
13
```

```py
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
```


___
### 3. Write a Python program that maps all lower-case vowels (a,e,i,o,u) in its standard input into their upper-case equivalents and, at the same time, maps all upper-case vowels (A, E, I, O, U) into their lower-case equivalents.
### The following shows an example input/output pair for this program:
| Sample Input Data | Corresponding Output |
|---|---|
| This is some boring text | ThIs Is sOmE bOrIng tExt. |
| A little foolish perhaps? | a lIttlE fOOlIsh pErhAps? |

```py
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
```


___
### 4. These commands both copy a directory tree to a CSE server.
```sh
$ scp -r directory1/ z1234567@login.cse.unsw.edu.au:directory2/
$ rsync -a directory1/ z1234567@login.cse.unsw.edu.au:directory2/
```
### What underlies them?

### How do they differ?

### Why are these differences important?

- Both run on ssh
- `rsync` is more efficient than `scp` as it only copies files that don't exist or are changed and for files which have small changes, it only copies over the differences
- `rsync -a` copies over file metadata such as permissions and last modified
- `scp -rp` would also copy over file metadata


___
### 5. Assume the Linux kernel source tree containing thousand of source files can be found in `/usr/src/linux`
### Write a shell script that emails each of the 50,000 source (.c) files to Andrew, each as an attachment to a separate email.

### The source files may be anywhere in a directory tree than goes 10+ levels deep.

### Please don't run this script, and in general be very careful with such scripts. It is very embarassing to accidentally send thousands of emails.

### What assumptions does your script make?

```sh
#!/bin/sh

directory="/usr/src/linux"

for file in $(find "$directory" -type f -name '*.c')
do
    echo mutt -s "Linux source" -a "$file" -- andrewt@unsw.edu.au
done
```


___
### 6. The Perl programming language a handful of useful functions.
### Write a Python module `perl.py` that that contains the following functions:

### `chomp` - The Perl function `chomp` removes a single newline from the end of a string (if there is one).

### `qw` - The Perl function `qw` splits a string into a list of words.

### `die` - The Perl function `die` prints an error message and exits the program.

```py
import sys

def chomp(string):
    if string[-1] == "\n":
        return string[:-1]
    else:
        return string

def qw(string):
    return string.split()

def die(message):
    sys.stderr(f"{sys.argv[0]}: Error: {message}\n")
    print(sys.argv[0], "Error", message, sep=": ", file=sys.stderr)
    sys.exit(1)
```


___
# Revision questions
### The following questions are primarily intended for revision, either this week or later in session.
### Your tutor may still choose to cover some of these questions, time permitting.

### 1. Write a shell script called `rmall.sh` that removes all of the files and directories below the directory supplied as its single command-line argument. The script should prompt the user with `Delete` __X__? before it starts deleting the contents of any directory __X__. If the user responds yes to the prompt, `rmall` should remove all of the plain files in the directory, and then check whether the contents of the subdirectories should be removed. The script should also check the validity of its command-line arguments.

```sh
#!/bin/sh

if [ $# -ne 1 ]
then
    echo "Usage: $0 dir"
    exit 1
fi

if [ ! -d $1 ]
then
    echo "$1 is not a directory"
    echo "Usage: $0 dir"
    exit 1
fi

echo -n "Delete $1? "
read answer

if [ $answer != "yes" ]
then
    exit 0
fi

cd $1
pwd

for file in .* *
do
    if [ -f "$file" ]
    then
        rm "$file"
    fi
done

for dir in .* *
do
    if [ -d "$dir" -a "$dir" != "." -a "$dir" != ".." ]
    then
        rmall "$dir"
    fi
done
```

___
### 2. Write a shell script called check that looks for duplicated student ids in a file of marks for a particular subject. The file consists of lines in the following format:
```
2233445 David Smith 80
2155443 Peter Smith 73
2244668 Anne Smith 98
2198765 Linda Smith 65
```

### The output should be a list of student ids that occur 2+ times, separated by newlines. (i.e. any student id that occurs more than once should be displayed on a line by itself on the standard output).

```sh
#!/bin/sh

# extract the first column to get just the student ids
cut -d" " -f1 < student.txt |
# sort the values so that uniq can work correctly
sort |
# print out lines which are duplicated
uniq -d
```

___
### 3. Write a Python script `revline.py` that reverses the fields on each line of its standard input.
### Assume that the fields are separated by spaces, and that only one space is required between fields in the output.

### For example
```
# ./revline.py
hi how are you
i'm great thank you
Ctrl-D
you are how hi
you thank great i'm
```

```py
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
```


___
### 4. Which one of the following regular expressions would match a non-empty string consisting only of the letters `x`, `y` and `z`, in any order?
### a. `[xyz]+`

### b. `x+y+z+`

### c. `(xyz)*`

### d. `x*y*z*`

- Option b means requires the string to contain at least one x, y and z in that order
- Option c also includes the empty string
- Option d means that x, y and z has to be in that order
- Option a is correct

___
### 5. Which one of the following commands would extract the student id field from a file in the following format:
```
COMP3311;2122987;David Smith;95
COMP3231;2233445;John Smith;51
COMP3311;2233445;John Smith;76
```
### a. `cut -f 2`

### b. `cut -d; -f 2`

### c. `sed -e 's/.*;//'`

### d. None of the above.

- Option a gives us the entire file as cut expects the deliminator to be `\t`
- Option b also fails because the semicolon turns the linen into 2 commands, `cut -d` followed by `-f 2`
- Option c removes everything until the last semicolon, giving us the last field
- Option d is correct

The correct command would be `cut -d';' -f2`

___
### 6. Write a Python program `frequencies.py` that prints a count of how often each letter ('a'..'z' and 'A'..'Z') and digit ('0'..'9') occurs in its input. Your program should follow the output format indicated in the examples below exactly.
### No count should be printed for letters or digits which do not occur in the input.

### The counts should be printed in dictionary order ('0'..'9','A'..'Z','a'..'z').

### Characters other than letters and digits should be ignored.

### The following shows an example input/output pair for this program:
``` sh
$ ./frequencies.py
The  Mississippi is
1800 miles long!
Ctrl-D
'0' occurred 2 times
'1' occurred 1 times
'8' occurred 1 times
'M' occurred 1 times
'T' occurred 1 times
'e' occurred 2 times
'g' occurred 1 times
'h' occurred 1 times
'i' occurred 6 times
'l' occurred 2 times
'm' occurred 1 times
'n' occurred 1 times
'o' occurred 1 times
'p' occurred 2 times
's' occurred 6 times
```

```py
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
```


___
### 8. A list `a1, a2, ... an` is said to be **converging** if
```
a1 > a2 > ... > an
```
### and
```
for all i, a(i - 1) - ai > ai - a(i + 1)
```

### In other words, the list is strictly decreasing and the difference between consecuctive list elements always decreases as you go down the list.

### Write a Python program `converging.py` that determines whether a sequence of positive integers read from standard input is converging. The program should write "converging" if the input is converging and write "not converging" otherwise. It should produce no other output.
| Sample Input Data | Corresponding Output |
|---|---|
| 2010 6 4 3 | converging |
| 20   15   9 | not converging |
| 1000     100   10     1 | converging |
| 6  5 2 2 | not converging |
|   1 2 4 8 | not converging |

### Your program's input will only contain digits and white space. Any amount of whitespace may precede or follow integers.

### Multiple integers may occur on the same line.

### A line may contain no integers.

### You can assume your input contains at least 2 integers.

### You can assume all the integers are positive.

```py
#!/usr/bin/env python3

import re
import sys

def main():
    lines = sys.stdin.readlines()
    content = " ".join(lines).strip()

    # re.findall will give us strings, we want ints for comparisons to work correctly
    nums = [int(x) for x in re.findall(r'\d+', content)]

    for i in range(len(nums) - 1):
        if nums[i] <= nums[i + 1]:
            print("not converging")
            sys.exit(0)

    for i in range(len(nums) - 2):
        if nums[i] - nums[i + 1] <= nums[i + 1] - nums[i + 2]:
            print("not converging")
            sys.exit(0)

    print("converging")


if __name__ == "__main__":
    main()
```
