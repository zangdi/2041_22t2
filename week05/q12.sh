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
