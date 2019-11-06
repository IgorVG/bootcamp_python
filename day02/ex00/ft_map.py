#!/usr/bin/env python

def ft_map(function_to_apply, list_of_inputs):
    for x in list_of_inputs:
        yield function_to_apply(x)

if __name__ == '__main__':
    l = [1,2,3,4,5]
    print('ft_map:')
    for i in ft_map(lambda x: x**2, l):
        print(i)
    print('real map:')
    for i in map(lambda x: x**2, l):
        print (i)
