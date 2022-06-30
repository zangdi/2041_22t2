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
