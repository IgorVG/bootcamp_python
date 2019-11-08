#!/usr/bin/env python

import importlib.util
import sys
sys.path.append('../ex00')
from FileLoader import FileLoader

def youngestFellah(df, year):
    m = d[(d.Year == year) & (d.Sex == 'M')].Age.min()
    f = d[(d.Year == year) & (d.Sex == 'F')].Age.min()
    return {'F':f, 'M':m}

if __name__ == '__main__':
    ld = FileLoader()
    df = ld.load('../resources/athlete_events.csv')
    ld.display(df, 3)

    print(youngestFellah(df, 2014))
