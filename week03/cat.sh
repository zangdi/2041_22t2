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
