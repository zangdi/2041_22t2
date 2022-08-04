#!/bin/sh

directory="/usr/src/linux"

for file in $(find "$directory" -type f -name '*.c')
do
    echo mutt -s "Linux source" -a "$file" -- andrewt@unsw.edu.au
done
