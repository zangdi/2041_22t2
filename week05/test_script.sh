#!/bin/sh

# mktemp creates a temporary file
expected_output="$(mktemp)"
actual_output="$(mktemp)"

# EOF acts like multi-line quotes
cat > "$expected_output" <<EOF
Initialized empty tigger repository in .tigger
EOF

# put stdout and stderr of command into expected output file
tigger-init > "$actual_output" 2>&1

# check if expected output and actual output are the same
if ! diff "$expected_output" "$actual_output"
then
    echo "failed test"
    exit 1
fi
