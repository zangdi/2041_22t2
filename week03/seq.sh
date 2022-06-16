#!/bin/sh

FIRST=1
INCREMENT=1
LAST=1

# $# -> number of command line arguments

if test $# -eq 1
then
    LAST=$1
elif [ $# -eq 2 ]
then
    FIRST=$1
    LAST=$2
elif [ $# -eq 3 ]
then
    FIRST=$1
    INCREMENT=$2
    LAST=$3
else
    echo "Usage: $0 [FIRST [INCREMENT]] LAST"
    exit 1
fi

# making sure that $FIRST is actually an integer
# 2> /dev/null means that messages from stderr won't be printed out
if [ $FIRST -eq $FIRST ] 2> /dev/null
then
    # if $FIRST is an integer, do nothing
    :
else
    echo "FIRST is not an integer"
    exit 1
fi

curr="$FIRST"
while [ $curr -le $LAST ]
do
    echo "$curr"
    curr=$(( curr + INCREMENT ))
done
