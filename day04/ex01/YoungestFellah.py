#!/usr/bin/env python

import importlib.util
import sys
sys.path.append('../ex00')
from FileLoader import FileLoader

def youngestFellah(df, year):
    f = next(iter(df.loc[(df['Year'] == 2010) & (df['Sex'] == 'F')][['Sex', 'Age']].set_index('Sex').min()), 'no match')
    m = next(iter(df.loc[(df['Year'] == 2010) & (df['Sex'] == 'M')][['Sex', 'Age']].set_index('Sex').min()), 'no match')
    mydic = {'F':f, 'M':m}
    return mydic

if __name__ == '__main__':
    ld = FileLoader()
    df = ld.load('../resources/athlete_events.csv')
    ld.display(df, 3)

    print(youngestFellah(df, 2014))
