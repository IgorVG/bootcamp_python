#!/usr/bin/env python

from random import shuffle

def generator(text, sep=' ', option=None):
    ''' text is mandatory,  '''
    options = ['shuffle', 'unique', 'ordered']
    if sep=='':
        yield('ERROR')
        return
    if not isinstance(text, str) or not isinstance(sep, str) or sep == '':
        return('ERROR')
    if option and option not in options:
        return('ERROR')
    if (option == 'shuffle'):
        t = text.split(sep)
        shuffle(t)
        for s in t:
            yield s
    elif option == 'unique':
        for s in list(set(text.split(sep))):
            yield s
    elif option == 'ordered':
        t = text.split(sep)
        for s in sorted(t, key=lambda x: x.swapcase()):
            yield s
    else:
        for s in text.split(sep):
            yield s

if __name__ == '__main__':
    text = "Le Lorem Ipsum est simplement du faux texte."
    # for word in generator(text, sep=" "):
    #     print(word)

    # for word in generator(text, sep=" ", option="shuffle"):
    #     print(word)

    # for word in generator(text, sep=" ", option="ordered"):
    #     print(word)

    print(generator(text, sep='', option="ordered"))
    