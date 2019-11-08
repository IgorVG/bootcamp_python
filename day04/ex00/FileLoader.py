#!/usr/bin/env python

import pandas as pd

class FileLoader:
    
    @staticmethod
    def load(path):
        data = pd.read_csv(path)
        print('Loading dataset of dimensions {} x {}'.format(data.shape[0],
              data.shape[1]))
        return data

    @staticmethod
    def display(df, n):
        if n:
            print(df.iloc[:n] if n > 0 else df.iloc[n:])

if __name__ == '__main__':
    fl = FileLoader()

    df = fl.load('/Users/igarbuz/MyProjects/bootcamp_python/day04/resources/\
athlete_events.csv')
    fl.display(df, 3)