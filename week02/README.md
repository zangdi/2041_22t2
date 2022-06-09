# Week 2 Tute

### 1. Consider the following columnar (space-delimited) data file containing (fictional) contact for various CSE academic staff:
```
G Heiser       Newtown      9381-1234
S Jha          Kingsford    9621-1234
C Sammut       Randwick     9663-1234
R Buckland     Randwick     9663-9876
J A Shepherd   Botany       9665-4321
A Taylor       Glebe        9692-1234
M Pagnucco     North Ryde   9868-6789
```
### This data is fictitious.
### Do not ring these phone numbers.

### The data is currently sorted in phone number order.
### Can we use the [_sort_](https://manpages.debian.org/jump?q=sort.1) filter to re-arrange the data into telephone-book order?
### (alphabetically by last name)
### If not, how would we need to change the file in order to achieve this?

It seems like we have an initial followed by a space and then the last name, so we can try
```sh
$ sort -t' ' -k2 q1.txt 
J A Shepherd   Botany       9665-4321
R Buckland     Randwick     9663-9876
G Heiser       Newtown      9381-1234
S Jha          Kingsford    9621-1234
M Pagnucco     North Ryde   9868-6789
C Sammut       Randwick     9663-1234
A Taylor       Glebe        9692-1234
```

However, JAS is not in the right place, so we need to edit the file.

Option 1: Join initials together
```
G. Heiser       Newtown      9381-1234
S. Jha          Kingsford    9621-1234
C. Sammut       Randwick     9663-1234
R. Buckland     Randwick     9663-9876
J.A. Shepherd   Botany       9665-4321
A. Taylor       Glebe        9692-1234
M. Pagnucco     North Ryde   9868-6789
```

By joining them together, now Shepherd is also the after the first space, so the command we tried previously works

```sh
$ sort -t' ' -k2 q1.txt 
R. Buckland     Randwick     9663-9876
G. Heiser       Newtown      9381-1234
S. Jha          Kingsford    9621-1234
M. Pagnucco     North Ryde   9868-6789
C. Sammut       Randwick     9663-1234
J.A. Shepherd   Botany       9665-4321
A. Taylor       Glebe        9692-1234
```


Option 2: Group initials
```
G, Heiser       Newtown      9381-1234
S, Jha          Kingsford    9621-1234
C, Sammut       Randwick     9663-1234
R, Buckland     Randwick     9663-9876
J A, Shepherd   Botany       9665-4321
A, Taylor       Glebe        9692-1234
M, Pagnucco     North Ryde   9868-6789
```

By grouping them together, now we can sort by the second field when delimited by a comma

```sh
$ sort -t' ' -k2 q1.txt 
R, Buckland     Randwick     9663-9876
G, Heiser       Newtown      9381-1234
S, Jha          Kingsford    9621-1234
M, Pagnucco     North Ryde   9868-6789
C, Sammut       Randwick     9663-1234
J A, Shepherd   Botany       9665-4321
A, Taylor       Glebe        9692-1234
```


Option 3: Rearrange names
```
Heiser G       Newtown      9381-1234
Jha S          Kingsford    9621-1234
Sammut C       Randwick     9663-1234
Buckland R     Randwick     9663-9876
Shepherd J A   Botany       9665-4321
Taylor A       Glebe        9692-1234
Pagnucco M     North Ryde   9868-6789
```

By putting the last name before the first name, we can now just sort the file

```sh
$ sort q1.txt 
Buckland R     Randwick     9663-9876
Heiser G       Newtown      9381-1234
Jha S          Kingsford    9621-1234
Pagnucco M     North Ryde   9868-6789
Sammut C       Randwick     9663-1234
Shepherd J A   Botany       9665-4321
Taylor A       Glebe        9692-1234
```

___
### 2. Consider this Unix password file
### (usually found in `/etc/passwd`):
```
root:ZHolHAHZw8As2:0:0:root:/root:/bin/dash
jas:iaiSHX49Jvs8.:100:100:John Shepherd:/home/jas:/bin/bash
andrewt:rX9KwSSPqkLyA:101:101:Andrew Taylor:/home/andrewt:/bin/cat
postgres::997:997:PostgreSQL Admin:/usr/local/pgsql:/bin/bash
oracle::999:998:Oracle Admin:/home/oracle:/bin/bash
cs2041:rX9KwSSPqkLyA:2041:2041:COMP2041 Material:/home/cs2041:/bin/bash
cs3311:mLRiCIvmtI9O2:3311:3311:COMP3311 Material:/home/cs3311:/bin/zsh
cs9311:fIVLdSXYoVFaI:9311:9311:COMP9311 Material:/home/cs9311:/bin/bash
cs9314:nTn.JwDgZE1Hs:9314:9314:COMP9314 Material:/home/cs9314:/bin/fish
cs9315:sOMXwkqmFbKlA:9315:9315:COMP9315 Material:/home/cs9315:/bin/bash
```
### Provide a command that would produce each of the following results:

