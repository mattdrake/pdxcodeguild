__author__ = 'drake'
from math import *

def primes():
    question = input("Please enter a number. ")
    i = 2
    msg = 'is a prime number'
    while i <= sqrt(question):
        if question % i == 0:
            msg = 'is not a prime number'
        i += 1
    print(question, msg)

primes()
