#!/usr/bin/env python

class Evaluator:
    def check_args(words, coefs):
        if not all(isinstance(w, str) for w in words):
            return False
        else:
            return True

    def zip_evaluate(words, coefs):
        assert Evaluator.check_args(words, coefs), 'ERROR' 
        try:
            return sum(len(z) * i for z, i in zip(words, coefs))
        except:
            return -1
    
    def enumerate_evaluate(words, coefs):
        assert Evaluator.check_args(words, coefs), 'ERROR'
        try:
            return sum(len(words[k]) * i for k, i in enumerate(coefs))
        except:
            return -1

if __name__ == '__main__':
    words = ['black', 'blue', 'brown']
    coefs = [1.4, 5.4, 1.2]
    print(Evaluator.zip_evaluate(words, coefs))  
    print(Evaluator.enumerate_evaluate(words, coefs))    
