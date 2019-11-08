#!/usr/bin/env python

import importlib.util
import sys
sys.path.append('../ex00')
from FileLoader import FileLoader

def proportionBySport(df, year, sport, sex):
    p = df[(df.Year == year) & (df.Sex == sex)]\
.drop_duplicates(subset=['Name', 'ID']).shape[0]
    p_s = df[(df.Year == year) & (df.Sex == sex) & (df.Sport == sport)]\
.drop_duplicates(subset=['Name', 'ID']).shape[0]
    return p_s / p
    

if __name__ == '__main__':
    ld = FileLoader()
    df = ld.load('../resources/athlete_events.csv')
    ld.display(df, 3)

    print(proportionBySport(df, 2004, 'Tennis', 'F'))
