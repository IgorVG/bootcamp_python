#!/usr/bin/env python

def ft_filter(function_to_apply, list_of_inputs):
    for x in list_of_inputs:
        if function_to_apply(x):
            yield x

if __name__ == '__main__':
    l = [1,2,4,8,10,15,20]
    print('real filter:')
    for i in filter(lambda x: x > 5, l):
        print(i)
    print('ft_filter:')
    for i in ft_filter(lambda x: x > 5, l):
        print(i)