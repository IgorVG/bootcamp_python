#!/usr/bin/env python

import numpy as np


class NumPyCreator:
    
    @staticmethod
    def from_list(lst):
        return np.array(lst)
    @staticmethod
    def from_tuple(tpl):
        return np.array(tpl)

    @staticmethod
    def from_iterable(itr):
        return (np.array([x for x in itr]))

    @staticmethod
    def from_shape(shape, value=0, dtype=None, order='C'):
        return np.full(shape, value, dtype=dtype, order=order)

    @staticmethod
    def random(shape):
        return np.random.normal(loc=0., scale=0.3, size=shape)

    @staticmethod
    def identity(n, dtype=None):
        return np.identity(n, dtype=dtype)
    
    def __repr__(self)


if __name__ == '__main__':
    npc = NumPyCreator()
    lst = [[1,2,3],[6,3,4]]
    print(repr(npc.from_list(lst)))
    print(repr(npc.from_tuple(("a", "b", "c"))))
    print(npc.from_iterable(range(5)))
    shape=(3,5)
    print(npc.from_shape(shape))
    print(npc.random(shape))
    print(npc.identity(4))