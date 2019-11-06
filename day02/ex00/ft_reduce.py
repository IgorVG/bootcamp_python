#!/usr/bin/env python

def ft_reduce(function_to_apply, list_of_inputs):
    x1 = list_of_inputs[0]
    list_of_inputs = list_of_inputs[1:]
    for x2 in list_of_inputs:
        x1 = function_to_apply(x1, x2)
    return x1

if __name__ == '__main__':
    from functools import reduce
    print('real reduce:')
    l = [1,2,4,8,6,7,8]
    i = reduce((lambda x, y: x + y), l)
    print(i)
    print('ft_reduce:')
    i = ft_reduce(lambda x, y: x + y, l)
    print(i)