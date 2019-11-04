#!/usr/bin/env python
import sys


def whois(arg):
    try:
        int(arg)
    except Exception:
        print('ERROR')
        sys.exit()
    if arg == '0':
        print("I'm Zero.")
    elif int(arg[-1]) % 2:
        print("I'm Odd.")
    else:
        print("I'm Even.")


if __name__ == '__main__':
    if (len(sys.argv) == 2):
        whois(sys.argv[1])
    else:
        print('ERROR')
