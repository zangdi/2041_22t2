#!/usr/bin/env python3

def print_dict(d):
    # iterating over d only gives us keys
    for key, value in d.items():
        print(f"[{key}] => {value}")
