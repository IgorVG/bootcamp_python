#!/usr/bin/env python
import sys


def main(str):
    print(str[::-1])
    sys.exit()


if __name__ == '__main__':
    if (len(sys.argv) > 1):
        main(sys.argv[1])