#### a) Display the first three lines of the file
[`head`](https://man7.org/linux/man-pages/man1/head.1.html) is a filter which prints the first 10 lines of a file

`head -n`, where n is a number, prints the first n lines of a file

```sh
head -3 q2.txt 
```

#### b) Display lines belonging to class accounts
#### (assuming that class accounts have a username that starts with either "cs", "se", "bi" or "en", followed by four digit)
The username is first field, so we want to ensure that our pattern starts at the start of the line and finishes with a : to avoid usernames which contain more characters afterwards

```sh
grep -E '^(cs|se|bi|en)[0-9]{4}:' q2.txt 
```

#### c) Display the username of everyone whose shell is /bin/bash
The shell is the last field, so once again, we start with : to avoid capturing lines where the shell has something before the /bin/bash and dollar sign to avoid things after the /bin/bash.

```sh
grep -E ':/bin/bash$' q2.txt | cut -d':' -f1
```

We cannot change the order of [`grep`](https://man7.org/linux/man-pages/man1/grep.1.html) and [`cut`](https://man7.org/linux/man-pages/man1/cut.1.html) as [`cut`](https://man7.org/linux/man-pages/man1/cut.1.html) will remove the information that we need for [`grep`](https://man7.org/linux/man-pages/man1/grep.1.html)

#### d) Create a tab-separated file passwords.txt containing only the username and password of each user
We can safetly [`cut`](https://man7.org/linux/man-pages/man1/cut.1.html) and then [`tr`](https://man7.org/linux/man-pages/man1/tr.1.html) or [`tr`](https://man7.org/linux/man-pages/man1/tr.1.html) and then [`cut`](https://man7.org/linux/man-pages/man1/cut.1.html) without losing information

```sh
cut -d':' -f1,2 q2.txt | tr ':' '\t' > passwords.txt
```

or

```sh
tr ':' '\t' < q2.txt | cut -f1,2 > passwords.txt 
```

___
### 3. Consider the fairly standard split-into-words technique from the previous question.
``` sh
$ tr -cs 'a-zA-Z0-9' '\n' < someFile
```
### Explain how this command works.
### What does each argument do?

The `-c` takes the complement of the first set of letters given. This means it applies the translation to all of the characters which are not in the first set of letters

The `-s` means squeeze, when letters are being replaced, if several consecuetive characters translate into the same letter, that letter will only appear once

Putting these meanings together, this replaces all non-alphanumeric characters with a newline and replaces consecutive newlines with just a single newline

___
### 4. What is the output of each of the following pipelines if the text:
```
this is big Big BIG
but this is not so big
```
### is supplied as the initial input to the pipeline?
#### a)
``` sh
tr -d ' ' | wc -w
```

- `tr -d ' '` removes the spaces in the line
- `wc -w` prints out the number of words in the input

```sh
$ tr -d ' ' <q4.txt 
thisisbigBigBIG
butthisisnotsobig
$ tr -d ' ' <q4.txt | wc -w
2
```


#### b)
``` sh
tr -cs 'a-zA-Z0-9' '\n' | wc -l
```

- [`tr -cs 'a-zA-Z0-9' '\n'` is explained in question 3](#3-consider-the-fairly-standard-split-into-words-technique-from-the-previous-question)
- `wc -l` prints out the number of lines in the input

```sh
$ tr -cs 'a-zA-Z0-9' '\n' <q4.txt 
this
is
big
Big
BIG
but
this
is
not
so
big
$ tr -cs 'a-zA-Z0-9' '\n' <q4.txt | wc -l
11
```

#### c)
``` sh
tr -cs 'a-zA-Z0-9' '\n' | tr '[:lower:]' '[:upper:]' | sort | uniq -c
```

- [`tr -cs 'a-zA-Z0-9' '\n'` is explained in question 3](#3-consider-the-fairly-standard-split-into-words-technique-from-the-previous-question)
- `tr '[:lower:]' '[:upper:]'` replaces lower case characters with upper case characters
- `sort` sorts the list in alphabetical order
- `uniq -c` prints duplicated lines once with a count of duplicates next to it
  - Beware that `uniq` only prints duplicate lines which are adjacent to each other

```sh
$ tr -cs 'a-zA-Z0-9' '\n' <q4.txt | tr '[:lower:]' '[:upper:]'
THIS
IS
BIG
BIG
BIG
BUT
THIS
IS
NOT
SO
BIG
$ tr -cs 'a-zA-Z0-9' '\n' <q4.txt | tr '[:lower:]' '[:upper:]' | sort
BIG
BIG
BIG
BIG
BUT
IS
IS
NOT
SO
THIS
THIS
$ tr -cs 'a-zA-Z0-9' '\n' <q4.txt | tr '[:lower:]' '[:upper:]' | sort | uniq -c
      4 BIG
      1 BUT
      2 IS
      1 NOT
      1 SO
      2 THIS
```

___
### 5. Consider a file containing (fake) zIDs and marks in COMP1511:
```
4279700|61
4212240|59
4234024|57
4286024|50
4270657|75
4227010|52
4299716|84
4236088|74
4245033|87
4222098|46
4228842|85
4209182|96
4276270|61
4224421|72
4207416|76
```
### and another file containing (fake) zIDs and marks in COMP2041:
```
4200549|92
4283960|77
4203704|48
4261741|43
4224421|67
4223809|75
4276270|80
4279700|68
4233865|61
4207416|56
4209669|71
4209182|70
4213591|49
4236221|53
4201259|91
```
#### a) Can the files be used as-is with the join command?
#### If not, what needs to be changed?
[`join`](https://man7.org/linux/man-pages/man1/join.1.html) can only work on sorted files

We create sorted versions of the 1511 and 2041 files by running

```sh
$ sort 1511_marks.txt > 1511_marks_sorted.txt 
$ sort 2041_marks.txt > 2041_marks_sorted.txt 
```

#### b) Write a join command which prints the marks in COMP1511 and COMP2041 of everyone who did both courses.
- `-t` specifies the delimiter of the file
  - In this case, the fields are separated by '|'
- `-j1` means that files are joined on the first field in both files
  - This is the same as writing `-11 -21`

```sh
join -t'|' -j1 1511_marks_sorted.txt 2041_marks_sorted.txt
```

#### c) Write another join command which prints the marks in COMP1511 and COMP2041 of everyone, across both files,
#### With -- in the case where a student didn't do a particular subject
Run `info join` to find out more information about the join function, particularly about the `-o` option
- `-a1` prints lines from the first file which aren't joined to lines in the second file
  - `-a2` is similar
- `-o` specifies the output for join
- `-e` specifies what to write for fields which exist in one file but not the other

```sh
join -t'|' -j1 -a1 -a2 -o auto -e '--' 1511_marks_sorted.txt 2041_marks_sorted.txt 
```

#### d) Write a shell pipeline which prints the marks in COMP1511 and COMP2041 of everyone who did both courses,
#### sorted by their COMP1511 mark in _ascending_ order,
#### then by their COMP2041 mark in _descending_ order.
In `sort`, when we write `-kF` where `F` is a field number, we sort from the start of the field to the end of the line

Writing `-kF,F` means that we only sort for the field

We can also specify several keys to first sort by the first key given, then the next one and so on

```sh
join -t'|' -j1 1511_marks_sorted.txt 2041_marks_sorted.txt | sort -t'|' -k2,2n -k3,3rn
```
___
### 6. Consider a file containing tab-separated benchmarking results for 20 programs, in three different benchmarks, all measured in seconds.
```
program1	08	03	05
program2	14	03	05
program3	17	08	10
program4	15	11	05
program5	16	10	24
program6	15	09	17
program7	15	06	10
program8	17	10	17
program9	12	07	08
program10	09	04	16
program11	11	03	24
program12	16	11	20
program13	16	08	17
program14	08	07	06
program15	06	06	05
program16	12	05	08
program17	09	05	10
program18	06	06	06
program19	14	09	22
program20	16	04	24
```
#### a) Write a sort command which sorts by the results in the second benchmark, then by the results in the first benchmark.
[Look at 5.d) for a similar explanation](#d-write-a-shell-pipeline-which-prints-the-marks-in-comp1511-and-comp2041-of-everyone-who-did-both-courses)

```sh
sort -k3,3 -k2,2 q6.txt
```

#### b) Write a sort command which sorts by the results in the third benchmark, then by the program number.
In `sort`, we can write a field number as `F.C` where `C` means `C` characters after the start of field `F`

Run `info sort` in a Linux terminal (e.g. CSE system) to find out more information

```sh
sort -k4,4n -k1.8,1n q6.txt 
```

#### c) Write a sed command which removes the leading zeroes from the benchmark times.
We use `s/[pattern]/[string]/` command to substitute the first occurrence of a pattern in a line with a string using [`sed`](https://man7.org/linux/man-pages/man1/sed.1.html)

Using `s/[pattern]/[string]/` replaces all occurrences of the pattern with the string

```sh
sed -Ee 's/\t0/\t/g' q6.txt 
```

#### d) Write a sed command which removes the benchmark results from program2 through program13.
When `sed` is run without a command, every single line in a file is printed out
- The `d` command will delete certain lines
- The `p` command will print out certain lines
  - This results in lines which match the pattern printing out twice, however you can also combine the `p` command with the `-n` argument to only print out the certain lines, e.g. `sed -n -Ee '2p'` prings only the second line of a file

```sh
sed -Ee '/^program2\b/,/^program13\b/d' q6.txt
```

This deletes the lines starting from the line which matches the `^program2\b` regex pattern up to and including the line which matches the `^program13\b` regex pattern
