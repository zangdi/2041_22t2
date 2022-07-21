#!/usr/bin/env python3
import sys


def create_words_set(filename):
    # use set rather than dict because we don't have a value to store, just a key
    words = set()

    with open(filename) as file1:
        for word in file1:
            word = word.strip()
            words.add(word)
    
    return words


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <file1> <file2>")
        sys.exit(1)

    words1 = create_words_set(sys.argv[1])
    words2 = create_words_set(sys.argv[2])

    # option 1: checks if word that is in words1 is not in words2
    words_list = []
    for word in words1:
        if word not in words2:
            words_list.append(word)

    # option2: this is same as option1, but using list comprehension
    words_list = [word for word in words1 if word not in words2]

    # option3: using set subtraction
    words_list = []
    for word in words1 - words2:
        words_list.append(word)

    # option4: this is same as option3, but using list comprehension
    words_list = [word for word in words1 - words2]

    # sorted: returns a sorted version of a list
    # .sort: sorts a list in place
    for word in sorted(words_list):
        print(word)


if __name__ == "__main__":
    main()
