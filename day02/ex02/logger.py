#!/usr/bin/env python

import time
from random import randint

def log2(function):
    def wrapper(*argc):
        #print(str(argc))
        return function(*argc)
    return wrapper

def log(function):
    def wrapper(*argc):
        time_milli = lambda x: round(x * 1000, 3)
        start = time.time()
        if function(*argc):
            return True
        delta = time.time() - start
        f = open('log.txt', 'a+')
        fstr = '(igarbuz)Running: {:25}[ exec-time = {} {} ]\n'.format(function.__name__, round(delta, 3) if delta >= 1. else time_milli(delta), 's' if delta >= 1. else 'ms' ) 
        f.write(fstr)
        f.close()
    return wrapper

class CoffeeMachine():

    water_level = 100

    @log
    def start_machine(self):
        #time.sleep(0.1)
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
        return False
    
    @log
    def boil_water(self):
        return "boiling..."
    
    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")
    
    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)