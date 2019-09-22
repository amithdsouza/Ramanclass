#!/usr/bin/env python

import os

def choose(a, divisor, remainder, skip_list=[]):
    b = a.split()
    count = len(b)
    c = []
    i = 0
    for word in b:
       if (i % divisor) == remainder and i not in skip_list:
           print i, word
           c.append(word)
       i += 1
    print c   
    d = ' '.join(c)
    print d

def main():
    a = "Hello World It's my first program"
    print a
    choose(a, 2, 0)
    choose(a, 2, 1)
    choose(a, 3, 0, [0])
    


if __name__ == '__main__':
   main()
