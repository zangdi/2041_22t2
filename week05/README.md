# Week 5 Tute

## Assignment

The [assignment](https://cgi.cse.unsw.edu.au/~cs2041/22T2/assignments/ass1/index.html) is to implement a small subset of [git](https://en.wikipedia.org/wiki/Git) in shell.

___
### 1. The assignment specification doesn't fully explain the assignment - what can I do?
- Understand what git does
- Check the lecture notes and look up online tutorials on how to use git if you're not sure what a command does
- Check the reference implementation
  - `2041 tigger-*` (* is whichever command you're testing)
  - Thinking about edge cases, e.g.
    - `tigger-add` without `tigger-init`


___
### 2. How hard are the subsets?
- Subset 0 is not very hard if you understand what you need to do
- Subset 1 will be harder than subset 0
- Subset 2 is really hard

___
### 3. What does **git init** do?
### How does this differ from **tigger-init**?
- `git init`
  - Creates the `.git` subdirectory
  - Creates files and subdirectories within `.git`

- `tigger-init`
  - Just needs to create the `.tigger` subdirectory
  - Can create files and subdirectories within `.tigger` depending on how you want to structure your `.tigger` directory

___
### 4. What do **git add** file and **tigger-add** file do?
Both add a copy of the file to the repository's index

For `tigger-add`, a copy of the file should be stored somewhere in the `.tigger` directory, but exactly how you store it is up to you


___
### 5. What is the index in **tigger** (and **git**), and where does it get stored?
The index (or staging area) is where files which are added to the repository are stored

You can decide how you want to store the index of your `.tigger` directory but one option is to create a `.tigger/index/` directory and store the files in there


___
### 6. What is a commit in **tigger** (and **git**), and where does it get stored?
A commit takes a snapshot of the index at a particular point in time.

You can decide how you want to store the commits in your `.tigger` directory but one option is to create a `.tigger/commit-number/` directory for each commit and store the files in there


___
### 7. Apart from the __tigger-*__ scripts what else do you need to submit (and give an example)?
- 10 test scripts
  - You must compare your output to correct output, examples of how you could do that include
    - Run 2041 tigger and copy the output as a string
    - Run 2041 tigger in your script
  - Your code does not need to pass your tests
  - Make sure to leave comments about what your script is testing and why
- Any helper files you write for your tests or for `tigger-*` scripts

Test script example:
```sh
#!/bin/sh

# mktemp creates a temporary file
expected_output="$(mktemp)"
actual_output="$(mktemp)"

# EOF acts like multi-line quotes
cat > "$expected_output" <<EOF
Initialized empty tigger repository in .tigger
EOF

# put stdout and stderr of command into expected output file
tigger-init > "$actual_output" 2>&1

# check if expected output and actual output are the same
if ! diff "$expected_output" "$actual_output"
then
    echo "failed test"
    exit 1
fi
```

___
## General assignment tips
You don't need to follow these but they could be useful.
- Think about how want to structure your repository before you start coding
  - What files and subdirectories do you want in your `.tigger` directory?
  - How will you store each commit?
  - etc.
- When you are doing later subsets, you may need to redesign the structure for your repository
  - This is completely fine! You don't need plan for this when you start subset 0
- Be aware of the programs you are allowed to use, there is a section called Permitted Languages) near the bottom of the page which contains all the details
  - Not all of the programs listed in there are useful for the assignment, in fact most of them aren't
  - If there is any program that you want to use but isn't in the list, ask for it on the forum
- Take a look at the Assumptions/Clarifications section, it might make your code simpler (e.g. restrictions about what the commit names, filenames and branch names can be)
- Keep an eye out on the Change Log at the bottom of the assignment page, that will let you know if any part of the spec has changed

___
### 8. You work on the assignment for a couple of hour tonight.
### What do you need to do when you are finished?

Make sure you submit your code using `give`

You must submit intermediate versions of your code

Submitting also creates backups of your code, which you can access using [the autotest and submission page](https://cgi.cse.unsw.edu.au/~cs2041/22T2/assignments/ass1/index.html)

___
## Case statement
Case statements in shell are an efficient way to handle conditions which depend on the value of a single variable

They also allow for globbing in each case

e.g.
```sh
case "$animal" in
    cat)
        echo "this is a cat"
        ;;
    dog)
        echo "this is a dog"
        ;;
    *t)
        echo "this animal name ends with t"
        ;;
    *)
        echo "i don't recognise this animal"
        ;;
esac
```

___
### 9. Write a shell script _extract.sh_ that, when given one or more archive files as command line arguments, will use the correct program to extract the files.

```sh
#!/bin/sh

for archive in "$@"
do
    if [ ! -f "$archive" ]
    then
        echo "$0: error: '$archive' is not a file" >&2
        continue
    fi

    case "$archive" in
        *.zip)
            unzip "$archive"
            ;;
        *.tar)
            tar xf "$archive"
            ;;
        *)
            echo "$0: error: '$archive' cannot be extracted" >&2
            ;;
    esac
done
```

___
### 10. Given an anonymous list of CSE logins.
### Write a shell script _last.sh_ that, using shell `case` statments, finds the number of logins that occurred from within UNSW.
### (Look for connections to from the uniwide network)
### Additionally, find the distribution of zIDs by their first digit.
```sh
#!/bin/sh

count=0
z0=0
z1=0
z2=0
z3=0
z4=0
z5=0
z6=0
z7=0
z8=0
z9=0
class=0

while read zid tty address other
do
    case "$address" in
        *uniwide*)
            count=$(( count + 1 ))
            ;;
    esac

    case "$zid" in
        z0*)    z0=$(( z0 + 1 )) ;;
        z1*)    z1=$(( z1 + 1 )) ;;
        z2*)    z2=$(( z2 + 1 )) ;;
        z3*)    z3=$(( z3 + 1 )) ;;
        z4*)    z4=$(( z4 + 1 )) ;;
        z5*)    z5=$(( z5 + 1 )) ;;
        z6*)    z6=$(( z6 + 1 )) ;;
        z7*)    z7=$(( z7 + 1 )) ;;
        z8*)    z8=$(( z8 + 1 )) ;;
        z9*)    z9=$(( z9 + 1 )) ;;
        *)      class=$(( class + 1 ))  ;;
    esac
done < last.log

echo "$count uniwide logins"
echo "z0: $z0"
echo "z1: $z1"
echo "z2: $z2"
echo "z3: $z3"
echo "z4: $z4"
echo "z5: $z5"
echo "z6: $z6"
echo "z7: $z7"
echo "z8: $z8"
echo "z9: $z9"
echo "class: $class"
```

___
## Shell functions

``` sh
function_name() {
    ...
    count=$((count + 1))
}

# command line argument variables used to get a function's arguments, e.g.
# $# -> number of args
# $1... -> arguments for functions

# calling a function
function_name ...
```

By default, variables in shell functions are global

Use the `local` keyword to make variables local

___
### 11. Write a shell function *top_and_bottom* that, given a file name, prints the file name, plus the first and last lines of the file.
```sh
$ . top-and-bottom.sh
$ top-and-bottom /usr/share/dict/british-english-insane
=================
/usr/share/dict/british-english-insane
-----------------
A
événements
=================
```

```sh
#!/bin/sh

top_and_bottom() {
    echo "=================="
    echo "$1"
    echo "------------------"
    head -1 "$1"
    tail -1 "$1"
    echo "=================="
}

for file in "$@"
do
    top_and_bottom "$file"
done
```

___
### 12. Write a shell function print_message that, given an optional exit status and a message:

### If no exit status is given the program should print a warning
### If an exit status is given the program should print an error and exit the program

```sh
#!/bin/sh

print_message() {
    if [ $# -eq 1 ]
    then
        echo "$0: warning: $1"
    else
        echo "$0: error: $2"
        exit $1
    fi
}


print_message "this is a warning"

print_message 1 "this is an error"
```


___
### 13. Create a git repository called _cs2041-Labs_ and add your week01 and week02 lab work.
### Then push your repository to the CSE gitlab servers.

Follow the instructions from the 'Creating a new Git repository' lab task to complete this exercise

___
### 14. There is a git repository located on the CSE gitlab servers at https://gitlab.cse.unsw.edu.au/cs2041/22t2-tut05
### Clone this repository to your local machine.

Run
```sh
$ git clone gitlab@gitlab.cse.unsw.EDU.AU:cs2041/22t2-tut05.git
```
