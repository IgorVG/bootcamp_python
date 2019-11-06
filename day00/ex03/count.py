#!/usr/bin/env python
import sys
from collections import Counter
import string


def text_analyzer(arg):
    c = dict()
    c['upper'] = sum(1 for c in arg if c.isupper())
    c['lower'] = sum(1 for c in arg if c.islower())
    c['punctuation'] = sum(1 for c in arg if c in string.punctuation)
    c['space'] = sum(1 for c in arg if c == ' ')
    # c = Counter("upper" if x.isupper() else "lower" if x.islower()
    #                else "space" if x.isspace()
    #                else "punctuation" if x in string.punctuation
    #                else "space" for x in arg)
    print("- {} upper letters".format(c['upper']))
    print("- {} lower letters".format(c['lower']))
    print("- {} punctuation marks".format(c['punctuation']))
    print("- {} spaces".format(c['space']))


if __name__ == '__main__':
    if (len(sys.argv) == 2):
        text_analyzer(sys.argv[1])
    else:
        print('ERROR')
