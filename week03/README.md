# Week 3 Tute

### 1. Assume that we are in a shell where the following shell variable assignments have been performed,
### and [`ls`](https://manpages.debian.org/jump?q=ls.1) gives the following result:
```sh
$ x=2  y='Y Y'  z=ls
$ ls
    a       b       c
```
### What will be displayed as a result of the following [`echo`](https://manpages.debian.org/jump?q=echo.1) commands:
| Part | Command | Result |
|:---:|---|---|
| a | ```echo a   b   c``` | `a b c`
| b | ```echo "a   b   c"``` | `a   b   c`
| c | ```echo $y``` | `Y Y`
| d | ```echo x$x``` | `x2`
| e | ```echo $xx``` | ''
| f | ```echo ${x}x``` | `2x`
| g | ```echo "$y"``` | `Y Y`
| h | ```echo '$y'``` | `$y`
| i | ```echo $($y)``` | error: tries to run a program called Y (which doesn't exist)
| j | ```echo $($z)``` | `a b c`: runs `ls` which does exist
| k | ```echo $(echo a b c)``` | `a b c`

___
### 2. The following C program and its equivalent in Python3
### all aim to give precise information about their command-line arguments.
``` C
#include <stdio.h>

int main(int argc, char *argv[]) {
	printf("#args = %d\n", argc - 1);

	for (int i = 1; i < argc; i++) {
		printf("arg[%d] = \"%s\"\n", i, argv[i]);
	}

	return 0;
}
```
``` py
#!/usr/bin/env python3
from sys import argv

def main():
    print(f"#args = {len(argv) - 1}")
    for index, arg in enumerate(argv[1:], 1):
        print(f'arg[{index}] = "{arg}"')

if __name__ == '__main__':
    main()
```

### Assume that these programs are compiled in such a way that we may invoke them as ./args.
### Consider the following examples of how it operates:
```sh
$ ./args a b c
#args = 3
arg[1] = "a"
arg[2] = "b"
arg[3] = "c"
$ args "Hello there"
#args = 1
arg[1] = "Hello there"
```
### Assume that we are in a shell where the following shell variable assignments have been performed,
### and `ls` gives the following result:
```sh
$ x=2  y='Y Y'  z=ls
$ ls
    a       b       c
```
What will be the output of the following:
| Part | Command | Length | Args |
|:---:|---|:---:|---|
| a | ```./args x y   z``` | 3 | 'x' 'y' 'z'
| b | ```./args $(ls)``` | 3 | 'a' 'b' 'c'
| c | ```./args $y``` | 2 | 'Y' 'Y'
| d | ```./args "$y"``` | 1 | 'Y Y'
| e | ```./args $(echo "$y")``` | 2 | 'Y' 'Y'
| f | ```./args $x$x$x``` | 1 | '222'
| g | ```./args $x$y``` | 2 | '2Y' 'Y'
| h | ```./args $xy``` | 0 

___
### 3. Imagine that we have just typed a shell script into the file my_first_shell_script.sh in the current directory.
### We then attempt to execute the script and observe the following:
```sh
$ my_first_shell_script.sh
my_first_shell_script.sh: command not found
```
### Explain the possible causes for this, and describe how to rectify them.

- Current is not in `$PATH`
  - Add current directory to `$PATH` or run file as `./my_first_shell_script.sh`
- No execute permissions
  - Give yourself executable permissions by running `chmod u+x my_first_shell_script.sh`
- The shebang line is wrong
  - Make sure you have `#!/bin/sh` as your first line and that `/bin/sh` is an executable program
- Copied from Windows: Windows uses `'\r\n'` for newline but Unix uses `'\n'`
  - Run `dos2unix my_first_shell_script.sh` to get rid of the `'\r'` from the program

___
### 4. Implement a shell script called `seq.sh` for writing sequences of integers onto its standard output, with one integer per line. The script can take up to three arguments, and behaves as follows:

- ### `seq.sh` _LAST_ writes all numbers from 1 up to _LAST_, inclusive. For example:
``` sh
$ ./seq.sh 5
1
2
3
4
5
```

- ### `seq.sh` _FIRST_ _LAST_ writes all numbers from _FIRST_ up to _LAST_, inclusive. For example:
``` sh
./seq.sh 2 6
2
3
4
5
6
```

- ### `seq.sh` _FIRST_ _INCREMENT_ _LAST_ writes all numbers from _FIRST_ to _LAST_ in steps of _INCREMENT_, inclusive; that is, it writes the sequence _FIRST_, _FIRST_ + _INCREMENT_, _FIRST_ + 2*_INCREMENT_, ..., up to the largest integer in this sequence less than or equal to LAST. For example:
``` sh
./seq.sh 3 5 24
3
8
13
18
23
```


```sh
#!/bin/sh

FIRST=1
INCREMENT=1
LAST=1

# $# -> number of command line arguments

if test $# -eq 1
then
    LAST=$1
elif [ $# -eq 2 ]
then
    FIRST=$1
    LAST=$2
elif [ $# -eq 3 ]
then
    FIRST=$1
    INCREMENT=$2
    LAST=$3
else
    echo "Usage: $0 [FIRST [INCREMENT]] LAST"
    exit 1
fi

# making sure that $FIRST is actually an integer
# 2> /dev/null means that messages from stderr won't be printed out
if [ $FIRST -eq $FIRST ] 2> /dev/null
then
    # if $FIRST is an integer, do nothing
    :
else
    echo "FIRST is not an integer"
    exit 1
fi

curr="$FIRST"
while [ $curr -le $LAST ]
do
    echo "$curr"
    curr=$(( curr + INCREMENT ))
done
```


___
### 5. What is **JSON**?

### Where might I encounter it?

### Why can **JSON** be difficult to manipulate with tools such as **grep**?

### How can a tool like [`jq`](https://stedolan.github.io/jq/tutorial/) help?

JSON = JavaScript Object Notation

It is a way to store structured data

JSON is commonly used in web applications to transfer data between the backend and the frontend and vice versa

JSON data can often be spread across several lines, which makes tools such as `grep` hard to use

___
### 6. Write a shell script, `no_blinking.sh`, which removes all HTML files in the current directory which use the [blink element](https://en.wikipedia.org/wiki/Blink_element):
```sh
$ no_blinking.sh
Removing old.html because it uses the <blink> tag
Removing evil.html because it uses the <blink> tag
Removing bad.html because it uses the <blink> tag
```

```sh
#!/bin/sh

# *.html -> all the files which end with .html in the current directory

for file in *.html
do
    echo "Removing $file because it uses the <blink> tag"
    rm "$file"
done
```

___
### 7. Modify the `no_blinking.sh` shell script to instead take the HTML files to be checked as command line arguments and, instead of removing them, adding the suffix **.bad** to their name:
```sh
$ no_blinking.sh awful.html index.html terrible.html
Renaming awful.html to awful.html.bad because it uses the <blink> tag
Renaming terrible.html to terrible.html.bad because it uses the <blink> tag
```

```sh
#!/bin/sh

# $@ -> gives us all the command line arguments

for file in "$@"
do
    echo "Renaming $file to $file.bad because it uses the <blink> tag"
    mv "$file" "$file.bad"
done
```

___
### 9. The following shell script emulates the [`cat`](https://manpages.debian.org/jump?q=cat.1) command using the built-in shell commands [`read`](https://manpages.debian.org/jump?q=read.1) and [`echo`](https://manpages.debian.org/jump?q=echo.1):
``` sh
#!/bin/sh
while read line
do
    echo "$line"
done
```
#### a) What are the differences between the above script and the real [`cat`](https://manpages.debian.org/jump?q=cat.1) command?
- Missing options/arguments
- Will only read from stdin


#### b) modify the script so that it can concatenate multiple files from the command line, like the real [`cat`](https://manpages.debian.org/jump?q=cat.1)

### (Hint: the shell's control structures — for example, `if`, `while`, `for` — are commands in their own right, and can form a component of a pipeline.)

```sh
#!/bin/sh

# if no command line arguments, read from stdin
if [ $# -lt 1 ]
then
    while read line
    do
        echo "$line"
    done

# otherwise, read from file
else

# $@ -> use this to loop over all command line arguments
    for file in "$@"
    do
        # check if file exists and is readable
        if [ ! -r "$file" ]
        then
            echo "Can not read $file"
        else
            # read lines from the current file
            while read line
            do
                echo "$line"
            done < "$file"
        fi
    done
fi
```
