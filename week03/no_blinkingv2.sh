#!/bin/sh

# $@ -> gives us all the command line arguments

for file in "$@"
do
    echo "Renaming $file to $file.bad because it uses the <blink> tag"
    mv "$file" "$file.bad"
done
