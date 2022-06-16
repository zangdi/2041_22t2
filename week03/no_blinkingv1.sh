#!/bin/sh

# *.html -> all the files which end with .html in the current directory

for file in *.html
do
    echo "Removing $file because it uses the <blink> tag"
    rm "$file"
done
