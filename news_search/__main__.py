#!/usr/bin/env python3
import sys

from .search import search


def main():

    try:
        results = search(sys.argv[1], sys.argv[2::])
        print(*results, sep="\n")
    except IndexError as e:
        print("Incorrect input. Please refer to the readme for instructions.")


if __name__ == "__main__":
    main()
