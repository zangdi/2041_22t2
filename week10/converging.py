#!/usr/bin/env python3

import re
import sys

def main():
    lines = sys.stdin.readlines()
    content = " ".join(lines).strip()

    # re.findall will give us strings, we want ints for comparisons to work correctly
    nums = [int(x) for x in re.findall(r'\d+', content)]

    for i in range(len(nums) - 1):
        if nums[i] <= nums[i + 1]:
            print("not converging")
            sys.exit(0)

    for i in range(len(nums) - 2):
        if nums[i] - nums[i + 1] <= nums[i + 1] - nums[i + 2]:
            print("not converging")
            sys.exit(0)

    print("converging")


if __name__ == "__main__":
    main()