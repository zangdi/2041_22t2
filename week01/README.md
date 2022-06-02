# Week 1 Tute

### 4. What is an operating system?
An operating system is a piece of software that runs between hardware and programs.


___
### 6. What operating system(s) do CSE lab computers run?
Linux, Debian distro

___
## Special characters in Regex

Regex = regular expression


| Character | Meaning | Example
|:---:|:---:|:---:|
| `.` | Any character | `.`: 'a' '5' ':'
| `*` | 0 or more | `a*`: '' 'a' 'aa' 'aaaa...'
| `+` | 1 or more | `a+`: 'a' 'aa' 'aaaa...'
| `?` | 0 or 1 | `a?`: '' 'a'
| `{m, n}` | Repeat from m to n times | `a{4}`: 'aaaa', a{1, 3}: 'a', 'aa', 'aaa'
| `[]` | Any character in set | `[abc]`: 'a' 'b' 'c'
| `[a-z]` | Any character in set, - to write range | `[-0-9a-zA-Z]`
| `[^]` | Any character not in the set | `[^abc]`: 'd', '5', '?'
| `^` | Start of string | `^abc`
| `$` | End of string | `abc$`
| `\|` | Or | `abc\|def\|ghi`: 'abc' 'def' 'ghi'
| `()` | Grouping things together | `(abc)*`: '' 'abc' 'abcabc'
| `\` | Escape special meaning of next character | `\\`: '\', `\.`: '.'
| `\s` | Any whitespace character | `\s`: ' '
| `\w` | Word character | `\w == [a-zA-Z0-9_]`

___
### 7. Write a regex to match:

#### a) C preprocessor commands in a C program source file.
`^#`

#### b) All the lines in a C program except preprocessor commands.
`^[^#]`

#### c) All lines in a C program with trailing white space (one or more white space at the end of line).
`\s$`

#### d) The names "Barry", "Harry", "Larry" and "Parry".
`[BHLP]arry`


#### e) A string containing the word "hello" followed, some time later, by the word "world".
`hello.*world`


#### f) The word "calendar" and mis-spellings where 'a' is replaced with 'e' or vice-versa.
`c[ae]l[ae]nd[ae]r`


#### g) A list of positive integers separated by commas, e.g. 2,4,8,16,32
`([1-9][0-9]*,)*[1-9][0-9]*`

or

`[1-9][0-9]*(,[1-9][0-9]*)*`


#### h) A C string whose last character is newline.
```C
// examples of C code with C strings:

printf("hello world\n");

char *string = "some string\n";
```

`"[^"]*\\n"`

___
### 8. When should you use:
- `fgrep/grep -F` look for fixed strings (i.e. no regex) in a file
  - `fgrep` is deprecated, so use `grep -F`
- `grep/grep -G` look for strings which match a basic regex pattern in a file
- `egrep/grep -E` look for strings which match an extended regex pattern in a file
  - `egrep` is deprecated, so use `grep -E`
  - extended regex has more special characters than basic, such as '+'
- `pgrep` looks for running processes, is unrelated to other `grep` programs
- `grep -P` looks for strings which match a Perl compatible regex pattern in a file
  - Perl compatible regex patterns contain additional features, especially with groups

___
### 9. grep takes many options (see the manual page for [grep](https://manpages.debian.org/jump?q=grep.1)).
``` sh
$ man 1 grep
```
### Give 3 (or more) simple/important options grep takes and explain what they do.

- `-i` means case insensitive: upper and lower case are the same
- `-v` inverts matches: shows lines that don't match the pattern
- `-c` counts the lines which match a pattern rather than printing them out

___
### 10. Why does this command seem to be taking a long time to run:
``` sh
grep -E hello
```

When no filename is provided, `grep` assumes it is running with `stdin` so it is waiting for you to type.
Press `Ctrl+D` to stop `grep` from running.

___
### 11. Why won't this command work:
``` sh
grep -E int main program.c
```

Shell considers spaces as separators for arguments.
When this code is run, `grep` looks for the pattern 'int' in the files 'main' and 'program.c'.

The correct command is
`grep -E 'int main' program.c`


___
### 12. Give five reasons why this attempt to search a file for HTML paragraph and break tags may fail.
```sh
grep <p>|<br> /tmp/index.html
```
### Give a grep command that will work.

- `grep` doesn't have alteration (|), so we need to use extended regex
- <, > and | have special meaning in shell, so we need quotes around the pattern
- HTML tags are also allowed to be in upper case, so we need to be case insensitive

`grep -Ei '<p>|<br> /tmp/index.html` will take us most of the way there

___
### 13. For each of the regular expression below indicate how many different strings the pattern matches and give some example of the strings it matches.
### If possible these example should include the shortest string and the longest string.

| part | regex | example | shortest | longest |
|---|---|---|---|---|
| a |`Perl`| 'Perl' | 'Perl' | 'Perl' |
| b |`Pe*r*l`| 'Pl' 'Pel' 'Peeeeerrrrl' 'Prl' | 'Pl' | Infinite es and rs |
| c |`Full-stop.`| 'Full-stop1' 'Full-stop.' | Same length | Same length |
| d |`[1-9][0-9][0-9][0-9]`| 1000 - 9999 | Same length | Same length |
| e |`I (love\|hate) programming in (Perl\|Python) and (Java\|C)`| 'I love programming in Python and C' | 'I hate programming in Perl and C' | 'I love programming in Python and Java'

___
### 14. This regular expression `[0-9]*.[0-9]*` is intended to match floating point numbers such as '42.5'
### Is it appropriate?

No,
- `.` means any character, so we can end up with any character in between the whole and decimal parts
  - `[0-9]*\.[0-9]*` fixes the problem so it must match with '.' literally
- `[0-9]*` means that we can have no whole or decimal part, e.g. '0.', '.0', or '.'
  - `[0-9]+\.[0-9]+` fixes the problem so we have at least one number before and after the decimal point
- `[0-9]+` in the whole part means that we can get leading 0s, e.g. '01.0', '00000.0'
  - `[1-9][0-9]*\.[0-9]+` fixes the problem so we will not have leading 0s
- `[1-9][0-9]*` doesn't let us have '0' as the whole part
  - `(0|[1-9][0-9]*)\.[0-9]+` lets us have 0 or a non-zero positive whole number

___
### 15. What does the command `grep -Ev .` print and why?

### Give an equivalent grep -E command with no options,
### in other words: without the -v.

`grep -Ev .` prints out all the lines that don't match with '.', i.e. don't have a single character, or all the empty lines

`grep -E '^$'` does the same thing

___
### 16. Write a grep -E command which will print any lines in a file ips.txt containing an IP addresses in the range `129.94.172.1` to `129.94.172.25`

The `129.94.172.` part is easy: just `129\.94\.172\.` works.

To catch between 1 and 25, we can break it up into 3 groups:
- 1 to 9: `[1-9]`
- 10 to 19: `1[0-9]`
- 20 to 25: `2[0-5]`

Putting this all together, we get
```sh
grep -E '129\.94\.172\.([1-9]|1[0-9]|2[0-5])' ips.txt
```
