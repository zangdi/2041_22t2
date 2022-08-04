#!/bin/sh

# extract the first column to get just the student ids
cut -d" " -f1 < student.txt |
# sort the values so that uniq can work correctly
sort |
# print out lines which are duplicated
uniq -d
